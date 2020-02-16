import matplotlib.pyplot as plt
import numpy as np

# 绘制一组误差为±0.8的数据的误差条图

if __name__ == "__main__":
    # 生成50个0-10的数据
    data = np.linspace(0, 10, 50)
    print(data)
    # 误差
    dy = 0.8
    y = np.sin(data) + dy * np.random.randn(50)
    # plt.errorbar(x, y,数据点的位置坐标
    #              yerr=None, xerr=None,数据的误差范围
    #              fmt='',数据点的标记样式以及相互之间连接线样式
    #              ecolor=None,误差棒的线条颜色
    #              elinewidth=None,误差棒的线条粗细
    #              capsize=None,误差棒边界横杠的大小
    #              capthick=None 误差棒边界横杠的厚度
    #              )
    plt.errorbar(data, y, yerr=dy, fmt='o', ecolor='r')
    plt.show()
