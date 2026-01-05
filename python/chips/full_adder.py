"""
Full Adder - Adds three bits

Allowed chips: half_adder, or_gate, xor_gate, and_gate
"""

from chips.half_adder import half_adder
from chips.or_gate import or_gate


def full_adder(a: bool, b: bool, c: bool) -> tuple[bool, bool]:
    """
    Full Adder - adds three single bits (a + b + carry_in).

    Truth table:
        a | b | c | sum | carry
        --|---|---|-----|------
        0 | 0 | 0 |  0  |   0
        0 | 0 | 1 |  1  |   0
        0 | 1 | 0 |  1  |   0
        0 | 1 | 1 |  0  |   1
        1 | 0 | 0 |  1  |   0
        1 | 0 | 1 |  0  |   1
        1 | 1 | 0 |  0  |   1
        1 | 1 | 1 |  1  |   1

    Returns: (sum, carry)

    Allowed chips: half_adder, or_gate
    Hint: Chain two half adders, OR the carries
    """
    raise NotImplementedError("full_adder")

