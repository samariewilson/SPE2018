from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import time
import numpy as np

global direction
global time
global strength
global x
global y
global angles

x = [0]
y = [0]
angles = [0]

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
    strength = get_strength()
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

    return x, y, strength

                                          # returns angle of car from initial
def get_angle(angles, time, direction):
    last_angle = angles[-1]
    degrees_moved = 360 * time / 9.6

    if direction == 'l':                 # if left arrow is pressed
        angle = (last_angle + degrees_moved) % 360

    elif direction == 'r':                 # if right arrow is pressed
        angle = (360 - ((360 - last_angle) + degrees_moved)) % 360

    elif direction == 'f' or direction == 'b' or direction == 's':
        angle = last_angle
    angles.append(angle)
    return angle

def get_strength():
    return strength
