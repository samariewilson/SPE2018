proc = open('/proc/net/wireless', 'rb')
proc.readline()
proc.readline()
data = proc.readline()
newData = data.split()
print newData
