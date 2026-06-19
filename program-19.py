import pandas as pd

# --- Create sample datasets ---
data1 = {
    "EmployeeID": [1, 2, 3, 4],
    "Name": ["John", "Sara", "Alex", "Riya"],
    "Department": ["HR", "IT", "Finance", "IT"]
}

data2 = {
    "EmployeeID": [3, 4, 5, 6],
    "Salary": [61000, 48000, 52000, 45000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# --- Merging ---
merged_df = pd.merge(df1, df2, on="EmployeeID", how="inner")
print("\nMerged DataFrame (Inner Join on EmployeeID):\n", merged_df)

# --- Joining ---
# For joining, we need to set index
df1_indexed = df1.set_index("EmployeeID")
df2_indexed = df2.set_index("EmployeeID")

joined_df = df1_indexed.join(df2_indexed, how="outer")
print("\nJoined DataFrame (Outer Join on EmployeeID):\n", joined_df)

# --- Concatenating ---
data3 = {
    "EmployeeID": [7, 8],
    "Name": ["Tom", "Nina"],
    "Department": ["Marketing", "Finance"]
}

df3 = pd.DataFrame(data3)

concat_df = pd.concat([df1, df3], ignore_index=True)
print("\nConcatenated DataFrame (df1 + df3):\n", concat_df)
