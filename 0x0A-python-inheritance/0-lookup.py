#!/usr/bin/python3
"""Define module `0-lookup.py` """

def lookup(obj):
    """A function that returns the list of available attributes and methods of an object
    
    Args:
        obj: the object class.

    Returns:
         list of available attributes and methods of an object.
    """
    return dir(obj)
