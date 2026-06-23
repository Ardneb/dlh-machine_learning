#!/usr/bin/env python3
"""Calculate the inverse matrix of a matrix"""


def determinant(matrix):
    """Function calculates the determinant of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    if matrix == [[]] or matrix == []:
        return 1
    elif len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")
    elif len(matrix) == 1:
        return matrix[0][0]
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
    if matrix == [[]] or matrix == []:
        raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) != len(matrix[0]):
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


def cofactor(matrix):
    """Function calculates the cofactor matrix of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    if matrix == [[]] or matrix == []:
        raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")
    cofac = []
    minor_matrix = minor(matrix)
    for i in range(len(matrix)):
        cofac_row = []
        for j in range(len(matrix)):
            cofac_row.append((-1)**(i+j) * minor_matrix[i][j])
        cofac.append(cofac_row)
    return cofac


def adjugate(matrix):
    """Function calculates the adjugate matrix of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    if matrix == [[]] or matrix == []:
        raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")
    matrix_trans = []
    cofac_matrix = cofactor(matrix)
    for i in range(len(cofac_matrix)):
        trans_row = []
        for j in range(len(cofac_matrix)):
            trans_row.append(cofac_matrix[j][i])
        matrix_trans.append(trans_row)
    return matrix_trans


def inverse(matrix):
    """Function calculates the inverse of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    if matrix == [[]] or matrix == []:
        raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")
    det_matrix = determinant(matrix)
    adj_matrix = adjugate(matrix)
    inverse_matrix = []
    if det_matrix == 0:
        return None
    else:
        for i in range(len(adj_matrix)):
            inv_row = []
            for j in range(len(adj_matrix)):
                inv_row.append(adj_matrix[i][j] / det_matrix)
            inverse_matrix.append(inv_row)
        return inverse_matrix
