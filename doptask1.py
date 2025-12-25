import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
t = np.arange(-10*np.pi, 10*np.pi, 0.01)
def cirle_plot(R=3):
    x = R*(t-np.sin(t))
    y = R*(1-np.cos(t))
    plt.plot(x, y, color='green', lw = 3)
    plt.axis('equal')
    plt.savefig('gogo.jpg')
def astro(R=3):
    x = R * np.cos(t)**3
    y = R * np.sin(t)**3
    plt.plot(x, y, color = 'blue', lw = 3)
    plt.axis('equal')
    plt.savefig('gogo.jpg')
    
astro()