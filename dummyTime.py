import time
import random
from itertools import groupby
from multiprocessing import Process, Value, Array, Manager

global master_array
global times
global i

manager = Manager()

master_array = manager.list(['s','s'])

# master_array = Array('c',10000)

 #master_array.append('s')

times = manager.list([0,0])

#times.append(0.0)
#times.append(0.0)

i = -1


def left_turn():
    master_array.append('l')
    start = time.time()
    # real function code
    times.append(start)


def right_turn():
    master_array.append('r')
    start = time.time()
    # real function code
    times.append(start)


def straight():
    master_array.append('f')
    start = time.time()
    # real function code
    times.append(start)


def backward():
    master_array.append('b')
    start = time.time()
    # real function code
    times.append(start)


def stop():
    master_array.append('s')
    start = time.time()
    # real function code
    times.append(start)

def control(master_array, times):
    while True:
        if master_array[-1] == master_array[-2] and len(master_array) <= 3 :
            pass

        else:
             sort = [(k, sum(1 for i in g)) for k,g in groupby(master_array)]
             dir, rep = zip(*sort)
             print rep

             difference = times[rep[1] + 1] - times[2]
             temp = [dir[1],difference]
             if (difference == 0):
                difference = times[3] - times[2]
                temp = [dir[1],difference]
                master_array.remove[2]
                times.remove[2]
             master_array.remove[2:rep[1] + 2]
             times.remove[2:rep[1] + 2]

             # socket.sendMessage...(temp)
             print (temp)
             print master_array
        time.sleep(1)

def actions(master_array, times):
    a = [left_turn, right_turn, straight, backward, stop]
    while True:
        a[random.randint(0,len(a)-1)]()
        print master_array
        time.sleep(0.1)

p1 = Process(target = control, args = (master_array, times))
p2 = Process(target = actions, args = (master_array, times))
p2.start()
p1.start()
p1.join()
p2.join()
