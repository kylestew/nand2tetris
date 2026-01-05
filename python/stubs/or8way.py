"""
OR8WAY - 8-way OR gate

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


def or8way(inp: tuple[bool, ...]) -> bool:
    """
    8-way OR - outputs True if ANY of the 8 input bits is True.

    out = OR(inp[0], inp[1], ..., inp[7])
        = inp[0] OR inp[1] OR inp[2] OR inp[3] OR inp[4] OR inp[5] OR inp[6] OR inp[7]

    Input:  inp[8] - 8-bit bus (tuple of 8 bools)
    Output: out - single bit

    Indexing: inp[0] is LSB, inp[7] is MSB

    Allowed chips: all previous chips
    Hint: Chain OR gates together, or build a tree:
          OR(OR(OR(inp[0],inp[1]), OR(inp[2],inp[3])), 
             OR(OR(inp[4],inp[5]), OR(inp[6],inp[7])))
    """
    # YOUR IMPLEMENTATION HERE
    pass

