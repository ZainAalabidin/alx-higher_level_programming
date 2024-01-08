#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for num1 in matrix:
            long = 1
            for num2 in num1:
                if long == len(num1):
                    print("{}".format(num2), end="")
                else:
                    print("{}".format(num2), end=" ")
                long = long + 1
            print()
