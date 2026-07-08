#!/usr/bin/env python3
"""Calculate the sum"""


def summation_i_squared(n):
    """Calculate Sum of i squared"""
    if not isinstance(n, int):
        return None
    elif n < 1:
        return None
    else:
        result = n * (n+1) * (2*n+1) // 6
        return result
