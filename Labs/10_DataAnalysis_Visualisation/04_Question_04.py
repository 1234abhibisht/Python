#     4.  Write a Pandas program to get the powers of an array values element-wise. 
# Note: First array elements raised to powers from second array
# Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
# Expected Output:
# X Y Z
# 0 78 84 86
# 1 85 94 97
# 2 96 89 96
# 3 80 83 72
# 4 86 86 83

import numpy as np
arr_values = np.array([1,2,3,4,5])
arr_powers = np.array([5,4,3,2,1])
result = np.power(arr_values, arr_powers)
print(result)