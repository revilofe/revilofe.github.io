"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este código asume un nivel básico de interacción en la consola y no incluye validación exhaustiva de errores de usuario.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.

"""

import random

# Dimensiones del tablero
FILAS = 8
COLUMNAS = 8
NUMERO_MINAS = 10

# Representación del tablero
VACIO = " "
MINA = "*"
BANDERA = "F"

def generar_tablero():
    tablero = [[VACIO for _ in range(COLUMNAS)] for _ in range(FILAS)]
    colocar_minas(tablero)
    calcular_numeros(tablero)
    return tablero

def colocar_minas(tablero):
    minas_plantadas = 0
    while minas_plantadas < NUMERO_MINAS:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if tablero[fila][columna] != MINA:
            tablero[fila][columna] = MINA
            minas_plantadas += 1

def calcular_numeros(tablero):
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if tablero[fila][columna] == MINA:
                continue
            numero_minas = contar_minas_adyacentes(tablero, fila, columna)
            if numero_minas > 0:
                tablero[fila][columna] = str(numero_minas)

def contar_minas_adyacentes(tablero, fila, columna):
    minas = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= fila + i < FILAS and 0 <= columna + j < COLUMNAS:
                if tablero[fila + i][columna + j] == MINA:
                    minas += 1
    return minas

def imprimir_tablero(tablero, revelar_minas=False):
    for fila in tablero:
        for celda in fila:
            if celda == MINA and not revelar_minas:
                print(VACIO, end=" ")
            else:
                print(celda, end=" ")
        print()

def imprimir_tablero_oculto(tablero, celdas_reveladas):
    """
    Esta función toma el tablero y el conjunto celdas_reveladas como argumentos.
    Imprime cada celda del tablero: si la celda ha sido revelada o marcada con una bandera,
    muestra su contenido actual (número, vacío o bandera); si no, muestra la celda como vacía.
    :param tablero: tablero de juego
    :param celdas_reveladas: conjunto de celdas que ya han sido mostradas al jugador
    """
    print("  " + " ".join(str(i + 1) for i in range(COLUMNAS)))
    for i, fila in enumerate(tablero):
        print(str(i + 1), end=" ")
        for j, celda in enumerate(fila):
            if (i, j) in celdas_reveladas:
                print(celda, end=" ")
            elif celda == BANDERA:
                print(BANDERA, end=" ")
            else:
                print(VACIO, end=" ")
        print()

def jugar():
    tablero = generar_tablero()
    celdas_reveladas = set()
    terminado = False

    while not terminado:
        imprimir_tablero_oculto(tablero, celdas_reveladas)
        accion, fila, columna = pedir_accion()

        if accion == "R":
            if tablero[fila][columna] == MINA:
                print("¡Oh no! ¡Has pisado una mina!")
                imprimir_tablero(tablero, revelar_minas=True)
                terminado = True
            else:
                revelar_celda(tablero, celdas_reveladas, fila, columna)
                if verificar_victoria(tablero, celdas_reveladas):
                    print("¡Felicidades! ¡Has despejado todas las minas!")
                    terminado = True
        elif accion == "M":
            marcar_celda(tablero, celdas_reveladas, fila, columna)


def pedir_accion():
    accion_valida = False
    while not accion_valida:
        accion = input("Elige una acción (R para revelar, M para marcar): ").upper()
        fila = int(input("Ingresa la fila: ")) - 1
        columna = int(input("Ingresa la columna: ")) - 1
        if accion in ["R", "M"] and 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
            accion_valida = True
        else:
            print("Acción inválida. Inténtalo de nuevo.")
    return accion, fila, columna


def revelar_celda(tablero, celdas_reveladas, fila, columna):
    if tablero[fila][columna] == VACIO:
        revelar_celdas_vacias(tablero, celdas_reveladas, fila, columna)
    else:
        celdas_reveladas.add((fila, columna))


def revelar_celdas_vacias(tablero, celdas_reveladas, fila, columna):
    # Lógica para revelar celdas vacías adyacentes
    pass


def marcar_celda(tablero, celdas_reveladas, fila, columna):
    if (fila, columna) not in celdas_reveladas:
        celdas_reveladas.add((fila, columna))
        tablero[fila][columna] = BANDERA


def verificar_victoria(tablero, celdas_reveladas):
    # Lógica para verificar si el jugador ha ganado
    pass


if __name__ == "__main__":
    jugar()
