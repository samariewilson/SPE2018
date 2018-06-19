from picar import back_wheels
from picar import front_wheels
import picar
import pygame

picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')

forward_speed = 100

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_turn()
            if event.key == pygame.K_q:
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
