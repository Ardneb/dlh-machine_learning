#!/usr/bin/env python3
"""Calculat a correlation matrix"""
import numpy as np


def correlation(C):
    """Function calculates a correlation matrix"""
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if C.ndim != 2 or len(C) != len(C[0]):
        raise ValueError("C must be a 2D square matrix")
    stdev = np.sqrt(np.diag(C))
    outer = np.outer(stdev, stdev)
    return C / outer
