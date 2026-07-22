#!/usr/bin/env python3
"""Create a class Normal that represents a normal distribution"""


class Normal:
    """Class represents a normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initialise Normal instance
        with parameters data, mean and stddev
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            else:
                self.mean = float(mean)
                self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            Deviation = 0
            for i in range(len(data)):
                Deviation += (data[i] - self.mean) ** 2
            self.stddev = float((Deviation / (len(data))) ** 0.5)

    def z_score(self, x):
        """Calculate the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculate the x-value of a given z-score"""
        return (z * self.stddev) + self.mean
