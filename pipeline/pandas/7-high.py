#!/usr/bin/env python3
"""Function sorts dataframe by High price in descending order"""


def high(df):
    """
    Sorts the DataFrame by High price in descending order
    """
    return df.sort_values('High', ascending=False)
