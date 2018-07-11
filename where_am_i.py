import time
import numpy as np
import matplotlib


def update_time():
    start = 0
    end = 0
    seconds = 0
    for i in range(5):
        start = time.time()
        time.sleep(.5)
        end = time.time()
        seconds = end - start
        return seconds


def update_x(x_list):
    x = x_list
    speed = 0.5488                        # meters per second at speed 90
    seconds = update_time()
    distance = speed * seconds
    random = np.random.randint(2)
    last_place = x[-1]
    distance = np.sin(20) * distance      # x distance traveled

    if random == 0:                       # if left arrow is pressed
        distance = np.sin(20) * distance
        x.append(last_place - distance)
    elif random == 1:                     # if right arrow is pressed
        distance = np.sin(20) * distance
        x.append(last_place + distance)

    return x


def update_y(y_list):
    y = y_list
    speed = 0.5488                        # meters per second at speed 90
    seconds = update_time()
    distance = speed * seconds
    random = np.random.randint(4)
    last_place = y[-1]

    if random == 0:                       # if down arrow is pressed
        y.append(last_place - distance)
    elif random == 1:                     # if up arrow is pressed
        y.append(last_place + distance)
    elif random == 2:                     # if left arrow is pressed
        distance = np.cos(20) * distance  # y distance traveled
        y.append(last_place + distance)
    elif random == 3:                     # if right arrow is pressed
        distance = np.cos(20) * distance  # y distance traveled
        y.append(last_place + distance)

    return y


def find_direction():                     # returns cardinal direction of car

    seconds = update_time()               # how long the car has been turning

    if seconds >= 9 or seconds < 0.6:     # directions based on the circle time
        north(x, y)
        return "north", x, y
    elif seconds >= 0.6 and seconds < 1.8:
        northeast(x, y)
        return "northeast", x, y
    elif seconds >= 1.8 and seconds < 3:
        east(x, y)
        return "east", x, y
    elif seconds >= 3 and seconds < 4.2:
        southeast(x, y)
        return "southeast", x, y
    elif seconds >= 4.2 and seconds < 5.4:
        south(x, y)
        return "south", x, y
    elif seconds >= 5.4 and seconds < 6.6:
        southwest(x, y)
        return "southwest", x, y
    elif seconds >= 6.6 and seconds < 7.8:
        west(x, y)
        return "west", x, y
    elif seconds >= 7.8 and seconds < 9:
        northwest(x, y)
        return "northwest", x, y


def north(x_list, y_list):
    x = x_list
    x.append(x[-1])                       # keeps x value the same

    y = y_list
    speed = 0.5488                        # meters per second at speed 90
    seconds = update_time()
    distance = speed * seconds
    y.append(y[-1] + distance)            # adds distance to y

    return x, y

def south(x_list, y_list):
    x = x_list
    x.append(x[-1])                       # keeps x value the same

    y = y_list
    speed = 0.5488                        # meters per second at speed 90
    seconds = update_time()
    distance = speed * seconds
    y.append(y[-1] - distance)            # subtracts distance from y

    return x, y

def east(x_list, y_list):
    x = x_list
    speed = 0.5488                        # meters per second at speed 90
    seconds = update_time()
    distance = speed * seconds
    x.append(x[-1] + distance)            # adds distance to x value

    y = y_list
    y.append(y[-1])                       # keeps y value the same

    return x, y

def west(x_list, y_list):
    x = x_list
    speed = 0.5488                        # meters per second at speed 90
    seconds = update_time()
    distance = speed * seconds
    x.append(x[-1] - distance)            # subtracts distance from x value

    y = y_list
    y.append(y[-1])                       # keeps y value the same

    return x, y

def northeast(x_list, y_list):
    x = x_list
    speed = 0.5488                        # meters per second at speed 90
    seconds = update_time()
    distance = np.sin(20) * speed * seconds
    x.append(x[-1] + distance)            # adds distance to x value

    y = y_list
    distance = np.cos(20) * speed * seconds
    y.append(y[-1] + distance)            # adds distance to y value

    return x, y

def southeast(x_list, y_list):
    x = x_list
    speed = 0.5488                        # meters per second at speed 90
    seconds = update_time()
    distance = np.sin(20) * speed * seconds
    x.append(x[-1] + distance)            # adds distance to x value

    y = y_list
    distance = np.cos(20) * speed * seconds
    y.append(y[-1] - distance)            # subtracts distance from y value

    return x, y

def northwest(x_list, y_list):
    x = x_list
    speed = 0.5488                        # meters per second at speed 90
    seconds = update_time()
    distance = np.sin(20) * speed * seconds
    x.append(x[-1] - distance)            # subtracts distance from x value

    y = y_list
    distance = np.cos(20) * speed * seconds
    y.append(y[-1] + distance)            # adds distance to y value

    return x, y


def southwest(x_list, y_list):
    x = x_list
    speed = 0.5488                        # meters per second at speed 90
    seconds = update_time()
    distance = np.sin(20) * speed * seconds
    x.append(x[-1] - distance)            # subtracts distance from x value

    y = y_list
    distance = np.cos(20) * speed * seconds
    y.append(y[-1] - distance)            # subtracts distance from y value

    return x, y

if __name__ == '__main__':
    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]

    print(find_direction())
