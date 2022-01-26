#!/usr/bin/python3
"""
    maxint
    integer
    return: end program
"""


def max_integer(list=[]):
    """maxint"""
    i = 1
    if len(list) == 0:
        return None
    out = list[0]
    while i < len(list):
        if list[i] > out:
            out = list[i]
        i += 1
    return out
