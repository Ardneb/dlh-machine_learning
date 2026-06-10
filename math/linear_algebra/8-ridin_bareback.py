#!/usr/bin/env python3
"""Perform matrix multiplication"""


def mat_mul(mat1, mat2):
    """Funtion that performs matrix multiplication"""
    new_matrix = []
    if len(mat1[0]) != len(mat2):
        return None
    else:
        for i in range(len(mat1)):
            row_new = []
            for j in range(len(mat2[0])):
                matrix_add = 0
                for k in range(len(mat2)):
                    matrix_add += mat1[i][k] * mat2[k][j]
                row_new.append(matrix_add)
            new_matrix.append(row_new)
        return new_matrix
