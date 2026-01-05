"""
Add16 - 16-bit Adder

Allowed chips: half_adder, full_adder
"""

from chips.half_adder import half_adder
from chips.full_adder import full_adder


def add16(a: tuple[bool, ...], b: tuple[bool, ...]) -> tuple[bool, ...]:
    """
    16-bit Adder - adds two 16-bit values.

    Inputs:
        a[16]: First 16-bit value (LSB first)
        b[16]: Second 16-bit value (LSB first)

    Output:
        out[16]: a + b (overflow is ignored)

    Allowed chips: half_adder, full_adder
    Hint: Use half_adder for bit 0, chain full_adders for bits 1-15
    """
    raise NotImplementedError("add16")

