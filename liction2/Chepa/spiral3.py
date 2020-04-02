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

def circlMy1(r,c, n):
    for a in range(0, 361, c):
        rd = pi/180*a
        shift = (a*n)/360
        x = cos(rd)*(r + shift) + x0
        y = sin(rd)*(r+ shift) + y0
        turtle.pendown()
        turtle.goto(x,y)
        #print(a,x,y)    
        time.sleep(0.005)
c = 45
for i in range(int(turtle.textinput("Введите колво петлей: ", "Введите колво петлей: "))):
    circlMy1(R + (n * i), c, n)


turtle.penup()
   
turtle.exitonclick()        

