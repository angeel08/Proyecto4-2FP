"""
Ejemplo de menu con submenu y match case anidados
"""
def todos_menus(opcion):
    match opcion:
        case 0:
            print("===== MENU =====")
            print("a) Desayuno")
            print("b) Comida")
            print("c) Cena")
            print("d) Salir del programa")
        case 1:
            print("#### Menu desayuno ####")
            print("1) Huevos con morcilla y alubias")
            print("2) Magras con tomate")
            print("3) Aguardiente con perronillas")
        case 2:
            print("@@@@ Menu Comida @@@@")
            print("1) Ensalada con lechuga con tomate")
            print("2) Sopa de cebolla")
            print("3) Callos con garbanzos")
        case 3:
            print("$$$$ Menu Cena $$$$")
            print("1) Cordero asado")
            print("2) Chuleton de buey")
            print("3) Yogur de agua")
todos_menus(0)
resp = input("Selecciona una opcion (a-d): ").upper()

match resp:
    case "A":
        todos_menus(1)
        resp = int(input("Selecciona una opcion (1-3): "))
        match resp:
            case 1:
                print("Has elegido Huevos con morcilla y alubias")
            case 2:
                print("Has elegido Magras con tomate")
            case 3:
                print("Has elegido Aguardiente con perronillas")
            case _:
                print("ESO NO ESTA EN EL MENU")
    case "B":
        todos_menus(2)
        resp = int(input("Selecciona una opcion (1-3): "))
        match resp:
            case 1:
                print("Has elegido Ensalada con lechuga con tomate")
            case 2:
                print("Has elegido Sopa de cebolla")
            case 3:
                print("Has elegido Callos con garbanzos")
            case _:
                print("ESO NO ESTA EN EL MENU")
    case "C":
        todos_menus(3)
        resp = int(input("Selecciona una opcion (1-3): "))
        match resp:
            case 1:
                print("Has elegido Cordero asado")
            case 2:
                print("Has elegido Chuleton de buey")
            case 3:
                print("Has elegido Yogur de agua")
            case _:
                print("ESO NO ESTA EN EL MENU")
    case _:
        print("LA OPCION ELEGIDA NO ESTA EN EL MENU")
        print("Gracias por su visita, vuelva pronto.") 