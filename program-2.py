import numpy as np

# Create your own dataset (2D array)
data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print("Original Dataset:\n", data)

# -------------------------------
# 1. Slicing
# -------------------------------
print("\n1. Slicing:")

# Extract rows 1 to 2 and columns 1 to 3
slice_data = data[1:3, 1:4]
print("Sliced data (rows 1-2, cols 1-3):\n", slice_data)

# First two rows
print("First two rows:\n", data[:2, :])

# Last column
print("Last column:\n", data[:, -1])

# -------------------------------
# 2. Integer Array Indexing
# -------------------------------
print("\n2. Integer Array Indexing:")

# Select specific elements
rows = np.array([0, 2, 3])
cols = np.array([1, 2, 0])

selected_elements = data[rows, cols]
print("Selected elements using integer indexing:", selected_elements)

# Select full rows using integer indexing
selected_rows = data[[0, 2]]
print("Selected rows (0 and 2):\n", selected_rows)

# -------------------------------
# 3. Boolean Array Indexing
# -------------------------------
print("\n3. Boolean Array Indexing:")

# Condition: Select elements greater than 80
bool_index = data > 80
print("Boolean condition (data > 80):\n", bool_index)

filtered_data = data[bool_index]
print("Filtered elements (greater than 80):\n", filtered_data)

# Replace elements less than 50 with 0
modified_data = data.copy()
modified_data[modified_data < 50] = 0
print("Modified data (values < 50 set to 0):\n", modified_data)