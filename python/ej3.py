"""
Ejmplo de uso de match
Recogemos la opcion seleccionada por el  usuario
Procesar la opcion

"""


print("a) Opcion")
print("b) Opcion")
print("c) Opcion")
print("D) Opcion")

resp = input("dame una opcion: ").lower()

match resp:
    case "a":
        print("Etiquta la opcion a")
    case "b":
        print("Etiquta la opcion b")
    case "c":
        print("Etiquta la opcion c")
    case "d":
        print("Etiquta la opcion d")
    case _: #esto sirve como (casi) cualquier caracter
        print("Opcion no valida...destruyendo la informacion del equipo")