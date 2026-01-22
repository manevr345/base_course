import numpy as np
import matplotlib.pyplot as plt

fig , ax = plt.subplots(subplot_kw={"projection": "3d"})

t = np.arange(0.01 , 16 * np.pi , 0.01)#parametr
edge = 1
R = 2
x = R*np.cos(t)**3
y = R*np.sin(t)**3
z = np.cos(2*t)
ax.set_xlim3d([-edge , edge])
ax.set_xlabel('X')
ax.set_ylim3d([-edge , edge])
ax.set_ylabel('Y')
ax.set_zlim3d([-edge , edge])
ax.set_zlabel('Z')
ax.plot(x,y,z)
ax.plot(x,y,z, label = 'Dich')




plt.savefig('coolline.png')