num = int(input("Введите число: "))
lista = [1]
for i in range(1, num+1):
    if i == 1:
        lista.append(i)
    else:
        lista.append(lista[i-2]+lista[i-1])
print(lista)
