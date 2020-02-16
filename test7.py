import matplotlib.pyplot as plt
import numpy as np

# 在一张图中绘制3组不同的直方图，并设置透明度

if __name__=="__main__":
    #  np.random.normal:正态分布
    # numpy.random.normal(loc=0.0, scale=1.0, size=None)  均值，标准差，shape
    x1 = np.random.normal(0, 0.8, 1000)
    x2 = np.random.normal(-2, 1, 1000)
    x3 = np.random.normal(3, 2, 1000)

    # kwargs:key = value是存储的字典。
    kwargs = dict(alpha=0.3, bins=40, density=True,histtype='step')

    plt.hist(x1, **kwargs)
    plt.hist(x2, **kwargs)
    plt.hist(x3, **kwargs)

    plt.show()