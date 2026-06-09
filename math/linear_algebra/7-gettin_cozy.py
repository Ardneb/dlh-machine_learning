#!/usr/bin/env python3
"""Concatenate two matrices"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Write a function def cat_matrices2D(mat1, mat2, axis=0):
    that concatenates two matrices along a specific axis
    """
    new_matrix = []
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        else:
            for i in range(len(mat1)):
                new_matrix.append(mat1[i])
            for i in range(len(mat2)):
                new_matrix.append(mat2[i])
            return new_matrix
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        else:
            for i in range(len(mat1)):
                new_matrix.append(mat1[i] + mat2[i])
            return new_matrix
