#!/usr/bin/python3
""" module square """


class Square:
    """
    class Square that defines a square
    """
    @property
    def size(self):
        """ gives the size of the square
        Returns:
            the size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the size of the square
        Args:
            value (int): the new size of the square
        Raises:
            TypeError: if size not an integer
            ValueError: if size less than 0
        Returns:
            the new size of the square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

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

    def area(self):
        """
        Instance method
        Returns:
            the current square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Instance method
        Returns:
            the printed square
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
