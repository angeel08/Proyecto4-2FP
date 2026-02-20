#EXAMEN DE ANGEL BLAZQUEZ JIMENEZ

from abc import ABC, abstractmethod

class CuentaGenerica:
    def __init__(self, titular, iban, saldo):
        self.__titular = titular
        self.__saldo  = saldo
        self.__iban = iban


    @property
    def consultar_saldo(self):
        return self.__saldo

    @property
    def depositar(self, cantidad):
        return self.__saldo + cantidad
        
    @property
    def retirar(self, cantidad):
        print(f"{self.__saldo - cantidad}")

    @property
    def consultar_saldo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular
    
    @property
    def get_iban(self):
        return self.__iban


class CuentaNomina(CuentaGenerica):
    @property
    def retirar(self, cantidad):
        print(f"{self.__saldo - cantidad}")
        


class CuentaJoven(CuentaGenerica):
    @property
    def retirar(self, cantidad):
        print(f"{self.__saldo - cantidad}")



#ejecucion del programa
#CUENTA JOVEN = PACO
Paco = CuentaGenerica("paco", 1234567, 3000)
print("Datos de la cuenta nomina: ")
print(f"Titular: {Paco.get_titular}")
print(f"Saldo: {Paco.consultar_saldo}")
print(f"IBAN: {Paco.get_iban}")

#CUENTA JOVEN = ANGEL
Angel= CuentaJoven("angel",2345678,1500)
print("Datos de la cuenta joven: ")
print(f"Titular: {Angel.get_titular}")
print(f"Saldo: {Angel.consultar_saldo}")
print(f"IBAN: {Paco.get_iban}")

#Depositos y retiros
print(f"Deposito exitoso. Saldo actual: {Paco.depositar}")
print(f"Retiro exitoso. Saldo actual: {Paco.retirar}")
print(f"Deposito exitoso. Saldo actual: {Paco.depositar}")
print(f"Retiro exitoso. Saldo actual: {Angel.retirar}")

