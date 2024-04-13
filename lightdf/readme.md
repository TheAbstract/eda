# lightdf

A pandas utility for optimising the memory usage of pandas DataFrames.
The default for pandas is to use the largest data type to store values in. For example a column of integers will always be assigned `int64`, which isn't usually necessary.

This utility will analyse each column of a DataFrame, suggest the smallest non-breaking data type conversion, provide a summary of the suggestions, and offer a way to apply these suggestions.

## usage

A 1.4 GB csv file is optimised to 114.4 MB.

```python
In [1]: import pandas as pd

In [2]: df = pd.read_csv('large_dataframe.csv')

In [3]: df.info(memory_usage='deep')
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20000000 entries, 0 to 19999999
Data columns (total 3 columns):
 #   Column         Dtype  
---  ------         -----  
 0   IntegerColumn  int64  
 1   FloatColumn    float64
 2   StringColumn   object
dtypes: float64(1), int64(1), object(1)
memory usage: 1.4 GB
```

Get estimated memory savings based on suggested conversions:

```python
In [4]: from lightdf import *

In [5]: suggestions = suggest_data_type_conversions(df)

In [6]: memory_savings(df, suggestions)
Estimated memory savings: 1.27 GB
```


Then apply the suggestions to the file:

```python
In [7]: optimised_df = apply_suggestions(df, suggestions)

In [8]: optimised_df.info(memory_usage='deep')
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20000000 entries, 0 to 19999999
Data columns (total 3 columns):
 #   Column         Dtype   
---  ------         -----   
 0   IntegerColumn  int8    
 1   FloatColumn    float32
 2   StringColumn   category
dtypes: category(1), float32(1), int8(1)
memory usage: 114.4 MB
```
