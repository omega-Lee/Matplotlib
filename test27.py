import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    fig = plt.figure()

    # 第一种方法
    ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4], ylim=(-1.2, 1.2))
    ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4], ylim=(-1.2, 1.2))

    # 第二种方法
    '''
    ax1 = plt.Axes(fig, [0.1, 0.5, 0.8, 0.4], ylim=(-1.2, 1.2))
    ax2 = plt.Axes(fig, [0.1, 0.1, 0.8, 0.4], ylim=(-1.2, 1.2))

    fig.add_axes(ax1)
    fig.add_axes(ax2)
    '''
    x = np.linspace(0, 10)
    print(x)

    ax1.plot(np.sin(x))
    ax2.plot(np.cos(x))

    plt.show()
