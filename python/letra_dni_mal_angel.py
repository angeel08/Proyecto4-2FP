#Programa que devuelve la letra del DNI usando un contenedor de tipo diccionario 
#para mapear cada número con la letra correspondiente. #La letra del dni se obtiene dividiendo el número del DNI entre 23. 
#Se consideran todas las letras del abecedario en español salvo tres: #la "Ñ", la "I" y la "O".
print("·················Ángel Blázquez Jimenez···············")

dni_letras = {
    0: 'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G', 5: 'M', 6: 'Y', 7: 'F',
    8: 'P', 9: 'D', 10: 'X', 11: 'B', 12: 'N', 13: 'J', 14: 'Z',
    15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L', 20: 'C', 21: 'K', 22: 'E'
}
#recoge_dni(): función que solicita al usuario el número del DNI. Devuelve el nº de DNI. 
#Parámetros:
# de entrada: no tiene 
# de salida: el DNI introducido por el usuario.
def recoge_dni():
    while True:
        dni_str = input("Introduce tu número de DNI (8 dígitos): ")
        if dni_str.isdigit() and len(dni_str) == 8:
            return int(dni_str)
        print("DNI inválido. Debe ser un número de 8 dígitos.")
#calcula_resto_23(): función que devuelve el resto de dividir el número del DNI entre 
#las 23 letras del abecedario usadas. 
#Parámetros: 
# de entrada: un número entero que representa el DNI 
# de salida: un número entre 0 y 22, resto de la división por 23
def calcula_resto_23(dni):
    return dni % 23

#devuelve_letra_dni(): función que devuelve la letra del DNI partiendo de un número (resto) que se le pasa. 
#Parámetros: 
# de entrada: un número entero que representa el resto de la división del nº de DNI por 23 
# de salida: 
# la letra del dni o bien -1 si se produjo error.
def devuelve_letra_dni(resto):
    if resto in dni_letras:
        return dni_letras[resto]
    return -1


def muestra_mensaje_inicial():
    print("######## PROGRAMA DE VALIDACIÓN DE DNI ########")
    print("Programa que comprueba la letra del dni de un usuario")
    print("A continuación se le pedirá su DNI SIN la letra.")

def muestra_mensaje_error():
    print("Error al calcular la letra del DNI, inténtelo de nuevo.")

def muestra_mensaje_dni_letra(dni, letra):
    print(f"El DNI {dni} corresponde con la letra: {letra}")

# Programa principal
while True:
    muestra_mensaje_inicial()
    dni = recoge_dni()
    resto = calcula_resto_23(dni)
    letra_dni = devuelve_letra_dni(resto)

    if letra_dni == -1:
        muestra_mensaje_error()
    else:
        muestra_mensaje_dni_letra(dni, letra_dni)

    seguir = input("¿Desea continuar (S/N)? ")
    if seguir.upper() != 'S':
        print("Programa finalizado.")
        break
