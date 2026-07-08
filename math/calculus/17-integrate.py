#!/usr/bin/env python3
"""Calculates the integral"""


def poly_integral(poly, C=0):
    """Function calculates the integral of a polynomial"""
    if not isinstance(poly, list):
        return None
    elif len(poly) == 0:
        return None
    elif not isinstance(C, int):
        return None
    else:
        result = [C]
        for i in range(len(poly)):
            value = poly[i] * 1 / (i + 1)
            if value.is_integer():
                result.append(int(poly[i] * 1 / (i + 1)))
            else:
                result.append(poly[i] * 1 / (i + 1))
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return result
