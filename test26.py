import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # 在一个10x0的画布中(0.65, 0.65)的位置创建一个0.2x0.2的子图

    ax1 = plt.axes()
    ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])

    plt.show()
