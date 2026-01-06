"""
Register - 16-bit Register
"""

from chips.bit import Bit


class Register:
    """
    16-bit register - stores a 16-bit value.

    If load=1, the register stores the input value.
    If load=0, the register maintains its current value.

    Behavior:
        if load(t-1) then out(t) = in(t-1)
        else out(t) = out(t-1)
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
