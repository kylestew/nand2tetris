# NAND2TETRIS Learning Environment

Build a complete computer from first principles, starting with just the NAND gate.

This is a Python-based implementation of Part 1 of the [Nand2Tetris](https://www.nand2tetris.org/) course (Hardware), covering:
- **Chapter 1:** Boolean Logic
- **Chapter 2:** Boolean Arithmetic
- **Chapter 3:** Sequential Logic

## The Challenge

**NAND is the only logic gate provided to you.** Everything else must be built from scratch.

**DFF is the only memory element provided to you.** All sequential chips are built using it.

You cannot use Python's boolean operators (`and`, `or`, `not`) or bitwise operators (`&`, `|`, `^`, `~`). The system enforces this with an AST linter that runs before every test.

## Quick Start

```bash
# Run all tests to see your progress
python verify.py

# Test a specific chip
python verify.py not
python verify.py mux16
python verify.py alu
python verify.py ram8

# Watch mode (re-runs tests on file changes)
python verify.py --watch

# Lint only (check for forbidden constructs)
python verify.py --lint-only

# Start over from scratch
python verify.py --restart
```

## Project Structure

```
python/
├── chips/                 # Your chip implementations (edit these!)
│   ├── nand.py           # Logic primitive (do not edit)
│   ├── clock.py          # Clock singleton (do not edit)
│   ├── dff.py            # Memory primitive (do not edit)
│   ├── not_gate.py       # ← Start here
│   ├── and_gate.py
│   ├── or_gate.py
│   └── ...
├── stubs/                # Original templates (for --restart)
├── chip_linter.py        # AST-based rule enforcement
├── verify.py             # Test runner
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

## Chapter 2: Boolean Arithmetic (5 Chips)

Build the computational heart of your computer.

| # | Chip | Description | Can Use |
|---|------|-------------|---------|
| 16 | `half_adder` | Adds two bits | all Ch1 chips |
| 17 | `full_adder` | Adds three bits | half_adder, all Ch1 |
| 18 | `add16` | 16-bit adder | full_adder, all above |
| 19 | `inc16` | 16-bit incrementer | add16, all above |
| 20 | `alu` | Arithmetic Logic Unit | inc16, all above |

The ALU is the crown jewel—it computes 18 different functions on two 16-bit inputs using just 6 control bits.

## Chapter 3: Sequential Logic (8 Chips)

Build memory and stateful components. These chips are **classes** (not functions) because they hold state. You only need to implement:
- `__init__()` — create components (DFFs, sub-chips)
- `__call__()` — wire the combinational logic

The DFF handles all clock timing internally—just focus on how signals connect.

| # | Chip | Description | Can Use |
|---|------|-------------|---------|
| ★ | `dff` | D Flip-Flop | **PROVIDED** (the memory primitive) |
| 21 | `bit` | 1-bit register | dff, mux |
| 22 | `register` | 16-bit register | bit (x16) |
| 23 | `ram8` | 8-register RAM | register, dmux8way, mux8way16 |
| 24 | `ram64` | 64-register RAM | ram8 (x8) |
| 25 | `ram512` | 512-register RAM | ram64 (x8) |
| 26 | `ram4k` | 4K RAM | ram512 (x8) |
| 27 | `ram16k` | 16K RAM | ram4k (x4) |
| 28 | `pc` | Program Counter | register, inc16, mux16 |

### How Sequential Chips Work

Sequential chips store values across clock cycles. The test harness controls timing:

```python
from chips.clock import Clock
from chips.bit import Bit

bit = Bit()

# Set input (doesn't change output yet)
bit(inp=True, load=True)

# Clock tick advances state (handled by test harness)
Clock.get().tick()

# Now output reflects previous input
out = bit(inp=False, load=False)  # Returns True
```

**Key concept:** `out(t) = f(in(t-1))` — output at time t depends on input at time t-1.

**Your job:** Wire the components. **DFF's job:** Handle timing.

## How to Implement a Chip

1. Open the chip file in `chips/` directory
2. Read the docstring for the truth table and hints
3. Replace `raise NotImplementedError(...)` with your implementation
4. Run `python verify.py` to check your work

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

### Example: Implementing Bit (Sequential)

Sequential chips are classes that wire together components. The DFF handles all timing internally—you just specify the connections.

```python
# chips/bit.py
from chips.dff import DFF
from chips.mux import mux

class Bit:
    def __init__(self):
        self._dff = DFF()  # DFF auto-registers with Clock

    def __call__(self, inp: bool, load: bool) -> bool:
        # Read current stored value
        current = self._dff.state
        
        # Wiring: MUX selects between hold (current) or load (inp)
        dff_input = mux(current, inp, load)
        
        # Feed into DFF and return current output
        return self._dff(dff_input)
```

Notice there's no `tick()` method—the DFF handles clock synchronization automatically.

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
- **Chips 16-17**: Adders complete! You can now add binary numbers.
- **Chip 20**: CHAPTER 2 COMPLETE! You've built the ALU—the brain of the CPU!
- **Chips 21-22**: Registers complete! You can now store data.
- **Chips 23-27**: RAM hierarchy complete! You've built 16K of memory from flip-flops.
- **Chip 28**: CHAPTER 3 COMPLETE! You've mastered sequential logic!

## Tips

1. **Start simple**: NOT is just `nand(a, a)`
2. **Use truth tables**: Compare your output to expected values
3. **Think in gates**: Draw the circuit on paper first
4. **Read the hints**: Each chip file has implementation hints
5. **Use watch mode**: `python verify.py --watch` for instant feedback

### Useful Identities

- `NOT(a) = NAND(a, a)`
- `AND(a, b) = NOT(NAND(a, b))`
- `OR(a, b) = NAND(NOT(a), NOT(b))` (De Morgan's law)
- `XOR(a, b) = OR(AND(a, NOT(b)), AND(NOT(a), b))`
- `MUX(a, b, sel) = OR(AND(a, NOT(sel)), AND(b, sel))`

### ALU Control Bits

The ALU uses 6 control bits to compute 18 functions:

| zx | nx | zy | ny | f | no | Output |
|----|----|----|----|----|-----|--------|
| 1 | 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 0 | 1 | 0 | -1 |
| 0 | 0 | 1 | 1 | 0 | 0 | x |
| 1 | 1 | 0 | 0 | 0 | 0 | y |
| 0 | 0 | 1 | 1 | 1 | 0 | x-1 |
| 0 | 0 | 0 | 0 | 1 | 0 | x+y |
| 0 | 1 | 0 | 0 | 1 | 1 | x-y |

## Troubleshooting

**"Import error"**: Make sure you're running from the project root directory.

**"Function returns None"**: You haven't implemented the chip yet (still has `raise NotImplementedError`).

**Lint violation**: You used a forbidden construct. Rewrite using only gate functions.

**Test fails**: Check your logic against the truth table in the docstring.

**Sequential chip not working**: Remember that state changes happen on `Clock.get().tick()`, not immediately.

## Starting Over

If you want to reset and try again:

```bash
python verify.py --restart
```

This will restore all chip files to their original stub state.

## Resources

- [Nand2Tetris Course](https://www.nand2tetris.org/)
- [Course Textbook](https://www.nand2tetris.org/book)
- [Boolean Algebra](https://en.wikipedia.org/wiki/Boolean_algebra)
- [De Morgan's Laws](https://en.wikipedia.org/wiki/De_Morgan%27s_laws)

---

Good luck! Remember: every computer ever built is made of gates like these.
