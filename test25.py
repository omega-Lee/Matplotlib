import matplotlib.pyplot as plt
import numpy as np

# 展示色阶
if __name__ == '__main__':
    x = np.linspace(0, 10, 10000)
    y1 = np.sin(x) * np.cos(x[:, np.newaxis])
    y2 = np.sin(x) * np.sin(x[:, np.newaxis])

    # 在Matplotlib库中，调用imshow()函数实现热图绘制。
    '''
    data数据要求：
    (1) M * N 此时数组必须为浮点型，其中值为该坐标的灰度；
    (2) M * N * 3 RGB（浮点型或者unit8类型）
    (3) M * N * 4 RGBA（浮点型或者unit8类型）
    '''
    # 将色阶分成6个离散值显示
    # get_cmap:色阶类型
    plt.imshow(y1,cmap=plt.cm.get_cmap('Spectral', 10))
    plt.colorbar()
    # 色阶范围
    plt.clim(-1, 1)
    plt.show()
