import pyodbc
from tabulate import tabulate # si nos aperece una advertencia, deberemos instalar el modulo "tabulate"


#al tener este proyecto compartido en Github, tenemos varias rutas en cada equipo (en casa y en clase)
#db_file = r'C:\Users\Gigabyte\Desktop\proyectos\Proyecto4 - clase 2º\python\acces\BD\base_datos\empresa.accdb' #en casa
db_file = r'C:\Users\angel.blajim\Proyecto4-2FP\python\acces\BD\base_datos\empresa.accdb' #en clase

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
    print("C = Por Apellido")
    print("D = Por Edad")
    print("E = Por Email")
    print("F = Por Ciudad")
    print("_ = cualquier letra")
menu()

#pedimos el nombre de la ciudad
respuesta = input("Dame una letra: ").upper()

# hacemos las diferentes consultas en SQL
match respuesta:
    case "A":
        #programa inicial
        print("Has elegido por ID")
        ID_usuario=int(input("\nDame un ID: "))
        cursor.execute(f"\nSELECT * FROM clientes WHERE id = {ID_usuario}")

        #Programa secundario
        filtrar_a=input("¿quieres filtar?(S/n)").upper()

        if filtrar_a == "S":
            filtrar_a_por = input("\n¿Por que quieres filtrar? (si quieres filtrar ponlo bien y separado por comas ','): ")
            cursor.execute(f"\nSELECT {filtrar_a_por} FROM clientes WHERE id = {ID_usuario}") # podemos filtrar con esta linea
            registros_a = cursor.fetchall()
            print(tabulate(registros_a, headers=["id","Nombre","Apellido","Edad", "Email", "Ciudad", "Fecha_de_registro"], tablefmt="fancy_grid"))
            # al filtrar, si el usuario nos pide un ID en concreto deberemos añadir "WHERE id = {ID_usuario}", esto solo pasa cuando la consulta hay numeros (INT)
        else:
            print("\nVale, pues no filtramos, aqui tienes todo relacionado con el ID: ")
            registros_a = cursor.fetchall()
            print(tabulate(registros_a, headers=["id","Nombre","Apellido","Edad", "Email", "Ciudad", "Fecha_de_registro"], tablefmt="fancy_grid")) #debe de tener fecha de registro
        
    case "B":
        print("Has elegido por nombre")
        nombre_usuario=input("Dame un nombre: ")
        cursor.execute(f"SELECT * FROM clientes WHERE Nombre = '{nombre_usuario}'")

        #Programa secundario
        filtrar_b=input("¿quieres filtar?(S/n)").upper()

        if filtrar_b == "S":
            filtrar_b_por = input("\n¿Por que quieres filtrar? (si quieres filtrar ponlo bien y separado por comas ','): ")
            cursor.execute(f"SELECT {filtrar_b_por} FROM clientes WHERE Nombre = '{nombre_usuario}'")
            registros_b = cursor.fetchall()
            print(tabulate(registros_b, headers=["id","Nombre","Apellido","Edad", "Email", "Ciudad", "Fecha_de_registro"], tablefmt="fancy_grid"))

        else:
            print("\nVale, pues no filtramos, aqui tienes todo relacionado con el Nombre: ")
            registros_b = cursor.fetchall()
            print(tabulate(registros_b, headers=["id","Nombre","Apellido","Edad", "Email", "Ciudad", "Fecha_de_registro"], tablefmt="fancy_grid"))

    case "C":
        print("Has elegido por Apellido")
        Apellido_usuario=input("Dame un Apellido: ")
        cursor.execute(f"SELECT * FROM clientes WHERE Apellido = '{Apellido_usuario}'")

        #Programa secundario
        filtrar_c=input("¿quieres filtar?(S/n)").upper()

        if filtrar_c == "S":
            filtrar_c_por = input("\n¿Por que quieres filtrar? (si quieres filtrar ponlo bien y separado por comas ','): ")
            cursor.execute(f"\nSELECT {filtrar_c_por} FROM clientes WHERE Apellido = '{Apellido_usuario}'") 
            registros_c = cursor.fetchall()
            print(tabulate(registros_c, headers=["id","Nombre","Apellido","Edad", "Email", "Ciudad", "Fecha_de_registro"], tablefmt="fancy_grid"))

        else:
            print("\nVale, pues no filtramos, aqui tienes todo relacionado con el Apellido: ")
            registros_c = cursor.fetchall()
            print(tabulate(registros_c, headers=["id","Nombre","Apellido","Edad", "Email", "Ciudad", "Fecha_de_registro"], tablefmt="fancy_grid"))
        
    case "D":
        print("Has elegido por edad")
        Edad_usuario=int(input("Dame un Edad: "))
        cursor.execute(f"SELECT * FROM clientes WHERE Edad = {Edad_usuario}")

        #Programa secundario
        filtrar_d=input("¿quieres filtar?(S/n)").upper()

        if filtrar_d == "S":
            filtrar_d_por = input("\n¿Por que quieres filtrar? (si quieres filtrar ponlo bien y separado por comas ','): ")
            cursor.execute(f"\nSELECT {filtrar_d_por} FROM clientes WHERE Edad = {Edad_usuario}") # podemos filtrar con esta linea
            registros_d = cursor.fetchall()
            print(tabulate(registros_d, headers=["id","Nombre","Apellido","Edad", "Email", "Ciudad", "Fecha_de_registro"], tablefmt="fancy_grid"))

        else:
            print("\nVale, pues no filtramos, aqui tienes todo relacionado con la Edad: ")
            registros_d = cursor.fetchall()
            print(tabulate(registros_d, headers=["id","Nombre","Apellido","Edad", "Email", "Ciudad", "Fecha_de_registro"], tablefmt="fancy_grid"))

    case "E":
        print("Has elegido por Email")
        Email_usuario=input("Dame un Email: ")
        cursor.execute(f"SELECT * FROM clientes WHERE Email = '{Email_usuario}'")

        #Programa secundario
        filtrar_e=input("¿quieres filtar?(S/n)").upper()

        if filtrar_e == "S":
            filtrar_e_por = input("\n¿Por que quieres filtrar? (si quieres filtrar ponlo bien y separado por comas ','): ")
            cursor.execute(f"\nSELECT {filtrar_e_por} FROM clientes")
            registros_e = cursor.fetchall()
            print(tabulate(registros_e, headers=["id","Nombre","Apellido","Edad", "Email", "Ciudad", "Fecha_de_registro"], tablefmt="fancy_grid"))
        else:
            print("\nVale, pues no filtramos, aqui tienes todo relacionado con el Email: ")
            registros_e = cursor.fetchall()
            print(tabulate(registros_e, headers=["id","Nombre","Apellido","Edad", "Email", "Ciudad", "Fecha_de_registro"], tablefmt="fancy_grid"))


    case "F":
        print("Has elegido por Ciudad")
        ciudad_usuario=input("Dame un Ciudad: ")
        cursor.execute(f"SELECT * FROM clientes WHERE Ciudad = '{ciudad_usuario}'")

        #Programa secundario
        filtrar_f=input("¿quieres filtar?(S/n)").upper()

        if filtrar_f == "S":
            filtrar_f_por = input("\n¿Por que quieres filtrar? (si quieres filtrar ponlo bien y separado por comas ','): ")
            cursor.execute(f"\nSELECT {filtrar_f_por} FROM clientes WHERE Ciudad = '{ciudad_usuario}'") 
            registros_f = cursor.fetchall()
            print(tabulate(registros_f, headers=["id","Nombre","Apellido","Edad", "Email", "Ciudad", "Fecha_de_registro"], tablefmt="fancy_grid"))

        else:
            print("\nVale, pues no filtramos, aqui tienes todo relacionado con la Ciudad: ")
            registros_f = cursor.fetchall()
            print(tabulate(registros_f, headers=["id", "Nombre", "Apellido", "Edad", "Email", "Ciudad", "Fecha_de_registro"], tablefmt="fancy_grid"))


# cerrar el cursor y la conexión
cursor.close()
conn.close()