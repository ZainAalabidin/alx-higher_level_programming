#!/usr/bin/python3
import calc_1

if __name__ == "__main__":
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calc_1.add(a, b)))
    print("{} - {} = {}".format(a, b, calc_1.sub(a, b)))
    print("{} * {} = {}".format(a, b, calc_1.mul(a, b)))
    print("{} / {} = {}".format(a, b, calc_1.div(a, b)))
