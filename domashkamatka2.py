import matplotlib.pyplot as plt
import numpy as np
def gipo(a, b, N):
    x = np.arange(a, b, N)
    y = [1/i for i in x]
    plt.plot(x, y, color = 'red', label = 'giperbola')
    plt.title('my giperbola')
    plt.legend()
    plt.savefig('domashkatwo')
if __name__ == '__main__':
   gipo(-10, 10, 1)
