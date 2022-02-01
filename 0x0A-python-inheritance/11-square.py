#!/usr/bin/python3
"""mod doc"""


rect = __import__('9-rectangle').Rectangle


class Square(rect):
    """rectangle doc"""
    def __init__(self, size):
        """init doc"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area doc"""
        return self.__size ** 2

    def __str__(self):
        """str doc"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
