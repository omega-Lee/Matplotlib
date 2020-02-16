import matplotlib.pyplot as plt
import numpy as np


def scatter():
    data = np.linspace(0, 10, 30)
    # scatter(x, y, 点的大小, 颜色，标记)
    plt.scatter(data, np.sin(data), s=90, c='r', marker='x')
    plt.show()


if __name__ == "__main__":
    scatter()
