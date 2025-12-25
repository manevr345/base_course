import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
t = 0.12*np.pi
# создаем анымацию и протсранство для нее
fig, ax = plt.subplots()

# Объект анимации 
anim_object, = plt.plot([], [], '-', lw =2)
x, y = [], []
t = np.linspace(0, 12*np.pi)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
def update(frame):
    x.append(np.sin(frame)*(np.e**np.cos(frame) - 2*np.cos(4*frame) + np.sin(t/12)**5))
    y.append(np.cos(frame)*(np.e**np.cos(frame) - 2*np.cos(4*frame) + np.sin(t/12)**5))
    anim_object.set_data(x, y)
    return anim_object
# вызов пространства для анимации
ani = FuncAnimation(fig,
                    update, # вызов функции постановки
                    frames=t, # интервал значений
                    interval=100) # интервал между кадрами
ani.save('domashkaanimatbabka.gif', writer='pillow')
