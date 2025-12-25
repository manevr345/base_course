from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

x_0 = 0.1
y_0 = 0.1
C=0.3
D= 0.33
x, y = [x_0], [y_0]
for n in range(1, 100):
    x.append(x[n-1]**2 - y[n-1]**2 + C)
    y.append(2 * x[n-1] * y[n-1] + D)

plt.plot(x, y)
plt.savefig('animation_1.png')
fig, ax = plt.subplots()

# Объект анимации
anim_object, = plt.plot([], [], '-', lw=2)

x, y = [], [] # Координаты объекта анимации
frames_interval = np.linspace(0, 2*np.pi, 100)

ax.set_xlim(0, 2*np.pi) # Пределы изменения переменной Х
ax.set_ylim(-1, 1) # Пределы изменения переменной У

# Функция подстановки параметра в объект анимации
def update(frame):
 # Расчет координаты У
    # Передача координат объекту анимации
    anim_object.set_data(x[:frame:], y[:frame:])

    return anim_object


ani = FuncAnimation(fig, # Вызов пространства для анимации
                    update, # Вызов функции подстановки координат
                    frames=frames_interval, # Интервал значений
                    interval=50) # Интервал между кадрами,
                                 # по умолчанию 200 милисекунд

ani.save('animation_1.gif', writer="pillow")