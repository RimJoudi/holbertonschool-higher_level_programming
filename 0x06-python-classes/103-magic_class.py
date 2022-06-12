#!/usr/bin/python3
""" module MagicClass """
import math


class MagicClass:
    """
    class MagicClass
    """
    def __init__(self, radius=0):
        """
        init method
        Args:
            radius (int or float): radius of the circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """
        Instance method
        Returns:
            the area of the circle
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """
        Instance method
        Returns:
            the perimeter of the circule
        """
        return (2 * math.pi * self.__radius)
