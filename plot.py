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
    sns.heatmap(corrmatrix, vmin=-1, vmax=1, cmap='RdBu')
    plt.title('Correlation of Variables')
    plt.show()
