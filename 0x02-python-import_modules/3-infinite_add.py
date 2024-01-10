#!/usr/bin/python3
import sys


def infinite_add(*a):
    result = 0
    for num in a:
        result += int(num)
    return result


if __name__ == "__main__":
    a = sys.argv[1:]
    print(infinite_add(*a))
