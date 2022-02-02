#!/usr/bin/python3
"""mod doc"""


def append_write(filename="", text=""):
    """append w"""
    with open(filename, 'a+', encoding='utf8') as f:
        return f.write(text)
