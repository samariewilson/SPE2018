from picar import back_wheels
from picar import front_wheels
from multiprocessing import Process

import picar
import curses


import time
import RPi.GPIO as GPIO

screen = curses.initscr()
#screen.addstr("Hello World!")
screen.refresh()

picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

forward_speed = 100

def loop_a():
    distance = UA.get_distance()
    print (distance)
    print ("test1")
    status = UA.less_than(threshold)
    print (status)
    print ("test2")

    if distance != -1:
        print 'distance', distance, 'cm'
        time.sleep(0.2)
    else:
        print False
        bw.stop()

def loop_b():
    if distance == -1:
        print('YIKES')
        bw.stop()
    if distance != -1:
        print('YAY')
        bw.speed = forward_speed
        bw.backward()
        fw.turn(102)

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

''' if __name__ == '__main__':
    UA = Ultrasonic_Avoidance(17)
    threshold = 10
    while True:


        c = screen.getch()
        screen.addstr(str(c))

        if c == 119:
            distance = UA.get_distance()
            print (distance)
            print ("test1")
            status = UA.less_than(threshold)
            print (status)
            print ("test2")
            bw.speed = forward_speed
            bw.backward()
            fw.turn(102)
            print("test3")

            if distance != -1:
                print 'distance', distance, 'cm'
                bw.speed = forward_speed
                bw.backward()
                fw.turn(102)
                time.sleep(0.2)
            else:
                print False
                bw.stop()

        elif  c == 113:
            bw.stop()
            curses.endwin()
            exit()



        print (distance)
        print (status)

        if distance != -1:
            print 'distance', distance, 'cm'
            bw.speed = forward_speed
            bw.backward()
            fw.turn(102)
            time.sleep(0.2)
        else:
            print False
            bw.stop()
        if status == 1:
            print "Less than %d" % threshold
            bw.speed = forward_speed
            bw.forward()
        elif status == 0:
            print "Over %d" % threshold
            bw.stop()
        else:
			print "Read distance error."
            '''

if __name__ == '__main__':
    UA = Ultrasonic_Avoidance(17)
    threshold = 10
    Process(target=loop_a).start()
    Process(target=loop_b).start()
