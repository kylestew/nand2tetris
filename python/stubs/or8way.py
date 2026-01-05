"""
OR8WAY - 8-way OR gate
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


def or8way(inp: tuple[bool, ...]) -> bool:
    """
    8-way OR - outputs True if ANY of the 8 input bits is True.

    Input: inp[8] (8-bit bus)
    Output: OR(inp[0], inp[1], ..., inp[7])
    """
    raise NotImplementedError("or8way")
