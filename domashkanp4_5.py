import numpy as np
import math
N = int(input())
M = int(input())
trigonometry_array = np.zeros((N, M))
print(trigonometry_array)
for i  in range(N):
    for j in range(M):
        trigonometry_array[i, j] = math.sin(N * i + M * j + 1)
print(trigonometry_array)
for el in range(N):
    a = trigonometry_array[el, 0]
    trigonometry_array[el, 0] = trigonometry_array[el,1]
    trigonometry_array[el,1]= a
print(trigonometry_array)
    
