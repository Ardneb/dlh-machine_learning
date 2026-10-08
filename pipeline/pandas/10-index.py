#!/usr/bin/env python3
"""Take a dataframe and perform several operations on it"""


def index(df):
    """
    Takes a dataframe and performs several operations on it
    """
    return df.set_index('Timestamp')
