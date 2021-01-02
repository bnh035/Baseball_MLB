#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import math
from scipy import stats
import seaborn as sns

def plot_data(df):
    #df.plot(x='break_angle', y='spin_dir')
    plt.scatter(df['total_mov'], df['spin_dir'])
    plt.show()

def plot_grid(df):#, col):
    col = list(df.columns.values)
    length = len(col)

    ex_list = []
    for i in col:
        for j in col:
            if j not in ex_list:
                fig, ax = plt.subplots(1, 1)
                ax.scatter(df[i], df[j])
                fig.savefig('fig' + str(i) + str(j) + '.png')
                plt.close(fig)
        ex_list.append(i)
    """
    for i in range(length):
        for j in range(length):
            axs[i, j].scatter(df[col[i]], df[col[j]])
    """
    plt.show()

def heatmap(df, n_bins):
    plt.hist2d(df['break_length'], df['spin_rate'], bins=n_bins, normed=True, cmap='plasma', norm=matplotlib.colors.LogNorm())
    plt.show()

def kde(df):
    sns.kdeplot(df['total_mov'], df['spin_rate'], shade=True, cmap='plasma')
    plt.show()

def data_surface(df):
    grid_num = 20
    h = 0.5

    y = df['break_y']
    x = df['spin_rate']

    bins_list = [100, 100]

    ret = stats.binned_statistic_2d(x, y, None, 'count', bins=bins_list)
    bin_arr = ret.statistic

    plt.imshow(bin_arr[::-1], interpolation='gaussian')
    plt.show()
