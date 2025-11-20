import pyodbc

db_file = r'C:\Users\Gigabyte\Desktop\proyectos\Proyecto4 - clase 2º\python\acces\Database1.accdb'

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_file};'
)

# conexión a la B.D.
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
def menu():
    print("---- MENU ----")
    print("A = Por ID")
    print("B = Por NOMBRE")
    print("C = Apellido")
    print("D = Edad")
    print("E = Email")
    print("")
menu()


#pedimos el nombre de la ciudad
respuesta = input("Dame una letra: ").upper()

# hacemos las diferentes consultas en SQL
match respuesta:
    case "A":
        print("Has elegido por ID")
        ID_usuario=int(input("Dame un ID: "))
        cursor.execute(f"SELECT * FROM clientes WHERE id = {ID_usuario}")

    case "B":
        print("Has elegido por nombre")
        nombre_usuario=input("Dame un nombre: ")
        cursor.execute(f"SELECT * FROM clientes WHERE Nombre = '{nombre_usuario}'")
    case "C":
        print("Has elegido por Apellido")
        Apellido_usuario=input("Dame un Apellido: ")
        cursor.execute(f"SELECT * FROM clientes WHERE Apellido = '{Apellido_usuario}'")
    case "D":
        print("Has elegido por edad")
        Edad_usuario=int(input("Dame un Edad: "))
        cursor.execute(f"SELECT * FROM clientes WHERE Edad = {Edad_usuario}")
    case "E":
        print("Has elegido por Email")
        Email_usuario=input("Dame un Email: ")
        cursor.execute(f"SELECT * FROM clientes WHERE Email = '{Email_usuario}'")
    case "F":
        print("Has elegido por Ciudad")
        ciudad_usuario=input("Dame un Ciudad: ")
        cursor.execute(f"SELECT * FROM clientes WHERE Ciudad = '{ciudad_usuario}'")
        


for row in cursor.fetchall():
    print(row)

# cerrar el cursor y la conexión
cursor.close()
conn.close()
