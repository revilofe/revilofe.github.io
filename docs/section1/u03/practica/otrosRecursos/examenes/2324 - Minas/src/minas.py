"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este código asume un nivel básico de interacción en la consola y no incluye validación exhaustiva de errores de usuario.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.

"""

import random

VALOR_CELDA_DEFECTO = "·"

# Acciones del jugador
MARCAR = "M"
REVELAR = "R"

# Dimensiones del tablero
FILAS = 8
COLUMNAS = 8
NUMERO_MINAS = 10

# Representación del tablero
VACIO = " "
MINA = "*"
BANDERA = "F"


def generar_tablero() -> list:
    """
    Esta función genera un tablero de juego vacío y coloca las minas en el tablero. Luego, calcula el número de minas adyacentes a cada celda.
    :return: tablero de juego
    """
    tablero = [[VACIO for _ in range(COLUMNAS)] for _ in range(FILAS)]
    colocar_minas(tablero)
    calcular_numeros(tablero)
    return tablero


def colocar_minas(tablero):
    """
    Esta función coloca las minas en el tablero de juego. Se asegura de que el número de minas colocadas sea igual a NUMERO_MINAS.
    """
    minas_plantadas = 0
    while minas_plantadas < NUMERO_MINAS:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if tablero[fila][columna] != MINA:
            tablero[fila][columna] = MINA
            minas_plantadas += 1


def calcular_numeros(tablero):
    """
    Esta función calcula el número de minas adyacentes a cada celda del tablero. Si la celda no contiene una mina, se coloca el número de minas adyacentes en la celda. Si la celda contiene una mina, se deja como está.
    :param tablero: tablero de juego
    """
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if tablero[fila][columna] != MINA:
                numero_minas = contar_minas_adyacentes(tablero, fila, columna)
                if numero_minas > 0:
                    tablero[fila][columna] = str(numero_minas)


def contar_minas_adyacentes(tablero, fila, columna):
    """
    Esta función cuenta el número de minas adyacentes a la celda(i,j) seleccionada.
    :param tablero: tablero de juego
    :param fila: fila de la celda seleccionada
    :param columna: columna de la celda seleccionada
    :return: número de minas adyacentes a la celda(i,j) seleccionada
    """
    minas = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= fila + i < FILAS and 0 <= columna + j < COLUMNAS:
                if tablero[fila + i][columna + j] == MINA:
                    minas += 1
    return minas


def imprimir_tablero(tablero):
    """
    Esta función toma el tablero como argumento e imprime cada celda del tablero.
    :param tablero: tablero de juego

    """
    print("  " + " ".join(str(i + 1) for i in range(COLUMNAS)))
    for i, fila in enumerate(tablero):
        print(str(i + 1), end=" ")
        for celda in fila:
            if celda == VACIO:
                celda = VALOR_CELDA_DEFECTO
            print(celda, end=" ")
        print()


def imprimir_tablero_oculto(tablero, celdas_reveladas, celdas_maracadas):
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
                if celda == VACIO:
                    celda = VALOR_CELDA_DEFECTO
                print(celda, end=" ")
            elif (i, j) in celdas_maracadas:
                print(BANDERA, end=" ")
            else:
                print(VACIO, end=" ")
        print()


def pedir_accion():
    """
    Esta función pide al jugador que ingrese una acción, una fila y una columna.
    Si la acción no es válida, se le pide al jugador que ingrese una acción nuevamente.
    Si la fila o la columna no son válidas, se le pide al jugador que ingrese una fila o columna nuevamente.
    :return: acción, fila y columna ingresadas por el jugador

    """
    accion_valida = False
    while not accion_valida:

        accion = input("Elige una acción (R para revelar, M para marcar): ").upper()
        fila = int(input("Ingresa la fila (1-8): ")) - 1
        columna = int(input("Ingresa la columna (1-8): ")) - 1

        if accion in [REVELAR, MARCAR] and 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
            accion_valida = True
        else:
            print("Acción inválida. Inténtalo de nuevo.")
    return accion, fila, columna


def revelar_celda(tablero, celdas_reveladas, celdas_marcadas, fila, columna):
    """
    Esta función revela la celda seleccionada.
    Si la celda contiene una mina, devuelve False.
    Si la celda no contiene una mina, se agrega a celdas_reveladas y devuelve True.
    :param tablero: tablero de juego
    :param celdas_reveladas: conjunto de celdas que ya han sido mostradas al jugador
    :param celdas_marcadas: conjunto de celdas que han sido marcadas con una bandera
    :param fila: fila de la celda seleccionada
    :param columna: columna de la celda seleccionada
    :return: False si la celda contiene una mina, True en caso contrario

    """
    revelada = True

    if tablero[fila][columna] == MINA:  # La celda contiene una mina
        revelada = False
    elif tablero[fila][columna] != VACIO:  # La celda contiene un número
        celdas_reveladas.add((fila, columna))
        celdas_marcadas.discard((fila, columna))
    else:  # La celda está vacía
        revelar_celdas_vacias(tablero, celdas_reveladas, celdas_marcadas, fila, columna)

    return revelada


def revelar_celdas_vacias(tablero, celdas_reveladas, celdas_marcadas, fila, columna):
    """
    Esta función revela la celda seleccionada. Si está vacía, revela recursivamente las celdas vacías adyacentes a la celda seleccionada.
    :param tablero: tablero de juego
    :param celdas_reveladas: conjunto de celdas que ya han sido mostradas al jugador
    :param celdas_marcadas: conjunto de celdas que han sido marcadas con una bandera
    :param fila: fila de la celda seleccionada
    :param columna: columna de la celda seleccionada

    """
    if (fila, columna) not in celdas_reveladas:
        celdas_reveladas.add((fila, columna))
        celdas_marcadas.discard((fila, columna))
        # Si la celda esta vacía, revela también las celdas adyacentes
        if tablero[fila][columna] == VACIO:
            # Recursivamente revela las celdas adyacentes
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= fila + i < FILAS and 0 <= columna + j < COLUMNAS:
                        revelar_celdas_vacias(tablero, celdas_reveladas, celdas_marcadas, fila + i, columna + j)


def marcar_celda(tablero, celdas_marcadas, fila, columna):
    """
    Esta función marca la celda seleccionada con una bandera.
    :param tablero: tablero de juego
    :param celdas_reveladas: conjunto de celdas que ya han sido mostradas al jugador
    :param fila: fila de la celda seleccionada
    :param columna: columna de la celda seleccionada

    """
    if (fila, columna) not in celdas_marcadas:
        celdas_marcadas.add((fila, columna))


def verificar_victoria(tablero, celdas_reveladas) -> bool:
    """
    Esta función verifica si el jugador ha ganado el juego. Que se daŕa solo y solo si todas las celdas que no contienen
     minas han sido reveladas.
    :param tablero: tablero de juego
    :param celdas_reveladas: conjunto de celdas que ya han sido mostradas al jugador
    :return: True si el jugador ha ganado, False de lo contrario
    """
    victoria = True

    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if tablero[fila][columna] != MINA and (fila, columna) not in celdas_reveladas:
                victoria = False
    return victoria


def jugar():
    """
    Esta función ejecuta el juego. Primero genera un tablero de juego, luego pide al jugador que ingrese una acción, una fila y una columna. Luego, revela la celda seleccionada y verifica si el jugador ha ganado o perdido el juego. Si el jugador ha ganado o perdido, termina el juego. Si no, pide al jugador que ingrese una acción, una fila y una columna nuevamente.
    """
    tablero = generar_tablero()
    celdas_reveladas = set()
    celdas_marcadas = set()
    terminar_juego = False

    while not terminar_juego:

        imprimir_tablero_oculto(tablero, celdas_reveladas, celdas_marcadas)

        accion, fila, columna = pedir_accion()

        if accion == REVELAR:
            celda_con_mina = not revelar_celda(tablero, celdas_reveladas, celdas_marcadas, fila, columna)

            if celda_con_mina:
                print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡Oh no! ¡Has pisado una mina!!!!!!!!!!!!!!!!!!!!!")
                imprimir_tablero(tablero)
                terminar_juego = True
            elif verificar_victoria(tablero, celdas_reveladas):
                print("¡Felicidades! ¡Has ganado el juego!")
                imprimir_tablero(tablero)
                terminar_juego = True
        elif accion == MARCAR:
            marcar_celda(tablero, celdas_marcadas, fila, columna)


if __name__ == "__main__":
    jugar()
