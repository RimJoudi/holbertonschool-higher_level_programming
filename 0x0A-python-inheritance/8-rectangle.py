#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
        area geometry function
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator value
        Args:
            name(string): name
            value(int): given value
        Raises:
            TypeError: when value is not integer
            ValueError: when value is less or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""
Rectangle Module
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """
        Init function
        Args:
            width(int): the width of rectangle
            height(int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
