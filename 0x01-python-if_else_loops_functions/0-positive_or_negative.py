#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    outp = "positive"
elif number < 0:
    outp = "negative"
else:
    outp = "zero"
print("{:d} is {}".format(number, outp))
