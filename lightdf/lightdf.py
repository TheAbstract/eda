import pandas as pd

def suggest_data_type_conversions(df):
    # Range of values that can be represented by different data types.
    INT8_MIN = -128
    INT8_MAX = 127
    INT16_MIN = -32768
    INT16_MAX = 32767
    INT32_MIN = -2147483648
    INT32_MAX = 2147483647
    FLOAT32_MIN = -3.4e38
    FLOAT32_MAX = 3.4e38
    FLOAT16_MIN = -6.8e38
    FLOAT16_MAX = 6.8e38

    suggestions = {}
    for col in df.columns:
        dtype = df[col].dtype
        col_min = df[col].min()
        col_max = df[col].max()
        if dtype == 'int64':
            if col_min >= INT8_MIN and col_max <= INT8_MAX:
                suggestions[col] = 'int8'
            elif col_min >= INT16_MIN and col_max <= INT16_MAX:
                suggestions[col] = 'int16'
            elif col_min >= INT32_MIN and col_max <= INT32_MAX:
                suggestions[col] = 'int32'
        elif dtype == 'float64':
            if col_min >= FLOAT32_MIN and col_max <= FLOAT32_MAX:
                suggestions[col] = 'float32'
            elif col_min >= FLOAT16_MIN and col_max <= FLOAT16_MAX:
                suggestions[col] = 'float16'
        elif dtype == 'object':
            # For strings, we can't suggest a more memory-efficient type without knowing the content.
            # But we can suggest using 'category' if the number of unique values is small.
            if df[col].nunique() <= 255:
                suggestions[col] = 'category'
    return suggestions

def bytes_to_human_readable(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f'{size:.{decimal_places}f} {unit}'

def memory_savings(df, suggestions):
    current_memory_usage = df.memory_usage(deep=True).sum()
    new_df = df.copy()
    for col, dtype in suggestions.items():
        new_df[col] = new_df[col].astype(dtype)
    new_memory_usage = new_df.memory_usage(deep=True).sum()
    savings = current_memory_usage - new_memory_usage
    savings_human_readable = bytes_to_human_readable(savings)
    print(f'Estimated memory savings: {savings_human_readable}')

def apply_suggestions(df, suggestions):
    for col, dtype in suggestions.items():
        df[col] = df[col].astype(dtype)
    return df


if __name__ == '__main__':
    df = pd.read_csv('large_dataframe.csv')
    df.info(memory_usage='deep')

    suggestions = suggest_data_type_conversions(df)
    memory_savings = memory_savings(df, suggestions)

    optimised_df = apply_suggestions(df, suggestions)
    optimised_df.info(memory_usage='deep')
