"""
DMUX - Demultiplexer (2-way)

Allowed chips: nand, not_gate, and_gate, or_gate, xor_gate, mux
"""

from chips.nand import nand
from chips.not_gate import not_gate
from chips.and_gate import and_gate
from chips.or_gate import or_gate
from chips.xor_gate import xor_gate
from chips.mux import mux


def dmux(inp: bool, sel: bool) -> tuple[bool, bool]:
    """
    Demultiplexer - routes input to one of two outputs based on selector.

    If sel=0, {a=inp, b=0}
    If sel=1, {a=0, b=inp}

    Truth table:
        inp | sel | a | b
        ----|-----|---|---
         0  |  0  | 0 | 0
         1  |  0  | 1 | 0
         0  |  1  | 0 | 0
         1  |  1  | 0 | 1

    Returns: (a, b) tuple

    Allowed chips: nand, not_gate, and_gate, or_gate, xor_gate, mux
    """
    return (and_gate(inp, not_gate(sel)), and_gate(inp, sel))
