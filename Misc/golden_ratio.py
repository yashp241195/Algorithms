from graphics import *

win = GraphWin(" Fibonacci - Golden Ratio ", 1000, 1000)

num = 16


def fib(n):

    first = 0
    second = 1
    third = 0

    for i in range(2, n+1):

        third = first + second

        first = second

        second = third

    return third


x_cord = [0]*(num + 4)

y_cord = [0]*(num + 4)

print(0, 0)

x_cord[1] = 1

y_cord[1] = 0

print(1, 0)

x = 2

y = 1

x_cord[2] = 2

y_cord[2] = 1

print(x, y)



k = 0



while k <= num:



    const = fib(k+3)



    rem = k % 4



    if rem == 0:

        x -= const

        y += const

    elif rem == 1:

        x -= const

        y -= const

    elif rem == 2:

        x += const

        y -= const

    elif rem == 3:

        x += const

        y += const



    x_cord[k + 3] = x
    y_cord[k + 3] = y



    print(x, y)

    k += 1



print("x : ", x_cord)
print("y : ", y_cord)



message = Text(Point(570, 20), " Golden Ratio and Fibonacci Sequence")

message.draw(win)

message = Text(Point(570, 40), "Golden Ratio = (a+b)/a = a/b = phi =  1.6180339887... ")

message.draw(win)



transX = 500

transY = 250

screenY = screenX = 13

for i in range(len(x_cord)):

    x_cord[i] /= screenX

    y_cord[i] /= screenY

    x_cord[i] += transX

    y_cord[i] += transY





def bezierItr(x, y):

    u = 0

    while u < 1:

        U = u

        V = 1 - u



        x1 = x[0] * U * U
        y1 = y[0] * U * U

        x2 = 2 * x[1] * U * V
        y2 = 2 * y[1] * U * V

        x3 = x[2] * V * V
        y3 = y[2] * V * V

        xt = x1 + x2 + x3
        yt = y1 + y2 + y3

        pt = Point(xt, yt)
        pt.setFill("green")

        pt.draw(win)

        if abs(x[2]-x[0]) < 2:
            u += 1
        else:
            u += 0.005  # change Accuracy here


for i in range(len(x_cord)-1):

    x1 = x_cord[i]
    y1 = y_cord[i]

    x2 = x_cord[i+1]
    y2 = y_cord[i+1]

    pt1 = Point(x1, y1)
    pt2 = Point(x2, y2)

    pt3 = Point(x1, y2)
    pt4 = Point(x2, y1)

    line = Line(pt1, pt2)
    rect = Rectangle(pt1, pt2)

    line.draw(win)
    rect.draw(win)

    x = [x1, x2, x2]
    y = [y1, y1, y2]
    bezierItr(x, y)
    x = [x1, x1, x2]
    y = [y1, y2, y2]
    bezierItr(x, y)

win.getMouse()
win.close()
