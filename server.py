from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import threading
import sys

port = 9876

class SimpleEcho(WebSocket):

    def handleMessage(self):
        print(self.data)
        if self.data == "up":
            bw.speed = forward_speed
            bw.backward()
            straight_turn()
        elif self.data == "down":
            bw.speed = forward_speed
            bw.forward()
            straight_turn()
        elif self.data == "right":
            right_turn()
            bw.speed = forward_speed
        elif self.data == "left":
            left_turn()
            bw.speed = forward_speed
        elif self.data == "straight":
            straight_turn()
        else:
            stop()


    def stop():
        bw.stop()

    def left_turn():
    	fw.turn(82)

    def straight_turn():
        fw.turn(102)
    def right_turn():
    	fw.turn(12)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')


class serverThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.server = SimpleWebSocketServer('', port, SimpleEcho)
    def run(self):
        self.server.serveforever()
class distanceThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            pass
            #test distance

st = serverThread()
ht = distanceThread()

st.start()
ht.start()
