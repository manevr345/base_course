import numpy as np
import imageio
import os
import matplotlib.pyplot as plt

fig , ax = plt.subplots(subplot_kw={"projection": "3d"})
edge = 20
phi = np.linspace(-1*np.pi , 3*np.pi, 100)#одинаковые параметры при линкспейс 
theta = np.linspace(-3*np.pi , 6*np.pi, 100)
l = 5
n = 8
f = np.sin(theta)
promx = np.outer(phi, np.cos(theta))
promy = np.outer(phi, np.sin(theta))
x = promx + l*f
y = promy + n*f
z = np.outer( n, f) # спроси Байга 
ax.set_xlim3d([-edge , edge])
ax.set_xlabel('X')
ax.set_ylim3d([-edge , edge])
ax.set_ylabel('Y')
ax.set_zlim3d([-edge , edge])
ax.set_zlabel('Z')
ax.plot_surface(x,y,z)

plt.savefig("konoid.png")