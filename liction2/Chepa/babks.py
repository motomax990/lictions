import turtle
from math import sin, cos, pi, radians
R = int(turtle.textinput("Введите радиус: ", "Введите радиус: "))

turtle.left(90)
for i in range(10):
    turtle.circle((R*i))
    turtle.circle(-(R*i))
    
