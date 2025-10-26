#Progama para reparar el if, if-else

edad = int(input("dame tu edad: "))

if edad < 18:
    print("Eres un niño")
elif edad == 18:
    print("Eres mayor de edad, pero eres muy joven ")
elif edad < 30:
    print("Eres un jovenazo")
elif edad >= 65:
    print("Estas jubilado")
else:
    print("Tienes entre 30 y 64 años te toca seguir trabajando")