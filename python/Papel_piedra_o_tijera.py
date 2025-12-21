import random

print("Piedra, papel o tijera \n")

#contadores
contador_BOT = 0
contador_USU = 0

#pedimos un numero para establecer un limite en los contadores
num = int(input("Dame un numero para establecer un limite (cuando alguien de los 2 llegue a ese limite es terminará el jeugo)"))

while True:
    #establecemos un limite en los contadores
    if contador_USU == num:
        print("HAS GANADO MAQUINA")
    elif contador_BOT == num:
        print("HAS PERDIDO.....")        
        
    opciones = ["PIEDRA", "PAPEL" , "TIJERA"]

    #pedimos la opcion al "BOT"
    bot_opcion = random.choice(opciones).upper()
    
    #pedimos la opcion al usuario
    respuesta = input("Dame una opcion (Piedra, papel o tijera), si quiere salirte del juego presiona 'N': ").upper()
    
    #SALIDA 
    if respuesta == "N":
        print("Adiooos... Gracias por jugarlo")
        exit()   

    #PROGRAMA
    if respuesta in opciones:
        if respuesta == bot_opcion:
            print(f"\nRESPUESTAS DE CADA UNO: \nUSUARIO = {respuesta}\nBOT = {bot_opcion}")
            print("EMPATE!")
            
        elif respuesta == "TIJERA" and bot_opcion == "PAPEL" or respuesta == "PAPEL" and bot_opcion == "PIEDRA" or respuesta == "PIEDRA" and bot_opcion == "TIJERA":
            print(f"\nRESPUESTAS DE CADA UNO: \nUSUARIO = {respuesta}\nBOT = {bot_opcion}")
            print("QUE BUENA...")
            contador_USU += 1
            print(f"El usuario lleva {contador_USU} y el BOT lleva {contador_BOT}")
            
        else:
            print(f"\nRESPUESTAS DE CADA UNO: \nUSUARIO = {respuesta}\nBOT = {bot_opcion}")
            print("CASI...")
            contador_BOT += 1
            print(f"El usuario lleva {contador_USU} y el BOT lleva {contador_BOT}")
    else:
        print("VUELVE A INTENTARLO...")