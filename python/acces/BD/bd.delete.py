import pyodbc

#db_file = r'C:\Users\Gigabyte\Desktop\proyectos\Proyecto4 - clase 2º\python\acces\BD\Base_datos\empresa.accdb' #en casa
db_file = r'C:\Users\angel.blajim\Proyecto4-2FP\python\acces\BD\base_datos\empresa.accdb' #en clase

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_file};'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

#pedir id del cliente
ID_buscar = int(input("Dime tu id: ")) 

#ver toda la informacion del usuario
cursor.execute("SELECT * FROM clientes WHERE id=?", (ID_buscar,))
cliente = cursor.fetchone()

#funcion de mostrar los datos del cliente
def mostrar(cliente):
    print("\n ----- TUS DATOS -----")
    print(cliente)

if cliente:
    mostrar(cliente)

    email = input("Nuevo email: ")
    edad = int(input("Nueva edad: "))
    ciudad = input("Nueva ciuadad: ")

    sql = "UPDATE clientes SET edad=?, email=?, ciudad=? WHERE id=?"
    params = (edad, email, ciudad, ID_buscar)

    cursor.execute(sql, params)
    conn.commit()

    mostrar(cliente) #error sin resolver => no se actualiza los datos guardados
else:
    print("EROR......")

cursor.close()
conn.close()
