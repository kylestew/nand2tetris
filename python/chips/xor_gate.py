"""
XOR gate - Exclusive OR

Allowed chips: nand, not_gate, and_gate, or_gate
"""

from chips.nand import nand
from chips.not_gate import not_gate
from chips.and_gate import and_gate
from chips.or_gate import or_gate


def xor_gate(a: bool, b: bool) -> bool:
    """
    XOR gate (exclusive or) - outputs True when inputs are DIFFERENT.

    Truth table:
        a | b | out
        --|---|----
        0 | 0 |  0
        0 | 1 |  1
        1 | 0 |  1
        1 | 1 |  0

    Allowed chips: nand, not_gate, and_gate, or_gate
    Hint: XOR = (a OR b) AND NOT(a AND b)
          "One or the other, but not both"

    Alternative using only NAND:
          XOR = NAND(NAND(a, NAND(a,b)), NAND(b, NAND(a,b)))
    """
    # YOUR IMPLEMENTATION HERE
    pass
