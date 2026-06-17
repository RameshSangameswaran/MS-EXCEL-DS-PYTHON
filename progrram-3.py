import numpy as np

# Create a NumPy array (own dataset)
data = np.array([12, 7, 25, 3, 18, 10], dtype=float)

# Find minimum value
min_value = np.min(data)

# Find maximum value
max_value = np.max(data)

# Find sum of elements
total_sum = np.sum(data)

# Find cumulative sum
cumulative_sum = np.cumsum(data)

# Display results
print("Array:", data)
print("Minimum value:", min_value)
print("Maximum value:", max_value)
print("Sum of elements:", total_sum)
print("Cumulative sum:", cumulative_sum)