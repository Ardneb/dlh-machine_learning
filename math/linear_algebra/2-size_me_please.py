#!/usr/bin/env python3
"""Size of a matrix"""


def matrix_shape(matrix):
    """Calculate the shape of a matrix"""
    my_list = []
    while isinstance(matrix, list):
        my_list.append(len(matrix))
        matrix = matrix[0]
    return my_list
