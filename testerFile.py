import time
direction = 0
difference = 0
strength = 0




with open('text.txt', 'r+') as f:
    direction = f.readline()
    difference = f.readline()
    strength = f.readline()

    f.seek(0)
    f.write("0")
    f.write("\n")
    f.write("0")
    f.write("\n")
    f.write("0")
    f.truncate()

print direction, difference, strength
