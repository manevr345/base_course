import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
 
anim_object, = plt.plot([], [], '-', lw =2)
plt.axis('equal')
x, y = [], []
t = np.linspace(0, 2*np.pi)
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
def update(frame):
    x.append(16*np.sin(frame)**3)
    y.append(13*np.cos(frame) - 5*np.cos(2*frame) - 2*np.cos(3*frame) - np.cos(4*frame))
    anim_object.set_data(x, y)
    return anim_object

ani = FuncAnimation(fig,
                    update, 
                    frames=t, 
                    interval=100) 
ani.save('domashkaanimatserce.gif', writer='pillow')