#!/usr/bin/env python3
"""Function takes a dataframe and extracts columns"""


def slice(df):
    """
    Function takes a pd.DataFrame and returns a slice of
    the columns High, Low, Close and Volume_(BTC)
    """
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]
