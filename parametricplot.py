import matplotlib.pyplot as plt
import numpy as np
def circus_plotter(R=10):
    alfa = np.arange(-2*np.pi, 2*3.14, 0.1)
    x = R*np.cos(alfa)
    y = R*np.sin(alfa)

    plt.plot(x, y, ls = '--', color='green', lw =3)
    plt.axis('equal')
    plt.savefig('fig1.png')
if __name__ == '__main__':
    circus_plotter(5)