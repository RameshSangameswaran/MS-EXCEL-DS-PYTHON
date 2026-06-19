import pandas as pd

# --- Create a sample dataset ---
data = {
    "Employee": ["John", "Sara", "Alex", "Riya", "Tom"],
    "Department": ["HR", "IT", "Finance", "IT", "Marketing"],
    "Salary": [45000, 52000, 61000, 48000, 50000]
}

# Create a DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# --- Row Selection ---
print("\nSelect row at index 2:\n", df.loc[2])  # Select a single row
print("\nSelect multiple rows (index 1 and 3):\n", df.loc[[1, 3]])  # Select multiple rows

# --- Row Addition ---
new_row = {"Employee": "Nina", "Department": "Finance", "Salary": 58000}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print("\nDataFrame after adding a new row:\n", df)

# --- Row Deletion ---
df = df.drop(4, axis=0)  # Delete row at index 4
print("\nDataFrame after deleting row with index 4:\n", df)
