import pandas as pd

# --- Step 1: Create sample datasets and save them into an Excel file with multiple sheets ---
data_marks = {
    "Student": ["John", "Sara", "Alex", "Riya", "Tom", "Nina", "Sara", None],
    "Marks": [85, 78, 92, None, 74, 90, 78, 88]
}

data_attendance = {
    "Student": ["John", "Sara", "Alex", "Riya", "Tom", "Nina", None],
    "Attendance": [90, 85, 95, 80, 70, 88, 75]
}

# Save to Excel with multiple sheets
with pd.ExcelWriter("students_raw.xlsx") as writer:
    pd.DataFrame(data_marks).to_excel(writer, sheet_name="Marks", index=False)
    pd.DataFrame(data_attendance).to_excel(writer, sheet_name="Attendance", index=False)

# --- Step 2: Load the Excel file ---
xls = pd.ExcelFile("students_raw.xlsx")
df_marks = pd.read_excel(xls, "Marks")
df_attendance = pd.read_excel(xls, "Attendance")

print("Original Marks Data:\n", df_marks)
print("\nOriginal Attendance Data:\n", df_attendance)

# --- Step 3: Clean the data ---
# Remove rows with missing values
df_marks = df_marks.dropna()
df_attendance = df_attendance.dropna()

# Remove duplicates
df_marks = df_marks.drop_duplicates()
df_attendance = df_attendance.drop_duplicates()

# --- Step 4: Normalize a selected column (Min-Max scaling on Marks) ---
df_marks["Marks_Normalized"] = (df_marks["Marks"] - df_marks["Marks"].min()) / (df_marks["Marks"].max() - df_marks["Marks"].min())

print("\nCleaned & Normalized Marks Data:\n", df_marks)

# --- Step 5: Save cleaned data back to a new Excel file ---
with pd.ExcelWriter("students_cleaned.xlsx") as writer:
    df_marks.to_excel(writer, sheet_name="Marks_Cleaned", index=False)
    df_attendance.to_excel(writer, sheet_name="Attendance_Cleaned", index=False)

print("\nCleaned data saved to 'students_cleaned.xlsx'")
