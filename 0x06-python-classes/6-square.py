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

    @property
    def position(self):
        """ gives the position of the square
        Returns:
            the position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets the position of the square
        Args:
            value (tuple): the new position of the square
                defined by 2 positive integers
        Raises:
            TypeError: if size not an integer
            ValueError: if size less than 0
        Returns:
            the new size of the square
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or type(value[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[1] < 0 or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __init__(self, size=0, position=(0, 0)):
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
            self.size = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or type(position[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[1] < 0 or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = position

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
            for i in range(0, self.__position[1]):
                print()
            for j in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                for l in range(0, self.__size):
                    print("#", end="")
                print()
