import numpy as np
import imageio
import os
import matplotlib.pyplot as plt
fig , ax = plt.subplots(subplot_kw={"projection": "3d"})
edge = 1
t = np.arange(0.01, 16*np.pi, 0.01)
x = np.sin(2*t)
y = 1 - np.cos(2*t)
z = np.cos(2*t)

ax.set_xlim3d([-3*edge , 3*edge])
ax.set_xlabel('X')
ax.set_ylim3d([-3*edge , 3*edge])
ax.set_ylabel('Y')
ax.set_zlim3d([-3*edge , 3*edge])
ax.set_zlabel('Z')
ax.plot(x, y, z)

plt.savefig("nonunderstandline.png")