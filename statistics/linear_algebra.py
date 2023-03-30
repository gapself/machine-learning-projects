import numpy as np

# Given vectors
vector_1 = np.array([-2,-6,2,3])
vector_2 = np.array([4,1,-3,8])
vector_3 = np.array([5,-7,9,0])


matrix = np.column_stack((vector_1, vector_2, vector_3))
print(matrix)
print(matrix.shape)
print('Ostatni wiersz:')
print(matrix[-1,:])
print('Ostatnia kolumna:')
print(matrix[:,-1])
print(matrix[:,2])

import numpy as np

# Given
# 2 x 3 matrix
A = np.array([[2,3,-4], [-2, 1, -3]])
# 2 x 3 matrix
B = np.array([[1,-1,4], [3,-3,3]])
# 3 x 2 matrix
C = np.array([[1, 2], [3, 4], [5, 6]])

#vectors
v = np.array([-1,-2,-3])
u = np.array([2,2,2])
UV = np.dot(v,u)
print(UV)

# Calculate D = 4A - 2B
D = 4*A - 2*B
print(f'Macierz D:\n {D} \n z rozmiarem {D.shape}')
# Calculate E = AC
E = np.matmul(A,C)
print(f'Macierz E:\n {E} \n z rozmiarem {E.shape}')
# Calculate F = CA
F = C@A
print(f'Macierz F:\n {F} \n z rozmiarem {F.shape}')

