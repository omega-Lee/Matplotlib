import matplotlib.pyplot as plt
import numpy as np

# 绘制垂直于x轴x<4 and x>6的参考区域，以及y轴y<0.2 and y>-0.2的参考区域

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

    # 设置参考区域:水平
    plt.axvspan(xmin=4, xmax=6, facecolor='r', alpha=0.3)
    # 设置参考区域:垂直
    plt.axhspan(ymin=-0.2, ymax=0.2, facecolor='b', alpha=0.3)

    # 添加注释文字
    plt.text(12,1.0,'sin(x)',weight='bold',color='b',fontsize=15)

    # 用箭头标出第一个峰值
    # 箭头参数：dict字典类型
    plt.annotate('maximum', xy=(np.pi / 2, 1), xytext=(np.pi / 2 + 1, 1),
                 weight='bold',
                 color='r',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='r'),fontsize=15)
    plt.show()
