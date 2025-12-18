import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
# создаем анымацию и протсранство для нее
fig, ax = plt.subplots()

# Объект анимации 
anim_object, = plt.plot([], [], '-', lw =2)
x, y = [], []
frames_interval = np.linspace(0, 2*np.pi, 100)
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)
def update(frame):
    x.append(frame)
    y.append(np.sin(frame))
    anim_object.set_data(x, y)
    return anim_object
# вызов пространства для анимации
ani = FuncAnimation(fig,
                    update, # вызов функции постановки
                    frames=frames_interval, # интервал значений
                    interval=50) # интервал между кадрами
ani.save('animation_1.gif', writer='pillow')