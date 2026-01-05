#!/usr/bin/env python3
"""
NAND2TETRIS Test Harness

Two-phase testing:
1. LINT - AST validation (must pass before Phase 2)
2. TEST - Truth table verification

Usage:
    python test_harness.py           # Run all tests
    python test_harness.py not       # Test specific chip
    python test_harness.py --lint-only   # Lint only
    python test_harness.py --restart     # Reset all chips to stubs
"""

import sys
import shutil
import importlib
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import Callable, Any, Optional

from chip_linter import lint_chips_directory, print_lint_results, CHIP_ORDER


# =============================================================================
# CONFIGURATION
# =============================================================================

CHIPS_DIR = Path(__file__).parent / "chips"
STUBS_DIR = Path(__file__).parent / "stubs"

# Milestones - chip index (0-based) -> (title, message)
# Note: index 0 is NAND (the primitive), so NOT is index 1, etc.
MILESTONES = {
    4: ("Basic Gates Complete!", "You've built NOT, AND, OR, XOR from NAND."),
    6: (
        "Routing Complete!",
        "You can now select and distribute signals with MUX/DMUX.",
    ),
    10: ("16-bit Operations Unlocked!", "Your chips now handle 16-bit words."),
    15: ("CHAPTER 1 COMPLETE!", "You've built ALL Boolean logic chips from scratch!"),
}


# =============================================================================
# TRUTH TABLES
# =============================================================================


@dataclass
class ChipTest:
    """Test specification for a chip."""

    name: str
    func_name: str
    truth_table: list[tuple]  # (*inputs, expected_output)
    description: str


def make_bus16(*bits: int) -> tuple[bool, ...]:
    """Create a 16-bit bus from individual bits (LSB first)."""
    if len(bits) == 1:
        # Single int - convert to 16-bit binary
        n = bits[0]
        return tuple((n >> i) & 1 == 1 for i in range(16))
    return tuple(bool(b) for b in bits) + (False,) * (16 - len(bits))


def make_bus8(*bits: int) -> tuple[bool, ...]:
    """Create an 8-bit bus from individual bits (LSB first)."""
    if len(bits) == 1:
        n = bits[0]
        return tuple((n >> i) & 1 == 1 for i in range(8))
    return tuple(bool(b) for b in bits) + (False,) * (8 - len(bits))


# All zeros and all ones for 16-bit
ZEROS16 = make_bus16(0)
ONES16 = make_bus16(0xFFFF)
ALT16_A = make_bus16(0xAAAA)  # 1010...
ALT16_B = make_bus16(0x5555)  # 0101...


CHIP_TESTS: list[ChipTest] = [
    # 0. NAND (the primitive - provided to you)
    ChipTest(
        name="nand",
        func_name="nand",
        truth_table=[
            (False, False, True),
            (False, True, True),
            (True, False, True),
            (True, True, False),
        ],
        description="NAND gate (THE PRIMITIVE)",
    ),
    # 1. NOT
    ChipTest(
        name="not_gate",
        func_name="not_gate",
        truth_table=[
            (False, True),
            (True, False),
        ],
        description="NOT gate (inverter)",
    ),
    # 2. AND
    ChipTest(
        name="and_gate",
        func_name="and_gate",
        truth_table=[
            (False, False, False),
            (False, True, False),
            (True, False, False),
            (True, True, True),
        ],
        description="AND gate",
    ),
    # 3. OR
    ChipTest(
        name="or_gate",
        func_name="or_gate",
        truth_table=[
            (False, False, False),
            (False, True, True),
            (True, False, True),
            (True, True, True),
        ],
        description="OR gate",
    ),
    # 4. XOR
    ChipTest(
        name="xor_gate",
        func_name="xor_gate",
        truth_table=[
            (False, False, False),
            (False, True, True),
            (True, False, True),
            (True, True, False),
        ],
        description="XOR gate (exclusive or)",
    ),
    # 5. MUX
    ChipTest(
        name="mux",
        func_name="mux",
        truth_table=[
            # a, b, sel -> out
            (False, False, False, False),
            (False, True, False, False),
            (True, False, False, True),
            (True, True, False, True),
            (False, False, True, False),
            (False, True, True, True),
            (True, False, True, False),
            (True, True, True, True),
        ],
        description="2-way Multiplexer",
    ),
    # 6. DMUX
    ChipTest(
        name="dmux",
        func_name="dmux",
        truth_table=[
            # inp, sel -> (a, b)
            (False, False, (False, False)),
            (True, False, (True, False)),
            (False, True, (False, False)),
            (True, True, (False, True)),
        ],
        description="2-way Demultiplexer",
    ),
    # 7. NOT16
    ChipTest(
        name="not16",
        func_name="not16",
        truth_table=[
            (ZEROS16, ONES16),
            (ONES16, ZEROS16),
            (ALT16_A, ALT16_B),
            (ALT16_B, ALT16_A),
        ],
        description="16-bit NOT",
    ),
    # 8. AND16
    ChipTest(
        name="and16",
        func_name="and16",
        truth_table=[
            (ZEROS16, ZEROS16, ZEROS16),
            (ONES16, ONES16, ONES16),
            (ZEROS16, ONES16, ZEROS16),
            (ALT16_A, ALT16_B, ZEROS16),
            (ALT16_A, ONES16, ALT16_A),
        ],
        description="16-bit AND",
    ),
    # 9. OR16
    ChipTest(
        name="or16",
        func_name="or16",
        truth_table=[
            (ZEROS16, ZEROS16, ZEROS16),
            (ONES16, ONES16, ONES16),
            (ZEROS16, ONES16, ONES16),
            (ALT16_A, ALT16_B, ONES16),
            (ALT16_A, ZEROS16, ALT16_A),
        ],
        description="16-bit OR",
    ),
    # 10. MUX16
    ChipTest(
        name="mux16",
        func_name="mux16",
        truth_table=[
            # a, b, sel -> out
            (ZEROS16, ONES16, False, ZEROS16),
            (ZEROS16, ONES16, True, ONES16),
            (ALT16_A, ALT16_B, False, ALT16_A),
            (ALT16_A, ALT16_B, True, ALT16_B),
        ],
        description="16-bit Multiplexer",
    ),
    # 11. OR8WAY
    ChipTest(
        name="or8way",
        func_name="or8way",
        truth_table=[
            (make_bus8(0b00000000), False),
            (make_bus8(0b00000001), True),
            (make_bus8(0b10000000), True),
            (make_bus8(0b00010000), True),
            (make_bus8(0b11111111), True),
        ],
        description="8-way OR",
    ),
    # 12. MUX4WAY16
    ChipTest(
        name="mux4way16",
        func_name="mux4way16",
        truth_table=[
            # a, b, c, d, sel -> out
            (
                make_bus16(1),
                make_bus16(2),
                make_bus16(3),
                make_bus16(4),
                (False, False),
                make_bus16(1),
            ),
            (
                make_bus16(1),
                make_bus16(2),
                make_bus16(3),
                make_bus16(4),
                (True, False),
                make_bus16(2),
            ),
            (
                make_bus16(1),
                make_bus16(2),
                make_bus16(3),
                make_bus16(4),
                (False, True),
                make_bus16(3),
            ),
            (
                make_bus16(1),
                make_bus16(2),
                make_bus16(3),
                make_bus16(4),
                (True, True),
                make_bus16(4),
            ),
        ],
        description="4-way 16-bit Multiplexer",
    ),
    # 13. MUX8WAY16
    ChipTest(
        name="mux8way16",
        func_name="mux8way16",
        truth_table=[
            # a-h, sel -> out
            (
                make_bus16(1),
                make_bus16(2),
                make_bus16(3),
                make_bus16(4),
                make_bus16(5),
                make_bus16(6),
                make_bus16(7),
                make_bus16(8),
                (False, False, False),
                make_bus16(1),
            ),
            (
                make_bus16(1),
                make_bus16(2),
                make_bus16(3),
                make_bus16(4),
                make_bus16(5),
                make_bus16(6),
                make_bus16(7),
                make_bus16(8),
                (True, False, False),
                make_bus16(2),
            ),
            (
                make_bus16(1),
                make_bus16(2),
                make_bus16(3),
                make_bus16(4),
                make_bus16(5),
                make_bus16(6),
                make_bus16(7),
                make_bus16(8),
                (False, True, False),
                make_bus16(3),
            ),
            (
                make_bus16(1),
                make_bus16(2),
                make_bus16(3),
                make_bus16(4),
                make_bus16(5),
                make_bus16(6),
                make_bus16(7),
                make_bus16(8),
                (True, True, True),
                make_bus16(8),
            ),
        ],
        description="8-way 16-bit Multiplexer",
    ),
    # 14. DMUX4WAY
    ChipTest(
        name="dmux4way",
        func_name="dmux4way",
        truth_table=[
            # inp, sel -> (a, b, c, d)
            (True, (False, False), (True, False, False, False)),
            (True, (True, False), (False, True, False, False)),
            (True, (False, True), (False, False, True, False)),
            (True, (True, True), (False, False, False, True)),
            (False, (False, False), (False, False, False, False)),
        ],
        description="4-way Demultiplexer",
    ),
    # 15. DMUX8WAY
    ChipTest(
        name="dmux8way",
        func_name="dmux8way",
        truth_table=[
            # inp, sel -> (a, b, c, d, e, f, g, h)
            (
                True,
                (False, False, False),
                (True, False, False, False, False, False, False, False),
            ),
            (
                True,
                (True, False, False),
                (False, True, False, False, False, False, False, False),
            ),
            (
                True,
                (False, True, False),
                (False, False, True, False, False, False, False, False),
            ),
            (
                True,
                (True, True, False),
                (False, False, False, True, False, False, False, False),
            ),
            (
                True,
                (False, False, True),
                (False, False, False, False, True, False, False, False),
            ),
            (
                True,
                (True, True, True),
                (False, False, False, False, False, False, False, True),
            ),
            (
                False,
                (False, False, False),
                (False, False, False, False, False, False, False, False),
            ),
        ],
        description="8-way Demultiplexer",
    ),
]


# =============================================================================
# TEST RUNNER
# =============================================================================


@dataclass
class TestResult:
    """Result of testing a single chip."""

    name: str
    passed: bool
    total_cases: int
    passed_cases: int
    error: Optional[str] = None
    not_implemented: bool = False


def test_chip(test: ChipTest) -> TestResult:
    """Test a single chip against its truth table."""
    try:
        # Dynamically import the chip module
        module = importlib.import_module(f"chips.{test.name}")
        # Reload in case it was modified
        importlib.reload(module)
        func = getattr(module, test.func_name)
    except ImportError as e:
        return TestResult(
            name=test.name,
            passed=False,
            total_cases=len(test.truth_table),
            passed_cases=0,
            error=f"Import error: {e}",
        )
    except AttributeError:
        return TestResult(
            name=test.name,
            passed=False,
            total_cases=len(test.truth_table),
            passed_cases=0,
            error=f"Function '{test.func_name}' not found",
        )

    passed_cases = 0
    total_cases = len(test.truth_table)

    for case in test.truth_table:
        *inputs, expected = case
        try:
            result = func(*inputs)
            if result == expected:
                passed_cases += 1
        except NotImplementedError:
            # Stub raises NotImplementedError - not started yet
            return TestResult(
                name=test.name,
                passed=False,
                total_cases=total_cases,
                passed_cases=0,
                not_implemented=True,
            )
        except Exception as e:
            return TestResult(
                name=test.name,
                passed=False,
                total_cases=total_cases,
                passed_cases=passed_cases,
                error=f"{type(e).__name__}: {e}",
            )

    return TestResult(
        name=test.name,
        passed=passed_cases == total_cases,
        total_cases=total_cases,
        passed_cases=passed_cases,
    )


# =============================================================================
# DISPLAY
# =============================================================================


# ANSI colors
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    DIM = "\033[2m"


def print_header():
    """Print the test harness header."""
    print()
    print("=" * 60)
    print(f"  {Colors.BOLD}NAND2TETRIS - Chapter 1: Boolean Logic{Colors.RESET}")
    print("=" * 60)
    print()


def print_results(results: list[TestResult]):
    """Print test results with progress tracking."""
    # NAND (index 0) is always provided, so don't count it in user progress
    user_results = results[1:]  # Skip NAND for progress counting
    completed = sum(1 for r in user_results if r.passed)
    total = len(user_results)

    # Find the first failing test (skip NAND at index 0)
    first_fail_idx = next(
        (i for i, r in enumerate(results) if not r.passed and i > 0), None
    )

    for i, result in enumerate(results):
        num = i  # NAND is 0, NOT is 1, etc.
        name = result.name.ljust(12)

        # Special handling for NAND (the primitive)
        if result.name == "nand":
            status = f"{Colors.CYAN}PROVIDED (the primitive){Colors.RESET}"
            marker = f"{Colors.CYAN}[★]{Colors.RESET}"
            print(f"  {marker}  {num}. {name} {status}")
            continue

        if result.passed:
            status = f"{Colors.GREEN}PASSED{Colors.RESET}"
            marker = f"{Colors.GREEN}[✓]{Colors.RESET}"
        elif result.not_implemented:
            status = f"{Colors.DIM}not yet implemented{Colors.RESET}"
            marker = f"{Colors.DIM}[ ]{Colors.RESET}"
        elif result.error:
            status = f"{Colors.RED}ERROR: {result.error}{Colors.RESET}"
            marker = f"{Colors.RED}[✗]{Colors.RESET}"
        else:
            status = f"{Colors.YELLOW}FAILED ({result.passed_cases}/{result.total_cases} cases){Colors.RESET}"
            marker = f"{Colors.YELLOW}[→]{Colors.RESET}"

        # Current chip indicator
        if i == first_fail_idx:
            print(f"  {marker} {num:2}. {Colors.BOLD}{name}{Colors.RESET} {status}")
        else:
            print(f"  {marker} {num:2}. {name} {status}")

    # Progress bar
    print()
    print("-" * 60)
    pct = int(completed / total * 100) if total > 0 else 0
    bar_width = 40
    filled = int(bar_width * completed / total) if total > 0 else 0
    bar = "█" * filled + "░" * (bar_width - filled)
    print(f"  Progress: [{bar}] {completed}/{total} chips ({pct}%)")

    # Check for milestones (index is chip index in CHIP_TESTS)
    # Milestone triggers when that chip passes
    achieved_milestones = []
    for chip_idx, (title, msg) in MILESTONES.items():
        if chip_idx < len(results) and results[chip_idx].passed:
            achieved_milestones.append((chip_idx, title, msg))

    # Show the most recent achieved milestone
    if achieved_milestones:
        _, title, msg = max(achieved_milestones, key=lambda x: x[0])
        print()
        print(f"  {Colors.CYAN}★ {title}{Colors.RESET}")
        print(f"    {msg}")

    # Next chip hint
    if first_fail_idx is not None and first_fail_idx < len(CHIP_TESTS):
        next_chip = CHIP_TESTS[first_fail_idx]
        print()
        print(
            f"  {Colors.DIM}Next: {next_chip.description} ({next_chip.name}.py){Colors.RESET}"
        )

    print("-" * 60)
    print()


def print_single_result(result: TestResult, test: ChipTest):
    """Print result for a single chip test."""
    print()
    print(f"Testing: {test.description} ({test.name}.py)")
    print("-" * 40)

    if result.passed:
        print(
            f"{Colors.GREEN}✓ PASSED{Colors.RESET} - All {result.total_cases} test cases passed!"
        )
    elif result.not_implemented:
        print(f"{Colors.YELLOW}○ NOT IMPLEMENTED{Colors.RESET} - Function returns None")
        print(f"  Edit chips/{test.name}.py to implement this chip.")
    elif result.error:
        print(f"{Colors.RED}✗ ERROR{Colors.RESET} - {result.error}")
    else:
        print(
            f"{Colors.YELLOW}✗ FAILED{Colors.RESET} - {result.passed_cases}/{result.total_cases} cases passed"
        )
    print()


# =============================================================================
# RESTART FUNCTIONALITY
# =============================================================================


def restart_chips():
    """Reset all chip files to their original stub state."""
    print()
    print("This will erase ALL your chip implementations.")
    response = input("Continue? [y/N] ").strip().lower()

    if response != "y":
        print("Cancelled.")
        return False

    print()
    print("Resetting chips to starting state...")

    reset_count = 0
    for chip_name in CHIP_ORDER:
        if chip_name == "nand":
            continue  # Don't reset the primitive

        stub_file = STUBS_DIR / f"{chip_name}.py"
        chip_file = CHIPS_DIR / f"{chip_name}.py"

        if stub_file.exists():
            shutil.copy(stub_file, chip_file)
            print(f"  ✓ {chip_name}.py reset")
            reset_count += 1
        else:
            print(f"  ? {chip_name}.py - stub not found")

    print()
    print(f"Reset {reset_count} chip(s) to stubs.")
    print("Run 'python test_harness.py' to begin again.")
    print()
    return True


# =============================================================================
# MAIN
# =============================================================================


def main():
    parser = argparse.ArgumentParser(
        description="NAND2TETRIS Test Harness",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python test_harness.py           Run all tests
  python test_harness.py not       Test specific chip
  python test_harness.py --lint-only   Lint only, no tests
  python test_harness.py --restart     Reset all chips to stubs
        """,
    )
    parser.add_argument(
        "chip", nargs="?", help="Specific chip to test (e.g., 'not', 'mux16')"
    )
    parser.add_argument(
        "--lint-only", action="store_true", help="Run linter only, skip tests"
    )
    parser.add_argument(
        "--restart", action="store_true", help="Reset all chips to original stub state"
    )
    parser.add_argument(
        "--no-lint", action="store_true", help="Skip linting (not recommended)"
    )

    args = parser.parse_args()

    # Handle restart
    if args.restart:
        restart_chips()
        return

    # Run linter first (unless skipped)
    if not args.no_lint:
        lint_results = lint_chips_directory(CHIPS_DIR)
        if lint_results:
            print()
            print_lint_results(lint_results)
            if not args.lint_only:
                print("Fix lint violations before running tests.")
            sys.exit(1)
        elif args.lint_only:
            print()
            print(f"{Colors.GREEN}LINT: All chips passed!{Colors.RESET}")
            print()
            sys.exit(0)

    # Single chip test
    if args.chip:
        # Find the test
        chip_name = args.chip.lower().replace("-", "_")
        # Handle short names
        if chip_name == "not":
            chip_name = "not_gate"
        elif chip_name == "and":
            chip_name = "and_gate"
        elif chip_name == "or":
            chip_name = "or_gate"
        elif chip_name == "xor":
            chip_name = "xor_gate"

        test = next((t for t in CHIP_TESTS if t.name == chip_name), None)
        if not test:
            print(f"Unknown chip: {args.chip}")
            print(f"Available chips: {', '.join(t.name for t in CHIP_TESTS)}")
            sys.exit(1)

        result = test_chip(test)
        print_single_result(result, test)
        sys.exit(0 if result.passed else 1)

    # Run all tests
    print_header()

    results = [test_chip(test) for test in CHIP_TESTS]
    print_results(results)

    all_passed = all(r.passed for r in results)
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
