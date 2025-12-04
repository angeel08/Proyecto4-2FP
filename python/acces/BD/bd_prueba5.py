import pyodbc

#al tener este proyecto compartido en Github, tenemos varias rutas en cada equipo (en casa y en clase)
db_file = r'C:\Users\Gigabyte\Desktop\proyectos\Proyecto4 - clase 2º\python\acces\empresa.accdb' #en casa
db_file = r'C:\Users\angel.blajim\Proyecto4-2FP\python\acces\empresa.accdb' #en clase

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_file};'
)

#le pedimos al usuario una ciudad:
ciudad_usuario = input("Dame una ciuadad: ")

#hamemos la consulta
print("Indique los campos a mostrar: ")
print("1. Nombre y apellido")
print("2. Nombre, apellido y ciudad")
print("3. Nombre, apellido y email")
print("4. Todos los campos")
print("Cualquier letra = sale del programa")

opcion = input("ELija una opcion: ")

consulta = "SELECT " # PONEMOS EL ESPACIO DESPUES DEL select 
match opcion:
    case '1':
        consulta = consulta + "Nombre, Apellido" #Como pongas estas lineas tal que asi: consulta = consulta + " nombre, apellido" te da error
    case '2':
        consulta = consulta + "Nombre, Apellido, Ciudad"
    case '3':
        consulta = consulta + "Nombre, Apellido, Email"
    case '4':
        consulta = consulta + "*"
    case _:
        print("lo siento.... saliendo del programa")
        exit()
        

consulta = consulta + f" FROM clientes WHERE Ciudad = {ciudad_usuario}" # como solucion puede poner el espacio antes del FROM clientes
# conexión a la B.D.
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

cursor.execute(consulta)
resultados = cursor.fetchall()

print(f"Se encontraron {len(resultados)} registros")
if resultados:
    for row in resultados:
        print(row)
else:
    print("No hay ningun registros que cumpla las condiciones de la consulta")

#Cerramos el cursor y la conexion
cursor.close()
conn.close()