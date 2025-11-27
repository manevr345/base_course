from math import pi
userdata = input("какаю фигуру хош выбрать?: Треугольник/Прямоугольник/Круг?" )

def triangle(h, a):
    S = 1/2*h*a
    print(S)
def kwadrat(a, b):
    S = a* b
    print(S)
def circus(R):
    S = pi* R**2
    print(S)
if userdata == 'Треугольник':
    h = int(input("Высота: "))
    a = int(input('Сторона, на которую опущена высота: '))
    triangle(h, a)
if userdata == 'Квадрат':
    a =int(input("Введите ширину: "))
    b = int(input("Введите высоту: "))
    kwadrat(a, b)
if userdata == "Круг":
    R = float(input("Введите радиус круга: "))
    circus(R)
    



