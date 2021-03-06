from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from multiprocessing import Process, Value
from picar import back_wheels
from picar import front_wheels
import matplotlib.pyplot as plt

import picar
import curses
import time
import RPi.GPIO as GPIO
import time
import numpy as np

import sys

picar.setup()
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
forward_speed = 90

port = 9876

close_to_wall = Value ('b', False)
emergency_backup = Value ('b', False)
x_list = [0]
y_list = [0]
start = 0

plt.ion()
fig, ax = plt.subplots()
x, y = [0],[0]
sc = ax.scatter(x,y)
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.draw()

class SimpleEcho(WebSocket):

    def handleMessage(self):
        if emergency_backup.value:
            return

        print(self.data, close_to_wall.value)
        if not close_to_wall.value and self.data == "up":
            global start
            start = time.time()
            print ("start")
            print start
            bw.speed = forward_speed
            bw.backward()
            straight_turn()
            print update_y("up")
            sc.set_offsets(np.c_[x,y])
            fig.canvas.draw_idle()
            plt.pause(0.1)

        elif self.data == "down":
            start = time.time()
            bw.speed = forward_speed
            bw.forward()
            straight_turn()
            print update_y("down")
        elif self.data == "right":
            right_turn()
            bw.speed = forward_speed
            print update_x("right")
        elif self.data == "left":
            left_turn()
            bw.speed = forward_speed
            print update_x("left")
        elif self.data == "straight":
            straight_turn()
            print update_y("straight")
        else:

            end = time.time()
            difference = end - start
            print "end"
            print end
            print "difference"
            print difference
            stop()

        #plt.waitforbuttonpress()

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

def stop():
    bw.stop()

def left_turn():
    fw.turn(87)

def straight_turn():
    fw.turn(97)
def right_turn():
    fw.turn(127)



def update_x(direction):
    x = x_list
    speed = 0.5488             # meters per second at speed 90
    distance = speed * seconds
    last_place = x[-1]
    distance = np.sin(20) * distance

    if direction == "left":     # if left arrow is pressed
        x.append(last_place - distance)
    elif direction == "right":   # if right arrow is pressed
        x.append(last_place + distance)
    return x

def update_y(direction):
    y = y_list
    speed = 0.5488             # meters per second at speed 90
    end = time.time()
    seconds = (end - start)
    distance = speed * seconds
    last_place = y[-1]

    if direction == "down":     # if down arrow is pressed
        y.append(last_place - distance)
    elif direction == "up":   # if up arrow is pressed
        y.append(last_place + distance)

    return y

class Ultrasonic_Avoidance:

    def __init__(self, trig, echo):
        GPIO.setmode(GPIO.BCM)
        self.TRIG = trig
        self.ECHO = echo

    def distance(self):
        #pulse_start = 0
        #pulse_end = 0

        print "Distance Measurement In Progress"

        GPIO.setup(self.TRIG,GPIO.OUT)
        GPIO.setup(self.ECHO,GPIO.IN)

        GPIO.output(self.TRIG, False)
        print "Waiting For Sensor To Settle"
        #time.sleep(2)

        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

        while GPIO.input(self.ECHO)==0:
          pulse_start = time.time()


        while GPIO.input(self.ECHO)==1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        return distance


    def less_than(self, alarm_gate):
		dis = self.distance()
		status = 0
		if dis >=0 and dis <= alarm_gate:
			status = 1
		elif dis > alarm_gate:
			status = 0
		else:
			status = -1
		#print 'distance =',dis
		#print 'status =',status
		return status

# Responses for status and distance
def distanceLoop():

    UA = Ultrasonic_Avoidance(20,16)
    threshold = 30
    while True:
        distance = UA.distance()
        status = UA.less_than(threshold)
        print(distance)
        #print(status)
        if distance != -1:
            print 'distance', distance, 'cm'
            time.sleep(0.2)
        else:
            print False
            close_to_wall.value = True
            bw.stop()
        # if the car is in the alarming range
        if status == 1:
            emergency_backup.value = True
            close_to_wall.value = True
            bw.speed = forward_speed
            bw.forward()
            straight_turn()
            print "Less than %d" % threshold
        # distance is fine so be normal
        elif status == 0:
            if (emergency_backup.value):
                bw.stop()
                emergency_backup.value = False

            print "Over %d" % threshold
            close_to_wall.value = False
        # too close to wall, STOP
        else:
            close_to_wall.value = True
            bw.stop()
            print "Read distance error."





server = SimpleWebSocketServer('', port, SimpleEcho)
p1 = Process(target = server.serveforever)
p2 = Process(target = distanceLoop)
p2.start()
p1.start()
p1.join()
p2.join()
