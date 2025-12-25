from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
N = int(input('Введи кол-во точек: '))
massx , massy = [], []
def plotnik(x0=0.1, y0=0.1, C=0.3, D=0.33):
    for i in range(N):
        if i == 0:
            massx.append(x0)
            massy.append(y0)
        if i !=0:
            massx.append(massx[i-1]**2 - massy[i-1]**2 + C)
            massy.append(2*massx[i-1]*massy[i-1]+ D)
    return massx, massy

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')
ball_line, = plt.plot([], [], '-', color='r', label='Ball')

frames = 180
coords = np.zeros((frames, 2))
print(coords)

def animate(i):
    coords[i] = massx[i], massy[i]
    ball.set_data([coords[i][0]], [coords[i][1]])
    ball_line.set_data(coords[:i, 0], coords[:i, 1])
    return ball, ball_line
edge = 14
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=frames, interval=10)
ani.save('domashkatask4.gif', writer="pillow")