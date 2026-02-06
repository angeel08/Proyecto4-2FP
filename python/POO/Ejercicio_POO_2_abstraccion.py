from abc import ABC, abstractmethod

class MetodoPago(ABC):
    #1º forma (mas rara, pero mas segura)
    @abstractmethod
    def pagar(self, cantidad):
        pass

    #2º forma (mas normal)
    #def __init__(self):
        #pass


class Tarjeta(MetodoPago):
    def pagar(self, cantidad):
        print(f"Pagando {cantidad}€ con tarjeta")

class Paypal(MetodoPago):
    def pagar(self, cantidad):
        print(f"Pagando {cantidad}€ con Paypal")

def procesar_pago(manera:MetodoPago):
    manera.pagar(50)

procesar_pago(Tarjeta())
procesar_pago(Paypal())
