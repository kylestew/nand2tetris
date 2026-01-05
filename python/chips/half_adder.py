"""
Half Adder - Adds two bits
"""

from chips.nand import nand
from chips.not_gate import not_gate
from chips.and_gate import and_gate
from chips.or_gate import or_gate
from chips.xor_gate import xor_gate
from chips.mux import mux
from chips.dmux import dmux
from chips.not16 import not16
from chips.and16 import and16
from chips.or16 import or16
from chips.mux16 import mux16
from chips.or8way import or8way
from chips.mux4way16 import mux4way16
from chips.mux8way16 import mux8way16
from chips.dmux4way import dmux4way
from chips.dmux8way import dmux8way


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
