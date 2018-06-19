from picar import back_wheels
from picar import front_wheels
import picar
import keyboard

picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')


def start_follower():

    while True:
        print("start_follow")
		# if turn left key was pressed
        if keyboard.is_pressed('l'):
            left_turn()
		elif keyboard.is_pressed('q'):
			stop()
        else:
            bw.speed = forward_speed

def stop():
    bw.stop()
	#fw.turn_straight()

def left_turn():
	fw.turn_left()

if __name__ == '__main__':
	try:
		start_follower()
	except KeyboardInterrupt:
		stop()
