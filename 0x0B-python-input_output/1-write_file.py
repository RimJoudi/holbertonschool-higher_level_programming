#!/usr/bin/python3
""" write file Module """


def write_file(filename="", text=""):
    """
    write file function
    Args:
        filename(string): the given file name
        text(string): the text
    Returns:
        number of characters written.

    """
    with open(filename, 'w', encoding="UTF8") as f:
        f.write(text)
        return len(text)
