#!/usr/bin/python3
"""Define `from_json_string` module"""


import json

"""Import json module"""


def from_json_string(my_str):
    """Define method that  reserialize json object"""
    res_obj = json.loads(my_str)
    return res_obj
