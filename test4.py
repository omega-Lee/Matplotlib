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

    plt.errorbar(data, y, yerr=dy, fmt='.k')
    plt.show()
