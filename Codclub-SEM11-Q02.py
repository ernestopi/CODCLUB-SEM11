from turtle import *

def planeta(tamanho, cor):
    color(cor)
    pendown()
    begin_fill()
    for side in range(4):
        left(90)
        forward(tamanho)
    end_fill()
    penup()

bgcolor('MidnightBlue')

planeta(50, 'Red')
forward(150)
planeta(30, 'White')
left(120)
forward(350)
planeta(70, 'Green')

hideturtle()
done()