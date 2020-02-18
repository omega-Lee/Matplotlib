import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # GridSpec:指定子图将放置的网格的几何位置。 需要设置网格的行数和列数
    grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
    '''
    00,01,02
    10,11,12
    '''
    plt.subplot(grid[0, 0])     # 00
    plt.subplot(grid[0, 1:])    # 01,02
    plt.subplot(grid[1, :2])    # 10,11
    plt.subplot(grid[1, 2])     # 12

    plt.show()
