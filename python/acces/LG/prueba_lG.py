import pyodbc
import getpass

#al tener este proyecto compartido en Github, tenemos varias rutas en cada equipo (en casa y en clase)
lg_file = r'C:\Users\Gigabyte\Desktop\proyectos\Proyecto4 - clase 2º\python\acces\LG\base_datos\Database1.accdb' #en casa
#lg_file = r'C:\Users\angel.blajim\Proyecto4-2FP\python\acces\LG\base_datos\Database1.accdb' #en clase

# Conexión a Access
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={lg_file};'
)

# conexión a la B.D.
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

Nombre = input("Nombre: ") #pedir usuario
Contraseña = getpass.getpass("Contraseña: ") #pedir contraseña

# Consulta SQL
cursor.execute(f"SELECT * FROM Tabla1 WHERE Nombre = '{Nombre}' AND Contraseña = '{Contraseña}'")

resultado = cursor.fetchone()


if resultado:
    print("✔ Inicio de sesión exitoso")
else:
    print("✘ Usuario o contraseña incorrectos")
    peticion = input("\n¿Quieres inscribirte? (S/n)").upper()
    if peticion == "S":
        nuevo_nombre = input("Dame el nombre: ")
        nueva_contraseña = getpass.getpass("Dame una contraseña: ")

        try:
            cursor.execute("INSERT INTO Tabla1 (Nombre, Contraseña) VALUES (?, ?)", (nuevo_nombre, nueva_contraseña))
            conn.commit()
            print("usuario registrado correctamente")
        except:
            print("Error al insertaR ")
            exit()

    else:
        print("Vale, pues hasta luego...")

# Cerrar la conexión
cursor.close()
conn.close()

