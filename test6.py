import matplotlib.pyplot as plt
import numpy as np

# 绘制1000个随机值的直方图

if __name__ == "__main__":
    data = np.random.randn(1000)

    # hist(x, bins=None, density=None,……*kwargs)
    # x:数据集
    # bins:统计的区间分布
    # hist type:线条的类型
    # density:频数统计结果，频率统计结果=区间数目/(总数*区间宽度)

    plt.hist(x=data,bins=10,color='gray',histtype='bar',density=True)
    plt.show()