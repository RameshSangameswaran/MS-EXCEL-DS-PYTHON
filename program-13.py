import pandas as pd
import numpy as np

# --- Create a sample dataset ---
data = {
    "Department": ["CS", "IT", "Math", "CS", "IT"],
    "Subject": ["AI", "Networks", "Algebra", "ML", "DBMS"],
    "Marks": [85, 78, 92, 88, 74]
}

# Create a DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Convert DataFrame to NumPy array
df_array = df.to_numpy()
print("\nDataFrame converted to NumPy array:\n", df_array)

# Create a Series (Marks column)
marks_series = df["Marks"]
print("\nOriginal Series:\n", marks_series)

# Convert Series to NumPy array
series_array = marks_series.to_numpy()
print("\nSeries converted to NumPy array:\n", series_array)

# --- Example usage of NumPy array ---
print("\nAverage marks (using NumPy):", np.mean(series_array))
