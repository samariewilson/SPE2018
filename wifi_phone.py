from sys import exit
import logging
import iwlist

content = iwlist.scan(interface='wlan0')
cells = iwlist.parse(content)
signal = 0

for i in cells:

    if i["essid"] == "Catherine\xE2\x80\x99s iPhone":

        mac = i["mac"]
        signal = i["signal_level_dBm"]
        age = 0
        break

print signal
