import numpy as np

# Create a two-dimensional array
one_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Filter the array with a condition
condition = one_d_array > 3
filtered_array = one_d_array[condition]
print("Filtered array:", filtered_array)

# Flatten the array for fancy indexing
flattened_array = one_d_array.flatten()

# Fancy indexing
indices = [0, 4]  # Indices are with respect to the flattened array
extracted_values = flattened_array[indices]
print("Extracted values:", extracted_values)
