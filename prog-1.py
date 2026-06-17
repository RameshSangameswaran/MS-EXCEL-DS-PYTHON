import numpy as np

# Creating a NumPy array from a list
my_list = [10, 20, 30, 40, 50]
array_from_list = np.array(my_list, dtype=float)

print("Array from list:")
print(array_from_list)
print("Data type:", array_from_list.dtype)

# Creating a NumPy array from a tuple
my_tuple = (1.5, 2.7, 3.9, 4.2)
array_from_tuple = np.array(my_tuple, dtype=float)

print("\nArray from tuple:")
print(array_from_tuple)
print("Data type:", array_from_tuple.dtype)