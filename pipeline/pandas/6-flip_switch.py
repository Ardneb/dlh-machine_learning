#!/usr/bin/env python3
"""Take a dataframe and perform several operations on it"""


def flip_switch(df):
    """
    Sorts the DataFrame in reverse chronological
    order and transposes the transformed DataFrame
    """
    return df.sortvalues(by='Timestamp', ascending=False).T
