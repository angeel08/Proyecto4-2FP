import pyodbc

#al tener este proyecto compartido en Github, tenemos varias rutas en cada equipo (en casa y en clase)
db_file = r'C:\Users\Gigabyte\Desktop\proyectos\Proyecto4 - clase 2º\python\acces\empresa.accdb' #en casa
db_file = r'C:\Users\angel.blajim\Proyecto4-2FP\python\acces\BD\base_datos\empresa.accdb' #en clase


conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_file};'
)

# conexión a la B.D.
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

#Pedimos la ciudad
ciudad = input("dame la localidad: ")

#hamemos la consulta
consulta = "SELECT * FROM clientes WHERE Ciudad = '" + ciudad +"'"

cursor.execute(consulta)
resultados = cursor.fetchall()
print(f"Se encontraron {len(resultados)} registros")
if resultados:
    for row in resultados:
        print(row)
else:
    print("No hay ningun registros que cumpla las condiciones de la consulta")