import pyodbc

#Ponemos la ruta de la base de datos
db_file = r'C:\Users\angel.blajim\Proyecto4-2FP\python\acces\BD\base_datos\empresa.accdb' 

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_file};'
)

#hamemos la consulta
print("Indique los campos a mostrar: ")
print("1. Nombre y apellido")
print("2. Nombre, apellido y ciudad")
print("3. Nombre, apellido y email")
print("4. Todos los campos")
print("Cualquier letra = sale del programa")

opcion = input("ELija una opcion: ")

#consulta = "SELECT " # PONEMOS EL ESPACIO DESPUES DEL select 
match opcion:
    case '1':
        consulta = "SELECT nombre, apellido FROM clientes" #Como pongas estas lineas tal que asi: consulta = consulta + " nombre, apellido" te da error
    case '2':
        consulta = "SELECT nombre, apellido, ciudad FROM clientes"
    case '3':
        consulta = "SELECT nombre, apellido, email FROM clientes"        
    case '4':
        consulta = "SELECT * FROM clientes"        
    case _:
        print("lo siento.... saliendo del programa")
        exit()
        

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