import time
import numpy as np


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


def find_direction(x, y, time):           # returns cardinal direction of car

    turn = (360 * time) / 9.6             # degrees the car has turned

    if degrees >= 337.5 or degrees < 22.5:# directions based on the circle time
        north(x, y)
        return "north", x, y
    elif degrees >= 22.6 and degrees < 67.5:
        northeast(x, y)
        return "northeast", x, y
    elif degrees >= 67.5 and degrees < 112.5:
        east(x, y)
        return "east", x, y
    elif degrees >= 112.5 and degrees < 157.5:
        southeast(x, y)
        return "southeast", x, y
    elif degrees >= 157.5 and degrees < 202.5:
        south(x, y)
        return "south", x, y
    elif degrees >= 202.5 and degrees < 247.5:
        southwest(x, y)
        return "southwest", x, y
    elif degrees >= 247.5 and degrees < 292.5:
        west(x, y)
        return "west", x, y
    elif degrees >= 292.5 and degrees < 337.5:
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
    seconds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(10):
        print(find_direction(x, y, seconds[i]))
