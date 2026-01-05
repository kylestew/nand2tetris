"""
Inc16 - 16-bit Incrementer

Allowed chips: add16
"""

from chips.add16 import add16


def inc16(inp: tuple[bool, ...]) -> tuple[bool, ...]:
    """
    16-bit Incrementer - adds 1 to a 16-bit value.

    Input:
        inp[16]: 16-bit value (LSB first)

    Output:
        out[16]: inp + 1 (overflow wraps around)
    """
    raise NotImplementedError("inc16")
