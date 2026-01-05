"""
AND16 - 16-bit AND gate

Allowed chips: nand, not_gate, and_gate, or_gate, xor_gate, mux, dmux, not16
"""

from chips.nand import nand
from chips.not_gate import not_gate
from chips.and_gate import and_gate
from chips.or_gate import or_gate
from chips.xor_gate import xor_gate
from chips.mux import mux
from chips.dmux import dmux
from chips.not16 import not16


def and16(a: tuple[bool, ...], b: tuple[bool, ...]) -> tuple[bool, ...]:
    """
    16-bit AND - applies AND to each pair of bits.

    For i = 0..15: out[i] = AND(a[i], b[i])

    Input:  a[16], b[16] - two 16-bit buses
    Output: out[16] - 16-bit bus

    Indexing: [0] is LSB, [15] is MSB

    Allowed chips: all basic gates, not16
    """
    return (
        and_gate(a[0], b[0]),
        and_gate(a[1], b[1]),
        and_gate(a[2], b[2]),
        and_gate(a[3], b[3]),
        and_gate(a[4], b[4]),
        and_gate(a[5], b[5]),
        and_gate(a[6], b[6]),
        and_gate(a[7], b[7]),
        and_gate(a[8], b[8]),
        and_gate(a[9], b[9]),
        and_gate(a[10], b[10]),
        and_gate(a[11], b[11]),
        and_gate(a[12], b[12]),
        and_gate(a[13], b[13]),
        and_gate(a[14], b[14]),
        and_gate(a[15], b[15]),
    )
