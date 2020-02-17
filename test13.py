import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    print(x)
    plt.plot(x, y, ':', label='sin(x)')
    # 设置y轴上下限
    plt.ylim(-1.5, 1.5)
    # 设置x轴上下限
    plt.xlim(-2, 15)

    # 设置xy轴标签
    plt.xlabel('---X---')
    plt.ylabel('---Y---')

    # 设置标题
    plt.title('Sin Function')

    # 设置网格
    plt.grid()

    plt.show()
