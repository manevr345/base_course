import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
type_of_linza = input('Type of linza (Рас/Соб): ')
type_of_linza = type_of_linza.upper().capitalize()
F = float(input('F: (фокусное расстояние, м)'))
d = float(input('d: (расстояние от предмета до линзы. м)'))
h = float(input('Введите высоту линейного объекта, м: '))
e = 0.2*h
l = 0.2*h
def standard_object_plotter(typ_of_linza, F):
    plt.plot([-4*F, 4*F], [ 0, 0], color='black', label='Главная оптическая линия', ms=5 )
    plt.plot([0, 0],[-h*3, h*3], color='black', label=f'{typ_of_linza} линза', ms=5)
    if typ_of_linza == 'Соб':
        plt.plot([0, e], [h*3, h*3-e], color='black', ms=5)
        plt.plot([0, -e], [h*3, h*3-e], color='black', ms=5)
        plt.plot([0, -e], [-h*3, -h*3+e], color='black', ms=5)
        plt.plot([0, e], [-h*3, -h*3+e], color='black', ms=5)
    if typ_of_linza == 'Рас':
        plt.plot([0, e], [h*3, h*3+e], color='black', ms=5)
        plt.plot([0, -e], [h*3, h*3+e], color='black', ms=5)
        plt.plot([0, -e], [-h*3, -h*3-e], color='black', ms=5)
        plt.plot([0, e], [-h*3, -h*3-e], color='black', ms=5)
    plt.plot([-F, -F], [l, -l], color='black', ms=5)
    plt.plot([F, F], [l, -l], color='black', ms=5)
    plt.plot([-2*F, -2*F],[l, -l] , color='black', ms=5)
    plt.plot([2*F, 2*F], [l, -l], color='black', ms=5)

    plt.axis('equal')
def definder(Focus, d_linzy):
    if type_of_linza == 'Соб'and Focus != d_linzy:
        f_linzy = (Focus*d_linzy)/(Focus-d_linzy)
        return float(f_linzy)
    if type_of_linza == 'Рас':
        f_linzy = (Focus*d_linzy)/(d_linzy + Focus)
        return float(f_linzy)


standard_object_plotter(type_of_linza, F)
f = definder(F, d)
def plotter(F, f, d, h):
    plt.plot([d, d], [0, h], color='blue', ms=5)
    plt.plot([d, d - 0.1*d], [h, h - 0.2*h], color='blue', ms=5)
    plt.plot([d, d + 0.1*d], [h, h - 0.2*h], color='blue', ms=5)
    if type_of_linza == 'Соб':
        if d != F:
            plt.plot([f, f ], [0, (h / d) * f], color='blue', ms=5)
            plt.plot([f, f - 0.1*f], [(h / d) * f, (h / d) * f + 0.05*h], color='blue', ms=5)
            plt.plot([f, f + 0.1*f], [(h / d) * f, (h / d) * f + 0.05*h], color='blue', ms=5)
    if type_of_linza == 'Рас' or d < F:
        plt.plot([f, f ], [0, -1 * (h / F) * f + h ], color='blue', ms=5)
        plt.plot([f, f - 0.1*f], [-1*(h / F) * f +h, -1*(h / F) * f+h - 0.05*h], color='blue', ms=5)
        plt.plot([f, f + 0.1*f], [-1*(h / F) * f + h, -1*(h / F) * f +h - 0.05*h], color='blue', ms=5)
plotter(F, f, d, h)
plt.legend()
anim_object1, = plt.plot([], [], '-', color='red', lw=2)
anim_object2, = plt.plot([], [], '-', color='red', lw=2)
if type_of_linza == 'Рас' or d<=F:
    anim_object1.set_linestyle('--')
    anim_object2.set_linestyle('--')

x = np.linspace(-4*F, 4*F, 100)[::-1]
x1, y1 = [], []
x2, y2= [], []
plt.title(f'Ход лучей в линзе при F = {F} и d = {d}')
def update1(frame):

    y1.insert(0, h/d * frame)
    x1.insert(0, frame)
    anim_object1.set_data(x1, y1 )

    if type_of_linza == 'Соб':
        if frame < 0:
            y2.insert(0, h / F * frame + h)
        if frame >= 0:
            y2.insert(0, h)

    else:
        if frame < 0:
            y2.insert(0, -h / F * frame + h)
        if frame >= 0:
            y2.insert(0, h)
    x2.insert(0, frame)
    anim_object2.set_data(x2, y2)


    return anim_object1,anim_object2

ani1 = FuncAnimation(fig, update1, frames=x[1:-1],interval=50)
ani1.save('linza.gif', writer='pillow')

