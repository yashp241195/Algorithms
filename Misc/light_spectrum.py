from graphics import *

win = GraphWin(" Color ", 1000, 1000)


def in_range(wavelength, x_min, x_max):
    if wavelength >= x_min:
        if wavelength <= x_max:
            return True

    return False


xt = 100
yt = 10

max_Intensity = 255

for j in range(380, 780):

    WL = j
    R = G = B = 1
    R1 = G1 = B1 = 1

    if in_range(WL, 380, 440):

        R = float(-(380 - 440) / (440 - 380))
        R1 = float(-(WL - 440) / (440 - 380))
        G = G1 = 0
        B = B1 = 1

    elif in_range(WL, 440, 490):

        R = R1 = 0
        G = float((440 - 440) / (490 - 440))
        G1 = float((WL - 440) / (490 - 440))
        B = B1 = 1

    elif in_range(WL, 490, 510):

        R = R1 = 0
        G = G1 = 1
        B = float(-(490 - 510) / (510 - 490))
        B1 = float(-(WL - 510) / (510 - 490))

    elif in_range(WL, 510, 580):

        R = float((510 - 510) / (580 - 510))
        R1 = float((WL - 510) / (580 - 510))
        G = G1 = 1
        B = B1 = 0

    elif in_range(WL, 580, 645):

        R = R1 = 1
        G = float(-(580 - 645) / (645 - 580))
        G1 = float(-(WL - 645) / (645 - 580))
        B = B1 = 0

    elif in_range(WL, 645, 780):

        R = R1 = 1
        G = G1 = 0
        B = B1 = 0

    else:

        R = R1 = 0
        G = G1 = 0
        B = B1 = 0

    R *= max_Intensity
    G *= max_Intensity
    B *= max_Intensity

    R1 *= max_Intensity
    G1 *= max_Intensity
    B1 *= max_Intensity

    rect = Rectangle(Point(xt, yt), Point(xt, yt + 100))
    rect2 = Rectangle(Point(xt, yt + 110), Point(xt, yt + 200))
    rect3 = Rectangle(Point(xt, yt + 210), Point(xt, yt + 310))
    rect4 = Rectangle(Point(xt, yt + 320), Point(xt, yt + 420))
    rect5 = Rectangle(Point(xt, yt + 440), Point(xt, yt + 540))

    rect.setOutline(color_rgb(int(R), int(G / max_Intensity), int(B / max_Intensity)))
    rect2.setOutline(color_rgb(int(R / max_Intensity), int(G), int(B / max_Intensity)))
    rect3.setOutline(color_rgb(int(R / max_Intensity), int(G / max_Intensity), int(B)))
    rect4.setOutline(color_rgb(int(R), int(G), int(B)))
    rect5.setOutline(color_rgb(int(R1), int(G1), int(B1)))

    # print(R1,G1,B1)

    rect.draw(win)
    rect2.draw(win)
    rect3.draw(win)
    rect4.draw(win)
    rect5.draw(win)

    xt += 1


win.getMouse()
win.close()
