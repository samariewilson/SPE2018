from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np
from where_am_i import update_x
from where_am_i import update_y
from where_am_i import southwest
from colors import colors
from colors import get_strength

port = 1234

class SimpleEcho(WebSocket):
    def handleMessage(self):
        threeList = json.loads(self.data)
        print threeList

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

plt.ion()
fig, ax = plt.subplots()
x, y, strength = [0],[0],[10, 20, 30, 40, 50, 60, 70, 80]

sc = ax.scatter(x,y, c = colors(get_strength()))
plt.xlim(-10,10)
plt.ylim(-10,10)

plt.draw()

for i in range(1000):
    update_x(x)
    update_y(y)
    get_strength()
    sc.set_offsets(np.c_[x,y])
    fig.canvas.draw_idle()
    plt.pause(0.1)

plt.waitforbuttonpress()
