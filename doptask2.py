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

ax.set_xlim(-10, 10)
ax.set_ylim(-5, 5)

def update(frame):
    R0 = frame*5
    x0 = R0*np.cos(frames_interval)
    y0 = R0*np.sin(frames_interval)
    anim_object.set_data(x0, y0)
    plt.axis('equal')
    return anim_object

ani = FuncAnimation(fig,
                    update, 
                    frames=frames_interval, 
                    interval=100) 

ani.save('animation_1.gif', writer = 'pillow')


