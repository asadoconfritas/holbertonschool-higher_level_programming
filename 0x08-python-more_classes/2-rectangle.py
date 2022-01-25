#!/usr/bin/python3
"""rectangle"""


class Rectangle:
    """class"""
    def __init__(self, width=0, height=0):
        """init"""
        self.height = height
        self.width = width

        @property
        def width(self):
        """width"""
        return self.__width

        @property
        def height(self):
        """height"""
        return self.__height

        @width.setter
        def width(self, width):
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            elif width < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = width

        @height.setter
        def height(self, height):
            if not isinstance(height, int):
                raise TypeError("height must be an integer")
            elif height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = height

        def area(self):
            """area"""
            return self.__height * self.__width

        def perimeter(self):
            """perimeter"""
            if (self.__height == 0) or (self.__width == 0):
                return 0
            return (2 * self.__height) + (2 * self.__width)
