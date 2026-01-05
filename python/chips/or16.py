"""
OR16 - 16-bit OR gate
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


def or16(a: tuple[bool, ...], b: tuple[bool, ...]) -> tuple[bool, ...]:
    """
    16-bit OR - ORs corresponding bits.

    Inputs: a[16], b[16] (LSB first)
    Output: out[16] where out[i] = OR(a[i], b[i])
    """
    raise NotImplementedError("or16")
