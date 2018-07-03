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
    speed = 0.5488             # meters per second at speed 90
    seconds = update_time()
    distance = speed * seconds
    random = np.random.randint(2)
    last_place = x[-1]
    distance = np.sin(20) * distance   # x distance traveled
    if random == 0:     # if left arrow is pressed
        x.append(last_place - distance)
    elif random == 1:   # if right arrow is pressed
        x.append(last_place + distance)
    return x

def update_y(y_list):
    y = y_list
    speed = 0.5488             # meters per second at speed 90
    seconds = update_time()
    distance = speed * seconds
    random = np.random.randint(2)
    last_place = y[-1]
    if random == 0:     # if down arrow is pressed
        y.append(last_place - distance)
    elif random == 1:   # if up arrow is pressed
        y.append(last_place + distance)
    return y

if __name__ == '__main__':
    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]
    print(update_time())
    print(update_x(x))
    print(update_y(y))
