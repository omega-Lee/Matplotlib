import matplotlib.pyplot as plt
import numpy as np

# 设置相同行和列共享x,y轴
if __name__ == '__main__':
    fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
    plt.show()
