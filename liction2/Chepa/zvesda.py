#!/usr/bin/python3
# -*- coding: utf-8 -*-

import turtle as t
from math import sin, cos, pi, radians 



def main():
    stars(int(t.textinput("Введите кол-во вершин: ", "Введите кол-во вершин: ")))
    t.exitonclick()

    return 0

def stars(n):
    a=180/n
    l=180-a
    forward = int(t.textinput("Введите кол-во вершин: ", "Введите длинну шага: "))
    for i in range(n + 1):
        t.lt(l)
        t.forward(forward)
    
    return 0


def rotatar():
    if t.heading() > 180:
        t.left(360 - t.heading())
    else:    
        t.right(t.heading())


if __name__ == '__main__':
    main()
