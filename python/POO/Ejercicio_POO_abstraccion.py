class Interruptor:
    def __init__(self):
        self.__proveedor = "Iberdrola"
        self.__tipocontrato = "Domestico"
        self.__tarifa = "Estandar"
    def encender(self):
        print("Luz encendida")
    def apagar(self):
        print("Luz apagada")

i = Interruptor()
i.encender()
i.apagar()