import numpy as np
import matplotlib.pyplot as plt

x = x = np.array([[3, 3], [3.65, 2.05], [4, 2], [5, 3], [4, 4]]) #
plt.scatter(x[:, 0], x[:, 1], marker='x', s=15)
y = x.T[1]
x = x.T[0]
dx = -1
step_size = 0.05

plot_x = np.arange(x[0], x[1] + step_size, step_size)

for i in range(0, len(x) - 1):
    x1 = x[i]
    x2 = x[i + 1]
    y1 = y[i]
    y2 = y[i + 1]
    a = (y2 - y1 - dx*(x2 - x1)) / (x2 ** 2 - x1 ** 2 - 2 * x1 * (x2 - x1))
    b = dx - 2*a*x1
    c = y2 - a*(x2**2) - b*x2
    dx = 2*a*x2 + b
    if x2 < x1:
        tmp = x2.copy()
        x2 = x1
        x1 = tmp
    plot_x2 = np.arange(x1, x2 + step_size, step_size)
    plt.plot(plot_x2, a * plot_x2 ** 2 + b * plot_x2 + c)


plt.show()
