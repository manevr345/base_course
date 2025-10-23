AB =int(input('AB: '))
BC = int(input('Bc: '))
AC = int(input('AC: '))
lista = [AB, BC, AC]
for i in range(len(lista)):
    a = "Треугольник не существует"
    if lista[i-2]+lista[i-1] >= lista[i] and a == "Треугольник не существует":
        a = 'Треугольник существует'
    else:
        continue
print(a)