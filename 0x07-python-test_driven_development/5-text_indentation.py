#!/usr/bin/python3
"""
This module contains a function to print a text with
2 new lines after certain characters.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
    text (str): Input text.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']
    new_line_flag = True

    for char in text:
        if new_line_flag and char == ' ':
            continue
        print(char, end='')

        if char in punctuation_chars:
            print('\n')
            new_line_flag = True
        else:
            new_line_flag = False
