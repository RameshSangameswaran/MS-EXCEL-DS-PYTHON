import pandas as pd

# --- Create a sample dataset ---
data = {
    "Department": ["CS", "IT", "Math", "CS", "IT"],
    "Subject": ["AI", "Networks", "Algebra", "ML", "DBMS"],
    "Marks": [85, 78, 92, 88, 74]
}

# Create a DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# --- Column Selection ---
print("\nSelect 'Department' column:\n", df["Department"])
print("\nSelect multiple columns (Department & Marks):\n", df[["Department", "Marks"]])

# --- Column Addition ---
df["Grade"] = ["A", "B", "A+", "A", "C"]   # Adding a new column
print("\nDataFrame after adding 'Grade' column:\n", df)

# --- Column Deletion ---
df = df.drop("Subject", axis=1)   # Deleting the 'Subject' column
print("\nDataFrame after deleting 'Subject' column:\n", df)
