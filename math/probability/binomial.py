#!/usr/bin/env python3
"""Create a class Binomial that represents a binomial distribution"""


class Binomial:
    """Class represents an binomial distribution"""
    def __init__(self, data=None, n=1, p=0.5):
        """
        Initialise Binomial instance
        with parameters data, n and p
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            elif p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            else:
                self.n = round(n)
                self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            val = 0
            for i in range(len(data)):
                val += ((data[i] - mean) ** 2)
            variance = val / len(data)
            p = 1 - (variance / mean)
            self.n = round(mean / p)
            self.p = float(mean / self.n)
