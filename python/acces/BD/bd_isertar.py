import pyodbc

db_file = r'C:\Users\angel.blajim\Proyecto4-2FP\python\acces\BD\base_datos\empresa.accdb'

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_file};'
)

#CONEXION BASE DE DATOS
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

#SUMAR A EL ULTIMO id UNO MAS 
consulta = "SELECT max(ID) FROM clientes_insertar" #sumo uno mas 
cursor.execute(consulta)
resultado = cursor.fetchone()

#pedimos datos
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
edad = int(input("Ingrese la edad: "))
ciudad = input("Ingrese la ciudad: ")

cursor.execute("INSERT INTO clientes_insertar (nombre, apellido, edad, ciudad) VALUES (?, ?, ?, ?)", (nombre, apellido, edad, ciudad))
conn.commit()

#DESARROLLO DEL PROGRAMA
consulta = "SELECT * FROM clientes_insertar"

#EJECUCION DEL PROGRMA  
cursor.execute(consulta)
resultados=cursor.fetchall()

for row in resultados:
    print(row)