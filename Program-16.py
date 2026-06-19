import pandas as pd

# --- Create a sample dataset ---
data = {
    "Student": ["John", "Sara", "Alex", "Riya", "Tom", "Nina"],
    "Department": ["CS", "IT", "Math", "IT", "Marketing", "Finance"],
    "Marks": [85, 78, 92, 88, 74, 90]
}

# Create a DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# --- Get n-largest values from 'Marks' column ---
n = 3
largest = df.nlargest(n, "Marks")
print(f"\nTop {n} students by Marks:\n", largest)

# --- Get n-smallest values from 'Marks' column ---
smallest = df.nsmallest(n, "Marks")
print(f"\nBottom {n} students by Marks:\n", smallest)
