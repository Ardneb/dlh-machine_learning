#!/usr/bin/env python3
"""Calculate the definiteness of a matrix"""
import numpy as np


def definiteness(matrix):
    """Function calculates the definiteness of a matrix"""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    elif matrix.ndim != 2:
        return None
    elif matrix.shape[0] == 0:
        return None
    elif matrix.shape[0] != matrix.shape[1]:
        return None
    elif not np.allclose(matrix, matrix.T):
        return None
    evalue, evector = np.linalg.eig(matrix)
    if np.all(evalue > 0):
        return "Positive definite"
    elif np.all(evalue >= 0):
        return "Positive semi-definite"
    elif np.all(evalue < 0):
        return "Negative definite"
    elif np.all(evalue <= 0):
        return "Negative semi-definite"
    else:
        return "Indefinite"
