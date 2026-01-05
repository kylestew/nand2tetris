"""
NOT16 - 16-bit NOT gate

Allowed chips: nand, not_gate, and_gate, or_gate, xor_gate, mux, dmux
"""

from chips.nand import nand
from chips.not_gate import not_gate
from chips.and_gate import and_gate
from chips.or_gate import or_gate
from chips.xor_gate import xor_gate
from chips.mux import mux
from chips.dmux import dmux


def not16(a: tuple[bool, ...]) -> tuple[bool, ...]:
    """
    16-bit NOT - applies NOT to each bit of a 16-bit input.

    For i = 0..15: out[i] = NOT(a[i])

    Input:  a[16] - 16-bit bus (tuple of 16 bools)
    Output: out[16] - 16-bit bus

    Indexing: a[0] is LSB, a[15] is MSB

    Allowed chips: all basic gates
    Hint: Apply not_gate to each bit individually.
    """
    # YOUR IMPLEMENTATION HERE
    pass
