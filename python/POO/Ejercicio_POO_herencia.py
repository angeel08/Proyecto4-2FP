class animal:
    def comer(self):
        print("ÑAMM")

class perro(animal):
    def ladrar(self):
        print("GUAO")

class gato(animal):
    def maullar(self):
        print("MIUA")

rocky = perro()
miki = gato()

rocky.comer()
rocky.ladrar()

miki.comer()
miki.maullar()