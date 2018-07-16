from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import time
import numpy as np

global direction
global time
global strength

class SimpleEcho(WebSocket):
    def handleMessage(self):
        #receiving the data from HTML file
        temp = json.loads(self.data)
        direction,time,strength = zip(*temp)
        get_point(angles, time, direction, x, y)
        get_angle(angles, time, direction)


                                          # returns next coordinate of car
def get_point(angles, time, direction, x, y):
    speed = 0.5488                        # meters per seconds at speed 90
    distance = speed * time               # distance traveled overall
    angle = get_angle(angles, time, direction)
    angle = np.radians(angle)             #convert to radians
                                          # distance travled in x direction
    x_dist = np.absolute(np.sin(angle) * distance)
                                          # distance travled in x direction
    y_dist = np.absolute(np.cos(angle) * distance)
    angle = np.degrees(angle)             # convert back to degrees

    if angle >= 0 and angle < 90:
        x.append(x[-1] - x_dist)
        y.append(y[-1] + y_dist)

    elif angle >= 90 and angle < 180:
        x.append(x[-1] - x_dist)
        y.append(y[-1] - y_dist)

    elif angle >= 180 and angle < 270:
        x.append(x[-1] + x_dist)
        y.append(y[-1] - y_dist)

    elif angle >= 270 and angle < 360:
        x.append(x[-1] + x_dist)
        y.append(y[-1] + y_dist)

    return x, y

                                          # returns angle of car from initial
def get_angle(angles, time, direction):
    last_angle = angles[-1]
    degrees_moved = 360 * time / 9.6

    if direction == 'left':               # if left arrow is pressed
        angle = (last_angle + degrees_moved) % 360

    if direction == 'right':              # if right arrow is pressed
        angle = (360 - ((360 - last_angle) + degrees_moved)) % 360

    angles.append(angle)
    return angle


if __name__ == '__main__':
    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]
    angles = [0]
    seconds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(get_point(angles, 5.5, 'left', x, y))
    print(get_angle(angles, 5.5, 'left'))
