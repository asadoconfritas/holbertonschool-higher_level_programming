#!/usr/bin/python3
"""
    text
    indentation
    return: end program
"""


def text_indentation(text):
    """textind"""
    if type(text) != str:
        raise TypeError("text must be a string")
        return
    string = text[:]
    for char in text:
        if char in [".", "?", ":"]:
            string += char
            print(string.strip())
            print()
            string = text[:]
        else:
            string += char
    print(string.strip(), end="")
        

