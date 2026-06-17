import numpy as np

# Create a NumPy array (own dataset)
data = np.array([[5, 10, 15],
                 [20, 25, 30]])

# Display the array
print("Array:")
print(data)

# Number of dimensions
print("\nNumber of dimensions (ndim):", data.ndim)

# Shape of the array (rows, columns)
print("Shape of the array:", data.shape)

# Total number of elements
print("Size of the array:", data.size)

# Data type of elements
print("Data type (dtype):", data.dtype)