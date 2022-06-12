#!/usr/bin/python3
"""
Module to print a text with 2 new lines
"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines/
    after each of these characters: ., ? and :
    Args:
        text(str): the given text
    Raises:
        TypeError: if the text is not str
    Returns:
        the new text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in ":.,?":
            print('\n')
            if i == len(text) - 1:
                break
            if text[i + 1] == ' ':
                i += 1
            while text[i] == ' ' and text[i + 1] == ' ' and i + 1 < len(text):
                i += 1
        i += 1
