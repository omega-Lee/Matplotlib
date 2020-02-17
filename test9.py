import matplotlib.pyplot as plt
import numpy as np

# 绘制x=(0,10)间sin的图像，设置线性为虚线

if __name__ == '__main__':
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    print(x)
    plt.plot(x, y, '--')
    plt.show()
