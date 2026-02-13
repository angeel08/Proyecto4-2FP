#Ejercicio cuadrado de ANGEL BLAZQUEZ JIMENEZ

import turtle

class Cuadrado:
    def __init__(self,ancho, alto, color):
        self.ancho = ancho
        self.alto = alto
        self.color = color
        self.t = turtle.Turtle()
        self.t.color(self.color)
    
    def dibujar(self):
        for _ in range(2):
            self.t.forward(self.ancho)
            self.t.right(90)
            self.t.forward(self.alto)
            self.t.right(90)

    def mueve_inicio(self, d):
        self.t.penup()
        self.t.goto(d*10, -d*10) 
        self.t.pendown()

colores = ["red","green", "blue", "yellow", 
"orange", "purple", "pink", "brown","gray","cyan"]

for x in range(10):
    cuadrado = Cuadrado(100,100,colores[x])
    cuadrado.mueve_inicio(x)
    cuadrado.dibujar()

turtle.done()