class circulo:
    def area(self):
        return 3.14 * 2 * 2

class cuadrado:
    def area(self):
        return 4*4

def mostrar_area(objeto):
    print(objeto.area())

area = [circulo(), cuadrado()]
for x in area:
    mostrar_area(x)
