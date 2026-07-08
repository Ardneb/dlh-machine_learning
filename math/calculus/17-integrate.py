#!/usr/bin/env python3
"""Calculates the integral"""


def poly_integral(poly, C=0):
    """Function calculates the integral of a polynomial"""
    if not isinstance(poly, list):
        return None
    elif len(poly) == 0:
        return None
    elif not isinstance(c, int):
        return None
    else:
        result = [c]
        for i in range(len(poly)):
            result.append(poly[i] * 1 / (i + 1))
        return result
