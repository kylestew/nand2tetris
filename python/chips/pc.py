"""
PC - Program Counter
"""

from chips.register import Register
from chips.inc16 import inc16
from chips.mux16 import mux16


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
