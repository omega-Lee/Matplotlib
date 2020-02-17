import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    x=np.arange(0, 2, 0.5)
    print(x)
    print(x.shape)
    # 添加新的轴
    x2=np.arange(0, 10)[:, np.newaxis]
    print(x2)
    print(x2.shape)