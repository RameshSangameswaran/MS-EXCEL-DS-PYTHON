# Import pandas library
import pandas as pd

# Create a dataset (dictionary with labels and values)
data = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 88,
    'Eva': 95
}

# Create a Pandas Series
marks_series = pd.Series(data)

# Display the Series
print("Pandas Series with Labels (Student Marks):\n")
print(marks_series)

# Access individual elements using labels
print("\nMarks of Bob:", marks_series['Bob'])

# Perform operations
print("\nAverage Marks:", marks_series.mean())
print("Highest Marks:", marks_series.max())
print("Lowest Marks:", marks_series.min())