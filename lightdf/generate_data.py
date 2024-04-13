import pandas as pd
import numpy as np


num_rows = 20_000_000

# Generate random data for each column type
data_int = np.random.randint(0, 128, size=num_rows)
data_float = np.random.rand(num_rows)
data_str = np.random.choice(['A', 'B', 'C', 'D', 'E'], size=num_rows)

# Create the DataFrame
df = pd.DataFrame({
    'IntegerColumn': data_int,
    'FloatColumn': data_float,
    'StringColumn': data_str
})

# Print the first few rows to verify the DataFrame
print(df.head())

# Write the DataFrame to a CSV file in chunks
# Adjust the chunk size based on your system's memory and the size of the DataFrame
chunk_size = 10000 # Adjust this value based on your system's memory
df.to_csv('large_dataframe.csv', index=False)

print('Done.')
