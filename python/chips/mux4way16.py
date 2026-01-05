"""
MUX4WAY16 - 4-way 16-bit Multiplexer
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


def mux4way16(
    a: tuple[bool, ...],
    b: tuple[bool, ...],
    c: tuple[bool, ...],
    d: tuple[bool, ...],
    sel: tuple[bool, bool],
) -> tuple[bool, ...]:
    """
    4-way 16-bit Multiplexer - selects one of four 16-bit inputs.

    sel[0] is LSB, sel[1] is MSB:
        sel=00 -> a
        sel=01 -> b
        sel=10 -> c
        sel=11 -> d

    Inputs: a[16], b[16], c[16], d[16], sel[2]
    Output: out[16]
    """
    raise NotImplementedError("mux4way16")
