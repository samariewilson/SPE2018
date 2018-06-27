import numpy as np
import matplotlib.pyplot as plt

# adds coordinates and strength to a 3 dimensional list
# need to make these lists global so we can use the function
def add_point(x, y, strength):
    x_coord = []
    y_coord = []
    signal_strength = []

    x_coord.append(x)
    y_coord.append(y)
    signal_strength.append(strength)
    print(x_coord)
    print(y_coord)
    print(signal_strength)

def map(x, y, strength):
    x_coord = x
    y_coord = y
    signal_strength = strength
    max = 70
    increment = 10
    size = 1000
    for i in range(len(x)):
        if strength[i] >= max:
            plt.scatter(x_coord[i], y_coord[i], c = '#FF0000', s = size)
        elif strength[i] < max and strength[i] >= (max - increment):
            plt.scatter(x_coord[i], y_coord[i], c = '#FF5D00', s = size)
        elif strength[i] < (max - increment) and strength[i] >= (max - (2*increment)):
            plt.scatter(x_coord[i], y_coord[i], c = '#FF8F00', s = size)
        elif strength[i] < (max - (2*increment)) and strength[i] >= (max - (3*increment)):
            plt.scatter(x_coord[i], y_coord[i], c = '#FFC500', s = size)
        elif strength[i] < (max - (3*increment)) and strength[i] >= (max - (4*increment)):
            plt.scatter(x_coord[i], y_coord[i], c = '#FFFF00', s = size)
        elif strength[i] < (max - (4*increment)) and strength[i] >= (max - (5*increment)):
            plt.scatter(x_coord[i], y_coord[i], c = '#00FFFB', s = size)
        elif strength[i] < (max - (5*increment)) and strength[i] >= (max - (6*increment)):
            plt.scatter(x_coord[i], y_coord[i], c = '#009BFF', s = size)
        elif strength[i] < (max - (6*increment)) and strength[i] >= (max - (7*increment)):
            plt.scatter(x_coord[i], y_coord[i], c = '#0A34F5', s = size)
        elif strength[i] < (max - (7*increment)) and strength[i] >= (max - (8*increment)):
            plt.scatter(x_coord[i], y_coord[i], c = '#220E80', s = size)
        else:
            print('data not in expected range')
        # would this work because the color has to depend on the signal not x,y
        '''plt.scatter(x_coord[i], y_coord[i], cmap = 'coolwarm', s = size,
        vmin = 0, vmax = 100)'''

    # need to make these scalable functions that depend on the max and min of the data
    plt.xticks(np.arange(0, 110, 10))
    plt.yticks(np.arange(0, 110, 10))
    plt.show()


if __name__ == '__main__':
    add_point(0, 1, 2)
    add_point(0, 1, 2)

    strength = [0, 10, 20, 30, 40, 50, 60, 70, 225, 250]
    x = [53, 98, 23, 5, 45, 21, 33, 76, 17, 59]
    y = [23, 87, 2, 47, 23, 90, 61, 33, 47, 12]

    map(x, y, strength)
