from sys import exit
import logging
import iwlist
import time

def strength():
    content = iwlist.scan(interface='wlan0')
    cells = iwlist.parse(content)
    signal = 0


    for i in cells:

        if i["essid"].startswith("Catherine"):

            mac = i["mac"]
            signal = i["signal_level_dBm"]
            age = 0
            break
    return signal
    #time.sleep (2)
#while True:
    #print strength()
