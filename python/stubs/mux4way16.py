"""
MUX4WAY16 - 4-way 16-bit Multiplexer

Allowed chips: all previous chips
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


def mux4way16(
    a: tuple[bool, ...],
    b: tuple[bool, ...],
    c: tuple[bool, ...],
    d: tuple[bool, ...],
    sel: tuple[bool, bool],
) -> tuple[bool, ...]:
    """
    4-way 16-bit Multiplexer - selects one of four 16-bit inputs.

    sel[0] is LSB, sel[1] is MSB of selector

    sel = (0,0) -> output a
    sel = (1,0) -> output b
    sel = (0,1) -> output c
    sel = (1,1) -> output d

    Input:  a[16], b[16], c[16], d[16] - four 16-bit buses
            sel[2] - 2-bit selector (tuple of 2 bools)
    Output: out[16] - 16-bit bus

    Allowed chips: all previous chips
    Hint: Use mux16 in two stages:
          Stage 1: mux16(a, b, sel[0]) and mux16(c, d, sel[0])
          Stage 2: mux16(stage1_result1, stage1_result2, sel[1])
    """
    # YOUR IMPLEMENTATION HERE
    pass

