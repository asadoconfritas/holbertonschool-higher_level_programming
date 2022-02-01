#!/usr/bin/python3
"""mod doc"""


class MyInt(int):
    """class doc"""
    def __eq__(self, other):
        """eq doc"""
        return (a is b)

    def __ne__(self, other):
        """ne doc"""
        return (a is not b)
