"""
DMUX8WAY - 8-way Demultiplexer

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
from chips.mux8way16 import mux8way16
from chips.dmux4way import dmux4way


def dmux8way(
    inp: bool, sel: tuple[bool, bool, bool]
) -> tuple[bool, bool, bool, bool, bool, bool, bool, bool]:
    """
    8-way Demultiplexer - routes input to one of eight outputs.

    sel[0] is LSB, sel[2] is MSB of selector

    sel = (0,0,0) -> {a=inp, b=0, c=0, d=0, e=0, f=0, g=0, h=0}
    sel = (1,0,0) -> {a=0, b=inp, c=0, d=0, e=0, f=0, g=0, h=0}
    sel = (0,1,0) -> {a=0, b=0, c=inp, d=0, e=0, f=0, g=0, h=0}
    sel = (1,1,0) -> {a=0, b=0, c=0, d=inp, e=0, f=0, g=0, h=0}
    sel = (0,0,1) -> {a=0, b=0, c=0, d=0, e=inp, f=0, g=0, h=0}
    sel = (1,0,1) -> {a=0, b=0, c=0, d=0, e=0, f=inp, g=0, h=0}
    sel = (0,1,1) -> {a=0, b=0, c=0, d=0, e=0, f=0, g=inp, h=0}
    sel = (1,1,1) -> {a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=inp}

    Input:  inp - single bit input
            sel[3] - 3-bit selector (tuple of 3 bools)
    Output: (a, b, c, d, e, f, g, h) - eight single bits

    Allowed chips: all previous chips
    """
    raise NotImplementedError("dmux8way")
