#!/usr/bin/python3
"""mod doc"""


def write_file(filename="", text=""):
    """write f"""
    with open(filename, 'w+', encoding='utf8') as f:
        return f.write(text)
