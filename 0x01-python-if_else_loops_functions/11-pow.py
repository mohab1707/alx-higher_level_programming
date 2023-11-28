#!/usr/bin/python3

def pow(a, b):
    """Computes a to the power of b and returns the value."""
    return a ** b


if __name__ == "__main__":
    pow = __import__('11-pow').pow

    print(pow(2, 2))
    print(pow(98, 2))
    print(pow(98, 0))
    print(pow(100, -2))
    print(pow(-4, 5))
