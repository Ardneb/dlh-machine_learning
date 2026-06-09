#!/usr/bin/env python3
"""Add two matrices element_wise"""


def add_matrices2D(mat1, mat2):
    """Function that adds 2 matrices element_wise"""
    new_matrix = []
    if len(mat1[0]) != len(mat2[0]):
        return None
    elif len(mat1) != len(mat2):
        return None
    else:
        for i in range(len(mat1)):
            row_new = []
            for j in range(len(mat2[0])):
                row_new.append(mat1[i][j] + mat2[i][j])
            new_matrix.append(row_new)
        return new_matrix
