class perro:
    def sonido(self):
        print("GUAOOO")

class gato:
    def sonido(self):
        print("MIAUUU")

class robot:
    def sonido(self):
        print("01010101010101")

def habla(objeto):
    objeto.sonido()

#definimos una lista con objetos, uno de cada clase
mascotas = [perro(), gato(), robot()]

for x in mascotas:
    habla(x)