#!/usr/bin/env python3
"""Take a dataframe and perform several operations on it"""
import pandas as pd


def array(df):
    """
    Function takes a pd.DataFrame and returns a numpy array
    of the Close column
    """
    return df[['High', 'Close']].tail(10).to_numpy()
