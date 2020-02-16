import matplotlib.pyplot as plt
import numpy as np

# 绘制一个柱状图

if __name__ == "__main__":
    x1 = [1, 2, 3, 4, 5, 6, 7, 8]
    y1 = [3, 1, 4, 5, 8, 9, 7, 2]

    x2=np.linspace(1,10,8)
    y2=np.sin(x2)
    label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    # bar(x, height, width=0.8, bottom=None,, align = 'center', data = None, kwargs *)
    plt.bar(x2, y2, tick_label=label,color='b',edgecolor='r')
    plt.show()