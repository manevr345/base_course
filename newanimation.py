import numpy as np
import imageio
import os
import matplotlib.pyplot as plt
fig, ax =  plt.subplots(subplot_kw={"projection": "3d"})
N =100
edge = 10
phi = np.linspace(0, 2*np.pi, 100)
theta = np.linspace(0, np.pi, 100)
def animate(R):
    x = R * np.outer(np.cos(phi), np.sin(theta))
    y = R * np.outer(np.sin(phi), np.sin(theta))
    z = R * np.outer(np.ones(np.size(phi)), np.cos(theta))
    return x, y, z
for i in range(N):
    ax.set_xlim3d([-10, 10])
    ax.set_ylim3d([-10, 10])
    ax.set_zlim3d([-10, 10])
    x, y, z = animate(edge/N*i)
    ax.plot_surface(x, y, z)
    plt.savefig(f'pic{i}.png')
images = []
filenames = [f'pic{i}.png' for i in range(N)]
for filename in filenames:
    images.append(imageio.imread(filename))
    os.remove(filename)
imageio.mimsave('movie.gif', images)
