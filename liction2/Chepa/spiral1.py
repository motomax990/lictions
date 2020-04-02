import turtle
from math import sin, cos, pi, radians
import time




R = int(turtle.textinput("Введите радиус: ", "Ввелите радиус: "))
n = int(turtle.textinput("Введите растояние между спиралями: ", "Ввелите растояние между спиралями: "))

x0 = int(turtle.textinput("Введите x чепы: ", "Ввелите x чепы: "))
y0 = int(turtle.textinput("Введите y чепы: ", "Ввелите y чепы: "))
turtle.color('red')
turtle.penup()
turtle.goto(x0 + R, y0)
turtle.pendown()


def circlMy1(r, a, n):
    shift = n/360
    #shift = 1
    print(shift)
    for c in range(0,361, a):
        rd = pi/180*a
        turtle.left(a)
        turtle.speed(100)   
        turtle.forward(sin(rd)* (r + shift * c))
        #turtle.right(90)
        #turtle.forward(shift)
        #turtle.left(90)
        
        
        
a = 1
for i in range(int(turtle.textinput("Введите колво петлей: ", "Введите колво петлей: "))):
    circlMy1(R + (n * i), a, n)

turtle.penup()
turtle.goto(x0 + (-R), y0)
turtle.pendown()

#turtle.circle(100)


turtle.exitonclick()        
