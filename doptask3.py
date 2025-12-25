import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
t = np.arange(0, 4*np.pi, 0.01)
R =10
x = R * np.cos(t)**3
y = R * np.sin(t)**3
print(len(x), len(y))


fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')


def animate(alpha):
    x0 = 3
    y0 = 3
    X = x0 + (x+10)*np.cos(alpha) - (y+10)*np.sin(alpha)
    Y = y0 + x*np.sin(alpha) + y*np.cos(alpha)
    ball.set_data(X, Y)
    return ball

plt.axis('equal')
ax.set_xlim(-50, 50)
ax.set_ylim(-25, 25)

ani = FuncAnimation(fig, animate, frames=np.arange( 0, 2*np.pi,  0.1), interval=30)
ani.save('dopanimation.gif', writer="pillow")