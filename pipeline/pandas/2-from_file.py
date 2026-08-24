#!/usr/bin/env python3
"""Loading data from a file"""
import pandas as pd


def from_file(filename, delimiter):
    """Function loads data from a file as a pd.DataFrame"""
    df = pd.read_csv(filename, sep=delimiter)
    return df
