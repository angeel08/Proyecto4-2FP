#Progama que recibe un numero y dice si es par o impar

# Programa que recibe un número y dice si es par o impar

while True:
    letra = input("Dame un número (o 'n' para salir): ")
    
    if letra.lower() == "n":
        print("Pues nada")
        break

    # Convertir a número después de comprobar que no es 'n'
    num = int(letra)
    if num % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
        
