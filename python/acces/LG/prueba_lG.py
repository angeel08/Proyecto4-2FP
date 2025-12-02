import pyodbc
import getpass

#al tener este proyecto compartido en Github, tenemos varias rutas en cada equipo (en casa y en clase)
#lg_file = r'C:\Users\Gigabyte\Desktop\proyectos\Proyecto4 - clase 2º\python\acces\LG\base_datos\Database1.accdb' #en casa
lg_file = r'C:\Users\angel.blajim\Proyecto4-2FP\python\acces\LG\base_datos\Database1.accdb' #en clase

# Conexión a Access
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={lg_file};'
)

# conexión a la B.D.
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

Nombre = input("Nombre: ")
Contraseña = getpass.getpass("Contraseña: ")

# Consulta SQL
cursor.execute(f"SELECT * FROM Tabla1 WHERE Nombre = '{Nombre}' AND Contraseña = '{Contraseña}'")
resultado = cursor.fetchone()

if resultado:
    print("✔ Inicio de sesión exitoso")
else:
    print("✘ Usuario o contraseña incorrectos")
