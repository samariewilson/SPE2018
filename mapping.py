import numpy as np
import matplotlib.pyplot as plt
from where_am_i import update_x
from where_am_i import update_y

# adds coordinates and strength to a 3 dimensional list
# need to make these lists global so we can use the function
def add_point(x, y, strength):
    x_coord = []
    y_coord = []
    signal_strength = []

    x_coord.append(x)
    y_coord.append(y)
    signal_strength.append(strength)

# returns the range of a list
def data_range(x):
    range = max(x) - min(x)
    return range
# maps the x,y coordinates to a scatter plot with different colors depending
# on signal strength
def map(x, y, strength):
    x_coord = x
    y_coord = y
    signal_strength = strength

    max = np.max(strength)                   # maximum recorded signal strength

    increment = data_range(strength) / 8     # evenly splits data into 8
                                             # sections for color coding

    increment_x = data_range(x) / 10         # evenly splits x,y lists for
    increment_y = data_range(y) / 10         # graphing

    size = 1000                              # size of markers

    # determines how strong signal is at each point and plots that point with
    # the corresponding color (strong signal = red, weak signal = blue)
    for i in range(len(x)):
        if strength[i] >= max:
            plt.scatter(x_coord[i], y_coord[i], c = '#D41107', s = size)
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
            plt.scatter(x_coord[i], y_coord[i], c = '#03C0FC', s = size)
        elif strength[i] < (max - (6*increment)) and strength[i] >= (max - (7*increment)):
            plt.scatter(x_coord[i], y_coord[i], c = '#1486EB', s = size)
        elif strength[i] < (max - (7*increment)) and strength[i] >= (max - (8*increment)):
            plt.scatter(x_coord[i], y_coord[i], c = '#1C2EEA', s = size)
        elif strength[i] < (max - (8*increment)):
            plt.scatter(x_coord[i], y_coord[i], c = '#11056E', s = size)
        else:
            print('data not in expected range', strength[i])
        # would this work because the color has to depend on the signal not x,y
        '''plt.scatter(x_coord[i], y_coord[i], cmap = 'coolwarm', s = size,
        vmin = 0, vmax = 100)'
        '''
    # scales the x and y axes with the max and min of the data
    # maybe should just use x parameters for both so map isn't skewed?
    plt.xticks(np.arange((np.min(x) - increment_x), (np.max(x) + increment_x), 10))
    plt.yticks(np.arange((np.min(y) - increment_y), (np.max(y) + increment_y), 10))
    plt.show()


if __name__ == '__main__':

    # dummy lists until we get real data
    strength = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    x = [0]
    y = [0]
    for j in range(8):
        x = update_x(x)
        y = update_y(y)

    map(x, y, strength)
