import numpy as np
import imageio
import os
import matplotlib.pyplot as plt

fig , ax = plt.subplots(subplot_kw={"projection": "3d"})
edge = 20
phi = np.linspace(0 , 6*np.pi, 100)#одинаковые параметры при линкспейс 
theta = np.linspace(0 , 6*np.pi, 100)
h = 10

x = np.outer(phi, np.cos(theta))
y = np.outer(phi, np.sin(theta))
z = np.outer( h, theta) # спроси Байга 
ax.set_xlim3d([-3*edge , 3*edge])
ax.set_xlabel('X')
ax.set_ylim3d([-3*edge , 3*edge])
ax.set_ylabel('Y')
ax.set_zlim3d([-3*edge , 3*edge])
ax.set_zlabel('Z')
ax.plot_surface(x,y,z)

plt.savefig("gikoid.png")