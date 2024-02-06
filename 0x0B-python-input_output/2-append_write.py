#!/usr/bin/python3
"""'2-append_write' module"""


def append_write(filename="", text=""):
    """Defile append_write method"""
    with open(filename, "a", encoding="utf-8") as f:
        append_text = f.write(text)
    return append_text
