import matplotlib.pyplot as plt
import numpy as np


# polt函数，画曲线
def plot():
    x = np.linspace(0, 10, 30)
    print(x)
    '''
    plt.plot(x, y, format_string, **kwargs)
    x轴数据，y轴数据，format_string控制曲线的格式字串
    format_string
    由颜色字符，风格字符，和标记字符
    '''
    plt.plot(x, np.sin(x), '-bo')
    plt.show()


if __name__ == "__main__":
    plot()
