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

    def pmf(self, k):
        """Calculate the value of the PMF"""
        if k < 0:
            return 0
        elif not isinstance(k, int):
            k = int(k)
        n_fac = 1
        k_fac = 1
        n_k_fac = 1
        for i in range(1, self.n + 1):
            n_fac *= i
        for i in range(1, k + 1):
            k_fac *= i
        for i in range(1, (self.n - k) + 1):
            n_k_fac *= i
        return (n_fac / (k_fac * n_k_fac) *
                self.p ** k * (1 - self.p) ** (self.n - k))
