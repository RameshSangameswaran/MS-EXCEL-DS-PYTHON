import pandas as pd
import matplotlib.pyplot as plt

# --- Create a sample dataset ---
data = {
    "Student": ["John", "Sara", "Alex", "Riya", "Tom", "Nina"],
    "Department": ["CS", "IT", "Math", "IT", "Marketing", "Finance"],
    "Marks": [85, 78, 92, 88, 74, 90],
    "Attendance": [90, 85, 95, 80, 70, 88]
}

# Create a DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# --- Bar Plot ---
df.plot(kind="bar", x="Student", y="Marks", title="Marks of Students (Bar Plot)")
plt.show()

# --- Histogram ---
df["Marks"].plot(kind="hist", bins=5, title="Distribution of Marks (Histogram)")
plt.show()

# --- Line Plot ---
df.plot(kind="line", x="Student", y=["Marks", "Attendance"], title="Marks vs Attendance (Line Plot)")
plt.show()

# --- Scatter Plot ---
df.plot(kind="scatter", x="Marks", y="Attendance", title="Marks vs Attendance (Scatter Plot)")
plt.show()
