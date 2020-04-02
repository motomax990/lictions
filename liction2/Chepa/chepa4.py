import turtle



turtle.shape('turtle')
turtle.color('orange') 
n = int(input('Введите кол-во палок: '))
lenght = int(input('Введите длинну палок: '))
turtle.width(int(input('Введите ширину палок: ')))

grad = 360/n
for i in range(n):
    turtle.forward(lenght)
    turtle.stamp()
    turtle.backward(lenght)
    turtle.left(grad)
    
input()
