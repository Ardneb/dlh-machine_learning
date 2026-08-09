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

    def pdf(self, x):
        """Method calculates the PDF at a data point"""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        d = self.mean.shape[0]
        if x.shape != (d, 1):
            raise ValueError(f"x must have the shape ({d}, 1)")
        k = len(self.mean)
        det_cov = np.linalg.det(self.cov)
        inv_cov = np.linalg.inv(self.cov)
        normal_const = 1.0 / np.sqrt((2 * np.pi) ** k * det_cov)
        deviation = x - self.mean
        expon = -0.5 * (deviation.T @ (inv_cov @ deviation)).item()
        return float(normal_const * np.exp(expon))
