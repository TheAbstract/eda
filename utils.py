def is_numeric(value):
    return isinstance(value, int) or isinstance(value, float) or isinstance(value, complex)

def is_series(value):
    return isinstance(value, list) or isinstance(value, tuple)

def describe_more(df):
    more = pd.DataFrame(df.dtypes, columns=['data type'])
    more['# missing'] = df.isna().sum().values 
    more['% missing'] = df.isna().sum().values / len(df) * 100
    more['# unique'] = df.nunique().values
    desc = df.describe().T
    more = pd.concat([more, desc], axis=1).style.background_gradient(cmap='BuGn')
    return more
