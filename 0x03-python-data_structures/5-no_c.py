#!/usr/bin/python3
def no_c(my_string):
    NewStr = ""
    if my_string:
        for str in my_string:
            if str != "c" and str != "C":
                NewStr += str
            return NewStr
