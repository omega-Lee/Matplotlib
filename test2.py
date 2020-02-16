import matplotlib.pyplot as plt
import numpy as np


def scatter():
    data=np.linspace(0,10,30)
    plt.scatter(data,np.sin(data))
    plt.show()

if __name__=="__main__":
    scatter()