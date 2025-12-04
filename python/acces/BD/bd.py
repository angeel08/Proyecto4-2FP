import pyodbc 

DATABASE = r'C:\Users\Gigabyte\Desktop\proyectos\Proyecto4 - clase 2º\python\acces\BD\base_datos\empresa.accdb'

#CONEXION
conexion = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    f'DBQ={DATABASE};'
)
conn = pyodbc.connect(conexion)
cursor = conn.cursor()
def menu():
    print("---- menu ----")
    print("1.todo")
    print("2.nombre y apellido")
    print("")
    print("")
menu()

opcion = int(input("Dame una opcion: "))

consulta = "SELECT " # 3 y 4 del match

match opcion:
    case 1:
        consulta = consulta + "*"
        
    case 2:
        consulta = consulta + "Nombre, Apellido "
        
    case 3:
        consulta = consulta + "Nombre, Apellido, Ciudad "

    case 4:
        consulta = consulta + "Nombre, Apellido "
    
    case _:
        print("adios..... SALIENDO DEL PROGRAMA")

consulta = consulta + f"FROM clientes"        

cursor.execute(consulta)

resultados = cursor.fetchall()

for row in resultados:
    print(row)
    
print(f"\nSe encontraron {len(resultados)}")    

cursor.close()
conn.close()