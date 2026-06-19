import pandas as pd
import re

# --- Step 1: Create a sample dataset and save it as CSV ---
data = {
    "Student": ["John", "Sara", "Alex", "Riya", "Tom", "Nina", "Sara", None],
    "Department": ["CS", "IT", "Math", "IT", "Marketing", "Finance", "IT", "CS"],
    "Marks": [85, 78, 92, None, 74, 90, 78, 88]
}

df = pd.DataFrame(data)
df.to_csv("students_raw.csv", index=False)

# --- Step 2: Load the CSV file ---
df = pd.read_csv("students_raw.csv")
print("Original DataFrame:\n", df)

# --- Step 3: Clean the data ---
# Remove duplicates
df = df.drop_duplicates()

# Handle missing values (fill with default values)
df["Student"] = df["Student"].fillna("Unknown")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())  # Replace missing marks with average

# --- Step 4: Normalize text using RegEx ---
# Example: Remove unwanted characters (digits/special chars) from Student names
df["Student"] = df["Student"].apply(lambda x: re.sub(r"[^A-Za-z]", "", x))

# Standardize Department names (convert to uppercase)
df["Department"] = df["Department"].str.upper()

print("\nCleaned DataFrame:\n", df)

# --- Step 5: Save cleaned data back to CSV ---
df.to_csv("students_cleaned.csv", index=False)
print("\nCleaned data saved to 'students_cleaned.csv'")
