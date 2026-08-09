#!/usr/bin/env python3
"""Create a class Multivariate Normal distribution"""
import numpy as np


class MultiNormal:
    """Class represents a Multivariat Normal distribution"""
    def __init__(self, data):
        """
        Initialise Multivariat Normal
        instance with parameter data
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        if data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")
        self.mean = np.mean(data, axis=1).reshape(-1, 1)
        deviation = data - self.mean
        self.cov = deviation @ deviation.T / (data.shape[1] - 1)
