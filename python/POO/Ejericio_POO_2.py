#EJEMPLO 1 DE POO: Definimos la clase perro y creaos un objeto de esta clase

#clase perro
class perro:
    def __init__(self, nombre, raza, color, edad):
        self.__nombre = nombre  #1º forma para encapsular: "__" 
        self.__raza = raza
        self.__color = color
        self.edad = int(edad)

        print("---------- Creado el objeto ----------")
    
    def get_raza(self): #2º forma para encapsular
        return self.__raza

    @property
    def color(self): #3º forma para encapsular
        return self.__color

    def ladrar(self):
        print("GUAOOO")

    def grunir(self):
        print("GGRRRRR")

    def dormir(self):
        print("Zzz")

#Rocky
Rocky = perro("Rocky","Pitbull", "marron", 4)

print(Rocky._perro__nombre) #1º Forma NO HACER
print(Rocky.get_raza()) #2º forma la CORRECTA
print(Rocky.color) #3º forma la MEJOR
print(Rocky.edad)

Rocky.grunir()
Rocky.ladrar()
Rocky.dormir()

"""
| Forma              | Correcta | Limpia |
| ------------------ | -------- | ------ |
| `get_nombre()`     | ✔        | 😐     |
| `@property`        | ✔✔✔      | 😍     |
| `_Clase__atributo` | ❌        | 💀     |

3 forma == (@property) permite acceder a atributos privados como si fueran públicos, manteniendo la encapsulación y permitiendo validaciones.
"""