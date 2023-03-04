import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def is_missing(df, plot=False):
    null = df.isnull()
    if plot:
        sns.heatmap(null.T, xticklabels=False, cbar=False, cmap='binary')
        plt.show()
    else:
        return null.mean().sort_values()[::-1]

def drop_missing(df, percent=0.8):
    thresh = len(df) * (1 - percent)
    return df.dropna(thresh=thresh, axis=1)

def fill_missing(df):
    for col in df:
        if df[col].dtypes == 'object':
            mode = df[col].value_counts().index[0]
            df[col].fillna(mode, inplace=True)
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col].fillna(df[col].median(), inplace=True)

def numeric_split(df):
    numeric = df.select_dtypes('number')
    objects = df.select_dtypes('object')
    return numeric, objects
