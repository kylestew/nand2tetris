"""
DMUX - 2-way Demultiplexer
"""

from chips.nand import nand
from chips.not_gate import not_gate
from chips.and_gate import and_gate
from chips.or_gate import or_gate
from chips.xor_gate import xor_gate
from chips.mux import mux


def dmux(inp: bool, sel: bool) -> tuple[bool, bool]:
    """
    2-way Demultiplexer - routes input to one of two outputs.

    If sel=0, {a=inp, b=0}. If sel=1, {a=0, b=inp}.

    Truth table:
        inp | sel | a | b
        ----|-----|---|---
         0  |  0  | 0 | 0
         1  |  0  | 1 | 0
         0  |  1  | 0 | 0
         1  |  1  | 0 | 1

    Returns: (a, b)
    """
    raise NotImplementedError("dmux")
