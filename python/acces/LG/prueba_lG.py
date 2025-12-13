import pyodbc
import getpass

lg_file = r'C:\Users\Gigabyte\Desktop\proyectos\Proyecto4 - clase 2º\python\acces\LG\base_datos\Database1.accdb'


conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={lg_file};'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

Nombre = input("Nombre: ")
Contraseña = getpass.getpass("Contraseña: ")

# LOGIN
cursor.execute("SELECT * FROM Tabla1 WHERE Nombre = ? AND Contraseña = ?", (Nombre, Contraseña))
resultado = cursor.fetchone()


if resultado:
    print("Inicio de sesión exitoso")
else:
    print("✘ Usuario o contraseña incorrectos")
    peticion = input("\n¿Quieres inscribirte? (S/n)").upper()


    if peticion == "S":
        nuevo_nombre = input("Dame el nombre: ")
        nueva_contraseña = getpass.getpass("Dame la contraseña: ")
        try:
            cursor.execute("INSERT INTO Tabla1 (Nombre, Contraseña) VALUES (?, ?)", (nuevo_nombre, nueva_contraseña))
            conn.commit()
            print("usuario registrado correctamente")
        except:
            print("Error al insertaR ")
            exit()

    else:
        print("Vale, pues hasta luego...")

cursor.close()
conn.close()
