import stddraw as std
import time as t
from where_am_i import *


std.setXscale(-10.0, 10.0)
std.setYscale(-10.0, 10.0)
RADIUS = 0.2

x = [0]
y = [0]
angles = [0]

direction = Value('d', 0.0)
time = Value('d', 0.0)
strength = Value ('d', 0.0)

def mapper():
    print ('hey')
    x2, y2, strength2 = get_point(angles, time, direction, x, y, strength)
    max = 90
    increment = 10
    #strength = s
    if strength2>= max:
        std.setPenColor(std.DARK_RED)
    elif strength2 < max and strength2 >= (max - increment):
        std.setPenColor(std.RED)
    elif strength2 < (max - increment) and strength2 >= (max - (2*increment)):
        std.setPenColor(std.MAGENTA)
    elif strength2 < (max - (2*increment)) and strength2 >= (max - (3*increment)):
        std.setPenColor(std.VIOLET)
    elif strength2 < (max - (3*increment)) and strength2 >= (max - (4*increment)):
        std.setPenColor(std.PINK)
    elif strength2 < (max - (4*increment)) and strength2 >= (max - (5*increment)):
        std.setPenColor(std.BOOK_LIGHT_BLUE)
    elif strength2 < (max - (5*increment)) and strength2 >= (max - (6*increment)):
        std.setPenColor(std.BOOK_BLUE)
    elif strength2 < (max - (6*increment)) and strength2 >= (max - (7*increment)):
        std.setPenColor(std.BLUE)
    elif strength2 < (max - (7*increment)) and strength2 >= (max - (8*increment)):
        std.setPenColor(std.DARK_BLUE)
    elif strength2 < (max - (8*increment)):
        std.setPenColor(std.BLACK)
    else:
        print('data not in expected range', strength)
    std.filledCircle(x2[-1], y2[-1], RADIUS)
    std.show(500)

while True:
    with open('text.txt', 'r') as z:
        direction = z.readline()
        difference = z.readline()
        strength = z.readline()
        print ("hello")
        print (direction, difference, strength)
        mapper()
        print ("no")
        t.sleep(1)

    print (direction, difference, strength)
