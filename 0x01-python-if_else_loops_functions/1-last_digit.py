#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * (-1)
    digit = number % 10
digit = number % 10
if digit > 5:
    outp = "greater than 5"
elif digit == 0:
    outp = "0"
else:
    outp = "less than 6 and not 0"
print("Last digit of {:d} is {:d} and is {}".format(number, digit, outp))
