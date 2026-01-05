"""
AND gate

Allowed chips: nand, not_gate
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

    Allowed chips: nand, not_gate
    Hint: NAND is NOT-AND. How do you undo the NOT?
    """
    return not_gate(nand(a, b))

