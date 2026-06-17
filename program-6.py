import numpy as np

# Define your own matrix
matrix = np.array([
    [4, 2],
    [1, 3]
])

# Calculate eigenvalues
eigenvalues = np.linalg.eigvals(matrix)

print("Matrix:")
print(matrix)

print("\nEigenvalues:")
print(eigenvalues)