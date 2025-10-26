"""
Tabla de multiplicar
"""

num = int(input("Dame un numero para la tabla de multiplicar: "))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")