import numpy as np
import matplotlib.pyplot as plt

x = np.array([[0.1, 1], [1, 0.2], [2, 1.0], [3, 0.2], [4, -3], [5, -2],[6, -6], [7, 1]])
plt.scatter(x[:, 0], x[:, 1], marker='x', s=15)
y = x.T[1]
x = x.T[0]
step_size = 0.05

c = 1
a = (y[1] - y[0] * x[1] / x[0] + c * (x[1] / x[0] - 1)) / (x[1] ** 2 - x[0])
b = y[0] / x[0] - a * x[0] - c / x[0]

plot_x = np.arange(x[0], x[1] + step_size, step_size)
plt.plot(plot_x, a * (plot_x ** 2) + b * plot_x + c)

for i in range(1, len(x) - 1):
    a2 = (y[i] - y[i + 1] - (2 * a * x[i] + b) * (x[i] - x[i + 1])) / (
                x[i] ** 2 - x[i + 1] ** 2 - 2 * x[i] * (x[i] - x[i + 1]))
    b2 = 2 * a * x[i] - 2 * a2 * x[i] + b
    c2 = y[i] - a2 * (x[i] ** 2) - b2 * x[i]
    plot_x2 = np.arange(x[i], x[i + 1] + step_size, step_size)
    plt.plot(plot_x2, a2 * plot_x2 ** 2 + b2 * plot_x2 + c2)
    a = a2
    b = b2
    c = c2

plt.show()
