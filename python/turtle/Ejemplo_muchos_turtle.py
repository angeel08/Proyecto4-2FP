import turtle

class Rectangulo:
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
        self.t.goto(d*5, -d*5)
        self.t.pendown()


colores = ["red","green", "blue", "yellow", "orange", "purple", "pink", "brown","gray","cyan","red","green", "blue", "yellow", "orange", "purple", "pink", "brown","gray","cyan"]

for i in range(10000):
    rectangulo = Rectangulo(100,50,colores[i])
    rectangulo.mueve_inicio(i)
    rectangulo.dibujar()

turtle.done()