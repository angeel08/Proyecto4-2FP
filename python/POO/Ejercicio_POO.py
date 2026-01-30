#EJEMPLO 1 DE POO: Definimos la clase perro y creaos un objeto de esta clase

#clase perro
class perro:
    def __init__(self, nombre, raza, edad, color):
        self.nombre = nombre
        self.raza = raza
        self.edad = int(edad)
        self.color = color
        print("---------- Creado el objeto ----------")

    def ladrar(self):
        print("GUAOOO")

    def grunir(self):
        print("GGRRRRR")

    def dormir(self):
        print("Zzz")
    
#Rocky
Rocky = perro("Rocky","Pitbull", 4, "marron")

print(Rocky.nombre)
print(Rocky.raza)
print(Rocky.edad)
print(Rocky.color)

Rocky.grunir()
Rocky.ladrar()
Rocky.dormir()

#lassie
lassie = perro("lassie", "Collie", 6, "blanco")

print(lassie.nombre)
print(lassie.raza)
print(lassie.edad)
print(lassie.color)

lassie.grunir()
lassie.ladrar()
lassie.dormir()

