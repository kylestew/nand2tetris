"""
XOR gate - Exclusive OR
"""

from chips.nand import nand
from chips.not_gate import not_gate
from chips.and_gate import and_gate
from chips.or_gate import or_gate


def xor_gate(a: bool, b: bool) -> bool:
    """
    XOR gate - outputs True when inputs are DIFFERENT.

    Truth table:
        a | b | out
        --|---|----
        0 | 0 |  0
        0 | 1 |  1
        1 | 0 |  1
        1 | 1 |  0
    """
    raise NotImplementedError("xor_gate")
