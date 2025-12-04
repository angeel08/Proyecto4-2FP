import pyodbc

db_file = r'C:\Users\angel.blajim\Proyecto4-2FP\python\acces\BD\base_datos\empresa.accdb' #en clase
db_file = r'C:\Users\Gigabyte\Desktop\proyectos\Proyecto4 - clase 2º\python\acces\BD\base_datos\empresa.accdb' #en casa


conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_file};'
)

# conexión a la B.D.
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

#hamemos la consulta
consulta = "SELECT * FROM clientes"

cursor.execute(consulta)
resultados = cursor.fetchall()

"""print(f"Se encontraron {len(resultados)} registros")"""

if resultados:
    for row in resultados:
        print(row)
else:
    print("No hay ningun registros que cumpla las condiciones de la consulta")