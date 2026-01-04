import random
import time
import requests

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
        r = requests.get(url, params=params, headers=headers, timeout=5)
        data = r.json()
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


print("\n💣 BOMBA DE LAS SÍLABAS 💣")

num_jugadores = int(input("Número de jugadores: "))
jugadores = []

for i in range(num_jugadores):
    nombre = input(f"Nombre jugador {i+1}: ")
    jugadores.append(nombre)

silabas = ["ca", "to", "ra", "ma", "te", "lo", "pa", "ri"]

turno = 0

while len(jugadores) > 1:
    jugador = jugadores[turno % len(jugadores)]
    print(f"\n👉 TURNO DE {jugador}")

    silabas_juego = random.sample(silabas, random.choice([1, 2]))
    tiempo_limite = random.randint(5, 10)

    print(f"SÍLABAS: {silabas_juego}")
    print(f"Tiempo: {tiempo_limite} segundos")

    inicio = time.time()
    palabra = input("Palabra: ").lower()
    fin = time.time()

    if fin - inicio > tiempo_limite:
        print("💥 BOOOM (fuera de tiempo)")
        jugadores.remove(jugador)

    elif not palabra_valida(palabra, silabas_juego):
        print("💥 BOOOM (palabra inválida)")
        jugadores.remove(jugador)

    else:
        print("✅ Sigue vivo")

    turno += 1


print(f"\n🏆 GANADOR: {jugadores[0]}")
