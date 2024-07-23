import numpy as np

one_d_array = np.array([[1,2,3],[4,5,6],[7,8,9]])


# Stacking arrays vertically
stacked_vertically = np.vstack((one_d_array, one_d_array))
print("Vertically stacked:")
print(stacked_vertically)
# Stacking arrays horizontally
stacked_horizontally = np.hstack((one_d_array, one_d_array))
print("Horizontally stacked:")
print(stacked_horizontally)