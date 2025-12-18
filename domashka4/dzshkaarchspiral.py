import matplotlib.pyplot as plt
import numpy as np
def arch_spiral(k=np.pi):
    fita = np.arange(0, 8*np.pi, 0.01)
    r = k*fita
    x = r*np.cos(fita)
    y = r*np.sin(fita)
    plt.axis("equal")
    plt.plot(x,y)
    plt.savefig('domashka4/achspiral.png')
arch_spiral()
