"""
MUX8WAY16 - 8-way 16-bit Multiplexer

Allowed chips: all previous chips
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

    sel[0] is LSB, sel[2] is MSB of selector

    sel = (0,0,0) -> output a
    sel = (1,0,0) -> output b
    sel = (0,1,0) -> output c
    sel = (1,1,0) -> output d
    sel = (0,0,1) -> output e
    sel = (1,0,1) -> output f
    sel = (0,1,1) -> output g
    sel = (1,1,1) -> output h

    Input:  a-h[16] - eight 16-bit buses
            sel[3] - 3-bit selector (tuple of 3 bools)
    Output: out[16] - 16-bit bus

    Allowed chips: all previous chips
    """
    raise NotImplementedError("mux8way16")
