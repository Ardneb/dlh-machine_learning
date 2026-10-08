#!/usr/bin/env python3
"""Function removes rows with NaN values in the Close column"""


def prune(df):
    """
    Removes rows with NaN values in the Close column
    """
    return df.dropna(subset=['Close'])
