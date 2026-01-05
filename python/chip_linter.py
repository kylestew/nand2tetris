"""
NAND2TETRIS Chip Linter

AST-based enforcement of the NAND-only constraint.
This linter runs BEFORE tests to reject any "cheating" at the syntax level.

Forbidden constructs:
- Boolean operators: and, or, not
- Bitwise operators: &, |, ^, ~
- Conditionals: if/else (Chapter 1 only)
- Comparisons used as logic: ==, !=
- Illegal imports: anything not in the allowed list for that chip
"""

import ast
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Optional


# Chip order - each chip can only import chips that come before it
CHIP_ORDER = [
    "nand",
    "not_gate",
    "and_gate",
    "or_gate",
    "xor_gate",
    "mux",
    "dmux",
    "not16",
    "and16",
    "or16",
    "mux16",
    "or8way",
    "mux4way16",
    "mux8way16",
    "dmux4way",
    "dmux8way",
]

# Map chip name to allowed imports (all chips before it in order)
ALLOWED_IMPORTS: dict[str, set[str]] = {}
for i, chip in enumerate(CHIP_ORDER):
    ALLOWED_IMPORTS[chip] = set(CHIP_ORDER[:i])


@dataclass
class Violation:
    """A linter violation."""
    line: int
    column: int
    message: str
    
    def __str__(self) -> str:
        return f"  line {self.line}: {self.message}"


class ChipLinter(ast.NodeVisitor):
    """AST visitor that checks for forbidden constructs."""
    
    def __init__(self, chip_name: str, enforce_no_conditionals: bool = True):
        self.chip_name = chip_name
        self.enforce_no_conditionals = enforce_no_conditionals
        self.violations: list[Violation] = []
        self.allowed_imports = ALLOWED_IMPORTS.get(chip_name, set())
        
    def add_violation(self, node: ast.AST, message: str) -> None:
        self.violations.append(Violation(
            line=getattr(node, 'lineno', 0),
            column=getattr(node, 'col_offset', 0),
            message=message
        ))
    
    def visit_BoolOp(self, node: ast.BoolOp) -> None:
        """Catch 'and' / 'or' boolean operators."""
        op_name = type(node.op).__name__
        if isinstance(node.op, ast.And):
            self.add_violation(node, "Boolean operator 'and' is forbidden - use and_gate()")
        elif isinstance(node.op, ast.Or):
            self.add_violation(node, "Boolean operator 'or' is forbidden - use or_gate()")
        self.generic_visit(node)
    
    def visit_UnaryOp(self, node: ast.UnaryOp) -> None:
        """Catch 'not' and '~' operators."""
        if isinstance(node.op, ast.Not):
            self.add_violation(node, "Boolean operator 'not' is forbidden - use not_gate()")
        elif isinstance(node.op, ast.Invert):
            self.add_violation(node, "Bitwise operator '~' is forbidden")
        self.generic_visit(node)
    
    def visit_BinOp(self, node: ast.BinOp) -> None:
        """Catch bitwise operators: &, |, ^"""
        if isinstance(node.op, ast.BitAnd):
            self.add_violation(node, "Bitwise operator '&' is forbidden - use and_gate()")
        elif isinstance(node.op, ast.BitOr):
            self.add_violation(node, "Bitwise operator '|' is forbidden - use or_gate()")
        elif isinstance(node.op, ast.BitXor):
            self.add_violation(node, "Bitwise operator '^' is forbidden - use xor_gate()")
        self.generic_visit(node)
    
    def visit_Compare(self, node: ast.Compare) -> None:
        """Catch == and != used as logic shortcuts."""
        for op in node.ops:
            if isinstance(op, ast.Eq):
                self.add_violation(node, "Comparison '==' is forbidden - can be used as XNOR shortcut")
            elif isinstance(op, ast.NotEq):
                self.add_violation(node, "Comparison '!=' is forbidden - can be used as XOR shortcut")
        self.generic_visit(node)
    
    def visit_If(self, node: ast.If) -> None:
        """Catch if/else conditionals (Chapter 1 restriction)."""
        if self.enforce_no_conditionals:
            self.add_violation(node, "Conditional 'if' is forbidden - use mux() for selection")
        self.generic_visit(node)
    
    def visit_IfExp(self, node: ast.IfExp) -> None:
        """Catch ternary expressions: x if cond else y"""
        if self.enforce_no_conditionals:
            self.add_violation(node, "Ternary expression is forbidden - use mux() for selection")
        self.generic_visit(node)
    
    def visit_Import(self, node: ast.Import) -> None:
        """Catch any non-chip imports."""
        for alias in node.names:
            self.add_violation(node, f"Import '{alias.name}' is forbidden - only chip imports allowed")
        self.generic_visit(node)
    
    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        """Check that only allowed chip imports are used."""
        if node.module is None:
            self.add_violation(node, "Relative imports are forbidden")
            return
            
        # Allow imports from chips package only
        if not node.module.startswith("chips"):
            self.add_violation(node, f"Import from '{node.module}' is forbidden - only 'chips' imports allowed")
            return
        
        # Check each imported name
        for alias in node.names:
            name = alias.name
            # The module being imported from (e.g., "chips.nand" -> "nand")
            if node.module == "chips":
                # Direct import from chips package (e.g., from chips import nand)
                imported_chip = name
            else:
                # Import from submodule (e.g., from chips.nand import nand)
                parts = node.module.split(".")
                if len(parts) >= 2:
                    imported_chip = parts[1]  # e.g., "nand" from "chips.nand"
                else:
                    imported_chip = name
            
            # nand is always allowed
            if imported_chip == "nand":
                continue
                
            # Check if this chip is allowed
            if imported_chip not in self.allowed_imports:
                if imported_chip in CHIP_ORDER:
                    idx = CHIP_ORDER.index(imported_chip)
                    self.add_violation(
                        node, 
                        f"Import '{imported_chip}' not allowed - it comes after '{self.chip_name}' in build order"
                    )
                else:
                    self.add_violation(node, f"Import '{imported_chip}' is not a recognized chip")
        
        self.generic_visit(node)


def lint_file(filepath: Path, enforce_no_conditionals: bool = True) -> list[Violation]:
    """
    Lint a single chip file.
    
    Args:
        filepath: Path to the chip file
        enforce_no_conditionals: Whether to forbid if/else (True for Chapter 1)
        
    Returns:
        List of violations found
    """
    # Extract chip name from filename
    chip_name = filepath.stem  # e.g., "not_gate" from "not_gate.py"
    
    # Skip nand.py - it's the primitive
    if chip_name == "nand":
        return []
    
    # Skip __init__.py
    if chip_name == "__init__":
        return []
    
    try:
        source = filepath.read_text()
        tree = ast.parse(source, filename=str(filepath))
    except SyntaxError as e:
        return [Violation(e.lineno or 0, e.offset or 0, f"Syntax error: {e.msg}")]
    
    linter = ChipLinter(chip_name, enforce_no_conditionals)
    linter.visit(tree)
    
    return linter.violations


def lint_chips_directory(chips_dir: Path, enforce_no_conditionals: bool = True) -> dict[str, list[Violation]]:
    """
    Lint all chip files in a directory.
    
    Args:
        chips_dir: Path to the chips directory
        enforce_no_conditionals: Whether to forbid if/else
        
    Returns:
        Dict mapping chip names to their violations
    """
    results: dict[str, list[Violation]] = {}
    
    for chip_name in CHIP_ORDER:
        if chip_name == "nand":
            continue  # Skip the primitive
            
        filepath = chips_dir / f"{chip_name}.py"
        if filepath.exists():
            violations = lint_file(filepath, enforce_no_conditionals)
            if violations:
                results[chip_name] = violations
    
    return results


def print_lint_results(results: dict[str, list[Violation]], verbose: bool = True) -> bool:
    """
    Print lint results in a readable format.
    
    Returns:
        True if all files passed, False if there were violations
    """
    if not results:
        if verbose:
            print("LINT: All chips passed!")
        return True
    
    print("LINT VIOLATIONS:")
    print("-" * 50)
    
    for chip_name, violations in results.items():
        print(f"\n{chip_name}.py:")
        for v in violations:
            print(f"  {v}")
    
    print()
    print("-" * 50)
    print(f"LINT FAILED: {len(results)} file(s) have violations")
    print("Fix violations before tests can run.")
    
    return False


def main():
    """CLI entry point for the linter."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Lint NAND2TETRIS chip files")
    parser.add_argument(
        "path",
        nargs="?",
        default="chips",
        help="Path to chips directory or specific chip file"
    )
    parser.add_argument(
        "--allow-conditionals",
        action="store_true",
        help="Allow if/else conditionals (disable Chapter 1 restriction)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )
    
    args = parser.parse_args()
    path = Path(args.path)
    enforce_no_conditionals = not args.allow_conditionals
    
    if path.is_file():
        violations = lint_file(path, enforce_no_conditionals)
        results = {path.stem: violations} if violations else {}
    elif path.is_dir():
        results = lint_chips_directory(path, enforce_no_conditionals)
    else:
        print(f"Error: {path} not found")
        sys.exit(1)
    
    success = print_lint_results(results, args.verbose)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

