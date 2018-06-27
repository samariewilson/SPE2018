import time

while(True):

    proc = open('/proc/net/wireless', 'rb')
    proc.readline()
    proc.readline()
    data = proc.readline()
    proc.close()
    newData = data.split()
    signal = float(newData[3])
    print signal
    time.sleep(1)
