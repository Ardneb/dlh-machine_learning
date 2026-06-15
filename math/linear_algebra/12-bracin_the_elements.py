#!/usr/bin/env python3
"""Addition, subtraction, multiplication, and division"""


def np_elementwise(mat1, mat2):
    """
    Function performs element-wise addition,
    subtraction, multiplication, and division
    """
    addition = np.add(mat1, mat2)
    subtraction = np.subtract(mat1, mat2)
    multiplication = np.multiply(mat1, mat2)
    division = np.divide(mat1, mat2)
    return (addition, subtraction, multiplication, division)
