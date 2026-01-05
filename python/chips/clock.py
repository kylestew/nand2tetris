"""
Clock - Global clock singleton for sequential chips.

The clock manages all registered sequential chips and advances their state
on each tick(). This simulates the behavior of a real clock signal.
"""

from typing import Protocol, runtime_checkable


@runtime_checkable
class Clocked(Protocol):
    """Protocol for chips that respond to clock ticks."""

    def tick(self) -> None:
        """Advance internal state on clock tick."""
        ...


class Clock:
    """
    Global clock singleton.

    Sequential chips register themselves with the clock, and their state
    advances when tick() is called.

    Usage:
        clock = Clock.get()
        dff = DFF()  # Auto-registers with clock

        dff(inp=True)  # Set input
        clock.tick()   # State advances
        out = dff(inp=False)  # Returns previous input (True)
    """

    _instance: "Clock | None" = None

    def __init__(self) -> None:
        self._chips: list[Clocked] = []
        self._tick_count: int = 0

    @classmethod
    def get(cls) -> "Clock":
        """Get the singleton clock instance."""
        if cls._instance is None:
            cls._instance = Clock()
        return cls._instance

    @classmethod
    def reset_instance(cls) -> None:
        """Reset the singleton (for testing)."""
        cls._instance = None

    def register(self, chip: Clocked) -> None:
        """Register a sequential chip with the clock."""
        self._chips.append(chip)

    def unregister(self, chip: Clocked) -> None:
        """Unregister a chip from the clock."""
        if chip in self._chips:
            self._chips.remove(chip)

    def tick(self) -> None:
        """
        Advance the clock by one cycle.

        All registered chips have their tick() method called,
        causing their internal state to advance.
        """
        for chip in self._chips:
            chip.tick()
        self._tick_count += 1

    def reset(self) -> None:
        """
        Reset the clock and all registered chips.

        Clears all registered chips and resets tick count.
        """
        self._chips.clear()
        self._tick_count = 0

    @property
    def tick_count(self) -> int:
        """Number of ticks since last reset."""
        return self._tick_count

    @property
    def chip_count(self) -> int:
        """Number of registered chips."""
        return len(self._chips)
