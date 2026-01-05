"""
NAND gate - THE UNIVERSAL PRIMITIVE

This is the ONLY gate provided to you. Every other chip in this course
must be built using NAND gates (directly or through chips you've built).

The NAND gate outputs False only when BOTH inputs are True.
This simple gate is "universal" - any digital circuit can be built from it.

DO NOT MODIFY THIS FILE.
"""


def nand(a: bool, b: bool) -> bool:
    """
    NAND gate - the universal gate from which all others can be built.

    Truth table:
        a | b | out
        --|---|----
        0 | 0 |  1
        0 | 1 |  1
        1 | 0 |  1
        1 | 1 |  0

    NAND = NOT(AND) = "Not both"
    """
    # This is the ONLY place where Python's boolean operators are allowed.
    # This is the foundation of everything you will build.
    return not (a and b)
