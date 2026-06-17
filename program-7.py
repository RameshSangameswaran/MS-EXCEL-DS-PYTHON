import numpy as np

# ----------------------------
# Custom Dataset
# ----------------------------

# Vectors
vector_a = np.array([2, 4, 6])
vector_b = np.array([1, 3, 5])

# Matrices
matrix_A = np.array([[1, 2],
                     [3, 4]])

matrix_B = np.array([[5, 6],
                     [7, 8]])

# ----------------------------
# Vector Operations
# ----------------------------

# Dot Product
dot_product = np.dot(vector_a, vector_b)

# Inner Product (same as dot for 1D vectors)
inner_product = np.inner(vector_a, vector_b)

# Outer Product
outer_product = np.outer(vector_a, vector_b)

# ----------------------------
# Matrix Operations
# ----------------------------

# Matrix Multiplication (Product)
matrix_product = np.dot(matrix_A, matrix_B)

# Matrix Exponentiation (A^n)
power = 3   # You can change this value
matrix_power = np.linalg.matrix_power(matrix_A, power)

# ----------------------------
# Display Results
# ----------------------------

print("Vector A:", vector_a)
print("Vector B:", vector_b)

print("\nDot Product:", dot_product)
print("Inner Product:", inner_product)

print("\nOuter Product:\n", outer_product)

print("\nMatrix A:\n", matrix_A)
print("Matrix B:\n", matrix_B)

print("\nMatrix Product (A * B):\n", matrix_product)

