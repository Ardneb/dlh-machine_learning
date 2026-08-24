#!/usr/bin/env python3
"""Rename the Timestamp column to Datetime"""
import pandas as pd


def rename(df):
    """
    Function takes a pd.DataFrame,
    renames the column Timestamp to DateTimeand
    and converts it from timestamp to datetime
    """
    new_col = df.rename(columns={"Timestamp": "Datetime"})
    new_col['Datetime'] = pd.to_datetime(new_col['Datetime'], unit='s')
    return new_col[['Datetime', "Close"]]
