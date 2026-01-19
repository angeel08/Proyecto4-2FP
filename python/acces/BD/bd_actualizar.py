import pyodbc

db_file = r'C:\Users\Gigabyte\Desktop\proyectos\Proyecto4 - clase 2º\python\acces\BD\Base_datos\empresa.accdb' #en casa
db_file = r'C:\Users\angel.blajim\Proyecto4-2FP\python\acces\BD\base_datos\empresa.accdb' #en clase

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_file};'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

nombre_buscar = input("Dime tu nombre: ") 

cursor.execute("SELECT * FROM clientes WHERE nombre=?", (nombre_buscar)) #peticion del nombre que quiere cambiar
cliente = cursor.fetchone()

if cliente:
    print("Cliente encontrado:")
    print(cliente)

    nombre = input("Nuevo nombre: ")
    apellido = input("nuevo apellido: ")
    edad = int(input("Nueva edad: "))
    ciudad = input("Nueva ciuadad: ")
    
    cursor.execute("UPDATE clientes SET nombre=?, apellido=?, edad=?, ciudad=? WHERE nombre=?",(nombre, apellido, edad, ciudad, nombre_buscar))
    conn.commit()

    print("Registro actualizado")

    cursor.execute("SELECT * FROM clientes WHERE nombre=?", (nombre,))
    print(cursor.fetchone())
else:
    print("EROR......")

cursor.close()
conn.close()
