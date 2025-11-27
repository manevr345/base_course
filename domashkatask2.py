import numpy as np
stol = int(input(("введи кол-во столбиков: ")))
lista = []
for i in range(stol):
    arg = int(input('Введите член массива: '))
    lista.append(arg)
mass = np.array(lista)
def counter(a = mass):
    newmass =np.ones(stol)
    for el in range(stol):
        newmass[0] *= mass[el]
    return newmass[0]
print(counter(mass))


