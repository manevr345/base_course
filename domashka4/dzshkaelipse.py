import matplotlib.pyplot as plt
import numpy as np
def kolomna_plt(a=10, b=5):
    x = np.arange(-10*a, 10*a, 0.1)
    y = np.arange(-10*a, 10*a, 0.1)
    X, Y = np.meshgrid(x,y)
    fxy = 1 - X**2/a**2 - Y**2/b**2
    plt.contour(X, Y, fxy, levels =[0], label = 'Elips')
    plt.axis('equal')
    plt.savefig('domashka4/elipse.png')
kolomna_plt()
