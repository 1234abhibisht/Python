# Create numpy array of (3,3) dimension. Now find sum of all rows & columns individually. 
# Also find 2nd maximum element in the array. 

import numpy as np
arr_3d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr_3d)

# sum of all rows individually
sum_rows = np.sum(arr_3d, axis = 1)
print(sum_rows)
# or
sum_rows = arr_3d.sum(axis = 1)
print(sum_rows)


# sum of all columns individually
sum_columns = np.sum(arr_3d, axis = 0)
print(sum_columns)


# finding 2nd maximum element
second_max = np.sort(np.unique(arr_3d))[-2]
print(second_max)

# -> np.unique() returns all elements in array individually in unique(means gives duplicate elements one time only)
# -> .sort() will sort all elements in ascending order
#      -> and we want second largest element, so we will do negative indexing
