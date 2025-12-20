# Cambios de base:

opciones = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "q"}

# ---- FUNCIONES DE CONVERSIÓN ----

def decimal_a_binario(numero):
    return bin(numero)[2:]

def decimal_a_hexadecimal(numero):
    return hex(numero)[2:]

def decimal_a_octal(numero):
    return oct(numero)[2:]

def binario_a_decimal(binario):
    return int(binario, 2)

def binario_a_hexadecimal(binario):
    return hex(int(binario, 2))[2:]

def binario_a_octal(binario):
    return oct(int(binario, 2))[2:]

def hexadecimal_a_decimal(hexadecimal):
    return int(hexadecimal, 16)

def hexadecimal_a_binario(hexadecimal):
    return bin(int(hexadecimal, 16))[2:]

def hexadecimal_a_octal(hexadecimal):
    return oct(int(hexadecimal, 16))[2:]

def octal_a_decimal(octal):
    return int(octal, 8)

def octal_a_binario(octal):
    return bin(int(octal, 8))[2:]

def octal_a_hexadecimal(octal):
    return hex(int(octal, 8))[2:]

# ---- MENÚ ----

def mostrar_menu():
    print("*~*~*~* MENÚ DE CAMBIOS DE BASE *~*~*~*")
    print("a) Decimal a binario")
    print("b) Decimal a hexadecimal")
    print("c) Decimal a octal")
    print("d) Binario a decimal")
    print("e) Binario a hexadecimal")
    print("f) Binario a octal")
    print("g) Hexadecimal a decimal")
    print("h) Hexadecimal a binario")
    print("i) Hexadecimal a octal")
    print("j) Octal a decimal")
    print("k) Octal a binario")
    print("l) Octal a hexadecimal")
    print("q) Salir del programa")

def recoger_respuesta():
    return input("Elige una opción: ").lower()

def comprobar_respuesta(resp):
    if resp in opciones:
        return True
    print("Opción no válida.")
    return False

# ---- PROGRAMA PRINCIPAL ----

while True:
    mostrar_menu()
    resp = recoger_respuesta()

    if not comprobar_respuesta(resp):
        continue

    match resp:

        case "q":
            print("Saliendo del programa...")
            break

        # DECIMAL →
        case "a":
            n = int(input("Número decimal: "))
            print("Binario =", decimal_a_binario(n))

        case "b":
            n = int(input("Número decimal: "))
            print("Hexadecimal =", decimal_a_hexadecimal(n))

        case "c":
            n = int(input("Número decimal: "))
            print("Octal =", decimal_a_octal(n))

        # BINARIO →
        case "d":
            n = input("Número binario: ")
            print("Decimal =", binario_a_decimal(n))

        case "e":
            n = input("Número binario: ")
            print("Hexadecimal =", binario_a_hexadecimal(n))

        case "f":
            n = input("Número binario: ")
            print("Octal =", binario_a_octal(n))

        # HEXADECIMAL →
        case "g":
            n = input("Número hexadecimal: ")
            print("Decimal =", hexadecimal_a_decimal(n))

        case "h":
            n = input("Número hexadecimal: ")
            print("Binario =", hexadecimal_a_binario(n))

        case "i":
            n = input("Número hexadecimal: ")
            print("Octal =", hexadecimal_a_octal(n))

        # OCTAL →
        case "j":
            n = input("Número octal: ")
            print("Decimal =", octal_a_decimal(n))

        case "k":
            n = input("Número octal: ")
            print("Binario =", octal_a_binario(n))

        case "l":
            n = input("Número octal: ")
            print("Hexadecimal =", octal_a_hexadecimal(n))

    print()  # línea en blanco
