#!/usr/bin/env python3
"""Show me the frquency"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """plot a histogram of student scores"""

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))
    plt.hist(student_grades, bins=10, edgecolor='black')
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.xlim(0, 100)
    plt.title("Project A")
