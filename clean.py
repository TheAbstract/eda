import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def is_empty(df, plot=False):
    null = df.isnull()
    if plot:
        sns.heatmap(null.T, xticklabels=False, cbar=False, cmap='binary')
        plt.show()
    else:
        return null.mean().sort_values()[::-1]

def drop_empty(df, percent=0.8):
    thresh = len(df) * (1 - percent)
    return df.dropna(thresh=thresh, axis=1)

def numeric_split(df):
    numeric = df.select_dtypes('number')
    objects = df.select_dtypes('object')
    return numeric, objects

