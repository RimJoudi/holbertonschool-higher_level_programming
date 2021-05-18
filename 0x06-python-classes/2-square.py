#!/usr/bin/python3
""" module square """


class Square:
    """
    class Square that defines a square
    """
    def __init__(self, size=0):
        """
        Init method
        Args:
            size (int): size of the square
        Raises:
            TypeError: if size not an integer
            ValueError: if size less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
