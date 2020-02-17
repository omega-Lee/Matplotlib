import matplotlib.pyplot as plt
import numpy as np

# 在一张图里绘制sin,cos的图形，并展示图例

if __name__ == '__main__':
    x = np.linspace(0, 10, 1000)

    # fig, ax = plt.subplots()等价于fig, ax = plt.subplots(11)
    figure, ax = plt.subplots()

    ax.plot(x, np.sin(x), label='sin')
    ax.plot(x, np.cos(x), label='cos')

    # 显示图例,调整图例位置，且不显示边框
    ax.legend(loc='upper left', frameon=False)

    plt.show()
