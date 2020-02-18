import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    # 用[] 的方式取出每个子图，并添加子图座标文字

    fig, axes = plt.subplots(2, 3, sharex='col', sharey='row')

    # 取法
    # ax1 = axes[0, 0]
    # ax2 = axes[0, 1]
    # ax3 = axes[0, 2]
    # ax4 = axes[1, 0]
    # ...

    for i in range(2):
        for j in range(3):
            axes[i, j].text(0.5, 0.5, str((i, j)), fontsize=18, ha='center')

    plt.show()
