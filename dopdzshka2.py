import matplotlib.pyplot as plt
import numpy as np
import random
def elipse_plot_p(fita=np.pi/4):
    p = np.arange(0.01, 10, 0.1)
    e = np.arange(0.01, 1, 0.01)
    r = p/(1 + e[random.randint(0, len(e))]*np.cos(fita))
    plt.plot(p, r)
    plt.savefig('grafic')
def elipse_plot_e(fita=np.pi/2):
    p = np.arange(0.01, 10, 0.1)
    e = np.arange(0.1, 1, 0.1)
    print(p)
    print(e)
    s = random.randint(0, len(p))
    r = [p[s]/(1 + i*np.cos(fita)) for i in e ]
    plt.plot(e, r)
    plt.savefig('grafic')
elipse_plot_e()
# elipse_plot_p()
