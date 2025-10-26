"""
17/10/2025
Progama que prueba la gestion de errores con try-except


Todas las excepciones mas usadas son las siguientes:
| Excepción                                 | Cuándo ocurre                                       | Ejemplo                         |
| ----------------------------------------- | --------------------------------------------------- | ------------------------------- |
| **`SyntaxError`**                         | Error de sintaxis en el código.                     | `if True print("hola")`         |
| **`NameError`**                           | Se usa una variable que no existe.                  | `print(x)`                      |
| **`TypeError`**                           | Operación con tipos incompatibles.                  | `"2" + 2`                       |
| **`ValueError`**                          | Valor no válido para una operación.                 | `int("abc")`                    |
| **`IndexError`**                          | Índice fuera del rango en una lista.                | `lista[10]`                     |
| **`KeyError`**                            | Clave inexistente en un diccionario.                | `dicc["edad"]`                  |
| **`AttributeError`**                      | Se intenta usar un atributo o método que no existe. | `"hola".append("x")`            |
| **`ZeroDivisionError`**                   | División entre cero.                                | `5 / 0`                         |
| **`FileNotFoundError`**                   | Archivo no encontrado.                              | `open("archivo.txt")`           |
| **`ImportError` / `ModuleNotFoundError`** | Error al importar un módulo.                        | `import modulo_que_no_existe`   |
| **`IOError`**                             | Error de entrada/salida (archivos, dispositivos).   | `open("/ruta/protegida")`       |
| **`RuntimeError`**                        | Error genérico en tiempo de ejecución.              | Casos imprevistos del programa. |
| **`AssertionError`**                      | Falla una afirmación con `assert`.                  | `assert 2 + 2 == 5`             |

"""

try:
    resp = int(input("Dame un numero entero: ")) 
except ValueError:
    print("Te pedi un numero")