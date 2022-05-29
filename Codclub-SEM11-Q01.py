#criando uma função para criar formas
from turtle import *
def drawstar():
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(50)
    end_fill()
    penup()

def desenha_quadrado():
    pendown()
    begin_fill()
    for side in range(4):
        left(90)
        forward(100)
    end_fill()
    penup()

color('WhiteSmoke')
bgcolor('MidnightBlue')

desenha_quadrado()
forward(150)
desenha_quadrado()
left(120)
forward(350)
desenha_quadrado()

hideturtle()
done()