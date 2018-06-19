from picar import back_wheels
from picar import front_wheels
import picar
import curses

screen = curses.initscr()
#screen.addstr("Hello World!")
screen.refresh()


#screen.addstr(str(c))



picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

forward_speed = 100

def start_follower():
    while True:
        c = screen.getch()
        screen.addstr(str(c))
        if  c == 113:
            stop()
            curses.endwin()
            exit()
        elif c == 97:
            left_turn()
            bw.speed = forward_speed
        elif c == 100:
            right_turn()
            bw.speed = forward_speed
        elif c  == 119:
            bw.speed = forward_speed
            bw.backward()
            straight_turn()
        elif  c == 115:
            bw.speed = forward_speed
            bw.forward()
            straight_turn()
        else:
			stop()

def stop():
    bw.stop()

def left_turn():
	fw.turn(80)

def straight_turn():
    fw.turn(100)
def right_turn():
	fw.turn(120)

if __name__ == '__main__':
	try:
		start_follower()
	except KeyboardInterrupt:
		stop()
