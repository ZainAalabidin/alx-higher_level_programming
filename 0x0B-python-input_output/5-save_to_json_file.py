#!/usr/bin/python3
"""`5-save_to_json_file` module"""


import json

"""Import json module"""


def save_to_json_file(my_obj, filename):
    """method that save json object in text file"""
    with open(filename, "w", encoding="utf-8") as f:
        s_obj = json.dumps(my_obj)
        w_obj = f.write(s_obj)
    return w_obj
