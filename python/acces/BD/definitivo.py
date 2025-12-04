import pyodbc

db_file = r'C:\Users\Gigabyte\Desktop\proyectos\Proyecto4 - clase 2º\python\acces\BD\Base_datos\empresa.accdb'

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_file};'
)

#CONEXION BASE DE DATOS
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


#DESARROLLO DEL PROGRAMA
consulta = "SELECT * FROM clientes"

#EJECUCION DEL PROGRMA
cursor.execute(consulta)
resultados=cursor.fetchall()

for row in resultados:
    print(row)