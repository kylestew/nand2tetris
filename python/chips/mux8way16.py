"""
MUX8WAY16 - 8-way 16-bit Multiplexer
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


def mux8way16(
    a: tuple[bool, ...],
    b: tuple[bool, ...],
    c: tuple[bool, ...],
    d: tuple[bool, ...],
    e: tuple[bool, ...],
    f: tuple[bool, ...],
    g: tuple[bool, ...],
    h: tuple[bool, ...],
    sel: tuple[bool, bool, bool],
) -> tuple[bool, ...]:
    """
    8-way 16-bit Multiplexer - selects one of eight 16-bit inputs.

    sel[0] is LSB, sel[2] is MSB:
        sel=000 -> a, sel=001 -> b, sel=010 -> c, sel=011 -> d
        sel=100 -> e, sel=101 -> f, sel=110 -> g, sel=111 -> h

    Inputs: a[16] through h[16], sel[3]
    Output: out[16]
    """
    raise NotImplementedError("mux8way16")
