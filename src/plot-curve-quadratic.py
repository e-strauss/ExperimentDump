import numpy as np
import matplotlib.pyplot as plt


def scatter_matrix(arg):
    plt.scatter(arg[:, 0], arg[:, 1], marker='x', s=50)


def quadratic_curve(arg, arg2):
    step_size = 0.05
    for i in range(len(arg) - 1):
        a = arg[i + 1] - arg[i] - arg2
        alpha = np.arange(0, 1 + 0.05, step_size).reshape((-1, 1))
        points = a * alpha ** 2 + arg2 * alpha + arg[i]
        plt.scatter(points[:, 0], points[:, 1], marker='x', s=3, c='g')
        arg2 = (2 * a + arg2)/5


x = np.array([[3, 3], [3.65, 2.05], [4, 2], [5, 3], [4, 4]])
dx = np.array([0.5, -0.5])

scatter_matrix(x)
quadratic_curve(x, dx)

x2 = np.linspace(2, 5, 5).reshape((-1, 1))
x2 = np.hstack((x2, x2))
scatter_matrix(x2)
dx2 = np.array([0.1, 0.0])
quadratic_curve(x2, dx2)

plt.show()
