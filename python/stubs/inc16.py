"""
Inc16 - 16-bit Incrementer
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
from chips.half_adder import half_adder
from chips.full_adder import full_adder
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
