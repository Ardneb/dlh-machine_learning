#!/usr/bin/env python3
"""Stacked bar power"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """Plot a stacked bar graph"""

    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    x = np.arange(3)
    apples = fruit[0, :]
    bananas = fruit[1, :]
    oranges = fruit[2, :]
    peaches = fruit[3, :]

    plt.xticks(np.arange(3), ['Farrah', 'Fred', 'Felicia'])
    plt.bar(x, apples, color='red', width=0.5,
            label='apples')
    plt.bar(x, bananas, color='yellow', width=0.5,
            bottom=apples, label='bananas')
    plt.bar(x, oranges, color='#ff8000', width=0.5,
            bottom=apples+bananas, label='oranges')
    plt.bar(x, peaches, color='#ffe5b4', width=0.5,
            bottom=apples+bananas+oranges, label='peaches')
    plt.legend()
    plt.ylabel('Quantity of Fruit')
    plt.ylim(0, 80)
    plt.title('Number of Fruit per Person')
    plt.yticks(np.arange(0, 90, 10))
    plt.show()
