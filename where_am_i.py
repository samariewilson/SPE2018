import numpy as np

# takes lists angles, x, and y, floats time and strength, and string direction
                                          # and returns next coordinate of car
def get_point(angles, time, direction, x, y, strength):
    speed = 0.5488                        # meters per seconds at speed 90
    distance = speed * time               # distance traveled overall
    angle = get_angle(angles, time, direction)
    angle = np.radians(angle)             #convert to radians
                                          # distance travled in x direction
    x_dist = np.absolute(np.sin(angle) * distance)
                                          # distance travled in x direction
    y_dist = np.absolute(np.cos(angle) * distance)
    angle = np.degrees(angle)             # convert back to degrees
    go_up = True
    go_down = False

    if direction == 'f':
        go_up = True
        go_down = False
    elif direction == 'b':
        go_up = False
        go_down = True
    else:
        pass

    if go_up == True:
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

    if go_up == False:
        if angle >= 0 and angle < 90:
            x.append(x[-1] + x_dist)
            y.append(y[-1] - y_dist)

        elif angle >= 90 and angle < 180:
            x.append(x[-1] + x_dist)
            y.append(y[-1] + y_dist)

        elif angle >= 180 and angle < 270:
            x.append(x[-1] - x_dist)
            y.append(y[-1] + y_dist)

        elif angle >= 270 and angle < 360:
            x.append(x[-1] - x_dist)
            y.append(y[-1] - y_dist)
    #print([x,y])
    return [x, y, strength]

                                           # returns angle of car from initial
def get_angle(angles, time, direction):
    last_angle = angles[-1]
    degrees_moved = 360 * time / 9.6

    go_up = True
    go_down = False

    if direction == 'f':
        go_up = True
        go_down = False
    elif direction == 'b':
        go_up = False
        go_down = True
    else:
        pass
    if go_up == True:
        if direction == 'l':                   # if left arrow is pressed
            angle = (last_angle + degrees_moved) % 360
        elif direction == 'r':                 # if right arrow is pressed
            angle = (360 - ((360 - last_angle) + degrees_moved)) % 360
        else:
            angle = last_angle

    if go_up == False:
        if direction == 'r':                   # if left arrow is pressed
            angle = (last_angle + degrees_moved) % 360
        elif direction == 'l':                 # if right arrow is pressed
            angle = (360 - ((360 - last_angle) + degrees_moved)) % 360
        else:
            angle = last_angle

    angles.append(angle)
    return angle

def get_strength(strength):
    return strength

if __name__ == '__main__':
    x = [0]
    y = [0]
    angles = [0]
    direction = 'b'
    time = 4.8
    strength = 1
    print(get_point(angles, time, direction, x, y, strength))
    print(angles)
