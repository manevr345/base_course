import matplotlib.pyplot as plt
import numpy as np
N = int(input())
def plotter(a=3, b=12, kon =N):
    x = np.arange(-5, 5, 0.1)
    if kon < a:
        y = [a**2 for i in range(len(x))]
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    if a <= kon <= b:
        y = x**2
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    if kon > b:
        y = [b**2 for i in range(len(x))]
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
plotter()



