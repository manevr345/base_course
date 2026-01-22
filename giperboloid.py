import numpy as np
import imageio
import os
import matplotlib.pyplot as plt


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

N = 100
a = 1
b = 2
c = 6
edge = 30
alpha = np.linspace(-2, np.pi, N)
phi = np.linspace(0, np.pi*2, N)
x =  np.outer( a*np.cosh(alpha), np.cos(phi))
y =  np.outer( b*np.cosh(alpha), np.sin(phi))
z = np.outer(c*np.sinh(alpha), np.ones(np.size(phi)))

ax.plot_surface(x, y, z)

ax.set_xlim3d([-edge , edge])
ax.set_xlabel('X')
ax.set_ylim3d([-edge , edge])
ax.set_ylabel('Y')
ax.set_zlim3d([-edge , edge])
ax.set_zlabel('Z')
ax.plot_surface(x,y,z)

plt.savefig('giperboloid.png')

