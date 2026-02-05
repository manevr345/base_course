import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
type_of_linza = input('Type of linza (Рассеивающая/Собирающая): ')
type_of_linza = type_of_linza.upper().capitalize()
F = int(input('F: (Если оно неизвестно, напиши знак ?)'))
d = int(input('d: (Если оно неизвестно, напиши знак ?)'))
h = int(input('Введите высоту линейного объекта: '))

def standard_object_plotter(typ_of_linza, F):
    plt.plot([-4*F, 4*F], [ 0, 0], color='black', label='Главная оптическая линия', ms=5 )
    plt.plot([0, 0],[-h*3, h*3], color='black', label=f'{typ_of_linza} линза', ms=5)
    if typ_of_linza == 'Собирающая':
        plt.plot([0, 2], [h*3, 25], color='black', ms=5)
        plt.plot([0, -2], [h*3, 25], color='black', ms=5)
        plt.plot([0, -2], [-h*3, -25], color='black', ms=5)
        plt.plot([0, 2], [-h*3, -25], color='black', ms=5)
    if typ_of_linza == 'Рассеивающая':
        plt.plot([0, 2], [h*3, 35], color='black', ms=5)
        plt.plot([0, -2], [h*3, 35], color='black', ms=5)
        plt.plot([0, -2], [-h*3, -35], color='black', ms=5)
        plt.plot([0, 2], [-h*3, -35], color='black', ms=5)
    plt.plot([-F, -F], [2, -2], color='black', ms=5)
    plt.plot([F, F], [2, -2], color='black', ms=5)
    plt.plot([-2*F, -2*F], [2, -2], color='black', ms=5)
    plt.plot([2*F, 2*F], [2, -2], color='black', ms=5)

    plt.axis('equal')
def definder(Focus, d_linzy):
    if type_of_linza == 'Собирающая'and Focus != d_linzy:
        f_linzy = (int(Focus)*int(d_linzy))/(int(Focus)-int(d_linzy))
    if type_of_linza == 'Рассеивающая' and Focus != d_linzy:
        f_linzy = (int(Focus)*int(d_linzy))/(int(d_linzy) + int(Focus))
    if Focus != d_linzy:
        return float(f_linzy)

standard_object_plotter(type_of_linza, int(F))
f = definder(F, d)
if type_of_linza == 'Рассеивающая' or d<=F:
    anim_object1, = plt.plot([], [], '-', linestyle='--', color='red', lw=2)
    anim_object2, = plt.plot([], [], '-',  linestyle='--', lw=2)
if type_of_linza == 'Собирающая' and d>=F:
    anim_object1, = plt.plot([], [], '-', color='red', lw=2)
    anim_object2, = plt.plot([], [], '-',  lw=2)
x = np.linspace(-4*F, 4*F, 100)[::-1]
x1, y1 = [], []
x2, y2= [], []
def update2(frame):
    if type_of_linza == 'Собирающая':
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

    return anim_object2
def update1(frame):
    y1.insert(0, h/d * frame)
    x1.insert(0, frame)
    anim_object1.set_data(x1, y1 )
    return anim_object1

def plotter(F, f, d, h):
    plt.plot([d, d], [0, h], color='blue', ms=5)
    plt.plot([d, d - 1], [h, h - 2], color='blue', ms=5)
    plt.plot([d, d + 1], [h, h - 2], color='blue', ms=5)
    if type_of_linza == 'Собирающая':
        if d != F:
            plt.plot([f, f], [0, (h / d) * f], color='blue', ms=5)
            plt.plot([f, f - 1], [(h / d) * f, (h / d) * f + 2], color='blue', ms=5)
            plt.plot([f, f + 1], [(h / d) * f, (h / d) * f + 2], color='blue', ms=5)
    if type_of_linza == 'Рассеивающая':
        if d != F:
            plt.plot([f, f], [0, -1*(h / F) * f + h], color='blue', ms=5)
            plt.plot([f, f - 1], [-1*(h / F) * f +h, -1*(h / F) * f+h - 2], color='blue', ms=5)
            plt.plot([f, f + 1], [-1*(h / F) * f + h, -1*(h / F) * f +h - 2], color='blue', ms=5)
ani1 = FuncAnimation(fig, update1, frames=x[1:-1],interval=50)
ani2 = FuncAnimation(fig, update2, frames=x[1:-1],interval=50)
plotter(F, f, d, h)
plt.legend()
ani1.save('animation_1.gif', writer="pillow")
ani2.save('animation_1.gif', writer="pillow")