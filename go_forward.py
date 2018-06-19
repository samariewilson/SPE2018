from picar import back_wheels
from picar import front_wheels
import picar
import keyboard

picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

forward_speed = 100

def start_follower():

    while True:
		if keyboard.is_pressed('q'):
			stop()
			exit()
		if keyboard.is_pressed('a'):
		 	left_turn()
		if keyboard.is_pressed('d'):
			right_turn()
		if keyboard.is_pressed('s'):
			bw.speed = forward_speed
			bw.backward()
		elif keyboard.is_press('w'):
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
