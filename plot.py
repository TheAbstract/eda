import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

def histbox(df, column):
    '''
    plots a histogram with a box-and-whiskers at the top.
    got this wonderful idea from @janmpia
        source - https://www.kaggle.com/competitions/playground-series-s3e8/discussion/391832
    '''
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={'height_ratios': (.15, .85)})
    ax_box.title.set_text(f'{column} histogram and boxplot')
    sns.boxplot(df['column'], orient='h', ax=ax_box)
    sns.histplot(data=df, x=column, ax=ax_hist)
    ax_box.set(xlabel='')  # remove x axis name for the boxplot
    plt.show()

def corrplot(df):
    '''
    use spearman since it doesn't make assumptions about underlying data distribution.
    '''
    corrmatrix = df.corr(method='spearman', numeric_only=True)
    mask = np.zeros_like(corrmatrix)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style(style='white'):
        sns.heatmap(corrmatrix, mask=mask, cmap='RdBu', linewidths=.5)
        plt.title('Correlation of Variables')
        plt.show()

def showcorr(df):
    corr = df.corr(method='spearman', numeric_only=True)
    corr = corr.style.background_gradient(cmap='RdBu', axis=None, vmin=-1, vmax=1)
    return corr.format(precision=4)

def prediction_error(model, X, y):
    fig, axes = plt.subplots(ncols=2, figsize=(11, 4))
    PredictionErrorDisplay.from_estimator(model, X, y, ax=axes[0], kind='actual_vs_predicted')
    PredictionErrorDisplay.from_estimator(model, X, y, ax=axes[1], kind='residual_vs_predicted')
    plt.show()
