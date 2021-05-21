#!/usr/bin/python3
"""
add 2 integers module
"""
def add_integer(a, b=98):
    """
    function that adds 2 integers.
    Args:
        a (int/float): the first given number
        b (int/float): the second given number
    Raises:
        TypeError: when a and b are not integers or floats
    Returns:
        an integer equal to the addition of a and b
    """
    if type(a) != int and type (a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type (b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int (a)
    if type(b) == float:
        b = int(b)
    return a + b
