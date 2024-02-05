#!/usr/bin/python3
"""Define module `0-lookup.py` """


def lookup(obj):
    """Lookup method

    Args:
        obj: the object class.

    Returns:
         list of available attributes and methods of an object.
    """
    return dir(obj)
