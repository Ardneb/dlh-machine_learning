#!/usr/bin/env python3
"""List with 9 elements"""
arr = [9, 8, 2, 3, 9, 4, 1, 0, 3]

"""Get the first 2 elements of the list"""
arr1 = arr[:1]

"""Get the last 5 elements of the list"""
arr2 = arr[-5:]

"""Get the elements 2 to 6"""
arr3 = arr[1:5]

"""Print the results"""
print("The first two numbers of the array are: {}".format(arr1))
print("The last five numbers of the array are: {}".format(arr2))
print("The 2nd through 6th numbers of the array are: {}".format(arr3))
