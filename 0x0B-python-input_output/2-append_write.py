#!/usr/bin/python3
""" append write Module """


def append_write(filename="", text=""):
    """ append function
    Args:
        filename(string): the given file name
        text(string): the text
    Returns:
        number of characters added.
    """
    with open(filename, 'a', encoding="UTF8") as f:
        f.write(text)
        return len(text)
