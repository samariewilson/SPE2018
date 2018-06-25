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

import urllib2
import json

# Pass mac address, ssid and signal strength from located ap's to google maps api
def geo_locator(mac_ssid_list):
    gl_url = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyBISsgHLO4Uf6N3WbzGkOfdQrfK5kLWlpM"

    data = {}
    data["wifiAccessPoints"] = mac_ssid_list
    dataString = json.dumps(data)
    print dataString
    api_response = urllib2.urlopen(gl_url).read() # reads the html response from server
    latitude = re.compile('"lat" : (.+),').findall(api_response)[0]
    longitude = re.compile('"lng" : (.+)').findall(api_response)[0]
    accuracy = re.compile('"accuracy" : (.+),').findall(api_response)[0]
    print '\nYour Location (as per google maps api):'
    print 'Latitude: ' + latitude
    print 'Longitude: ' + longitude
    print 'Accuracy: Within ' + accuracy + ' mts'

geo_locator(mac_ssid_list)
