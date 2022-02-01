#!/usr/bin/python3
"""mod doc"""

class MyList(list):
    """class doc"""
    def print_sorted(self):
        """print sorted"""
        for item in self:
            if type(item) is not int:
                raise TypeError("must be a list of integers")
        print(sorted(self))
