from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from multiprocessing import Process, Value
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
forward_speed = 80

port = 9876

close_to_wall = Value('b', False)
emergency_backup = Value('b', False)


class SimpleEcho(WebSocket):

    def handleMessage(self):
        if emergency_backup.value:
            return

        print(self.data, close_to_wall.value)
        if not close_to_wall.value and self.data == "up":
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

    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        GPIO.setmode(GPIO.BOARD)

    def distance(self):
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

        GPIO.output(self.trig, GPIO.LOW)

        print("Waiting for sensor to settle")
        time.sleep(2)
        print("Calculating distance")

        GPIO.output(self.trig, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trig, GPIO.LOW)

        timeout_start = time.time()
        while GPIO.input(self.echo) == 0:
            pulse_start_time = time.time()
            if pulse_start - timeout_start > self.timeout:
                return -1
        while GPIO.input(self.echo) == 1:
            pulse_end_time = time.time()
            if pulse_start - timeout_start > self.timeout:
                return -1
        # Computes distance
        if pulse_start != 0 and pulse_end != 0:
            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 100 * 343.0 /2
            distance = int(distance)
        # print 'start = %s'%pulse_start,
        # print 'end = %s'%pulse_end
            if distance >= 0:
                return distance
            else:
                return -1
        else:
            # print 'start = %s'%pulse_start,
            # print 'end = %s'%pulse_end
            return -1

# Computes average distances
    def get_distance(self, mount = 10):
		sum = 0
		for i in range(mount):
			a = self.distance()
			#print '    %s' % a
			sum += a
		return int(sum/mount)

# Sets distance condtions for status
    def less_than(self, alarm_gate):
		dis = self.get_distance()
		status = 0
		if dis >= 5 and dis <= alarm_gate:
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

    UA = Ultrasonic_Avoidance(16, 20)
    threshold = 30
    while True:
        distance = UA.get_distance()
        status = UA.less_than(threshold)
        print(distance)
        print(status)
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
p1 = Process(target=server.serveforever)
p2 = Process(target=distanceLoop)
p2.start()
p1.start()
p1.join()
p2.join()
