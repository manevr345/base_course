import matplotlib.pyplot as plt
import numpy as np
def zezl_plot(k=np.pi):
    fita = np.arange(0.01, 8*np.pi, 0.01)
    r = k/fita**(1/2)
    y = r*np.sin(fita)
    x = r*np.cos(fita)
    plt.plot(x, y, color='gray')
    plt.axis('equal')
    plt.show()
zezl_plot(1)