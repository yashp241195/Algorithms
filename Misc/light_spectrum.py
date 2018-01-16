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

    rect = Rectangle(Point(xt, yt), Point(xt, yt + 100))
    rect2 = Rectangle(Point(xt, yt + 110), Point(xt, yt + 200))
    rect3 = Rectangle(Point(xt, yt + 210), Point(xt, yt + 310))
    rect4 = Rectangle(Point(xt, yt + 320), Point(xt, yt + 420))

    rect.setOutline(color_rgb(int(R), int(G / max_Intensity), int(B / max_Intensity)))
    rect2.setOutline(color_rgb(int(R / max_Intensity), int(G), int(B / max_Intensity)))
    rect3.setOutline(color_rgb(int(R / max_Intensity), int(G / max_Intensity), int(B)))
    rect4.setOutline(color_rgb(int(R), int(G), int(B)))

    rect.draw(win)
    rect2.draw(win)
    rect3.draw(win)
    rect4.draw(win)

    xt += 2


win.getMouse()
win.close()
