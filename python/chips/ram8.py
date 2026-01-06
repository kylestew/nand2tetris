"""
RAM8 - 8-Register RAM
"""

from chips.register import Register
from chips.mux8way16 import mux8way16
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
