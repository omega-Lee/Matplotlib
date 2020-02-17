import matplotlib.pyplot as plt
import numpy as np
from matplotlib.legend import Legend

if __name__ == '__main__':

    fig, ax = plt.subplots()

    lines = []

    # 线条风格数列
    styles = ['-', '--', '-.', ':']

    x = np.linspace(0, 10, 1000)

    # 移动相位
    for i in range(4):
        lines += ax.plot(x, np.sin(x - i * np.pi / 2), styles[i], color='black')

    # ax.axes('equal')用来使X和Y上的轴间距相等
    ax.axis('equal')

    ax.legend(lines[:2], ['line A', 'line B'],
              loc='upper right', frameon=False)

    # 创建第二组标签

    leg = Legend(ax, lines[2:], ['line C', 'line D'],
                 loc='lower right', frameon=False)
    ax.add_artist(leg)

    plt.show()
