import pyodbc

#db_file = r'C:\Users\Gigabyte\Desktop\proyectos\Proyecto4 - clase 2º\python\acces\BD\Base_datos\empresa.accdb' #en casa
db_file = r'C:\Users\angel.blajim\Proyecto4-2FP\python\acces\BD\base_datos\empresa.accdb' #en clase

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={db_file};'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

#funcion de mostrar los datos del cliente
def mostrar(cliente):
    print("\n----- TUS DATOS -----")
    print(cliente)

#pedir id del cliente
ID_buscar = int(input("Dime tu id, PARA BORRARLO: ")) 

#ver toda la informacion del usuario
cursor.execute("SELECT * FROM clientes WHERE id=?", (ID_buscar))
cliente = cursor.fetchone()

if cliente:
    mostrar(cliente)

    borrar = input("Seguro que lo quieres BORRAR (S/n):").upper()
    if borrar == "S":
        cursor.execute("DELETE FROM clientes WHERE id=?", ID_buscar)
        conn.commit()
        print("Ya estan borrados tus datos :(")
    else:
        print("Vale... Mejor no borramos")
else:
    print("EROR......")

cursor.close()
conn.close()
