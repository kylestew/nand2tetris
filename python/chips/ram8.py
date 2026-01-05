"""
RAM8 - 8-Register RAM
"""

from chips.clock import Clock
from chips.dff import DFF
from chips.bit import Bit
from chips.register import Register
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


class RAM8:
    """
    8-register RAM - stores eight 16-bit values.

    The address (3 bits) selects which register to read/write.
    If load=1, the selected register stores the input.
    Output is always the value of the selected register.

    Behavior:
        if load(t-1) then RAM[address(t-1)](t) = in(t-1)
        out(t) = RAM[address(t)]

    Usage:
        ram = RAM8()

        # Write to address 3
        ram(inp=value, load=True, address=(True, True, False))
        Clock.get().tick()

        # Read from address 3
        out = ram(inp=zeros, load=False, address=(True, True, False))
    """

    def __init__(self) -> None:
        raise NotImplementedError("ram8")

    def __call__(
        self,
        inp: tuple[bool, ...],
        load: bool,
        address: tuple[bool, bool, bool],
    ) -> tuple[bool, ...]:
        """
        Access RAM at given address.

        Args:
            inp: 16-bit value to potentially store
            load: If True, write inp to selected address
            address: 3-bit address (selects 1 of 8 registers)

        Returns:
            16-bit value at selected address
        """
        raise NotImplementedError("ram8")

    def tick(self) -> None:
        """Called by Clock - advance internal state."""
        raise NotImplementedError("ram8")
