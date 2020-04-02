import turtle
from math import sin, cos, pi, radians



R = int(turtle.textinput("Введите радиус: ", "Введите радиус: "))
n = int(turtle.textinput("Введите растояние между спиралями: ", "Ввелите растояние между спиралями: "))

x0 = int(turtle.textinput("Введите x чепы: ", "Ввелите x чепы: "))
y0 = int(turtle.textinput("Введите y чепы: ", "Ввелите y чепы: "))

def flower():
    c = int(turtle.textinput("Введите y чепы: ", "Ввелите кол-во кругов: "))
    for i in range(c):
        turtle.circle(R)
        turtle.left(360/c)
flower()
