 
from turtle import *
startLength = int(input("Ввелите длинну стороны: "))
decrement = int(input("Введмте сколько вычитать: "))
while startLength > decrement:
    forward(startLength)
    left(90)
    startLength = startLength - decrement
forward(startLength)

input()
