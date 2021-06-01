#!/usr/bin/python3
"""
is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    function to check if an object is an instance of a class
    Args:
        obj (object): the object
        a_class (class): the class
    Returns:
        True: if object is an instance of class or inherited from it
        False: if object is not an instance class or inherited from it
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
