#!/usr/bin/python3
"""Define module contained `is_kind_of_class` method"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class method.

    Returns:
        True : if object is same instance or object of class
    """
    return isinstance(obj, a_class)
