"""
NOT16 - 16-bit NOT gate
"""

from chips.nand import nand
from chips.not_gate import not_gate
from chips.and_gate import and_gate
from chips.or_gate import or_gate
from chips.xor_gate import xor_gate
from chips.mux import mux
from chips.dmux import dmux


def not16(inp: tuple[bool, ...]) -> tuple[bool, ...]:
    """
    16-bit NOT - inverts all 16 bits.

    Input: inp[16] (LSB first)
    Output: out[16] where out[i] = NOT(inp[i])
    """
    raise NotImplementedError("not16")
