## 0. From Numpy
Write a function def from_numpy(array): that creates a pd.DataFrame from a np.ndarray
## 1. From Dictionary
Write a python script that creates a pd.DataFrame from a dictionary
## 2. From File
Write a function def from_file(filename, delimiter): that loads data from a file as a pd.DataFrame
## 3. Rename
Write a function def rename(df): that takes a pd.DataFrame as input and performs the following
### 4. To Numpy
Write a function that takes a pd.DataFrame as input and performs the following
### 5. Slice
Write a function that takes a pd.DataFrame and extracts columns
### 6. Flip it and Switch it
Write a function that takes a pd.DataFrame and sorts the data in reverse chronological order
### 7. Sort
Write a function that takes a pd.DataFrame and sorts it by the High price in descending order
### 8. Prune
Write a function def that takes a pd.DataFrame and removes any entries where Close has NaN values
### 9. Fill
Write a function that takes a pd.DataFrame and removes the Weighted_Price column and fills missing columns
### 10. Indexing
Write a function that takes a pd.DataFrame and sets the Timestamp column as the index of the dataframe
### 11. Concat
Write a function that takes two pd.DataFrame objects and indexes both dataframes on their Timestamp columns. Includes all timestamps from df2 (bitstamp) up to and including timestamp 1417411920. Concatenates the selected rows from df2 to the top of df1 (coinbase). Adds keys to the concatenated data, labeling the rows from df2 as bitstamp and the rows from df1 as coinbase.