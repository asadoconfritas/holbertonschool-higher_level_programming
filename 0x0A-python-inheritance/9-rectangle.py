#!/usr/bin/python3
"""mod doc"""


basegeo = __import__('7-base_geometry').BaseGeometry


class Rectangle(basegeo):
    """rectangle doc"""
    def __init__(self, width, height):
        """init doc"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area doc"""
        return self.__width * self.__height

    def __str__(self):
        """str doc"""
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
