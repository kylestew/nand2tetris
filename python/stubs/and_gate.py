"""
AND gate
"""

from chips.nand import nand
from chips.not_gate import not_gate


def and_gate(a: bool, b: bool) -> bool:
    """
    AND gate - outputs True only when BOTH inputs are True.

    Truth table:
        a | b | out
        --|---|----
        0 | 0 |  0
        0 | 1 |  0
        1 | 0 |  0
        1 | 1 |  1
    """
    raise NotImplementedError("and_gate")
