import time
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
        if master_array[i] == master_array[i-1] and len(master_array) < 3:
            pass

        else:
             sort = [(k, sum(1 for i in g)) for k,g in groupby(master_array)]
             dir, rep = zip(*sort)
             repeats = rep[1]
             difference = times[reapeats-1] - times[2]
             temp[dir[1],difference]
             # socket.sendMessage...(temp)
             print (temp)

def actions(master_array, times):
    left_turn()
    left_turn()
    left_turn()
    left_turn()
    left_turn()
    straight()
    straight()
    straight()
    straight()
    straight()
    straight()
    left_turn()
    left_turn()
    backward()
    backward()
    right_turn()
    stop()

p1 = Process(target = control, args = (master_array, times))
p2 = Process(target = actions, args = (master_array, times))
p2.start()
p1.start()
p1.join()
p2.join()
