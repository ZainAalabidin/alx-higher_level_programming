#!/usr/bin/python3
"""Define `write_file` module"""


def write_file(filename="", text=""):
    """Define method that return number of text"""
    with open(filename, "w", encoding="utf-8") as f:
        num_of_chr = f.write(text)
    return num_of_chr
