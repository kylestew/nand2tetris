"""
NAND2TETRIS - Chapter 1: Boolean Logic Chips

This package contains all the chips for Chapter 1 of the Nand2Tetris course.
NAND is the only primitive - all other chips must be built from it.

Chip order (each can only use chips above it):
    1. nand      - THE PRIMITIVE (provided)
    2. not_gate  - Inverter
    3. and_gate  - AND gate
    4. or_gate   - OR gate
    5. xor_gate  - XOR gate
    6. mux       - Multiplexer
    7. dmux      - Demultiplexer
    8. not16     - 16-bit NOT
    9. and16     - 16-bit AND
    10. or16     - 16-bit OR
    11. mux16    - 16-bit MUX
    12. or8way   - 8-way OR
    13. mux4way16 - 4-way 16-bit MUX
    14. mux8way16 - 8-way 16-bit MUX
    15. dmux4way  - 4-way DMUX
    16. dmux8way  - 8-way DMUX
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

__all__ = [
    "nand",
    "not_gate",
    "and_gate",
    "or_gate",
    "xor_gate",
    "mux",
    "dmux",
    "not16",
    "and16",
    "or16",
    "mux16",
    "or8way",
    "mux4way16",
    "mux8way16",
    "dmux4way",
    "dmux8way",
]
