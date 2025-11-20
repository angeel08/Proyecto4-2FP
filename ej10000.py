#EJERCICIO 1
"""
🟦 EJERCICIO 1: Números pares e impares

Pide al usuario 10 números e indica cuántos son pares y cuántos son impares.

numeros=[]
for i in range(1,11):
    num = int(input("dame un numero: "))
    numeros.append(num)
    if num %2:
        print("Es impar")
    else:
        print("Es par")
print(f"Lista completa: {numeros}") 


🟩 EJERCICIO 2: Máximo, mínimo y promedio

Pide números al usuario hasta que escriba "fin".
Luego muestra:

el número mayor

el número menor

el promedio de todos los introducidos
"""
numeros=[]
respuesta = ""
while respuesta != "FIN":
    #necesito un .algo que haga para poder hacer dos caminos uno de numeros y otro de letras, que lo compruebe como con .isdigit
    num=int(input("Dame numeros: "))
    
    #los numeros se guardaran aqui
    numeros.append(num)

    #Ejecucion max/min/promedio
    max_num = max(numeros)
    min_num = min(numeros)
    promedio = sum(numeros)/len(numeros)

    #En el momento que el usuario responda fin en esta variable el bucle se parará
    respuesta=input("¿Quieres terminar....? Si quieres terminar pon FIN o fin: ")
    
    if num == "fin":
        print("Pues adios......mostrando menu")
        print(f"El maximo de los numeros: {max_num}")
        print(f"El minimo de los numeros: {min_num}")
        print(f"El promedio de los numeros: {promedio}")
        exit()


"""
🟧 EJERCICIO 3: Palíndromo

Pide una palabra y di si es un palíndromo (se lee igual al derecho y al revés).
"""


"""
🟥 EJERCICIO 4: Contador de vocales

Pide una frase al usuario y cuenta cuántas veces aparece cada vocal:

a

e

i

o

u
"""


"""
🟪 EJERCICIO 5: Simulador de cajero

Crea un programa que:

Tenga un saldo inicial de 1000 €.

Muestre un menú: ingresar, retirar, consultar saldo, salir.

Actualice el saldo según la operación.
"""


"""
🟨 EJERCICIO 6: Adivina el número

El programa genera un número aleatorio entre 1 y 50.
El usuario debe adivinarlo en el menor número de intentos.
El programa debe indicar si el número es mayor o menor.
"""


"""
🟫 EJERCICIO 7: Tabla de multiplicar

Pide un número del 1 al 10 y muestra su tabla completa del 1 al 10.
"""


"""
🔵 EJERCICIO 8: Contador de palabras

Pide una frase y muestra:

número total de palabras

palabra más larga

cuántas veces aparece cada palabra
"""


"""
🔶 EJERCICIO 9: Lista ordenada

Pide al usuario una lista de números separados por comas, conviértelos a enteros y:

ordénalos de menor a mayor

elimínalos duplicados

muestra el resultado
"""


"""
🟥 EJERCICIO 10: Conversor de temperaturas

El usuario elige:

Celsius → Fahrenheit

Fahrenheit → Celsius

Luego ingresa el valor y el programa convierte la temperatura.
"""