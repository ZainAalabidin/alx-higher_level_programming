#!/usr/bin/python3
"""Define fucnction that add 2 interger.

Attributes:
    add_integer: function that adds two integers.
"""


def add_integer(a, b=98):
    """Adds tow integer and/or float values.

    Args:
        a (int): first value .
        b (int): second value . defult to 98.

    Raises:
        TypeError: if a or b are not integer or float.

    Returns:
        int: result add a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
