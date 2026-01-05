"""
OR gate

Allowed chips: nand, not_gate, and_gate
"""

from chips.nand import nand
from chips.not_gate import not_gate
from chips.and_gate import and_gate


def or_gate(a: bool, b: bool) -> bool:
    """
    OR gate - outputs True when AT LEAST ONE input is True.

    Truth table:
        a | b | out
        --|---|----
        0 | 0 |  0
        0 | 1 |  1
        1 | 0 |  1
        1 | 1 |  1

    Allowed chips: nand, not_gate, and_gate
    Hint: De Morgan's law is interesting here
    """
    raise NotImplementedError("or_gate")
