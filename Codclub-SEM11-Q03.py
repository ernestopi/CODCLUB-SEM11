# desenhando formas aleatórias

from turtle import *
from random import *

def mover():
    penup()
    setpos(randint(-400, 400), randint(-400, 400))
    pendown()

def triangulo(tamanho, cor):
    color(cor)
    pendown()
    begin_fill()
    for side in range(3):
        left(120)
        forward(tamanho)
    end_fill()
    penup()

def quadrado(tamanho, cor):
    color(cor)
    pendown()
    begin_fill()
    for side in range(4):
        left(90)
        forward(tamanho)
    end_fill()
    penup()

bgcolor('MidnightBlue')

for star in range(30):
    mover()
    triangulo(randint(5,25), 'White')
    forward(randint(-400, 400))
    quadrado(randint(5, 25), 'Red')

hideturtle()
done()