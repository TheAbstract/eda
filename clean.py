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

def to_snake_case(df):
    df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]
    return df

def remove_highly_correlated(df, threshold):
    corr_matrix = df.corr(method='spearman', numeric_only=True)
    corr_triu = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    above_threshold = [col for col in corr_triu.columns if any(abs(corr_triu[col]) > threshold)]
    df.drop(above_threshold, axis=1, inplace=True)
    print('Removed variables:', *above_threshold)
    return df
