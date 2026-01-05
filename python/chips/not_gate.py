"""
NOT gate - Inverter

Allowed chips: nand
"""

from chips.nand import nand


def not_gate(a: bool) -> bool:
    """
    NOT gate (inverter) - outputs the opposite of the input.

    Truth table:
        a | out
        --|----
        0 |  1
        1 |  0

    Allowed chips: nand
    """
    return nand(a, a)
