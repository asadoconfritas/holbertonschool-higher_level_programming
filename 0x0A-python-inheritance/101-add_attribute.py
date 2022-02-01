#!/usr/bin/python3
"""mod doc"""


def add_attribute(obj, name, value):
    """add attr"""
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
