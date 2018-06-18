from picar import back_wheels
import picar

picar.setup()

bw = back_wheels.Back_Wheels(db='config')
forward_speed = 90

def start_follower():
	print "start_follow"
	bw.speed = forward_speed

start_follower()
