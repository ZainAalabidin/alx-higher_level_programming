#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    lengt = 0
    for t in range(0, x):
        try:
            print("{:d}".format(my_list[t]), end="")
            leng = leng + 1
        except IndexError:
            continue
    print("")
    return leng
