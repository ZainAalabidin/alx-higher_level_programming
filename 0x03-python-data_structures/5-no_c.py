#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        New_list = list(my_string)
        for str in my_string:
            if str == "c" or str == "C":
                New_list.remove(str)
        return "".join(New_list)
