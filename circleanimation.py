from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

R =1
time = np.linspace(0, 50, 100)
alpha = np.arange(0, 3*np.pi, 0.1)
y = R*np.sin(alpha)
def circle_move(R, vx0, time):
    x0 = vx0 * time
    alpha = np.arange(0, 3*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)
    
    return x
fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')
anim_object, = plt.plot([], [], '-', lw=2)
frames = 180


def animate(i):
    ball.set_data(circle_move(R=R, vx0=0.01, time=i), y)
    x.append(R*(i -np.sin(i)))
    y.append(R*(1 - np.cos(i)))
    anim_object.set_data(x, y)
    return anim_object
    return ball


edge = 10
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=time, interval=10)
ani.save('dopanimation.gif', writer="pillow")