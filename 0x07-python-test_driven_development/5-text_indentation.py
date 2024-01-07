#!/usr/bin/python3
"""
This module contains a function that prints 
a text with 2 new lines after '.', '?', and ':'.

"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentence_endings = ['.', '?', ':']
    start_index = 0

    for i in range(len(text)):
        if text[i] in sentence_endings:
            print(text[start_index:i + 1].strip())
            print()
            start_index = i + 1

    print(text[start_index:].strip())
