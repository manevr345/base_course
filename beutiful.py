import matplotlib.pyplot as plt
g =10
u = 89
import numpy as np
x = np.arange(0, 1000)
y = [u*i - i**2*g/2 for i in x]
plt.plot(x, y, color = 'g', label ='Graf1', marker ='>', ms=5)
# plt.plot(y, x, color = 'r', label='Graf2', marker='o', ms=3)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Base')
plt.grid()
plt.savefig('fig.png')