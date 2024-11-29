import json
import os


CONFIG = {
    "matriz": {
        "min": 1,
        "max": 10,
    },
    "valor": {
        "min": -9.98,
        "max": 9.98,
        "pos_decimales": 2,
        "pos_totales": 5
    }
}

# O también...
"""
CONFIG = {
    "min_filas": 1,
    "max_filas": 10,
    "min_valores": -9.98,
    "max_valores": 9.98,
    "pos_decimales": 2
    "pos_totales": 5
}
"""


def borrar_consola():
    """
    Borra la consola según el sistema operativo.
    """
    try:
        os.system("clear") if os.name == "posix" else os.system("cls")
    except Exception as e:
        mostrar_error(e)


def mostrar_error(msj: str):
    """
    Muestra un mensaje de error formateado.

    Args:
        msj (str): El mensaje de error a mostrar.
    """
    print(f"*ERROR* {msj}")


def pedir_numero(msj: str, min: float, max: float) -> float:
    """
    Solicita al usuario un número flotante dentro de un rango definido.

    Args:
        msj (str): Mensaje que se mostrará al usuario.
        min (float): Valor mínimo permitido.
        max (float): Valor máximo permitido.

    Returns:
        float: Número válido ingresado por el usuario dentro del rango.
    """
    num = None
    while num is None:
        try:
            num = float(input(msj))
            if num < min or num > max:
                raise ValueError(f"*ERROR* El número debe estar en el rango {min} a {max}!")
        except ValueError as e:
            num = None
            mostrar_error("*ERROR* El número no es válido!") if num is None else mostrar_error(e)

    return num


def pedir_entero(msj: str, min: int, max: int) -> int:
    """
    Solicita al usuario un número entero dentro de un rango definido.

    Args:
        msj (str): Mensaje que se mostrará al usuario.
        min (int): Valor mínimo permitido.
        max (int): Valor máximo permitido.

    Returns:
        int: Número entero válido ingresado por el usuario dentro del rango.
    """
    num = None
    while num is None:
        try:
            num = int(input(msj))
            if num < min or num > max:
                raise ValueError(f"*ERROR* El número debe estar en el rango {min} a {max}!")
        except ValueError as e:
            num = None
            mostrar_error("*ERROR* El número no es válido!") if num is None else mostrar_error(e)

    return num


# O también con una sola función y un parámetro que indique el tipo de dato de retorno
def pedir_numero_v1(msj: str, min: float, max: float, entero = True) -> float:
    """
    Solicita al usuario un número flotante dentro de un rango definido.

    Args:
        msj (str): Mensaje que se mostrará al usuario.
        min (int | float): Valor mínimo permitido.
        max (int | float): Valor máximo permitido.
        entero (bool): Indica el tipo de dato de retorno (int | float)

    Returns:
        int | float: Número válido ingresado por el usuario dentro del rango (int o float dependiendo del parámetro entero).
    """
    num = None
    while num is None:
        try:           
            num = int(input(msj)) if entero else float(input(msj))
            if num < min or num > max:
                raise ValueError(f"*ERROR* El número debe estar en el rango {min} a {max}!")
        except ValueError as e:
            num = None
            mostrar_error("*ERROR* El número no es válido!") if num is None else mostrar_error(e)

    return num


def generar_matriz(filas: int, columnas: int) -> tuple[tuple]:
    """
    Genera una matriz solicitando al usuario los elementos uno por uno.

    Args:
        filas (int): Número de filas de la matriz.
        columnas (int): Número de columnas de la matriz.

    Returns:
        tuple[list]: Matriz generada en forma de una tupla de listas.
    """    
    num_elementos = filas * columnas
    numeros = list()

    print("Dame los elementos:")

    for _ in range(num_elementos):
        numeros.append(pedir_numero_v1(">> ", CONFIG["valor"]["min"], CONFIG["valor"]["max"], False))

    return convertir_lista_en_matriz(numeros, columnas)


def convertir_lista_en_matriz(numeros: list, columnas: int) -> tuple[tuple]:
    """
    Convierte una lista en una matriz de dimensiones definidas.

    Args:
        numeros (list): Lista de números a convertir en matriz.
        columnas (int): Número de columnas de la matriz.

    Returns:
        tuple[tuple]: Matriz resultante representada como una tupla de tuplas.
    """
    fila = list()
    matriz = list()
    cont = 0

    for numero in numeros:
        cont += 1
        fila.append(numero)

        if cont == columnas:
            matriz.append(tuple(fila))
            fila = list()
            cont = 0

    return tuple(matriz)


def extraer_lista_numeros(matriz: tuple[tuple]) -> list:
    """
    Extrae todos los números de una matriz y los almacena en una lista.

    Args:
        matriz (tuple[tuple]): Matriz de la que se extraerán los números.

    Returns:
        list: Lista con todos los números de la matriz.
    """
    numeros = list()
    for fila in matriz:
        for valor in fila:
            numeros.append(valor)

    return numeros

    # O también...
    # return [valor for fila in matriz for valor in fila]


def ordenar_matriz(matriz: tuple[tuple], columnas: int) -> tuple[tuple]:
    """
    Ordena todos los elementos de una matriz de menor a mayor.

    Args:
        matriz (tuple[tuple]): Matriz a ordenar.
        columnas (int): Número de columnas de la matriz.

    Returns:
        tuple[tuple]: Matriz ordenada.
    """
    numeros = extraer_lista_numeros(matriz)
    numeros.sort()
    return convertir_lista_en_matriz(numeros, columnas)


def formatear_numero(num: float, pos_decimales: int, pos_totales: int) -> str:
    """
    Formatea un número para que siempre tenga 2 posiciones decimales
    y ocupe al menos 5 caracteres, incluyendo el signo si es negativo.

    Args:
        num (float): El número a formatear.

    Returns:
        str: El número formateado.
    """
    return f"{num:{pos_totales}.{pos_decimales}f}"


def mostrar_matriz(nombre: str, matriz: tuple[tuple], filas: int, columnas: int, pos_decimales: int, pos_totales: int):
    """
    Muestra una matriz en formato legible.

    Args:
        nombre (str): Nombre de la matriz que se está mostrando.
        matriz (tuple[tuple]): Matriz a mostrar.
        filas (int): Número de filas de la matriz.
        columnas (int): Número de columnas de la matriz.
        pos_decimales (int): Número de decimales a mostrar.
        pos_totales (int): Ancho total de cada número mostrado.
    """
    espacios = len(nombre)

    for fila in range(filas):
        if fila != filas - 1:
            print(" " * espacios, end = "")
        else:
            print(nombre, end = "")

        for col in range(columnas):
            print(f"{formatear_numero(matriz[fila][col], pos_decimales, pos_totales)} ", end = "")
        print()


def pedir_dimensiones_matriz(min: int, max: int) -> tuple[int]:
    """
    Solicita al usuario las dimensiones de una matriz (filas y columnas) dentro de un rango definido.

    Args:
        min (int): Valor mínimo permitido para las dimensiones.
        max (int): Valor máximo permitido para las dimensiones.

    Returns:
        tuple[int, int]: Una tupla con las dimensiones de la matriz en el formato (filas, columnas).
    """
    print("Dime las dimensiones de la matriz...")
    
    filas = pedir_numero_v1("Filas >> ", min, max)
    columnas = pedir_numero_v1("Columnas >> ", min, max)

    return filas, columnas


def guardar_json(nombre_fichero: str, datos: dict):
    """
    Guarda los datos en un fichero JSON.

    Args:
        nombre_fichero (str): Nombre del fichero JSON.
        datos (dict): Datos a guardar.
    """
    try:
        with open(nombre_fichero, "w") as archivo:
            json.dump(datos, archivo, indent = 4)

        return True

    except PermissionError:
        print(f"*ERROR* No tienes permisos para escribir en el archivo '{nombre_fichero}'.")

    except TypeError as e:
        print(f"*ERROR* Los datos no son serializables a JSON. Detalle: {e}")        

    except Exception as e:
        print(f"*ERROR* Problemas al guardar los datos: {e}")

    return False


def main():
    borrar_consola()
    
    filas, columnas = pedir_dimensiones_matriz(CONFIG["matriz"]["min"], CONFIG["matriz"]["max"])

    # Incluyo esta línea por si en una configuración diferente se permitieran mínimos inferiores a 1
    if filas <= 0 or columnas <= 0:
        print("\n\nNo es posible generar una matriz con filas o columnas inferiores a 1")
    else:
        print("\n")
        matriz_orig = generar_matriz(filas, columnas)
    
        print("\n")
        pos_decimales = CONFIG["valor"]["pos_decimales"]
        pos_totales = CONFIG["valor"]["pos_totales"]

        mostrar_matriz("Matriz 2x2 original: ", matriz_orig, filas, columnas, pos_decimales, pos_totales)

        matriz_ordenada = ordenar_matriz(matriz_orig, columnas)

        print("\n")

        mostrar_matriz("Matriz 2x2 ordenada: ", matriz_ordenada, filas, columnas, pos_decimales, pos_totales)
    
        datos = dict(CONFIG)
        datos["matriz_orig"] = matriz_orig
        datos["matriz_ordenada"] = matriz_ordenada

        if guardar_json("examenes/practica1_matriz_ordenada.json", datos):
            print("\nFichero JSON guardado correctamente!")

    print("\n")


if __name__ == "__main__":
    main()
