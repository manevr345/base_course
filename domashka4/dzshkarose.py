import matplotlib.pyplot as plt
import numpy as np
import time
def rose_plot(k=np.pi):
    fita = np.arange(0.01, 8*np.pi, 0.01)
    r = np.sin(k*fita)
    y = r*np.sin(fita)
    x = r*np.cos(fita)
    plt.plot(x, y, color='gray')
    plt.axis('equal')
    plt.savefig('domashka4/rose.png')
for i in range(10):
    rose_plot(i)

