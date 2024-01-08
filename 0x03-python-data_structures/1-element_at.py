#!/usr/bin/python3
def element_at(my_list, idx):
    index = len(my_list) - 1

    if idx < 0:
        return None
    elif idx > index:
        return None
    else:
        return my_list[idx]
