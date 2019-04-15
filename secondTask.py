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


def main():
    y_count = math.fabs(p) * 10
    draw_directrix(y_count)



if __name__ == "__main__":
    global a
    global b
    global c
    global d
    global p
    print("введите 4 числа:")
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
