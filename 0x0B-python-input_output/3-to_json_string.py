#!/usr/bin/python3
"""Define `3-to_json_string` module"""


import json

"""Importing json module"""


def to_json_string(my_obj):
    """Module that serialize object"""
    s_obj = json.dumps(my_obj)
    return s_obj
