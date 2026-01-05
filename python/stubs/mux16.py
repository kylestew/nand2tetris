"""
MUX16 - 16-bit Multiplexer

Allowed chips: nand, not_gate, and_gate, or_gate, xor_gate, mux, dmux, not16, and16, or16
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


def mux16(a: tuple[bool, ...], b: tuple[bool, ...], sel: bool) -> tuple[bool, ...]:
    """
    16-bit Multiplexer - selects between two 16-bit inputs.

    If sel=0, output a[16]
    If sel=1, output b[16]

    For i = 0..15: out[i] = MUX(a[i], b[i], sel)

    Input:  a[16], b[16] - two 16-bit buses
            sel - single bit selector
    Output: out[16] - 16-bit bus

    Indexing: [0] is LSB, [15] is MSB

    Allowed chips: all basic gates, not16, and16, or16
    Hint: Apply mux to each pair of bits with the same sel.
    """
    # YOUR IMPLEMENTATION HERE
    pass

