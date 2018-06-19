from picar import back_wheels
from picar import front_wheels
import picar
import sys

picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

forward_speed = 100

def start_follower():
	print ("start Follower")
	for line in sys.stdin:
		print("test1")
		c = line[0]
		print (c)
		print line

		if  c == 'q':
			stop()
			exit()
		if c =='a':
		 	left_turn()
		if c == 'd':
			right_turn()
		if c  == 's':
			bw.speed = forward_speed
			bw.backward()
		elif  c == 'w':
			bw.speed = forward_speed
			bw.forward()
		else:
			stop()

def stop():
    bw.stop()

def left_turn():
	fw.turn_left()

def right_turn():
	fw.turn_right()

if __name__ == '__main__':
	try:
		start_follower()
	except KeyboardInterrupt:
		stop()
