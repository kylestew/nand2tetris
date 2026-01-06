"""
RAM16K - 16K-Register RAM (16384 registers)
"""

from chips.ram4k import RAM4K
from chips.mux4way16 import mux4way16
from chips.dmux4way import dmux4way


class RAM16K:
    """
    16K-register RAM - stores 16384 16-bit values.

    The address (14 bits) selects which register to read/write.
    If load=1, the selected register stores the input.
    Output is always the value of the selected register.

    Built from 4 RAM4K chips (not 8, to save gates).

    Address breakdown:
        address[0:12]  -> selects register within RAM4K
        address[12:14] -> selects which RAM4K (only 4)
    """

    def __init__(self) -> None:
        raise NotImplementedError("ram16k")

    def __call__(
        self,
        inp: tuple[bool, ...],
        load: bool,
        address: tuple[bool, ...],  # 14 bits
    ) -> tuple[bool, ...]:
        """
        Access RAM at given address.

        Args:
            inp: 16-bit value to potentially store
            load: If True, write inp to selected address
            address: 14-bit address (selects 1 of 16384 registers)

        Returns:
            16-bit value at selected address
        """
        raise NotImplementedError("ram16k")
