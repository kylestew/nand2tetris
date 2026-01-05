"""
MUX - Multiplexer (2-way, 1-bit)

Allowed chips: nand, not_gate, and_gate, or_gate, xor_gate
"""

from chips.nand import nand
from chips.not_gate import not_gate
from chips.and_gate import and_gate
from chips.or_gate import or_gate
from chips.xor_gate import xor_gate


def mux(a: bool, b: bool, sel: bool) -> bool:
    """
    Multiplexer - selects between two inputs based on selector.

    If sel=0, output a
    If sel=1, output b

    Truth table:
        a | b | sel | out
        --|---|-----|----
        0 | 0 |  0  |  0
        0 | 1 |  0  |  0
        1 | 0 |  0  |  1
        1 | 1 |  0  |  1
        0 | 0 |  1  |  0
        0 | 1 |  1  |  1
        1 | 0 |  1  |  0
        1 | 1 |  1  |  1

    Allowed chips: nand, not_gate, and_gate, or_gate, xor_gate
    Hint: out = (a AND NOT(sel)) OR (b AND sel)
    """
    # DELETE THIS LINE AND IMPLEMENT:
    raise NotImplementedError("mux")

