"""
Ejercicio: El Juego de la Búsqueda del Tesoro en la Isla

Descripción del Problema:

Los estudiantes están atrapados en una isla desierta y deben encontrar un tesoro escondido para escapar.
La isla está representada como una cuadrícula donde cada celda puede contener una pista que indica
la dirección general del tesoro, nada o una trampa que le impide el paso.
Los estudiantes deben usar su conocimiento de estructuras de datos y control de flujo para interpretar
las pistas, evitar las trampas y encontrar el tesoro.


--
PENDIENTE DE TERMINAR!!!!!!!!

La idea es añadir errores para que corrijan el codigo los estudiantes.
Solicitarles que modifiquen el codigo para que almacenen las posiciones por las que va pasando el jugador, y se pinte en el mapa.

"""

import random

# Constantes para el mapa
TESORO = "X"
TRAMPA = "!"
ARRIBA = "^"
ABAJO = "V"
DERECHA = ">"
IZQUIERDA = "<"
DIMENSIONES = 5
MOVIMIENTOS = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}
COLUMNAS = 1
FILAS = 0


def genera_pista(posicion_tesoro: tuple, posicion: tuple) -> str:
    """
    Genera una pista para el mapa
    """
    # FILAS
    if posicion_tesoro[COLUMNAS] == posicion[COLUMNAS] or (
            posicion_tesoro[FILAS] != posicion[FILAS] and random.choice(["fila", "columna"]) == "fila"):
        pista = ABAJO
        if posicion_tesoro[FILAS] < posicion[FILAS]:
            pista = ARRIBA
    # COLUMNAS
    else:
        pista = DERECHA
        if posicion_tesoro[COLUMNAS] < posicion[COLUMNAS]:
            pista = IZQUIERDA
    return pista


def generar_mapa() -> list:
    """Genera un mapa de la isla con pistas y trampas correctamente colocadas. Con el siguiente contenido:
        - "X" indica el tesoro, y es única en el mapa.
        - "!" indica una trampa, y puede haber varias.
        - ^: indica que el tesoro esta una o mas filas arriba.
        - <: indica que el tesoro esta una o mas columnas a la izquierda.
        - >: indica que el tesoro esta una o mas columnas a la izquierda.
        - v: indica que el tesoro esta una o mas filas abajo.

    Genera mapas que puede que no tengan camino a la solución.
    """

    mapa = [[" " for _ in range(DIMENSIONES)] for _ in range(DIMENSIONES)]
    tesoro_x, tesoro_y = random.randint(0, DIMENSIONES - 1), random.randint(0, DIMENSIONES - 1)
    mapa[tesoro_x][tesoro_y] = TESORO

    # Colocar pistas y trampas
    for i in range(DIMENSIONES):
        for j in range(DIMENSIONES):
            if mapa[i][j] != TESORO:
                # Decidir aleatoriamente si colocar una pista o una trampa
                mapa[i][j] = random.choice([genera_pista((tesoro_x, tesoro_y), (i, j))] + [TRAMPA, " "])

    return mapa


def procesar_movimiento(x, y, mapa) -> int:
    """Procesa el movimiento del jugador y devuelve el código de resultado."""
    if not (0 <= x < DIMENSIONES and 0 <= y < DIMENSIONES):
        return 1  # Código de error para movimiento fuera de rango
    elif mapa[x][y] == TESORO:
        return 2  # Código para tesoro encontrado
    elif mapa[x][y] == TRAMPA:
        return 3  # Código para trampa encontrada
    else:
        return 4  # Código para pista encontrada


def imprimir_mapa_oculto(mapa):
    """Imprime el mapa sin revelar el tesoro ni las trampas."""
    for fila in mapa:
        print(" ".join(["?" if celda != " " else " " for celda in fila]))


def imprimir_mapa(mapa):
    """Imprime el mapa sin revelar el tesoro ni las trampas."""
    for fila in mapa:
        print(fila)


def pedir_movimiento(mapa):
    """Pide al jugador su próximo movimiento y devuelve las coordenadas de desplazamiento."""
    while True:
        entrada = input("Ingresa tu movimiento (formato: 'u:arriba', 'd:abajo', 'l:izquierda', 'r:derecha', q:salir): ")
        if entrada in MOVIMIENTOS:
            return MOVIMIENTOS[entrada]
        elif entrada == "s":
            imprimir_mapa(mapa)
        else:
            print("Movimiento no reconocido. Usa 'arriba', 'abajo', 'izquierda' o 'derecha'.")


def jugar():
    """Función principal para iniciar el juego."""
    mapa = generar_mapa()
    posicion_jugador = (DIMENSIONES // 2, DIMENSIONES // 2)  # Iniciar al jugador en el centro del mapa
    while True:
        imprimir_mapa_oculto(mapa)
        print(f"Tu posición es {posicion_jugador}")
        direccion = pedir_movimiento(mapa)
        nueva_posicion = (posicion_jugador[0] + direccion[0], posicion_jugador[1] + direccion[1])
        resultado = procesar_movimiento(nueva_posicion[0], nueva_posicion[1], mapa)
        if resultado == 1:
            print("Movimiento inválido. Estás intentando salir del mapa.")
        elif resultado == 2:
            print("¡Has encontrado el tesoro y ganado el juego!")
            break
        elif resultado == 3:
            print("Es una trampa. Intenta de nuevo.")
        elif resultado == 4:
            pista = mapa[nueva_posicion[0]][nueva_posicion[1]]
            print(f"La pista es: {pista}")
            posicion_jugador = nueva_posicion  # Actualizar la posición del jugador


if __name__ == "__main__":
    jugar()
