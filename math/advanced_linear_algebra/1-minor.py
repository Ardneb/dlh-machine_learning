#!/usr/bin/env python3
"""Calculate the minor matrix of a matrix"""
determinant = __import__('0-determinant').determinant


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
