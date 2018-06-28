from picar import back_wheels
from picar import front_wheels
import picar

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
fw.turn(102)
bw.stop()
