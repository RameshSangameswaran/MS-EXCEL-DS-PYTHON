# Import pandas library
import pandas as pd

# Create your own dataset (dictionary)
data = {
    'Employee_Name': ['Ravi', 'Priya', 'Amit', 'Neha', 'Arjun'],
    'Age': [28, 32, 25, 29, 35],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'IT'],
    'Salary': [40000, 50000, 45000, 48000, 55000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Employee DataFrame:\n")
print(df)

# Display specific column
print("\nEmployee Names:\n", df['Employee_Name'])

# Display first 3 rows
print("\nFirst 3 rows:\n", df.head(3))

# Basic information about DataFrame
print("\nDataFrame Info:")
print(df.info())