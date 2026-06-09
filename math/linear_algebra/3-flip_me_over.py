#!/usr/bin/env python3
"""Transpose a 2D Matrix"""


def matrix_transpose(matrix):
    """Function returns the transpose of a 2D matrix"""
    trans_list = []
    for i in range(len(matrix[0])):
        row_new = []
        for j in range(len(matrix)):
            row_new.append(matrix[j][i])
        trans_list.append(row_new)
    return trans_list
