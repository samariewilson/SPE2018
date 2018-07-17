from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from multiprocessing import Process, Value, Array, Manager
import stddraw as std
from where_am_i import *

std.setXscale(-10.0, 10.0)
std.setYscale(-10.0, 10.0)
RADIUS = 0.2

manager = Manager()
x = manager.list([0])
y = manager.list([0])
angles = manager.list([0])

direction = manager.Value('d', 0.0)
time = manager.Value('d', 0,0)
strength = manager.Value ('d', 0,0)

port = 1234

class SimpleEcho(WebSocket):
    def handleMessage(self):
        global direction
        global time
        global strength
        #receiving the data from HTML file
        temp = json.loads(self.data)
        directions,times,strengths = zip(*temp)
        direction = directions[0]
        time = times[0]
        strength = strengths[0]

        #print(direction)
        #print(time)
        #print(strength)

def mapper():
    x, y, strength = get_point(angles, time, direction, x, y, strength)
    max = 90
    increment = 10
    #strength = s
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

    std.filledCircle(x, y, RADIUS)
    std.show(500)

while True:
    pass

server = SimpleWebSocketServer('', port, SimpleEcho)
p1 = Process(target = server.serveforever)
p2 = Process(target = mapper)
p2.start()
p1.start()
p1.join()
p2.join()
