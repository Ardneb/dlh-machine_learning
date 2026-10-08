#!/usr/bin/env python3
"""Take a dataframe and perform several operations on it"""


def analyze(df):
    """
    Computes descriptive statistics for all columns except the Timestamp column
    """
    return df.drop(columns=['Timestamp']).describe()
