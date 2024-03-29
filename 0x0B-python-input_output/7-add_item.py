#!/usr/bin/python3
"""Add item script."""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    lst = load_from_json_file("add_item.json")
except:
    lst = []

new_items = sys.argv[1:]
lst.extend(new_items)

save_to_json_file(lst, "add_item.json")
