import numpy as np
import matplotlib.pyplot as plt


def orthogonal_point(p1, p2):
    tmp = (p2 - p1) / 2
    return p1 + tmp + np.array([-tmp[1], tmp[0]])


def approx(arg_x, arg_dx, step=0.05):
    #plt.scatter(arg_x[:, 0], arg_x[:, 1], marker='x', s=50)
    for i in range(len(arg_x) - 1):
        x3 = orthogonal_point(arg_x[i], arg_x[i + 1])
        b = (arg_x[i + 1] - arg_x[i]) / 2
        a = (b - arg_dx) / 2
        c = arg_x[i] + b - a
        # c = x3
        # a = (argx_[i] + argx_[i + 1] - 2 * x3) / 2

        alpha = np.arange(-1, 1 + step, step).reshape((-1, 1))
        points = a * alpha ** 2 + b * alpha + c
        plt.scatter(points[:, 0], points[:, 1], marker='x', s=3, c='g')
        arg_dx = (2 * a + b)
        arg_dx = arg_dx / np.linalg.norm(arg_dx) * np.linalg.norm(arg_x[i + 1] - arg_x[i]) / 4


def approx2(arg_x, arg_dx, arg_dx2, step=0.05):
    plt.scatter(arg_x[:, 0], arg_x[:, 1], marker='x', s=50)
    for i in range(len(arg_x) - 1):
        a = (arg_x[i + 1] - arg_x[i] - 2 * arg_dx - 2 * arg_dx2) / 8
        b = (6 * a + arg_dx2) / 2
        c = arg_dx + arg_dx2 + 3 * a
        d = (arg_x[i] + arg_x[i + 1] - 2 * b) / 2

        alpha = np.arange(-1, 1 + step, step).reshape((-1, 1))
        points = a * alpha ** 3 + b * alpha ** 2 + c * alpha + d
        plt.scatter(points[:, 0], points[:, 1], marker='x', s=1, c='r')
        arg_dx = 3 * a + 2*b + c
        arg_dx = arg_dx / np.linalg.norm(arg_dx) * np.linalg.norm(arg_x[i + 1] - arg_x[i]) / 4
        arg_dx2 = 6 * a + 2 * b
        arg_dx2 = arg_dx2 / np.linalg.norm(arg_dx2) * np.linalg.norm(arg_x[i + 1] - arg_x[i]) / 8


step_size = 0.4
x = np.linspace(2, 5, 5).reshape((-1, 1))
x = np.hstack((x, x + 1))
dx = np.array([1, 1])
# approx(x, dx)

x = np.array([[3, 3], [3.25, 2.25], [4, 2], [4.6, 2.25], [5, 3], [4, 4], [3.8, 3.15]])
dx = np.array([0.2, -1]) / 3
# approx(x, dx)

x = np.arange(0, 2 * np.pi, step_size).reshape((-1, 1))
a_ = np.sin(x) + 2.5
b_ = np.cos(x) + 5.5
x = np.hstack((a_, b_))
dx = np.array([1, -0.1]) / 30
dx2 = np.array([1, -0.05]) / 30
approx2(x, dx, dx2)
#approx(x, dx)

x1 = x[0]
x2 = x[1]
x = np.vstack((x1, x2, orthogonal_point(x1, x2)))
# plt.scatter(x[:, 0], x[:, 1], marker='x', s=50)

#plt.xlim(2, 4)
#plt.ylim(5, 7)
plt.show()
