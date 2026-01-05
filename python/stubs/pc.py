"""
PC - Program Counter
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
from chips.add16 import add16
from chips.inc16 import inc16


class PC:
    """
    Program Counter - 16-bit counter with load, increment, and reset.

    The PC supports three operations (priority: reset > load > inc):
        reset=1: Set counter to 0
        load=1:  Set counter to input value
        inc=1:   Increment counter by 1

    Behavior (by priority):
        if reset(t-1) then out(t) = 0
        else if load(t-1) then out(t) = in(t-1)
        else if inc(t-1) then out(t) = out(t-1) + 1
        else out(t) = out(t-1)

    Usage:
        pc = PC()

        # Increment
        pc(inp=zeros, load=False, inc=True, reset=False)
        Clock.get().tick()
        out = pc(...)  # Returns 1

        # Load value
        pc(inp=value, load=True, inc=False, reset=False)
        Clock.get().tick()
        out = pc(...)  # Returns value

        # Reset to 0
        pc(inp=zeros, load=False, inc=False, reset=True)
        Clock.get().tick()
        out = pc(...)  # Returns 0
    """

    def __init__(self) -> None:
        raise NotImplementedError("pc")

    def __call__(
        self,
        inp: tuple[bool, ...],
        load: bool,
        inc: bool,
        reset: bool,
    ) -> tuple[bool, ...]:
        """
        Set control signals and return current counter value.

        Args:
            inp: 16-bit value for load operation
            load: If True (and not reset), load inp
            inc: If True (and not reset/load), increment
            reset: If True, reset to 0 (highest priority)

        Returns:
            Current 16-bit counter value
        """
        raise NotImplementedError("pc")

    def tick(self) -> None:
        """Called by Clock - advance internal state."""
        raise NotImplementedError("pc")
