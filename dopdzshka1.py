import matplotlib.pyplot as plt
import numpy as np
def liss_plot(faza=np.pi/2, alfa=1, A=1, beta=0.5, B =5):
    t = np.arange(0, 15, 0.1)
    x= A * np.sin(alfa*t +faza)
    y = B * np.sin(beta*t)
    plt.plot(x, y, color='black')
    plt.show()
liss_plot()