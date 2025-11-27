import numpy as np
a = int(input("Введите минимальное значение области определения: "))
b = int(input("Введите минимальное значение области определения: "))
N = np.arange(a+1, b)
def y(*args):
    funk = N**2 
    return funk
print(y(N))

