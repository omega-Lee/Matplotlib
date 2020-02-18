import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    mean = [0, 0]
    cov = [[1, 1], [1, 2]]
    x, y = np.random.multivariate_normal(mean, cov, 3000).T

    # 宽和高:6
    fig = plt.figure(figsize=(6, 6))
    grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
    main_ax = fig.add_subplot(grid[:-1, 1:])
    
    # 直方图：x,y
    y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
    x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)
    main_ax.scatter(x, y, s=3, alpha=0.2)

    x_hist.hist(x, 40, histtype='stepfilled', orientation='vertical')
    x_hist.invert_yaxis()

    y_hist.hist(y, 40, histtype='stepfilled', orientation='horizontal')
    y_hist.invert_xaxis()

    plt.show()
