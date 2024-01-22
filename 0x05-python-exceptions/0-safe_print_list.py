#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    leng = 0
    for t in range(x):
        try:
            print("{:d}".format(my_list[t]), end="")
            leng = leng + 1
        except IndexError:
            continue
    print("")
    return leng
