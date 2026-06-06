#!/usr/bin/python3
"""
This module computes the factorial of a non-negative integer
passed as a command-line argument, using recursion.
"""
import sys


def factorial(n):
    """
    Compute the factorial of a non-negative integer recursively.

    Args:
        n (int): A non-negative integer whose factorial is computed.

    Returns:
        int: The factorial of n (n!). Returns 1 when n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)