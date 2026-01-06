"""
RAM4K - 4K-Register RAM (4096 registers)
"""

from chips.ram512 import RAM512
from chips.mux8way16 import mux8way16
from chips.dmux8way import dmux8way


class RAM4K:
    """
    4K-register RAM - stores 4096 16-bit values.

    The address (12 bits) selects which register to read/write.
    If load=1, the selected register stores the input.
    Output is always the value of the selected register.

    Built from 8 RAM512 chips.

    Address breakdown:
        address[0:9]  -> selects register within RAM512
        address[9:12] -> selects which RAM512
    """

    def __init__(self) -> None:
        raise NotImplementedError("ram4k")

    def __call__(
        self,
        inp: tuple[bool, ...],
        load: bool,
        address: tuple[bool, ...],  # 12 bits
    ) -> tuple[bool, ...]:
        """
        Access RAM at given address.

        Args:
            inp: 16-bit value to potentially store
            load: If True, write inp to selected address
            address: 12-bit address (selects 1 of 4096 registers)

        Returns:
            16-bit value at selected address
        """
        raise NotImplementedError("ram4k")
