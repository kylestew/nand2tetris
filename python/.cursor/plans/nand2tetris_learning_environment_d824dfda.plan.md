---
name: Nand2Tetris Learning Environment
overview: Build a modular Python-based learning environment for Nand2Tetris Part 1, with NAND as the sole primitive, AST-enforced constraints, and one file per chip that students implement progressively.
todos:
  - id: chips-dir
    content: Create chips/ directory with __init__.py and nand.py primitive
    status: completed
  - id: basic-gates
    content: "Create stub files for basic gates: not, and, or, xor, mux, dmux"
    status: completed
  - id: multibit-chips
    content: "Create stub files for 16-bit chips: not16, and16, or16, mux16"
    status: completed
  - id: multiway-chips
    content: "Create stub files for multi-way chips: or8way, mux4way16, mux8way16, dmux4way, dmux8way"
    status: completed
  - id: ast-linter
    content: Create chip_linter.py with AST-based enforcement of NAND-only rules
    status: completed
  - id: stubs-dir
    content: Create stubs/ directory with original templates for --restart functionality
    status: completed
    dependencies:
      - basic-gates
      - multibit-chips
      - multiway-chips
  - id: test-harness
    content: Create test_harness.py with lint, test, progression display, and restart
    status: completed
    dependencies:
      - stubs-dir
      - ast-linter
  - id: readme
    content: Create README.md with course instructions and how to run tests
    status: completed
    dependencies:
      - test-harness
---

# Nand2Tetris Part 1 Learning Environment

## Architecture

```
python/
├── chips/
│   ├── __init__.py          # Exports all chips
│   ├── nand.py              # The ONLY primitive (provided)
│   ├── not_gate.py          # Student implements
│   ├── and_gate.py
│   ├── or_gate.py
│   ├── xor_gate.py
│   ├── mux.py
│   ├── dmux.py
│   ├── not16.py
│   ├── and16.py
│   ├── or16.py
│   ├── mux16.py
│   ├── or8way.py
│   ├── mux4way16.py
│   ├── mux8way16.py
│   ├── dmux4way.py
│   └── dmux8way.py
├── stubs/                   # Original stub templates (for --restart)
│   └── (copies of all chip stubs)
├── chip_linter.py           # AST-based rule enforcement
├── test_harness.py          # Main test runner (lint + tests + restart)
└── README.md                # Course instructions
```



## Design Principles

1. **NAND is sacred** - `chips/nand.py` is the only file with a working implementation. All other chips import from `nand` or previously-built chips.
2. **AST-enforced constraints** - A linter runs BEFORE tests to reject any cheating at the syntax level.
3. **Progressive building** - Each chip file imports only from chips that come before it in the course order.
4. **Buses are tuples** - Multi-bit values use `tuple[bool, ...]` for immutability and clean indexing.
5. **Clear contracts** - Each chip file contains:

- Function signature with type hints
- Truth table in docstring
- Hints for implementation
- A `pass` stub for students to fill in

## Data Types

| Type | Representation | Example |
|------|----------------|---------|
| Single bit | `bool` | `True`, `False` |
| 16-bit bus | `tuple[bool, ...]` | `(False, True, False, ...)` |
| 8-bit bus | `tuple[bool, ...]` | `(True, False, ...)` |
| 2-bit selector | `tuple[bool, bool]` | `(False, True)` |
| 3-bit selector | `tuple[bool, bool, bool]` | `(True, False, True)` |

Indexing convention: `bus[0]` is LSB (least significant bit), `bus[15]` is MSB.

```python
# Example: Not16 applies NOT to each bit
def not16(a: tuple[bool, ...]) -> tuple[bool, ...]:
    return tuple(not_gate(a[i]) for i in range(16))
```

## First 15 Chips (Chapter 1: Boolean Logic)

| Order | Chip | Inputs | Outputs | Can Use ||-------|------|--------|---------|---------|| 1 | Not | a | out | nand || 2 | And | a, b | out | nand, not || 3 | Or | a, b | out | nand, not, and || 4 | Xor | a, b | out | all above || 5 | Mux | a, b, sel | out | all above || 6 | DMux | in, sel | a, b | all above || 7 | Not16 | in[16] | out[16] | all above || 8 | And16 | a[16], b[16] | out[16] | all above || 9 | Or16 | a[16], b[16] | out[16] | all above || 10 | Mux16 | a[16], b[16], sel | out[16] | all above || 11 | Or8Way | in[8] | out | all above || 12 | Mux4Way16 | a-d[16], sel[2] | out[16] | all above || 13 | Mux8Way16 | a-h[16], sel[3] | out[16] | all above || 14 | DMux4Way | in, sel[2] | a, b, c, d | all above || 15 | DMux8Way | in, sel[3] | a-h | all above |

## AST Linter (Critical Enforcement)

The linter (`chip_linter.py`) uses Python's `ast` module to parse each chip file and reject violations BEFORE running any tests. This is the core mechanism that makes the learning environment actually work.

### Forbidden Constructs

| Category | Forbidden | Why |
|----------|-----------|-----|
| Boolean operators | `and`, `or`, `not` | Must use gates instead |
| Bitwise operators | `&`, `\|`, `^`, `~` | Prevents bit-twiddling shortcuts |
| Conditionals | `if`/`else` (Ch1 only) | Forces pure gate composition |
| Comparisons as logic | `a == b`, `a != b` | Can't use equality as XOR/XNOR |
| Illegal imports | Anything not in allowed list | Can only use previously-built chips |

### Per-Chip Allowed Imports

Each chip declares what it can import. The linter enforces this:

```python
# Chip: not_gate
# Allowed: nand

# Chip: and_gate  
# Allowed: nand, not_gate

# Chip: or_gate
# Allowed: nand, not_gate, and_gate
# ... and so on
```

### Linter Output Example

```
LINT: not_gate.py
  VIOLATION line 12: Boolean operator 'and' is forbidden
  VIOLATION line 15: Import 'or_gate' not allowed (not yet built)
  
LINT FAILED: Fix violations before tests can run
```

## Test Harness Design

The test harness runs in two phases:

**Phase 1: Lint** - AST validation (must pass before Phase 2)
**Phase 2: Test** - Truth table verification

Features:
- Auto-discover all chip files in `chips/`
- Run linter FIRST - reject cheating before testing correctness
- Run truth table tests for each chip in order
- Show clear PASS/FAIL status with progress tracking
- Use colorized output for clarity
- **Restart command** - reset all chips to stub state
- **Progression tracking** - celebrate milestones and show overall progress

```bash
# Run all tests (lint + truth tables)
python test_harness.py

# Run specific chip test
python test_harness.py not
python test_harness.py mux16

# Lint only (no tests)
python test_harness.py --lint-only

# Reset to starting state (clears all implementations)
python test_harness.py --restart
```

### Progression Display

The harness shows clear progress through the course:

```
============================================================
  NAND2TETRIS - Chapter 1: Boolean Logic
============================================================

  [✓] 1. Not        PASSED
  [✓] 2. And        PASSED  
  [✓] 3. Or         PASSED
  [✓] 4. Xor        PASSED
  [→] 5. Mux        FAILED (3/4 cases)
  [ ] 6. DMux       not yet implemented
  [ ] 7. Not16      not yet implemented
  ...

------------------------------------------------------------
  Progress: 4/15 chips complete (27%)
  
  ★ Milestone: Basic gates complete! 
    You've built NOT, AND, OR, XOR from scratch.
    Next up: Multiplexers and Demultiplexers
------------------------------------------------------------
```

### Milestone Celebrations

| After | Milestone |
|-------|-----------|
| Chip 4 (Xor) | "Basic gates complete! You built NOT, AND, OR, XOR from NAND." |
| Chip 6 (DMux) | "Routing complete! You can now select and distribute signals." |
| Chip 10 (Mux16) | "16-bit operations unlocked! Your chips now handle words." |
| Chip 15 (DMux8Way) | "Chapter 1 COMPLETE! You've built all Boolean logic chips." |

### Restart Command

`python test_harness.py --restart` will:
1. Prompt for confirmation ("This will erase all your implementations. Continue? [y/N]")
2. Replace each chip file with its original stub template
3. Keep `nand.py` untouched (it's the primitive)
4. Report what was reset

```
$ python test_harness.py --restart
This will erase all your implementations. Continue? [y/N] y

Resetting chips to starting state...
  ✓ not_gate.py reset
  ✓ and_gate.py reset
  ✓ or_gate.py reset
  ... (15 files reset)

All chips reset to stubs. Run 'python test_harness.py' to begin again.
```




## Example Chip File Structure

Each chip file follows a consistent pattern:

```python
# chips/not_gate.py
"""NOT gate - inverts input signal."""
from chips.nand import nand

def not_gate(a: bool) -> bool:
    """
    NOT gate (inverter)
    
    Truth table:
        a | out
        --|----
        0 |  1
        1 |  0
    
    Allowed chips: nand
    Hint: What happens when you NAND a signal with itself?
    """
    # YOUR IMPLEMENTATION HERE
    pass
```



## Implementation Tasks

1. Create `chips/` directory structure with `__init__.py`
2. Create `chips/nand.py` with the working NAND primitive
3. Create stub files for all 15 chips with truth tables and hints
4. Create `stubs/` directory with copies of original templates (for `--restart`)
5. Create `chip_linter.py` with AST-based rule enforcement
6. Create `test_harness.py` with lint, tests, progression tracking, and restart
7. Create `README.md` with course workflow and instructions