#!/usr/bin/python3
"""
Rectangle module
"""


from typing import AsyncIterable


class Rectangle:
    """
    class that defines Rectangle
    Args:
        width(int): width of the rectangle
        height(int): height of the rectangle
    Raises:
        TypeError: when width/height not int type
        ValueError: when width/height less than 0
    """
    def __init__(self, width=0, height=0):
        """
        Init method to construct a rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        width getter
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height getter attribute
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        height setter attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        returns the rectangle area
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))
