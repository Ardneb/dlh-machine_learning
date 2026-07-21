#!/usr/bin/env python3
"""Create a class Poisson that represents a poisson distribution"""


class Poisson:
    """Class represents a poisson distribution"""
    def __init__(self, data=None, lambtha=1.):
        """
        Initialise Poisson instances
        with parameters data and lambtha
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data)/len(data))

    def pmf(self, k):
        """Calculate the value of the PMF"""
        if k < 0:
            return 0
        elif not isinstance(k, int):
            k = int(k)
        factorial = 1
        e = 2.7182818285
        for i in range(1, k + 1):
            factorial *= i
        return (self.lambtha ** k * e ** (-self.lambtha)) / factorial

    def cdf(self, k):
        """Calculate the value of the CDF"""
        if k < 0:
            return 0
        elif not isinstance(k, int):
            k = int(k)
        cdf = 0
        for i in range(0, k + 1):
            cdf += self.pmf(i)
        return cdf
