"""
MUX16 - 16-bit Multiplexer
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


def mux16(a: tuple[bool, ...], b: tuple[bool, ...], sel: bool) -> tuple[bool, ...]:
    """
    16-bit Multiplexer - selects between two 16-bit inputs.

    If sel=0, output a. If sel=1, output b.

    Inputs: a[16], b[16], sel
    Output: out[16]
    """
    raise NotImplementedError("mux16")
