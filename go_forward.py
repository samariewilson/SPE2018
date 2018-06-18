from picar import back_wheels
from picar import front_wheels
import picar
import time
import keyboard

picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

def start_follower():

	while True:

		print "start_follow"

		try:

        #if turn left key was pressed
			if keyboard.is_pressed('q'):

				left_turn()
				print("test2")

			else:
				bw.speed = forward_speed
				print("test3")
		except KeyboardInterrupt:
			stop()
def stop():
	bw.stop()
	#fw.turn_straight()

def left_turn():
	fw.turn_left()
	print("test1")

if __name__ == '__main__':
	try:
		start_follower()
	except KeyboardInterrupt:
		stop()
