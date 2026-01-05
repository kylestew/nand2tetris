"""
ALU - Arithmetic Logic Unit

The centerpiece of the Hack CPU.
"""

from chips.nand import nand
from chips.not_gate import not_gate
from chips.and_gate import and_gate
from chips.or_gate import or_gate
from chips.xor_gate import xor_gate
from chips.mux import mux
from chips.dmux import dmux
from chips.not16 import not16
from chips.and16 import and16
from chips.or16 import or16
from chips.mux16 import mux16
from chips.or8way import or8way
from chips.mux4way16 import mux4way16
from chips.mux8way16 import mux8way16
from chips.dmux4way import dmux4way
from chips.dmux8way import dmux8way
from chips.half_adder import half_adder
from chips.full_adder import full_adder
from chips.add16 import add16
from chips.inc16 import inc16


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
