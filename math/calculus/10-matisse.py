#!/usr/bin/env python3
"""Calculates the derivative of a polynomial"""


def poly_derivative(poly):
    """Derivative of a polynomial"""
    if not isinstance(poly, list):
        return None
    elif len(poly) == 0:
        return None
    elif len(poly) == 1:
        return [0]
    else:
        result = []
        for i in range(1, len(poly)):
            result.append(i-1, poly[i] * i)
        return result
