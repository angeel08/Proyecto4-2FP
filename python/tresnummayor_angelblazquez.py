#progama que pide tres numeros (enteros) y nos dice cual es el mayor de los tres

print("@@@@@@@@@@@@@@@@   Hecho por: Ángel   @@@@@@@@@@@@@@@@")

num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))
num3 = int(input("Dame otro numero: "))

if num1 >= num2 and num1 >= num3: #comparamos el num1 con los demas numeros
    print(f"El mayor es: {num1}")

else:
    if num2 >= num1 and num2 >= num3: #comparamos el num2 con los demas numeros
        print(f"El mayor es: {num2}")

    else:
        print(f"El mayor es: {num3}") #comparamos el num3 con los demas numeros