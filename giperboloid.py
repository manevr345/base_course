import numpy as np
import imageio
import os
import matplotlib.pyplot as plt


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

N = 100
a = 0.1
b = 0.2
c = 0.01
alpha = np.linspace(0, np.pi, N)
phi = np.linspace(0, np.pi*2, N)
x =  a* np.outer( np.cos(phi), np.sinh(alpha))
y = b* np.outer( np.sin(phi), np.sinh(alpha))
z = c*np.outer( np.sinh(alpha), np.ones(np.size(phi)))

ax.plot_surface(x, y, z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig('giperboloid.png')

