"""
Programa que usa el match-case para procesar
un menu que muestre varia opciones al usuario
que despues hay que resolver usando funciones

Mostrar menu
Recoger respuesta del usuario
Llamar a la funciona apropiada usando match-case
mostrar los resultados



Cambiar de Dolares a Euros
Cambiar de Euros a Dolares
Cambiar de millas a kilometros
Cambiar de kilometros a millas
Cambiar grados centigrados a grados Fahrenheit
Cambiar grados Fahrenheit a grados centigrados
"""
def saludo():
    print("---------- Menu ----------")
    print("A) Cambiar de Dolares a Euros")
    print("B) Cambiar de Euros a Dolares")
    print("C) Cambiar de millas a kilometros")
    print("D) Cambiar grados centigrados a grados Fahrenheit")
    print("E) Cambiar grados Fahrenheit a grados centigrados")
saludo()

def respuesta():
    resp = input("dame una opcion: ").upper()
    return resp

def A():
    print("A) Cambiar de Dolares a Euros")
    print("0.86$ = 1€")
    numA=float(input("¿Cuantos Euros quieres? "))
    print(f"{numA}$ pasando a {numA * 0.86}€ ")

def B():
    print("B) Cambiar de Euros a Dolares")
    print("1€ = 0.86$ ")
    numB=float(input("¿Cuantos dolares quieres? "))
    print(f"{numB}€ pasando a {numB *  1.17}$ ")


def C():
    print("C) Cambiar de millas a kilometros")
    print("1 milla = 1,60KM")
    numC=float(input("¿Cuantos kilometros quieres? "))
    print(f"{numC} milla/s  {numC * 1.60}KM")


def D():
    print("D) Cambiar de grados centigrados a grados Fahrenheit")
    print("1 grado centigrado = 33,8 grado Fahrenheit")
    numD=float(input("¿Cuantos grados Fahrenheit quieres? "))
    print(f"{numD} grado centigrado {numD * 33.8} grado Fahrenheit")


def E():
    print("E) Cambiar grados Fahrenheit a grados centigrados")
    print("33,8 grado Fahrenheit = 1 grado centigrado  ")
    numE=float(input("¿Cuantos grados centigrados quieres? "))
    print(f"{numE} grado centigrado {numE * 33.8} grado Fahrenheit")

def _():
    print("Opcion no valida...destruyendo la informacion del equipo")

match respuesta():
    case "A":
        A()
    case "B":
        B()
    case "C":
        C()
    case "D":
        D()
    case "E":
        E()
    case _: 
        _()