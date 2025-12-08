import pyodbc

db_file = r'C:\Users\angel.blajim\Proyecto4-2FP\python\acces\BD\base_datos\empresa.accdb'
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_file};'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

#MOSTRAR LAS CIUDADES DISPONIBLES
informacion="SELECT DISTINCT(Ciudad) FROM clientes"

cursor.execute(informacion)
resultados_info = cursor.fetchall()
    
for fila in resultados_info:
    print(fila)
    
#PREGUNTA AL USUARIO (ciudad)
ciudad_usuario = input("Elija una ciudad: ")
if not ciudad_usuario:
    print("No has seleccionado ninguna ciudad..... SALIENDO DEL PROGRAMA.......") 
    exit()
else:
    print(f"Mostrando los datos de los clientes de {ciudad_usuario}")

#MOSTRAR MENU
def menu():
    print("INDIQUE LOS CAMPOS A MOSTRAR:")
    print("1. NOMBRE Y APELLIDO")
    print("2. NOMBRE, APELLIDO Y CIUDAD")
    print("3. NOMBRE, APELLIDO Y EMAIL")
    print("4. TODOS LOS CAMPOS")
menu()

#DESARROLLO DEL PROGRAMA
opcion = input("Elija una opcion: ")
consulta = "SELECT "
match opcion:
    case '1':
        consulta = consulta + "Nombre, Apellido"

    case '2':
        consulta = consulta + "Nombre, Apellido, Ciudad"

    case '3':
        consulta = consulta + "Nombre, Apellido, Email"

    case '4':
        consulta = consulta + "*"


consulta = consulta + f" FROM clientes WHERE ciudad = '{ciudad_usuario}'"

#MOSTRAR LA CONSULTA
cursor.execute(consulta)
resultados = cursor.fetchall()

print(f"Se encontraron {len(resultados)} registros en la ciudad: {ciudad_usuario}")
for row in resultados:
    print(row)

#Cerramos el cursor y la conexión
cursor.close()
conn.close()
