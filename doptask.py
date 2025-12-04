import math as m
import numpy as np
n = int(input('Введите кол-во элементов ряда фибоначи: '))

def fib(nf=n):
    if n > 0:
        lista = [0,1]
        for i in range(2, n):
           lista.append(lista[i-2]+lista[i-1])
        print(lista)
        return lista[n-1]
    if n < 0:
        lista = [ 1, 0]
        for i in range(2, n*(-1)):
            lista.insert(0, lista[1]-lista[0])
        print(lista)
        return lista[0]
        

print(fib(n))
