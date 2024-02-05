#!/usr/bin/python3
"""Define `2-is_same_class` module"""


def is_same_class(obj, a_class):
    """is_same_class method

    Returns:
        True : if object is same onstance of class
    """
    return type(obj) == a_class
