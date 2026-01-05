"""
Bit - 1-bit Register
"""

from chips.clock import Clock
from chips.dff import DFF
from chips.nand import nand
from chips.not_gate import not_gate
from chips.and_gate import and_gate
from chips.or_gate import or_gate
from chips.xor_gate import xor_gate
from chips.mux import mux
from chips.dmux import dmux


class Bit:
    """
    1-bit register - stores a single bit.

    If load=1, the register stores the input value.
    If load=0, the register maintains its current value.

    Behavior:
        if load(t-1) then out(t) = in(t-1)
        else out(t) = out(t-1)

    Usage:
        bit = Bit()

        bit(inp=True, load=True)   # Load 1
        Clock.get().tick()
        out = bit(inp=False, load=False)  # Returns True, holds value
    """

    def __init__(self) -> None:
        raise NotImplementedError("bit")

    def __call__(self, inp: bool, load: bool) -> bool:
        """
        Set input and load signal, return current output.

        Args:
            inp: Value to potentially store
            load: If True, store inp; if False, maintain current value

        Returns:
            Current stored value
        """
        raise NotImplementedError("bit")

    def tick(self) -> None:
        """Called by Clock - advance internal DFF state."""
        raise NotImplementedError("bit")
