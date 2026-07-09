#!/usr/bin/env python3
"""Show me the frquency"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """plot a histogram of student scores"""

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))
    bin_unit = np.arange(0, 110, 10)
    plt.hist(student_grades, bins=bin_unit, edgecolor='black')
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title("Project A")
