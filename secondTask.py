from tkinter import *
import math


def main(a, b, c, d):
    pass


if __name__ == "__main__":
    print("введите 2 числа:")
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    root = Tk()
    canvas = Canvas(root, width=500, height=500, bg='white')
    canvas.pack()
    main(a, b, c, d)
    root.mainloop()