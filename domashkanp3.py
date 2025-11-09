from module_const import g
import numpy as np
x0 = int(input('Введите начальное координату по оси ОХ: '))
y0 =int(input('введите начальное координату по оси ОУ: '))
ux =int(input('введите значение проекции скорости на ось ОХ: '))
uy = int(input('введите значение проекции скорости на ось ОY: '))
mass = np.zeros((5, 3))
print(mass)
for i in range(0, 5):
    mass[i, 0] = i+1
    mass[i, 1] = x0 + ux*(i+1)
    mass[i, 2] = y0 + uy*(i+1) - ((g* (i+1)**2)/2)
print(mass)


    
         