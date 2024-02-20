import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([0, -5, 6, 40, 8])


def approx(argx, argy, input):
    tmp = 0
    m_glob = 0
    for i in range(len(argx) - 1):
        m = argy[i + 1] - m_glob*(argx[i + 1] - argx[i]) -  argy[i]
        if m < 0:
            print("m < 0")
        m_glob += m
        tmp += m * np.maximum((input - argx[i]) / (argx[i + 1] - argx[i]), 0)
    return tmp


plt.scatter(x, y)
inX = np.linspace(0, 10, 100)
out = approx(x, y, inX)
plt.plot(inX, out)
plt.show()
