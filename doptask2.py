from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Объект анимации 
anim_object, = plt.plot([], [], '-', lw =2)
plt.axis('equal')
x, y = [], []
R0 = 3
frames_interval = np.linspace(0, 2*np.pi, 100)
x0 = R0*np.cos(frames_interval)
y0 = R0*np.sin(frames_interval)
ax.set_xlim(-10, 10)
ax.set_ylim(-5, 5)
def update(frame):
    R = frame*5
    x.append(np.sin(x0 + R))
    y.append(np.cos(y0 + R))
    anim_object.set_data(x, y)
    plt.axis('equal')
    return anim_object
# вызов пространства для анимации
ani = FuncAnimation(fig,
                    update, # вызов функции постановки
                    frames=frames_interval, # интервал значений
                    interval=100) # интервал между кадрами
ani.save('animation_1.gif', writer = 'pillow')


