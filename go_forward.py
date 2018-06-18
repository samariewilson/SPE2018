from picar import back_wheels
import picar

picar.setup()

bw = back_wheels.Back_Wheels(db='config')
forward_speed = 100

def start_follower():

	while True:

		print "start_follow"
		bw.speed = forward_speed

def stop():
	bw.stop()
	#fw.turn_straight()

if __name__ == '__main__':
	try:
		start_follower()
	except KeyboardInterrupt:
		stop()
