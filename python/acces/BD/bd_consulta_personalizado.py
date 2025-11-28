import pyodbc
from tabulate import tabulate

db_file = r'C:\Users\angel.blajim\Proyecto4-2FP\python\acces\BD\base_datos\empresa.accdb'

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_file};'
)

#Conectamos con la base de datos
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

consulta = "SELECT * FROM clientes"
cursor.execute(consulta)

registros = cursor.fetchall()


# MÉTODO 1: 
print(" \nMÉTODO 1: ")
for row in registros:
    print(" | ".join(map(str, row)))



# MÉTODO 2: 
print(" \nMÉTODO 2: ")
for row in registros:
    id_cliente, nombre, apellido, edad, email, ciudad, fecha = row
    print(f"ID={id_cliente} | {nombre} {apellido} | {edad} años | {email} | {ciudad} | Registro: {fecha}")



# MÉTODO 3: 
print(" \nMÉTODO 3: ")
headers = ["ID", "Nombre", "Apellido", "Edad", "Email", "Ciudad", "Fecha de registro"]

print(tabulate(registros, headers=headers, tablefmt="fancy_grid"))

cursor.close()
conn.close()
