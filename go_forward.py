from picar import back_wheels
from picar import front_wheels
import picar


from curses import wrapper

curses.initscr()

curses.wrapper(stop)
curses.wrapper(left_turn)
curses.wrapper(start_follower)
picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')


def start_follower():
    stdscr.nodelay(True)
    stdscr.clear()

    while True:
        c = stdscr.getch()
        curses.flushinp()
        print("start_follow")

		# if turn left key was pressed
        if c == curses.KEY_LEFT:
            fw.left_turn()
        else:
            bw.speed = forward_speed
            print("test3")



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
