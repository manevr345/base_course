from module_const import g
def counter(m, h, u):
    Eful = m*g*h + (m*u**2)/2
    return Eful
mass = float(input('Введите значени массы: '))
height = float(input('Введите значени высоты относительно поверхности земли: '))
speed = float(input('Введите значени скорости относительно поверхности земли: '))
print(counter(mass, height, speed))
