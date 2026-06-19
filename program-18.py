import pandas as pd

# --- Create a sample dataset ---
data = {
    "Student": ["John", "Sara", "Alex", "Riya", "Tom", "Nina", "Arjun", "Meena"],
    "Department": ["CS", "IT", "Math", "IT", "Marketing", "Finance", "CS", "Math"],
    "Marks": [85, 78, 92, 88, 74, 90, 81, 95]
}

# Create a DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# --- Group by Department and calculate average marks ---
avg_marks = df.groupby("Department")["Marks"].mean()
print("\nAverage Marks by Department:\n", avg_marks)

# --- Group by Department and count number of students ---
count_students = df.groupby("Department")["Student"].count()
print("\nNumber of Students in each Department:\n", count_students)

# --- Group by Department and get maximum marks ---
max_marks = df.groupby("Department")["Marks"].max()
print("\nMaximum Marks in each Department:\n", max_marks)
