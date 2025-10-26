def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


numero = int(input("dame un numero >= 0:"))
if numero < 0:
    print("no se puede usar numeros negativos")
resp = factorial(numero)
print(f"El factorial de {numero} es: {resp}")