#!/usr/bin/python3
"""4. Access and update private attribute"""


class Square:
    """Square"""
    def __init__(self, size=0):
        """cons method"""
        self.__size = size

    def area(self):
        """area of the Square"""
        return self.__size * self.__size

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
