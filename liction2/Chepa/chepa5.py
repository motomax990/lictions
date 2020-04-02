import turtle



lenghtSpir = int(input('Введите длинну спирали: '))
turtle.shape('turtle')
turtle.color('red') 

for i in range(lenghtSpir):
    turtle.forward(i * 1)
    turtle.left(20)
    
input()
 
