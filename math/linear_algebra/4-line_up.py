#!/usr/bin/env python3
"""Add two arrays element-wise"""


def add_arrays(arr1, arr2):
    """Function adds arrays element-wise"""
    new_list = []
    if len(arr1) != len(arr2):
        return None
    else:
        for i in range(len(arr1)):
            new_list.append(arr1[i] + arr2[i])
        return new_list
