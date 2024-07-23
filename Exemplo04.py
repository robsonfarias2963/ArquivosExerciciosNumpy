import numpy as np

# Create a one-dimensional array
one_d_array = np.array([1, 2, 3, 4, 5])

# Reshape the array to a 5x1 two-dimensional array
reshaped_array = one_d_array.reshape(5, 1)

# Print the reshaped array
print("Reshaped Array:")
print(reshaped_array)
