#!/usr/bin/python3
"""mod doc"""


def read_file(filename=""):
    """read f"""
    with open(filename, encoding='utf8') as f:
        print(f.read(), end="")
