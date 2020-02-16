import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # 随机数生成器
    rdm = np.random.RandomState(1)

    # 产生100对随机数据，服从正态分布N(0,1)
    x = rdm.randn(100)
    y = rdm.randn(100)
    # 颜色种类，范围：[0,1)
    colors=rdm.rand(100)

    print('x:', x)
    print('y:', y)
    print('colors:', colors)

    # 尺寸种类
    sizes=1000*rdm.rand(100)

    plt.scatter(x,y,c=colors,s=sizes,alpha=0.3)
    plt.colorbar()
    plt.show()
