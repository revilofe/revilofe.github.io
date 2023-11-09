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

Lo siguiente es un ejemplo de mapa del tesoro con dimension 5, con el tesoro en la posicion (0,0) y el jugador en la posicion (2,2)
columnas  0    1    2    3    4
filas
0       ["X", " ", "!", " ", "<"]
1       ["!", "^", " ", "<", "!"]
2       ["^", "^", "!", "<", " "]
3       [" ", "<", " ", "!", "^"]
4       ["!", "<", "!", " ", "^"]

"""

import random

DIMENSIONES = 5

# Constantes para el mapa
TESORO = "X"
TRAMPA = "!"
VACIA = " "

# Constantes para las pistas de los movimientos
ARRIBA = "^"
ABAJO = "V"
DERECHA = ">"
IZQUIERDA = "<"

DESCONOCIDO = "?"

# Constantes para el resultado del movimiento
MOVIMIENTO_INVALIDO = 1
TESORO_ENCONTRADO = 2
TRAMPA_ENCONTRADA = 3
PISTA_ENCONTRADA = 4
VACIA_ENCONTRADA = 5
MOVIMIENTOS_NO_PERMITIDO = [MOVIMIENTO_INVALIDO, TRAMPA_ENCONTRADA]

# Movimientos permitidos
MOVIMIENTOS = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}

# Constantes para las posiciones
FILAS = 0
COLUMNAS = 1


def genera_pista(posicion_tesoro: tuple, posicion: tuple) -> str:
    """
    Genera una pista para el mapa, en función de donde se encuentre el tesoro y la posición de la celda para la que se genera la pista.
    :param posicion_tesoro: La posición del tesoro
    :param posicion: La posición de la celda para la que se genera la pista
    :return: La pista generada

    """
    # A veces se generará una pisa sobre la filas (movimienot arriba, abajo) , y otras veces sobre las columnas (movimiento izquierda, derecha)
    # FILAS
    if posicion_tesoro[COLUMNAS] == posicion[COLUMNAS] or (
            posicion_tesoro[FILAS] != posicion[FILAS] and random.choice([FILAS, COLUMNAS]) == FILAS):
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
    :return: El mapa generado.
    """

    mapa = [[VACIA for _ in range(DIMENSIONES)] for _ in range(DIMENSIONES)]
    tesoro_x, tesoro_y = random.randint(0, DIMENSIONES - 1), random.randint(0, DIMENSIONES - 1)
    mapa[tesoro_x][tesoro_y] = TESORO

    # Colocar pistas y trampas
    for i in range(DIMENSIONES):
        for j in range(DIMENSIONES):
            if mapa[i][j] != TESORO:
                # Decidir aleatoriamente si colocar una pista o una trampa
                mapa[i][j] = random.choice([genera_pista((tesoro_x, tesoro_y), (i, j))] + [TRAMPA, " "])

    return mapa


def procesar_movimiento(posicion, mapa) -> int:
    """Procesa el movimiento del jugador y devuelve el código de resultado.
    :param posicion: La posición a la que se mueve el jugador.
    :param mapa: El mapa del juego.
    :return: El código de resultado del movimiento.

    """

    resultado = VACIA_ENCONTRADA
    if not (0 <= posicion[FILAS] < DIMENSIONES and 0 <= posicion[COLUMNAS] < DIMENSIONES):
        resultado = MOVIMIENTO_INVALIDO  # Código de error para movimiento fuera de rango
    elif mapa[posicion[FILAS]][posicion[COLUMNAS]] == TESORO:
        resultado = TESORO_ENCONTRADO  # Código para tesoro encontrado
    elif mapa[posicion[FILAS]][posicion[COLUMNAS]] == TRAMPA:
        resultado = 3  # Código para trampa encontrada
    elif mapa[posicion[FILAS]][posicion[COLUMNAS]] != VACIA:
        resultado = 4  # Código para pista encontrada

    return resultado

def imprimir_mapa_oculto(mapa):
    """Imprime el mapa sin revelar el tesoro ni las trampas."""
    for fila in mapa:
        print(" ".join([DESCONOCIDO if celda != VACIA else VACIA for celda in fila]))


def imprimir_mapa(mapa):
    """
    Imprime el mapa sin revelar el tesoro ni las trampas.
    :param mapa: El mapa a imprimir.
    """
    for fila in mapa:
        print(fila)


def pedir_movimiento(mapa):
    """
    Pide al jugador su próximo movimiento y devuelve las coordenadas de desplazamiento.
    return: el movimiento del jugador
    """

    entrada = input("Ingresa tu movimiento (formato: 'u:arriba', 'd:abajo', 'l:izquierda', 'r:derecha', q:salir): ")
    entradaCorrecta = False
    while not entradaCorrecta:
        if entrada in MOVIMIENTOS or entrada == "q":
            return entrada
        elif entrada == "s":
            imprimir_mapa(mapa)
        entrada = input(
                "Ingresa tu movimiento (formato: 'u:arriba', 'd:abajo', 'l:izquierda', 'r:derecha', q:salir): ")



def obtener_nueva_posicion(posicion_jugador, movimiento):
    """
    Realiza el movimiento del jugador y devuelve la nueva posición.

    :param posicion_jugador: La posición actual del jugador.
    :param movimiento: El movimiento a realizar.
    :return: La nueva posición del jugador.
    """

    direccion = MOVIMIENTOS[movimiento]
    nueva_posicion = (posicion_jugador[FILAS] + direccion[FILAS], posicion_jugador[COLUMNAS] + direccion[COLUMNAS])
    return nueva_posicion


def muestra_resultado_del_movimiento(resultado, nueva_posicion, mapa):
    """
    Muestra en consola el resultado del movimiento del jugador.
    :param resultado: El resultado del movimiento.
    :param nueva_posicion: La nueva posición del jugador.
    :param mapa: El mapa del juego.

    """
    if resultado == MOVIMIENTO_INVALIDO:
        print("Movimiento inválido. Estás intentando salir del mapa.")
    elif resultado == TESORO_ENCONTRADO:
        print("¡Has encontrado el tesoro y ganado el juego!")
        final = True
    elif resultado == TRAMPA_ENCONTRADA:
        print("Es una trampa. Intenta de nuevo.")
    elif resultado == PISTA_ENCONTRADA:
        pista = mapa[nueva_posicion[FILAS]][nueva_posicion[COLUMNAS]]
        print(f"Hay una pista!!!! La pista es: {pista}")

def jugar():
    """Función principal para iniciar el juego."""


    # Iniciar el mapa y al jugador en el centro del mapa
    mapa = generar_mapa()
    posicion_jugador = (DIMENSIONES // 2, DIMENSIONES // 2)
    final = False

    imprimir_mapa_oculto(mapa)
    print(f"Tu posición es {posicion_jugador}")

    movimiento = pedir_movimiento(mapa)
    while movimiento != "q" and not final: # Loop principal del juego. El juego termina cuando el jugador ingresa "q".


        # Obtener la nueva posición del jugador y procesar el movimiento
        nueva_posicion = obtener_nueva_posicion(posicion_jugador, movimiento)
        resultado = procesar_movimiento(nueva_posicion, mapa)
        muestra_resultado_del_movimiento(resultado, nueva_posicion, mapa)

        final = resultado == TESORO_ENCONTRADO
        if not final:
            # Actualizar la posición del jugador si el movimiento es válido
            if resultado not in MOVIMIENTOS_NO_PERMITIDO:
                posicion_jugador = nueva_posicion

            # Imprimir el mapa y la posición del jugador
            imprimir_mapa_oculto(mapa)
            print(f"Tu posición es {posicion_jugador}")

            # Pedir el siguiente movimiento
            movimiento = pedir_movimiento(mapa)




if __name__ == "__main__":
    jugar()
