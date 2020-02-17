import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.linspace(0, 10, 100)

    # 绘制sin(x),sin(x+pi/2),sin(x+pi)
    y1 = np.sin(x[:, np.newaxis])
    y2 = np.sin(x[:, np.newaxis] + np.pi * 0.5)
    y3 = np.sin(x[:, np.newaxis] + np.pi)

    plt.plot(x, y1, label='first')
    plt.plot(x, y2, label='second')
    plt.plot(x, y3)

    plt.legend(loc='upper left')

    plt.show()
