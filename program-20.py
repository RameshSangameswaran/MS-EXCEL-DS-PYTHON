import pandas as pd

# --- Step 1: Create a sample dataset and save it as CSV and Excel ---
data = {
    "Student": ["John", "Sara", "Alex", "Riya", "Tom", "Nina"],
    "Department": ["CS", "IT", "Math", "IT", "Marketing", "Finance"],
    "Marks": [85, 78, 92, 88, 74, 90]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("students.csv", index=False)

# Save to Excel
df.to_excel("students.xlsx", index=False)

# --- Step 2: Read the dataset back into DataFrames ---
# Read from CSV
df_csv = pd.read_csv("students.csv")
print("DataFrame created from CSV file:\n", df_csv)

# Read from Excel
df_excel = pd.read_excel("students.xlsx")
print("\nDataFrame created from Excel file:\n", df_excel)
