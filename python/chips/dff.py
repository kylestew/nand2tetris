"""
DFF - D Flip-Flop (Data Flip-Flop)

THE MEMORY PRIMITIVE - like NAND is for logic, DFF is for memory.

This is a HARDWIRED primitive. Students do NOT implement this chip.
All other sequential chips are built using DFF.

A DFF stores one bit. On each clock tick, the output becomes whatever
the input was during the previous cycle.
"""

from chips.clock import Clock


class DFF:
    """
    D Flip-Flop - the fundamental memory element.

    The DFF captures its input on the rising edge of the clock
    and holds that value until the next clock tick.

    Behavior:
        out(t) = in(t-1)

    In other words, the output at time t equals the input at time t-1.

    Usage:
        dff = DFF()

        dff(inp=True)     # Set input to True
        # out is still False (initial state)

        Clock.get().tick()  # Clock ticks

        out = dff(inp=False)  # out is now True (previous input)
    """

    def __init__(self) -> None:
        self._state: bool = False  # Current output
        self._next: bool = False  # Next state (set by input)
        Clock.get().register(self)

    def __call__(self, inp: bool) -> bool:
        """
        Set the input and return current output.

        Args:
            inp: The input bit to store (will become output after tick)

        Returns:
            The current stored bit (from previous tick)
        """
        self._next = inp
        return self._state

    def tick(self) -> None:
        """Advance state on clock tick (called by Clock)."""
        self._state = self._next

    def reset(self) -> None:
        """Reset to initial state (for testing)."""
        self._state = False
        self._next = False

    @property
    def state(self) -> bool:
        """Current stored state (for debugging)."""
        return self._state
