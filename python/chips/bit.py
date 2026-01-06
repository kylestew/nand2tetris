"""
Bit - 1-bit Register
"""

from chips.dff import DFF
from chips.mux import mux


class Bit:
    """
    1-bit register - stores a single bit.

    If load=1, the register stores the input value.
    If load=0, the register maintains its current value.

    Behavior:
        if load(t-1) then out(t) = in(t-1)
        else out(t) = out(t-1)
    """

    def __init__(self) -> None:
        # you're going to need one of these, so we will help you out...
        self._dff = DFF()  # DFF auto-registers with Clock

    def __call__(self, inp: bool, load: bool) -> bool:
        """
        Set input and load signal, return current output.

        Args:
            inp: Value to potentially store
            load: If True, store inp; if False, maintain current value

        Returns:
            Current stored value
        """
        # hint: this is how you get the DFF's current state
        current = self._dff.state

        next_state = mux(inp, current, load)

        # hint: and this is how you latch the next value (and read the current at the same
        # time)
        return self._dff(next_state)
