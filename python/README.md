# NAND2TETRIS Learning Environment

Build a complete computer from first principles, starting with just the NAND gate.

This is a Python-based implementation of Part 1 of the [Nand2Tetris](https://www.nand2tetris.org/) course (Hardware), focusing on Chapter 1: Boolean Logic.

## The Challenge

**NAND is the only gate provided to you.** Everything else must be built from scratch.

You cannot use Python's boolean operators (`and`, `or`, `not`) or bitwise operators (`&`, `|`, `^`, `~`). The system enforces this with an AST linter that runs before every test.

## Quick Start

```bash
# Run all tests to see your progress
python test_harness.py

# Test a specific chip
python test_harness.py not
python test_harness.py mux16

# Lint only (check for forbidden constructs)
python test_harness.py --lint-only

# Start over from scratch
python test_harness.py --restart
```

## Project Structure

```
python/
├── chips/                 # Your chip implementations (edit these!)
│   ├── nand.py           # The ONLY primitive (do not edit)
│   ├── not_gate.py       # ← Start here
│   ├── and_gate.py
│   ├── or_gate.py
│   └── ...
├── stubs/                # Original templates (for --restart)
├── chip_linter.py        # AST-based rule enforcement
├── test_harness.py       # Test runner
└── README.md
```

## Chapter 1: Boolean Logic (15 Chips)

Work through these in order. Each chip can only use chips that come before it.

| # | Chip | Description | Can Use |
|---|------|-------------|---------|
| 1 | `not_gate` | Inverter | nand |
| 2 | `and_gate` | AND gate | nand, not |
| 3 | `or_gate` | OR gate | nand, not, and |
| 4 | `xor_gate` | Exclusive OR | all above |
| 5 | `mux` | 2-way Multiplexer | all above |
| 6 | `dmux` | 2-way Demultiplexer | all above |
| 7 | `not16` | 16-bit NOT | all above |
| 8 | `and16` | 16-bit AND | all above |
| 9 | `or16` | 16-bit OR | all above |
| 10 | `mux16` | 16-bit MUX | all above |
| 11 | `or8way` | 8-way OR | all above |
| 12 | `mux4way16` | 4-way 16-bit MUX | all above |
| 13 | `mux8way16` | 8-way 16-bit MUX | all above |
| 14 | `dmux4way` | 4-way DMUX | all above |
| 15 | `dmux8way` | 8-way DMUX | all above |

## How to Implement a Chip

1. Open the chip file in `chips/` directory
2. Read the docstring for the truth table and hints
3. Replace `pass` with your implementation
4. Run `python test_harness.py` to check your work

### Example: Implementing NOT

```python
# chips/not_gate.py
from chips.nand import nand

def not_gate(a: bool) -> bool:
    # NAND(a, a) = NOT(a AND a) = NOT(a)
    return nand(a, a)
```

### Example: Implementing AND

```python
# chips/and_gate.py
from chips.nand import nand
from chips.not_gate import not_gate

def and_gate(a: bool, b: bool) -> bool:
    # AND = NOT(NAND)
    return not_gate(nand(a, b))
```

## Data Types

| Type | Python Type | Example |
|------|-------------|---------|
| Single bit | `bool` | `True`, `False` |
| 16-bit bus | `tuple[bool, ...]` | `(False, True, False, ...)` |
| 2-bit selector | `tuple[bool, bool]` | `(False, True)` |
| 3-bit selector | `tuple[bool, bool, bool]` | `(True, False, True)` |

**Bus indexing:** `bus[0]` is LSB (least significant bit), `bus[15]` is MSB.

### Working with 16-bit Buses

```python
# NOT16 - apply NOT to each bit
def not16(a: tuple[bool, ...]) -> tuple[bool, ...]:
    return tuple(not_gate(a[i]) for i in range(16))
```

## Rules (Enforced by Linter)

The linter automatically checks your code before tests run. These are forbidden:

| Forbidden | Why | Use Instead |
|-----------|-----|-------------|
| `and`, `or`, `not` | Boolean operators | `and_gate()`, `or_gate()`, `not_gate()` |
| `&`, `\|`, `^`, `~` | Bitwise operators | Gate functions |
| `if`/`else` | Conditionals | `mux()` for selection |
| `==`, `!=` | Comparisons | Can be used as XOR/XNOR shortcuts |

If you try to cheat, you'll see:

```
LINT VIOLATIONS:
--------------------------------------------------

not_gate.py:
  line 12: Boolean operator 'not' is forbidden - use not_gate()

LINT FAILED: Fix violations before tests can run.
```

## Milestones

As you progress, you'll hit milestones:

- **Chips 1-4**: Basic gates complete! You've built NOT, AND, OR, XOR from NAND.
- **Chips 5-6**: Routing complete! You can select and distribute signals.
- **Chips 7-10**: 16-bit operations unlocked! Your chips handle words.
- **Chips 11-15**: CHAPTER 1 COMPLETE! All Boolean logic chips built!

## Tips

1. **Start simple**: NOT is just `nand(a, a)`
2. **Use truth tables**: Compare your output to expected values
3. **Think in gates**: Draw the circuit on paper first
4. **Read the hints**: Each chip file has implementation hints

### Useful Identities

- `NOT(a) = NAND(a, a)`
- `AND(a, b) = NOT(NAND(a, b))`
- `OR(a, b) = NAND(NOT(a), NOT(b))` (De Morgan's law)
- `XOR(a, b) = OR(AND(a, NOT(b)), AND(NOT(a), b))`
- `MUX(a, b, sel) = OR(AND(a, NOT(sel)), AND(b, sel))`

## Troubleshooting

**"Import error"**: Make sure you're running from the project root directory.

**"Function returns None"**: You haven't implemented the chip yet (still has `pass`).

**Lint violation**: You used a forbidden construct. Rewrite using only gate functions.

**Test fails**: Check your logic against the truth table in the docstring.

## Starting Over

If you want to reset and try again:

```bash
python test_harness.py --restart
```

This will restore all chip files to their original stub state.

## Resources

- [Nand2Tetris Course](https://www.nand2tetris.org/)
- [Course Textbook](https://www.nand2tetris.org/book)
- [Boolean Algebra](https://en.wikipedia.org/wiki/Boolean_algebra)
- [De Morgan's Laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws)

---

Good luck! Remember: every computer ever built is made of gates like these.

