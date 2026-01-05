"""
ALU - Arithmetic Logic Unit

The centerpiece of the Hack CPU.

Allowed chips: mux16, not16, and16, add16, or8way, or_gate, not_gate
"""

from chips.mux16 import mux16
from chips.not16 import not16
from chips.and16 import and16
from chips.add16 import add16
from chips.or8way import or8way
from chips.or_gate import or_gate
from chips.not_gate import not_gate


def alu(
    x: tuple[bool, ...],
    y: tuple[bool, ...],
    zx: bool,
    nx: bool,
    zy: bool,
    ny: bool,
    f: bool,
    no: bool,
) -> tuple[tuple[bool, ...], bool, bool]:
    """
    Hack ALU - computes one of 18 functions on two 16-bit inputs.

    Inputs:
        x[16], y[16]: Two 16-bit data inputs
        zx: Zero the x input
        nx: Negate the x input
        zy: Zero the y input
        ny: Negate the y input
        f:  Function select (1=Add, 0=And)
        no: Negate the output

    Outputs: (out, zr, ng)
        out[16]: 16-bit output
        zr: True if out == 0
        ng: True if out < 0 (MSB is 1)

    Control bit combinations:
        zx nx zy ny  f no | out
        -------------------|----
         1  0  1  0  1  0 | 0
         1  1  1  1  1  1 | 1
         1  1  1  0  1  0 | -1
         0  0  1  1  0  0 | x
         1  1  0  0  0  0 | y
         0  0  1  1  0  1 | !x
         1  1  0  0  0  1 | !y
         0  0  1  1  1  1 | -x
         1  1  0  0  1  1 | -y
         0  1  1  1  1  1 | x+1
         1  1  0  1  1  1 | y+1
         0  0  1  1  1  0 | x-1
         1  1  0  0  1  0 | y-1
         0  0  0  0  1  0 | x+y
         0  1  0  0  1  1 | x-y
         0  0  0  1  1  1 | y-x
         0  0  0  0  0  0 | x&y
         0  1  0  1  0  1 | x|y
    """
    raise NotImplementedError("alu")
