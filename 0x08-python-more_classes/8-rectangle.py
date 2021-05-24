#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """
    class that defines Rectangle
    Args:
        width(int): width of the rectangle
        height(int): height of the rectangle
        number_of_instances(int): public class attribute
        print_symbol(str): public class attribute
    Raises:
        TypeError: when width/height not int type
        ValueError: when width/height less than 0
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Init method to construct a rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1


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

    def __str__(self):
        """
        returns a printed rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rectangle = []
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    rectangle.append(str(self.print_symbol))
                rectangle.append("\n")
            return (''.join(rectangle))

    def __repr__(self):
        """
        string representation of the rectangle
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        deletes an instance of Rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")


    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area
        Args:
            rect_1(int): rectangle 1
            rect_2(int): rectangle 2
        Raises:
            TypeError: when rect_1/rect_2 are not istance of Rectangle
        Returns:
            the biggest rectangle based on the area
            rect_1 if equals
            
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 == area2:
            return (rect_1)
        elif area1 > area2:
            return (rect_1)
        else:
            return (rect_2)

