#Programa que devuelve la letra del DNI usando un contenedor de tipo diccionario 
#para mapear cada número con la letra correspondiente.
#La letra del dni se obtiene dividiendo el número del DNI entre 23.
#Se consideran todas las letras del abecedario en español salvo tres:
#la "Ñ", la "I" y la "O".
print ("________ángel blázquez jiménez___________")
 
dni_letras = {
    0: 'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G', 5: 'M', 6: 'Y', 7: 'F',
    8: 'P', 9: 'D', 10: 'X', 11: 'B', 12: 'N', 13: 'J', 14: 'Z',
    15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L', 20: 'C', 21: 'K', 22: 'E'
}
 
#calcula_resto_23(): función que devuelve el resto de dividir el número del DNI entre
#las 23 letras del abecedario usadas.
#Parámetros:
# de entrada: un número entero que representa el DNI
# de salida: un número entre 0 y 22, resto de la división por 23 
def calcula_resto_23(num):
    return num % 23
 
 
#devuelve_letra_dni(): función que devuelve la letra del DNI partiendo de un número (resto)
#que se le pasa.
#Parámetros:
# de entrada: un número entero que representa el resto de la división del nº de DNI por 23
# de salida: la letra del dni o bien -1 si se produjo error. 
def devuelve_letra_dni(resto):
    if resto in dni_letras:
        return dni_letras[resto]
    return -1
#dni_valido(): función que devuelve true si el dni es válido o false en caso contrario.
#Parámetros:
# de entrada: un nuúmero entero con el DNI introducido por el usuario
# de salida: true o false.
def dni_valido(dni):
    dni = str(dni)
    if str(dni):
        if len(dni) == 7 or len(dni) == 8: 
            return True
    return False
 
#recoge_dni(): función que solicita al usuario el número del DNI. Devuelve el nº de DNI.
#Parámetros:
# de entrada: no tiene
# de salida: el DNI introducido por el usuario.
def recoge_dni():
    while True:
        dni = input("Introduce tu número de DNI (sin letra): ")
        if dni.isdigit() and 7 <= len(dni) <= 8:
            return int(dni)
        else:
            print("Error: El DNI debe contener 7 u 8 dígitos numéricos.")

 
#muestra_mensaje_inicial(): función que muestra el mensaje inicial que explica
#el funcionamiento del programa.
#Parámetros:
# de entrada: no tiene
# de salida: no tiene
def muestra_mensaje_inicial():
    print("######## PROGRAMA DE VALIDACIÓN DE DNI ########")
    print("Programa que comprueba la letra del dni de un usuario")
    print("A continuación se le pedirá su DNI SIN la letra.")
 
#muestra_mensaje_error(): función que muestra un mensaje de error si se produjo
#un error al calcular la letra del DNI.
#Parámetros:
# de entrada: no tiene
# de salida: no tiene
def muestra_mensaje_error():
     print("Error al calcular la letra del DNI, inténtelo de nuevo.")
#muestra_mensaje_dni_letra(): función que muestra el DNI introducido por el usuario
#y la letra que le corresponde.
#Parámetros:
# de entrada: 1. dni: número entero de 8 dígitos máx.
#             2. letra: la letra del dni 
# de salida: no tiene
def muestra_mensaje_dni_letra(dni, letra):
    print(f" Muestra el DNI {dni} corresponde con la letra: {letra}")
 
while(True):   
    muestra_mensaje_inicial()
    dni = recoge_dni()
 
    resto = calcula_resto_23(dni)
    letra_dni = devuelve_letra_dni(resto)
    if letra_dni == -1:
        muestra_mensaje_error()
    else:
        muestra_mensaje_dni_letra(dni, letra_dni)
 
    seguir = input("¿Desea continuar (S/N)?")
    if not seguir.upper() == 'S':
        quit()
