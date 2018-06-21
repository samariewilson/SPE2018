from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from multiprocessing import Process
from picar import back_wheels
from picar import front_wheels

import picar
import curses
import time
import RPi.GPIO as GPIO

import sys

picar.setup()
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
forward_speed = 100

port = 9876

close_to_wall = False

class SimpleEcho(WebSocket):

    def handleMessage(self):
        print(self.data)
        if not close_to_wall and self.data == "up":
            bw.speed = forward_speed
            bw.backward()
            straight_turn()
        elif self.data == "down":
            bw.speed = forward_speed
            bw.forward()
            straight_turn()
        elif self.data == "right":
            right_turn()
            bw.speed = forward_speed
        elif self.data == "left":
            left_turn()
            bw.speed = forward_speed
        elif self.data == "straight":
            straight_turn()
        else:
            stop()


def stop():
    bw.stop()

def left_turn():
    fw.turn(82)

def straight_turn():
    fw.turn(102)
def right_turn():
    fw.turn(122)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

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
		if dis >= 0 and dis <= alarm_gate:
			status = 1
		elif dis > alarm_gate:
			status = 0
		else:
			status = -1
		#print 'distance =',dis
		#print 'status =',status
		return status
def distanceLoop():
    UA = Ultrasonic_Avoidance(20)
    threshold = 10
    while True:
        distance = UA.get_distance()
        status = UA.less_than(threshold)
        print(distance)
        print (status)
        if distance != -1:
            print 'distance', distance, 'cm'
            time.sleep(0.2)
        else:
            print False
            close_to_wall = True
            bw.stop()
        # if the car is in the alarming range
        if status == 1:
            close_to_wall = True
            bw.stop()
            print "Less than %d" % threshold
        # distance is greater so be normal
        elif status == 0:
            print "Over %d" % threshold
        else:
            bw.stop()
            print "Read distance error."


server = SimpleWebSocketServer('', port, SimpleEcho)
p1 = Process(target=server.serveforever)
p2 = Process(target=distanceLoop)
p2.start()
p1.start()
p1.join()
p2.join()
