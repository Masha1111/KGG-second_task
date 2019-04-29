from tkinter import *
import math


def draw_directrix(count):
    directrix_coord = b - p / 2
    scale = 800 / count
    yy = scale * math.fabs(directrix_coord)
    if directrix_coord < 0:
        canvas.create_line(0, 400 + yy, 800, 400 + yy, fill="green")
    if directrix_coord > 0:
        canvas.create_line(0, 400 - yy, 800, 400 - yy, fill="green")
    if directrix_coord == 0:
        canvas.create_line(0, 400, 800, 400, fill="green", arrow=LAST)


def draw_symmetrical(xx, yy):
    canvas.create_line(xx, yy, xx + 1, yy, fill="red")
    canvas.create_line(xx, yy, xx, yy + 1, fill="red")


# реализация алгоритма
def brezenham(count, xx_0, yy_0):
    xx = xx_0
    yy = yy_0
    delta = (xx - d)**2 + (yy - b - (c**2)/(4 * a))**2 - (yy - b + (c**2)/(4 * a))**2
    while 0 < yy < 800:
        # draw_symmetrical(xx, yy)
        #canvas.create_line(xx, yy, xx, yy+1, fill="red")
        canvas.create_line(xx, yy, xx + 1, yy + 1, fill="red")
        if delta < 0:
            # D or C
            xx += 1
            delta += 2 * xx - 2 * d + 1
            if delta + 2 * p > delta:
                yy += 1
                delta -= 2 * p
        if delta > 0:
            # B or C
            yy += 1
            delta -= 2 * p
            if delta - 2 * xx + 2 * d - 1 > delta:
                xx += 1
                delta += 2 * xx - 2 * d + 1



def main():
    # вычисление масштаба (кол-во y)
    y_count = math.fabs(p) * 100
    draw_directrix(y_count)
    yy_b = 0
    x_pixel = d * (800 / y_count)
    if b < 0:
        yy_b = 400 + (800 / y_count) * math.fabs(b)
    if b > 0:
        yy_b = 400 - (800 / y_count) * math.fabs(b)
    brezenham(y_count, x_pixel, yy_b)


if __name__ == "__main__":
    global a
    global b
    global c
    global d
    global p
    print("y = at^2 + b\nx = ct + d\nвведите 4 числа:")
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if (a != 0):
        p = (c * c)/(2 * a)
    else:
        print("это не парабола")
    root = Tk()
    canvas = Canvas(root, width=1000, height=800, bg='white')
    canvas.create_line(0, 400, 800, 400, fill="black", arrow=LAST)
    canvas.create_line(400, 800, 400, 0, fill="black", arrow=LAST)
    canvas.pack()
    main()
    root.mainloop()

