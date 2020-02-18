import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    plt.figure()
    # 1...6
    # subplot(x, y, i):将当前窗口分成x行y列，当前位置为第i个
    for i in range(1, 7):
        plt.subplot(2, 3, i)
        plt.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')

    # 方法二
    # fig = plt.figure()
    # fig.subplots_adjust(hspace=0.4, wspace=0.4)
    # for i in range(1, 7):
    #     ax = fig.add_subplot(2, 3, i)
    #     ax.text(0.5, 0.5, str((2, 3, i)),fontsize=18, ha='center')

    plt.show()
