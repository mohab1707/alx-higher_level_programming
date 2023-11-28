#!/usr/bin/python3

def uppercase(s):
    """Prints a string in uppercase followed by a new line."""
    for char in s:
        upper_char = char
        if ord('a') <= ord(char) <= ord('z'):
            upper_char = chr(ord(char) - ord('a') + ord('A'))
        print("{}".format(upper_char), end='')

    print()  # Add a newline at the end

    
if __name__ == "__main__":
    uppercase = __import__('8-uppercase').uppercase

    uppercase("best")
    uppercase("Best School 98 Battery street")
