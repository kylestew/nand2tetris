"""
DMUX4WAY - 4-way Demultiplexer

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


def dmux4way(inp: bool, sel: tuple[bool, bool]) -> tuple[bool, bool, bool, bool]:
    """
    4-way Demultiplexer - routes input to one of four outputs.

    sel[0] is LSB, sel[1] is MSB of selector

    sel = (0,0) -> {a=inp, b=0, c=0, d=0}
    sel = (1,0) -> {a=0, b=inp, c=0, d=0}
    sel = (0,1) -> {a=0, b=0, c=inp, d=0}
    sel = (1,1) -> {a=0, b=0, c=0, d=inp}

    Input:  inp - single bit input
            sel[2] - 2-bit selector (tuple of 2 bools)
    Output: (a, b, c, d) - four single bits

    Allowed chips: all previous chips
    """
    raise NotImplementedError("dmux4way")
