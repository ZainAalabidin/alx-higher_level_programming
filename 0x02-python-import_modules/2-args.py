#!/usr/bin/python3

import sys

if __name__ == "__main__":

    argsl = len(sys.argv) - 1
    if argsl == 0:
        print("0 arguments.")
    elif argsl == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argsl))
    i = 0
    for args in sys.argv:
        if i != 0:
            print("{:d} {}".format(i, args))
        i = i + 1
