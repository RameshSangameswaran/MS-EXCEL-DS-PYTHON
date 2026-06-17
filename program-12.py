# Import pandas library
import pandas as pd

# Create your own dataset
data = {
    'Name': ['Anil', 'Bhavna', 'Chetan', 'Deepa', 'Eshan', 'Farah', 'Gaurav'],
    'Maths': [78, 85, 67, 90, 88, 76, 95],
    'Science': [82, 79, 75, 92, 85, 80, 89],
    'English': [74, 88, 70, 91, 87, 78, 93]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display complete DataFrame
print("Full DataFrame:\n")
print(df)

# Using head() method
print("\nFirst 5 rows using head():\n")
print(df.head())

# Using tail() method
print("\nLast 5 rows using tail():\n")
print(df.tail())

# Using describe() method
print("\nStatistical Summary using describe():\n")
print(df.describe())