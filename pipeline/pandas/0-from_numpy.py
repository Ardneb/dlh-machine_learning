#!/usr/bin/env python3
""" function creating a data frame from an np ndarray"""
import pandas as pd


def from_numpy(array):
    """
    Create a dataframe df from array
    which is an np ndarray
    """
    arr = array.shape
    col = arr[1]
    col_range = list(chr(65 + i) for i in range(col))

    df = pd.DataFrame(array, columns=col_range)
    return df
