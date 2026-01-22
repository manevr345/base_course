import numpy as np
import matplotlib.pyplot as plt

fig , ax = plt.subplots(subplot_kw={"projection": "3d"})

t = np.arange(0.01 , 16 * np.pi , 0.01)#parametr
R = 1
x = 2**(-0.1*t) * np.cos(2*t)
y = 2**(-0.1*t) * np.sin(2*t)
z = -t

ax.plot(x,y,z, label = 'Dich')
ax.set_xlabel("X")
ax.set_ylabel("Y")



plt.savefig('pruzyna.png')