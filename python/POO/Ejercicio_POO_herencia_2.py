class animal:
    def comer(self):
        print("ÑAMM")

class perro(animal):
    def ladrar(self):
        print("GUAO")

class gato(animal):
    def maullar(self):
        print("MIUA")
    #un poco de polimorfismo
    def comer(self):
        print("Eso no me gusta")

rocky = perro()
miki = gato()

rocky.comer()
rocky.ladrar()

miki.comer()
miki.maullar()