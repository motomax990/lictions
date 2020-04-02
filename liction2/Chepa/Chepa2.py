import turtle
from math import sin, cos, pi, radians
import time



turtle.color('red')

r = int(input("Ввелите радиус: "))
x0 = int(input("Ввелите x чепы: "))
y0 = int(input("Ввелите y чепы: "))
turtle.penup()
turtle.goto(x0 + r, y0)


for a in range(361):
    rd = pi/180*a
    x = cos(rd)*r + x0
    y = sin(rd)*r + y0
    turtle.pendown()
    turtle.goto(x,y)
    #print(a,x,y)    
    time.sleep(0.005)
turtle.penup()
turtle.back(r)
    
    
input()    
