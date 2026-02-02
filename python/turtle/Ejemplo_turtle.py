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

Rectangulo = Rectangulo(100,50, "red")
Rectangulo.dibujar()


turtle.done()