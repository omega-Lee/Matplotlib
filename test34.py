from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)

    ax.plot3D(xline, yline, zline)

    plt.show()
