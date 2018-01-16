from graphics import *

win = GraphWin(" Color ", 1000, 1000)


def in_range(wavelength, x_min, x_max):
    if wavelength >= x_min:
        if wavelength <= x_max:
            return True

    return False


xt = 100
yt = 100

max_Intensity = 255

for j in range(380, 780):
    WL = j
    R = G = B = 1

    if in_range(WL, 380, 440):
        R = float(-(WL - 440) / (440 - 380))
        G = 0
        B = 1
    elif in_range(WL, 440, 490):
        R = 0
        G = float((WL - 440) / (490 - 440))
        B = 1
    elif in_range(WL, 490, 510):
        R = 0
        G = 1
        B = float(-(WL - 510) / (510 - 490))
    elif in_range(WL, 510, 580):
        R = float((WL - 510) / (580 - 510))
        G = 1
        B = 0
    elif in_range(WL, 580, 645):
        R = 1
        G = float(-(WL - 645) / (645 - 580))
        B = 0
    elif in_range(WL, 645, 780):
        R = 1
        G = 0
        B = 0
    else:
        R = 0
        G = 0
        B = 0

    R *= max_Intensity
    G *= max_Intensity
    B *= max_Intensity

    print(R, G, B)
    pt = Point(xt, yt)

    pt2 = Point(xt+1, yt+100)
    rect = Rectangle(pt, pt2)
    rect.setOutline(color_rgb(int(R),int(G),int(B)))
    rect.draw(win)
    xt += 1


win.getMouse()
win.close()
