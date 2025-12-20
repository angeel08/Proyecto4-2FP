import pyodbc
import getpass

lg_file = r'C:\Users\Gigabyte\Desktop\proyectos\Proyecto4 - clase 2º\python\acces\LG\base_datos\Database1.accdb'

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={lg_file};'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

#FUNCION QUE ES EL 3º PROGRAMA
def bucle(): 
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Opción A")
        print("2. Opción B")
        print("3. Opción C")
        print("4. Opcion D")
        print("Cualquier letra para Salir")
        print("---------------------------")
        opcion = input("Seleccione una opción (1, 2, 3, 4): ")
        match opcion:
            case '1':
                print("Ha seleccionado la Opción A. Realizando acción...")
            case '2':
                print("Ha seleccionado la Opción B. Realizando acción...")
            case '3':
                print("Ha seleccionado la Opción C. Realizando acción...")
            case '4':
                print("Ha seleccionado la Opción D. Realizando acción...")
            case '5' | _:
                print("No has seleccinado ninguna opcion propuesta..... SALIENDO DEL PROGRAMA  ")
                exit()
                

#1ºPROGRAMA (LOGIN)
Nombre = input("Nombre: ")
Contraseña = getpass.getpass("Contraseña: ")

cursor.execute("SELECT * FROM Tabla1 WHERE Nombre = ? AND Contraseña = ?", (Nombre, Contraseña))
resultado = cursor.fetchone()

if resultado:
    print("Inicio de sesión exitoso")
    bucle()
    
else:
    print("Usuario o contraseña incorrectos")
    #2ºPROGRAMA
    peticion = input("\n¿Quieres inscribirte? (S/n)").upper()
    if peticion == "S":
        nuevo_nombre = input("Dame el nombre: ")
        nueva_contraseña = getpass.getpass("Dame la contraseña: ")
        try:
            cursor.execute("INSERT INTO Tabla1 (Nombre, Contraseña) VALUES (?, ?)", (nuevo_nombre, nueva_contraseña))
            conn.commit()
            print("usuario registrado correctamente")
            bucle()
        except:
            print("Error al insertar... Saliendo del programa ")
            exit()
    else:
        print("Vale, pues hasta luego...")

                    
cursor.close()
conn.close()
