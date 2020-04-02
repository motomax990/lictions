import turtle
from math import sin, cos, pi, radians
import time




R = int(turtle.textinput("Ввелите радиус: ", "Ввелите радиус: "))
n = int(turtle.textinput("Ввелите растояние между спиралями: ", "Ввелите растояние между спиралями: "))

x0 = int(turtle.textinput("Ввелите x чепы: ", "Ввелите x чепы: "))
y0 = int(turtle.textinput("Ввелите y чепы: ", "Ввелите y чепы: "))
turtle.color('red')
turtle.penup()
turtle.goto(x0 + R, y0)



def circlMy(r, a):
    for c in range(361):
        #m = n/360
        #shift = a*m+r
        rd = pi/180*a
        turtle.left(a)
        print(a)
        turtle.pendown()
        turtle.forward(sin(rd)*r)    
    

    

a = 1
circlMy(R, a)

    
    
input()     
