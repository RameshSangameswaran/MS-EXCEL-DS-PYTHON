import numpy as np

# Create a square matrix (own dataset)
matrix = np.array([[4, 2, 1],
                   [0, 5, 3],
                   [2, 1, 6]])

# Calculate rank
rank = np.linalg.matrix_rank(matrix)

# Calculate determinant
determinant = np.linalg.det(matrix)

# Calculate trace (sum of diagonal elements)
trace = np.trace(matrix)

# Display results
print("Matrix:")
print(matrix)

print("\nRank of the matrix:", rank)
print("Determinant of the matrix:", determinant)
print("Trace of the matrix:", trace)