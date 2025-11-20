#Hecho por Ángel Blázquez Jiménez

def saludo():
    print("---------------- Todas las tablas, desde la 1 hasta la 10 ----------------")
    print("---------------- Hecho por Ángel Blázquez Jiménez ----------------")

saludo()
for i in range(1,11):
    print(f"\nTabla del {i}: ")
    for j in range(1,11):
        print(f"{j} x {i} = {j*i}")
