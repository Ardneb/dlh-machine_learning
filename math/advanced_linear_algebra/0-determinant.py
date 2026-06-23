#!/usr/bin/env python3
"""Calculate the determinant of a matrix"""


def determinant(matrix):
    """Function calculates the determinant of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 1
    elif len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a square matrix")
    elif len(matrix) == 1:
        return matrix[0][0]
    det = 0
    for i in range(len(matrix)):
        minor = [row[:i] + row[i + 1:]
        for row in matrix[1:]]
        det += ((-1) ** i) * matrix[0][i] * determinant(minor)
    return det
