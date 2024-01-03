#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
negstr = " and is less than 6 and not 0"
posstr = " and is greater than 5"
zerstr = " and is 0"

if number >= 0:
    the_last = number % 10
else:
    the_last = number % -10
if the_last > 5:
    print(f"Last digit of {number} is {the_last}{posstr}")
elif the_last == 0:
    print(f"last digit of {number} is {the_last}{zerstr}")
else:
    print(f"last digit of {number} is {the_last}{negstr}")

