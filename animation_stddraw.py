import stddraw as std

std.setXscale(-50.0, 50.0)
std.setYscale(-50.0, 50.0)
RADIUS = 0.9
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [0, 1, 2, 3, 4, 5, 6, 7, 8]
strength = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for i, j, k in zip(x, y, strength):
    max = 90
    increment = 10
    strength = k
    if strength >= max:
        std.setPenColor(std.DARK_RED)
    elif strength < max and strength >= (max - increment):
        std.setPenColor(std.RED)
    elif strength < (max - increment) and strength >= (max - (2*increment)):
        std.setPenColor(std.MAGENTA)
    elif strength < (max - (2*increment)) and strength >= (max - (3*increment)):
        std.setPenColor(std.PINK)
    elif strength < (max - (3*increment)) and strength >= (max - (4*increment)):
        std.setPenColor(std.VIOLET)
    elif strength < (max - (4*increment)) and strength >= (max - (5*increment)):
        std.setPenColor(std.BOOK_LIGHT_BLUE)
    elif strength < (max - (5*increment)) and strength >= (max - (6*increment)):
        std.setPenColor(std.BOOK_BLUE)
    elif strength < (max - (6*increment)) and strength >= (max - (7*increment)):
        std.setPenColor(std.BLUE)
    elif strength < (max - (7*increment)) and strength >= (max - (8*increment)):
        std.setPenColor(std.DARK_BLUE)
    elif strength < (max - (8*increment)):
        std.setPenColor(std.BLACK)
    else:
        print('data not in expected range', strength)

    std.filledCircle(i, j, RADIUS)
    std.show(500)

while True:
    pass
