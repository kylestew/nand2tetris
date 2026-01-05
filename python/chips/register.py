"""
Register - 16-bit Register
"""

from chips.clock import Clock
from chips.dff import DFF
from chips.bit import Bit
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


class Register:
    """
    16-bit register - stores a 16-bit value.

    If load=1, the register stores the input value.
    If load=0, the register maintains its current value.

    Behavior:
        if load(t-1) then out(t) = in(t-1)
        else out(t) = out(t-1)

    Usage:
        reg = Register()

        reg(inp=(True,)*16, load=True)  # Load all 1s
        Clock.get().tick()
        out = reg(inp=(False,)*16, load=False)  # Returns all 1s
    """

    def __init__(self) -> None:
        raise NotImplementedError("register")

    def __call__(self, inp: tuple[bool, ...], load: bool) -> tuple[bool, ...]:
        """
        Set input and load signal, return current output.

        Args:
            inp: 16-bit value to potentially store (LSB first)
            load: If True, store inp; if False, maintain current value

        Returns:
            Current stored 16-bit value (LSB first)
        """
        raise NotImplementedError("register")

    def tick(self) -> None:
        """Called by Clock - advance internal state."""
        raise NotImplementedError("register")
