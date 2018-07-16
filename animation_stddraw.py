import stddraw as std
from where_am_i import *

std.setXscale(-10.0, 10.0)
std.setYscale(-10.0, 10.0)
RADIUS = 0.2
x = [0]
y = [0]
angles = [0]
time = [.5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5, .5,
.5, .5]
direction = ['right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right',
'left', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'left', 'left']
strength = [10, 20, 30, 40, 50, 60, 70, 80, 90, 34, 56, 76, 87, 345, 64, 34, 25, 657, 23, 5, 63, 34, 5, 6, 34]

for i, j, k, m, n in zip(x, y, strength, time, direction):
    max = 90
    increment = 10
    strength = k
    if strength >= max:
        std.setPenColor(std.DARK_RED)
    elif strength < max and strength >= (max - increment):
        std.setPenColor(std.RED)
    elif strength < (max - increment) and strength >= (max - (2*increment)):
        std.setPenColor(std.MAGENTA)
    elif strength < (max - (2*increment)) and strength >= (max - (3*increment)):
        std.setPenColor(std.VIOLET)
    elif strength < (max - (3*increment)) and strength >= (max - (4*increment)):
        std.setPenColor(std.PINK)
    elif strength < (max - (4*increment)) and strength >= (max - (5*increment)):
        std.setPenColor(std.BOOK_LIGHT_BLUE)
    elif strength < (max - (5*increment)) and strength >= (max - (6*increment)):
        std.setPenColor(std.BOOK_BLUE)
    elif strength < (max - (6*increment)) and strength >= (max - (7*increment)):
        std.setPenColor(std.BLUE)
    elif strength < (max - (7*increment)) and strength >= (max - (8*increment)):
        std.setPenColor(std.DARK_BLUE)
    elif strength < (max - (8*increment)):
        std.setPenColor(std.BLACK)
    else:
        print('data not in expected range', strength)

    get_point(angles, m, n, x, y)
    print(angles)

    std.filledCircle(i, j, RADIUS)
    std.show(500)

while True:
    pass
