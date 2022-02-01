#!/usr/bin/python3
"""mod doc"""


def BaseGeometry:
    """base geo"""
    
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """int validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0").format(name))
