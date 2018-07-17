from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from multiprocessing import Process, Value, Array, Manager
import stddraw as std
from where_am_i import *
import tkinter

std.setXscale(-10.0, 10.0)
std.setYscale(-10.0, 10.0)
RADIUS = 0.2

manager = Manager()
x = manager.list([0])
y = manager.list([0])
angles = manager.list([0])

direction = Value('d', 0.0)
time = Value('d', 0.0)
strength = Value ('d', 0.0)

port = 1234

class SimpleEcho(WebSocket):
    def handleMessage(self):
        global direction
        global time
        global strength
        #receiving the data from HTML file
        temp = json.loads(self.data)
        directions,times,strengths = zip(*temp)
        with direction.get_lock():
            direction.value = directions[0]
        with time.get_lock():
            time.value = times[0]
        with strength.get_lock():
            strength.value = strengths[0]

        #print(direction)
        #print(time)
        #print(strength)

def mapper():

    print (time.value, direction.value, strength.value)
    x2, y2, strength2 = get_point(angles, time.value, direction.value, x, y, strength.value)
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

    std.filledCircle(x, y, RADIUS)
    std.show(500)

#while True:
    #pass

def mapLoop():
    while True:
        mapper()


server = SimpleWebSocketServer('', port, SimpleEcho)
p1 = Process(target = server.serveforever)
p2 = Process(target = mapLoop)
p2.start()
p1.start()
p1.join()
p2.join()
