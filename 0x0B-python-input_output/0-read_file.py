#!/usr/bin/python3
"""`0-read_file` module"""


def read_file(filename=""):
    """Method that read files"""
    with open(filename, "r", encoding="utf-8") as f:
        read_text = f.read()

    print(read_text)
