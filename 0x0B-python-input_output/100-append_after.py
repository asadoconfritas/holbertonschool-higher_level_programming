#!/usr/bin/python3
"""mod doc"""


def append_after(filename="", search_string="", new_string=""):
    """append after"""
    with open(filename, 'r+', encoding='utf8') as f:
        out = ""
        for line in f:
            out += line
            if search_string in line:
                out += new_string
        f.seek(0)
        f.write(out)
