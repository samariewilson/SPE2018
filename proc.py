proc = open('/proc/net/wireless', 'rb')
proc.readline()
proc.readline()
data = proc.readline()

print data
