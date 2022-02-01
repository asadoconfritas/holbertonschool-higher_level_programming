#!/usr/bin/python3
"""mod doc"""


def inherits_from(obj, a_class):
    """inherits from"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
