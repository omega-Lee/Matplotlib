import matplotlib.pyplot as plt
import numpy as np

# 绘制一张二维直方图

if __name__=="__main__":

    # 第一种方法
    mean=[0,0]
    cov=[[1,1],[1,2]]

    # 多元正态分布矩阵
    # def multivariate_normal(mean, cov, size=None, check_valid=None, tol=None)
    #  mean：mean是多维分布的均值维度为1；
    #     cov：协方差矩阵,注意：协方差矩阵必须是对称的且需为半正定矩阵；
    x,y=np.random.multivariate_normal(mean,cov,10000).T
    plt.hist2d(x,y,bins=20)
    plt.show()

    # 第二种方法
    x1 = np.random.randn(1000) + 3
    y1 = np.random.randn(1000) + 3
    plt.hist2d(x1, y1, bins=20)
    plt.show()
