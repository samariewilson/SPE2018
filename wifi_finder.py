from sys import exit
import logging
import iwlist

content = iwlist.scan(interface='wlan0')
cells = iwlist.parse(content)
mac_ssid_list = []

for i in cells:
    mac = i["mac"]
    signal = i["signal_level_dBm"]
    age = 0
    mac_ssid_list.append({"macAddress": mac, "signalStrength": signal, "age": 0})

print mac_ssid_list
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBISsgHLO4Uf6N3WbzGkOfdQrfK5kLWlpM')
location = gmaps.geolocate(wifi_access_points=mac_ssid_list)

print location
