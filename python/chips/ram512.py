"""
RAM512 - 512-Register RAM
"""

from chips.clock import Clock
from chips.dff import DFF
from chips.bit import Bit
from chips.register import Register
from chips.ram8 import RAM8
from chips.ram64 import RAM64
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


class RAM512:
    """
    512-register RAM - stores 512 16-bit values.

    The address (9 bits) selects which register to read/write.
    If load=1, the selected register stores the input.
    Output is always the value of the selected register.

    Built from 8 RAM64 chips.

    Address breakdown:
        address[0:6] -> selects register within RAM64
        address[6:9] -> selects which RAM64
    """

    def __init__(self) -> None:
        raise NotImplementedError("ram512")

    def __call__(
        self,
        inp: tuple[bool, ...],
        load: bool,
        address: tuple[bool, ...],  # 9 bits
    ) -> tuple[bool, ...]:
        """
        Access RAM at given address.

        Args:
            inp: 16-bit value to potentially store
            load: If True, write inp to selected address
            address: 9-bit address (selects 1 of 512 registers)

        Returns:
            16-bit value at selected address
        """
        raise NotImplementedError("ram512")

    def tick(self) -> None:
        """Called by Clock - advance internal state."""
        raise NotImplementedError("ram512")
