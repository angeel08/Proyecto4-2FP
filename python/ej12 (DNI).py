"""
Programa que devuelve la letra del DNI usando un contenedor de tipo diccionario 
para mapear cada número con la letra correspondiente.
La letra del dni se obtiene dividiendo el número del DNI entre 23.
Se consideran todas las letras del abecedario en español salvo tres:
la "Ñ", la "I" y la "O".
"""

DNI_letras = {
    0: 'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G', 5: 'M', 6: 'Y', 7: 'F',
    8: 'P', 9: 'D', 10: 'X', 11: 'B', 12: 'N', 13: 'J', 14: 'Z',
    15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L', 20: 'C', 21: 'K', 22: 'E'
}

DNI_usuario = int(input("Dame tu DNI: "))
resto = DNI_usuario%23
letras = DNI_letras[resto]                                                                  
print(f"✅ Tu DNI completo es:{DNI_usuario}{letras}")
