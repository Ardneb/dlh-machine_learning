#!/usr/bin/env python3
"""Calculate the minor matrix of a matrix"""


def determinant(matrix):
    """Function calculates the determinant of a matrix"""
    det = 0
    for i in range(len(matrix)):
        minor = [row[:i] + row[i + 1:]
                 for row in matrix[1:]]
        det += ((-1) ** i) * matrix[0][i] * determinant(minor)
    return det


def minor(matrix):
    """Function calculates the minor matrix of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    if len(matrix) != len(matrix[0]) or matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")
    minormatrix = []
    for i in range(len(matrix)):
        minor_row = []
        for j in range(len(matrix[0])):
            submatrix = [row[:j] + row[j + 1:]
                         for row in matrix[:i] + matrix[i+1:]]
            minor_row.append(determinant(submatrix))
        minormatrix.append(minor_row)
    return minormatrix
