from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import stddraw as std
from where_am_i import *

std.setXscale(-10.0, 10.0)
std.setYscale(-10.0, 10.0)
RADIUS = 0.2


port = 1234

class SimpleEcho(WebSocket):
    def handleMessage(self):
        x = [0]
        y = [0]
        angles = [0]
        direction = [0]
        time = [0]
        strength = [0]
        #receiving the data from HTML file
        temp = json.loads(self.data)
        direction,time,strength = zip(*temp)
        get_point(angles, time, direction, x, y)
        get_angle(angles, time, direction)

for i, j, s, t, d in zip(x, y, strength, time, direction):
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

    x, y, strength = get_point(angles, t, d, x, y)

    std.filledCircle(i, j, RADIUS)
    std.show(500)

while True:
    pass

server = SimpleWebSocketServer('', port, SimpleEcho)
server.serveforever()
