#!/usr/bin/env python3
"""Calculate the intersection"""
import numpy as np
likelihood = __import__("0-likelihood").likelihood


def intersection(x, n, P, Pr):
    """
    Function calculates the intersection
    of obtaining this data with the various
    hypothetical probabilities
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    elif not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer that is "
                         "greater than or equal to 0")
    elif x > n:
        raise ValueError("x cannot be greater than n")
    elif not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    elif not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    elif np.any((P < 0) | (P > 1)):
        raise ValueError(f"All values in {P} must be in the range [0, 1]")
    elif np.any((Pr < 0) | (Pr > 1)):
        raise ValueError(f"All values in {Pr} must be in the range [0, 1]")
    elif not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")
    return likelihood(x, n, P) * Pr
