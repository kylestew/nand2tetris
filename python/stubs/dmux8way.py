"""
DMUX8WAY - 8-way Demultiplexer
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

    sel[0] is LSB, sel[2] is MSB:
        sel=000 -> a=inp, rest=0
        sel=001 -> b=inp, rest=0
        ...
        sel=111 -> h=inp, rest=0

    Returns: (a, b, c, d, e, f, g, h)
    """
    raise NotImplementedError("dmux8way")
