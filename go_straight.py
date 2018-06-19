from picar import back_wheels
from picar import front_wheels
import picar


picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

def start_follower():

    while True:

		# if up key was pressed
        if c == curses.KEY_UP:
            fw.no_turn()
        else:
            bw.speed = forward_speed
            print("test3")

def stop():
    bw.stop()

def no_turn():
	fw.turn_straight()


if __name__ == '__main__':
	try:
		no_turn()
	except KeyboardInterrupt:
		stop()
