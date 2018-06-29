import numpy
import matplotlib
import time
import keyboard

def update_distance():
    seconds = 0
    while keyboard.is_pressed(38):
        stopwatch.reset()
        stopwatch.start()
    seconds = stopwatch.read()
    return seconds

if __name__ == '__main__':
    print (update_distance())
