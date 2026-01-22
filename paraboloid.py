import numpy as np
import matplotlib.pyplot as plt

fig , ax = plt.subplots(subplot_kw={"projection": "3d"})
edge = 20
phi = np.linspace(0 , 2*np.pi, 100)#одинаковые параметры при линкспейс 
theta = np.linspace(0 , np.pi, 100)


x = np.outer(phi, np.cos(theta))
y = np.outer(phi, np.sin(theta))
z = np.outer( phi**2,np.ones(np.size(theta))) # спроси Байга 
ax.set_xlim3d([-edge , edge])
ax.set_xlabel('X')
ax.set_ylim3d([-edge , edge])
ax.set_ylabel('Y')
ax.set_zlim3d([-edge , edge])
ax.set_zlabel('Z')
ax.plot_surface(x,y,z)

plt.savefig("paraboloid.png")