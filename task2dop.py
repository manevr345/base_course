AB =int(input('AB: '))
BC = int(input('Bc: '))
AC = int(input('AC: '))
lista = [AB, BC, AC]
for i in range(0, len(lista)):
    isexist = 'Треугольник существует'
    if lista[i-2]+lista[i-1] <= lista[i]:
        isexist = 'Треугольник не существует'
        break
    print(i)
print(isexist)
if isexist == 'Треугольник существует':
    if AB == BC == AC:
        print('Треугольник равносторонний')
    elif AB != BC != AC:
        print('Треугольник разносторонний')
    else:
        print("Треугольник равнобедренный")


