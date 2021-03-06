#!/usr/bin/python3
"""3. Area of a square"""


class Square:
    """Square"""
    def __init__(self, size=0):
        """cons method"""
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    def area(self):
        """area of the Square"""
        return self.__size * self.__size
