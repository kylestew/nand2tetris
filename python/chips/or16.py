"""
OR16 - 16-bit OR gate

Allowed chips: nand, not_gate, and_gate, or_gate, xor_gate, mux, dmux, not16, and16
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


def or16(a: tuple[bool, ...], b: tuple[bool, ...]) -> tuple[bool, ...]:
    """
    16-bit OR - applies OR to each pair of bits.

    For i = 0..15: out[i] = OR(a[i], b[i])

    Input:  a[16], b[16] - two 16-bit buses
    Output: out[16] - 16-bit bus

    Indexing: [0] is LSB, [15] is MSB

    Allowed chips: all basic gates, not16, and16
    Hint: Apply or_gate to each pair of bits.
    """
    # YOUR IMPLEMENTATION HERE
    pass
