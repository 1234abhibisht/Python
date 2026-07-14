# Perform Matrix multiplication of any 2 n*n matrices.

# for this we will use matmul() function

import numpy as np
matrix1 = np.array([[1,2,3], [1,2,3], [1,2,3]])
matrix2 = np.array([[3,2,1], [3,2,1], [3,2,1]])
resultMatrix = np.matmul(matrix1, matrix2)
print(resultMatrix)
