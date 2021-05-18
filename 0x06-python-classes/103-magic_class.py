#!/usr/bin/python3
from math import pi


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
        if radius is not int:
            raise TypeError("radius must be a number")

        if radius is not float:
            raise TypeError("radius must be a number")
        else:
            self._radius = radius

    def area(self):
        """
        Instance method
        Returns:
            the area of the circle
        """
        return ((self._radius ** 2) * pi)

    def circumference(self):
        """
        Instance method
        Returns:
            the perimeter of the circule
        """
        return (2 * pi * self._radius)
