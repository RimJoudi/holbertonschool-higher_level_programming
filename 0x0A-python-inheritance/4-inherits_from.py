#!/usr/bin/python3
""" inherits_from """


def inherits_from(obj, a_class):
    """
    function to check if an object is an instance of a class inherited from
    Args:
        obj (object): the object
        a_class (class): the class
    Returns:
        True:  if the object is an instance of a class\
            that inherited (directly or indirectly) from the specified class
        False: otherwise
    """
    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    else:
        return False
