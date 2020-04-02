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
    turtle.penup()
    for l in range(c+1):
        
        a = 360/c
        rd = pi/180*a
        #shift = (a*n)/360S
        x = cos(rd)*(r) + x0
        y = sin(rd)*(r) + y0
        turtle.goto(x,y)
        turtle.pendown()
        #print(a,x,y)    
        time.sleep(0.005)
k = 0

for i in range(3,int(turtle.textinput("Введите кол-во вершин: ", "Введите кол-во вершин: "))):
    
    c = i
    turtle.write(c)
    turtle.penup()
    #turtle.goto((R + (n * k))+x0,(R + (n * k))+y0)
    circlMy1(R + (n * k), c, n)
    #circlMy1(R, c, n)
    turtle.left(90)
    turtle.penup()
    turtle.forward(n)
    turtle.right(90)
    k += 1



turtle.penup()
   
turtle.exitonclick()        

 
