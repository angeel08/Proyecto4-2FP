#Ejemplo de funcion que devuelve 2 valores

def obtener_coordenadas(loc):
    if loc == "Peñaranda":
        latitud = 40.7128
        longitud = -74.0060
    else:
        latitud = 40.7128
        longitud = 84.0060
    return latitud, longitud
localizacion = "Peñaranda"
lat, long = obtener_coordenadas(localizacion)
print(f"Localizacion: tu latitud es: {lat}, y tu longitud es: {long}")
lat, long = obtener_coordenadas("Macotera")
print(f"Localizacion: tu latitud es: {lat}, y tu longitud es: {long}")