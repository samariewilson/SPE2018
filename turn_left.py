from picar import back_wheels
from picar import front_wheels
import picar


picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

def start_follower():

    while True:

		# if turn left key was pressed
        if c == curses.KEY_LEFT:
            fw.left_turn()
        else:
            bw.speed = forward_speed
            print("test3")

def stop():
    bw.stop()

def left_turn():
	fw.turn_left()


if __name__ == '__main__':
	try:
		left_turn()
	except KeyboardInterrupt:
		stop()
