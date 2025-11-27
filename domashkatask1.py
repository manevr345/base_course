import numpy as np
stol = int(input())
b = np.zeros((stol))
print(b)
for i in range(stol):
    b[i] = int(input())
print(b)
def medium(mass = b):
    result = sum(b)/len(b)
    return result
print(medium(b))
