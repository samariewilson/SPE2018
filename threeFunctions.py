from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from multiprocessing import Process, Value, Array, Manager
from picar import back_wheels
from picar import front_wheels
from itertools import groupby

import json
import picar
import curses
import time
import RPi.GPIO as GPIO
import time
import numpy as np

import wifi_phone as wi
import sys

global master_array
global times


manager = Manager()
master_array = manager.list(['s','s'])
times = manager.list([0,0])


picar.setup()
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
forward_speed = 90

port = 9876

close_to_wall = Value ('b', False)
emergency_backup = Value ('b', False)
x_list = [0]
y_list = [0]
strength_list = [0]
sec = [0]
start = 0
start2 = 0
end = 0
end2 = 0

class SimpleEcho(WebSocket):
    def handleMessage(self):
        if emergency_backup.value:
            return

        print(self.data, close_to_wall.value)
        if not close_to_wall.value and self.data == "up":

            #start = time.time()
            #print ("start")
            #print start
            print "dog"
            bw.speed = forward_speed
            print "cat"
            forward()
            #bw.backward()
            print "rat"
            straight_turn()

        elif self.data == "down":
            #start = time.time()
            bw.speed = forward_speed
            backward()
            #bw.forward()
            straight_turn()

        elif self.data == "right":
            #start2 = time.time()
            right_turn()

        elif self.data == "left":
            #start2 = time.time()
            left_turn()
        elif self.data == "stopLeft":
            #end2 = time.time()
            #difference = end2 - start2
            #print difference
            #print update_x("left", difference, self)
            straight_turn()
        elif self.data == "stopRight":
            #end2 = time.time()
            #difference = end2 - start2
            #print update_x("right", difference, self)
            straight_turn()
        elif self.data == "stopUp":
            #end = time.time()
            #difference = end - start
            #print update_y("up", difference, self)
            stop()
        elif self.data == "stopDown":
            #end = time.time()
            #difference = end - start
            #print update_y("down", difference, self)
            stop()

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

def stop():
    master_array.append('s')
    start = time.time()
    times.append(start)

    bw.stop()

def left_turn():
    master_array.append('l')
    start = time.time()
    times.append(start)
    fw.turn(87)

def right_turn():
    master_array.append('r')
    start = time.time()
    times.append(start)
    fw.turn(127)

def straight_turn():
    fw.turn(97)

def forward():
    print "hello"
    print master_array, times
    master_array.append('f')
    start = time.time()
    times.append(start)
    bw.backward()

def backward():
    master_array.append('b')
    start = time.time()
    times.append(start)
    bw.forward()


def update_x(direction, seconds, socket):
    global x_list
    global y_list
    global strength_list
    global sec

#    x = x_list
    speed = 0.5488             # meters per second at speed 90
    distance = speed * seconds
    last_place = x_list[-1]
    distance = np.sin(20) * distance
    y_list.append(y_list[-1])

    sig = wi.strength()        # get wifi strength
    strength_list.append(sig)
    sec.append(seconds)


    if direction == "left":     # if left arrow is pressed
        x_list.append(last_place - distance)
    elif direction == "right":   # if right arrow is pressed
        x_list.append(last_place + distance)
    #x_list =  x
    # print (zip(x_list,y_list, strength_list))
    print sec

    threeList = list(zip(x_list,y_list, strength_list, sec))

    socket.sendMessage(json.dumps(threeList))
    return x_list

def update_y(direction, seconds, socket):
    global y_list
    global x_list
    global strength_list
    global sec

    #y = y_list
    speed = 0.5488             # meters per second at speed 90
    #seconds = (end - start)
    distance = speed * seconds
    last_place = y_list[-1]
    distance = np.cos(20) * distance
    x_list.append(x_list[-1])

    sig = wi.strength()        # get wifi strength
    strength_list.append(sig)
    sec.append(seconds)

    if direction == "down":     # if down arrow is pressed
        y_list.append(last_place - distance)
    elif direction == "up":   # if up arrow is pressed
        y_list.append(last_place + distance)
    #y_list = y
    print sec
#    print (list(zip(x_list,y_list, strength_list)))
    threeList = list(zip(x_list,y_list, strength_list, sec))


    socket.sendMessage(json.dumps(threeList))

    return y_list

class Ultrasonic_Avoidance(object):
	timeout = 0.05

	def __init__(self, channel):
		self.channel = channel
		GPIO.setmode(GPIO.BCM)

	def distance(self):
		pulse_end = 0
		pulse_start = 0
		GPIO.setup(self.channel,GPIO.OUT)
		GPIO.output(self.channel, False)
		time.sleep(0.01)
		GPIO.output(self.channel, True)
		time.sleep(0.00001)
		GPIO.output(self.channel, False)
		GPIO.setup(self.channel,GPIO.IN)

		timeout_start = time.time()
		while GPIO.input(self.channel)==0:
			pulse_start = time.time()
			if pulse_start - timeout_start > self.timeout:
				return -1
		while GPIO.input(self.channel)==1:
			pulse_end = time.time()
			if pulse_start - timeout_start > self.timeout:
				return -1

		if pulse_start != 0 and pulse_end != 0:
			pulse_duration = pulse_end - pulse_start
			distance = pulse_duration * 100 * 343.0 /2
			distance = int(distance)
			#print 'start = %s'%pulse_start,
			#print 'end = %s'%pulse_end
			if distance >= 0:
				return distance
			else:
				return -1
		else :
			#print 'start = %s'%pulse_start,
			#print 'end = %s'%pulse_end
			return -1

	def get_distance(self, mount = 5):
		sum = 0
		for i in range(mount):
			a = self.distance()
			#print '    %s' % a
			sum += a
		return int(sum/mount)
	def less_than(self, alarm_gate):
		dis = self.get_distance()
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

    UA = Ultrasonic_Avoidance(20)
    threshold = 30
    while True:
        distance = UA.get_distance()
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

def control(master_array, times, sock):
    while True:
        if len(master_array) <= 3:
            if master_array[-1] == master_array[-2]:
                pass

        else:
             sort = [(k, sum(1 for i in g)) for k,g in groupby(master_array)]
             dir, rep = zip(*sort)
             difference = times[rep[1] + 1] - times[2]
             #gets signal strength
             sig = wi.strength()
             temp = [dir[1],difference, sig]
             if (difference == 0):
                difference = times[3] - times[2]
                #gets signal strength
                sig = wi.strength()
                temp = [dir[1], difference, sig]
                print "no"
                print temp


                sock.sendMessage(json.dumps(temp))
                print "nah"
                print master_array
                #send message to SAM
                del master_array[2]
                del times[2]
             else:
                 print "hi"
                 print temp
                 socket.sendMessage(json.dumps(temp))
                 print "Yay"
                 print master_array
                 del master_array[2: rep[1] + 2]
                 del times[2: rep[1] + 2]

             # socket.sendMessage...(temp)


        time.sleep(1)




server = SimpleWebSocketServer('', port, SimpleEcho)
p1 = Process(target = server.serveforever)
p2 = Process(target = distanceLoop)
p3 = Process(target = control, args = (master_array, times, server))
p3.start()
p2.start()
p1.start()
p1.join()
p2.join()
p3.join()
