#!/usr/bin/python3
"""5. Printing a square"""


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

    def my_print(self):
        """myprint"""
        for y in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print()
        if not self.__size:
            print()
