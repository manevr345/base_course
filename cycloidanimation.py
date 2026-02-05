import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# создаем анымацию и протсранство для нее
fig, ax = plt.subplots()

# Объект анимации 
anim_object, = plt.plot([], [], '-', lw =2)
x, y = [], []
t = np.linspace(0, 12*np.pi, 500)
ax.set_xlim(-4, 20)
ax.set_ylim(-4, 20)
R = 1
def update(frame):
    x.append(R*(frame -np.sin(frame)))
    y.append(R*(1 - np.cos(frame)))
    anim_object.set_data(x, y)
    return anim_object
# вызов пространства для анимации
ani1 = FuncAnimation(fig,
                    update, # вызов функции постановки
                    frames=t, # интервал значений
                    interval=10) # интервал между кадрами


ani1.save('domashkacycloid.gif', writer='pillow')
