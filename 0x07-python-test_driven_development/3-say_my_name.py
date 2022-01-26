#!/usr/bin/python3
"""
    saymyname
    myname
    return: end program
"""


def say_my_name(first_name, last_name=""):
    """saymynameeeee"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
        return
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
        return
    print("My name is {} {}".format(first_name, last_name))
