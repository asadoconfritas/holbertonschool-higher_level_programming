#!/usr/bin/python3
"""mod doc"""


class MyInt(int):
    """class doc"""
    def __eq__(self, other):
        """eq doc"""
        return (self is other)

    def __ne__(self, other):
        """ne doc"""
        return (self is not other)
