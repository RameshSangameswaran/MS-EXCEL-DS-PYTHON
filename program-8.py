import numpy as np

# Define your own coefficient matrix A
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])

# Define constants matrix B
B = np.array([8, -11, -3])

# Solve for X
X = np.linalg.solve(A, B)

print("Coefficient Matrix A:")
print(A)

print("\nConstant Matrix B:")
print(B)

print("\nSolution X:")
print(X)