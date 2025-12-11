import matplotlib.pyplot as plt
import numpy as np
import math
def rose(r, fita):
    x = np.arange()
    y = np.arange(0, r*math.sin(fita))
    X, Y = np.meshgrid(x, y)
    # Сопоставлние всех игриков к иксам
    fxy = math.sqrt(X**2 + Y**2) - 5*math.sin(5*math.arctan(Y/X))
    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal')
    plt.savefig('domashka5.png')
if __name__ == '__main__':
    rose(5, 0.5)