from sys import exit
import logging
import iwlist

content = iwlist.scan(interface='wlan0')
cells = iwlist.parse(content)
mac_ssid_list = []
for i in cells:
    mac = i.mac
    ssid = i.essid
    signal = i.db
    mac_ssid_list.append((mac, ssid, signal))
import urllib2

# Pass mac address, ssid and signal strength from located ap's to google maps api
def geo_locator():
    gl_url = 'https://maps.googleapis.com/maps/api/browserlocation/json?browser=firefox&sensor=true'
    for (mac, ssid, sig) in mac_ssid_list:
        gl_url += "&wifi=mac:%s%%7Cssid:%s%%7Css:%s" % (mac.replace(":", "-"), ssid.replace(" ", "%20"), sig)
    api_response = urllib2.urlopen(gl_url).read() # reads the html response from server
    latitude = re.compile('"lat" : (.+),').findall(api_response)[0]
    longitude = re.compile('"lng" : (.+)').findall(api_response)[0]
    accuracy = re.compile('"accuracy" : (.+),').findall(api_response)[0]
    print '\nYour Location (as per google maps api):'
    print 'Latitude: ' + latitude
    print 'Longitude: ' + longitude
    print 'Accuracy: Within ' + accuracy + ' mts'
