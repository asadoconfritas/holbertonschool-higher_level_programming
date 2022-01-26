#!/usr/bin/python3
"""
    print
    square
    return: end program
"""


def print_square(size):
    """printsq"""
    if type(size) != int:
        raise TypeError("size must be an integer")
        return
    if size < 0:
        raise ValueError("size must be >= 0")
        return
    for a in range(size):
        for b in range(size):
            print("#", end="")
        print()
