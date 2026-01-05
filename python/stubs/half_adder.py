"""
Half Adder - Adds two bits

Allowed chips: nand, not_gate, and_gate, or_gate, xor_gate
"""

from chips.xor_gate import xor_gate
from chips.and_gate import and_gate


def half_adder(a: bool, b: bool) -> tuple[bool, bool]:
    """
    Half Adder - adds two single bits.

    Truth table:
        a | b | sum | carry
        --|---|-----|------
        0 | 0 |  0  |   0
        0 | 1 |  1  |   0
        1 | 0 |  1  |   0
        1 | 1 |  0  |   1

    Returns: (sum, carry)
    """
    raise NotImplementedError("half_adder")
