import numpy as np
ar1 = np.zeros((2, 3))
ar2 =np.zeros((2, 3))
for i in range(2):
    for j in range(3):
        ar1[i, j] = int(input('Введите число: '))
        ar2[i, j] = int(input('Введите число: '))
print(ar1)
print(ar2)
ar3 = np.zeros((2,3))
for i in range(2):
    for j in range(3):
        if  ar1[i, j] >= ar2[i, j]:
            ar3[i,j] = ar1[i, j ]
        else:
            ar3[i, j ] = ar2[i, j]
print(ar3)

