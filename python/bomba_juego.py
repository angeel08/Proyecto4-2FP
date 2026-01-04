import random
import time
import requests # deberemos de instalar un modulo y en todo momento deberemos tener internet

"""
JUEGO para X personas
"""

def palabra_existe_api(palabra):
    url = "https://es.wiktionary.org/w/api.php"

    params = {
        "action": "query",
        "titles": palabra,
        "format": "json"
    }

    headers = {
        "User-Agent": "JuegoBombaPython/1.0"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=5)
        data = response.json()
        paginas = data["query"]["pages"]
        return "-1" not in paginas
    except:
        return False


def palabra_valida(palabra, silabas):
    if not palabra_existe_api(palabra):
        return False

    for s in silabas:
        if s not in palabra:
            return False

    return True


print("BOMBA DE LAS SÍLABAS\n")

silabas = ["ca", "to", "ra", "ma", "te", "lo", "pa", "ri"]

silabas_juego = random.sample(silabas, random.choice([1, 2]))
tiempo_limite = random.randint(5, 10)

print(f"SÍLABAS: {silabas_juego}")
print(f"Tienes {tiempo_limite} segundos")

inicio = time.time()
palabra = input("Palabra: ").lower()
fin = time.time()

tiempo_usado = fin - inicio

if tiempo_usado > tiempo_limite:
    print("\nBOOOM")
    print("Te has pasado de tiempo")
    
elif palabra_valida(palabra, silabas_juego):
    print("\nBOMBA DESACTIVADA")
    print(f"Tiempo usado: {tiempo_usado:.2f} segundos") #los ":." son para señalizar las 2 primeras decimas
    
else:
    print("\nBOOOM")
    print("Palabra inválida o no existe")
