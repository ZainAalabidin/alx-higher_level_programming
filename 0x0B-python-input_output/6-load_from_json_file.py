#!/usr/bin/python3
"""`6-load_from_json_file` module"""

import json

"""Importion json module"""


def load_from_json_file(filename):
    """Define method that reserialize json object"""
    with open(filename, "r") as f:
        s_obj = json.load(f)
    return s_obj
