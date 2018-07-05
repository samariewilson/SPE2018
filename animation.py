import matplotlib.pyplot as plt
import numpy as np
from threeFunctions import update_x
from threeFunctions import update_y

plt.ion()
fig, ax = plt.subplots()
x, y = [0],[0]
sc = ax.scatter(x,y)
plt.xlim(-10,10)
plt.ylim(-10,10)

plt.draw()
for i in range(1000):
    update_x(x)
    update_y(y)
    sc.set_offsets(np.c_[x,y])
    fig.canvas.draw_idle()
    plt.pause(0.1)

plt.waitforbuttonpress()
