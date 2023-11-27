"""
Ejercicio: El Juego de la Búsqueda del Tesoro en la Isla

Descripción del Problema:

Los estudiantes están atrapados en una isla desierta y deben encontrar un tesoro escondido para escapar.

La isla está representada como una cuadrícula donde cada celda puede contener una pista que indica
la dirección general del tesoro, nada o una trampa que le impide el paso.

Los estudiantes deben usar su conocimiento de estructuras de datos y control de flujo para interpretar
las pistas, evitar las trampas y encontrar el tesoro.

Este es un ejemplo de mapa del tesoro con dimensión 5, con el tesoro en la posicion (0,0) y el jugador en la posicion (2,2)

El programa muestra lo siguiente al  usuario:

?   ?   ?
? ? ? ? ?
  ?   ?      
  ?   ? ?
? ? ?   ?
Tu posición es (2, 2)
Ingresa tu movimiento (formato: 'u:arriba', 'd:abajo', 'l:izquierda', 'r:derecha', q:salir):

Internamente tendréis una lista anidada para contener un mapa similar al siguiente:

columnas  0    1    2    3    4
filas
0       ["X", " ", "!", " ", "<"]
1       ["!", "^", "!", "<", "!"]
2       [" ", "^", " ", "<", " "]
3       [" ", "<", " ", "!", "^"]
4       ["!", "<", "!", " ", "^"]


Se pide realizar lo siguiente:

CORRECCIÓN DE ERRORES O PROBLEMAS:

* 1: El juego no se puede jugar()

* 2: Acaba la función generar_mapa() sino no vas a poder hacer nada.

* 3: Existen errores típicos de no declarar correctamente las funciones.

* 4: Las funciones pedir_movimiento() y obtener_nueva_posicion() tienen algo raro, ya que aparentemente parece que son correctas, pero dan problemas... igual depurando puedes aclararte y corregirlo.

* 5: Corrige otros errores sintácticos que está indicando Visual Studio Code para evitar problemas y pasar a las mejoras.

MEJORAS:

* 1: Mostrar los números del tablero asociados a las filas y las columnas.
     Pero las filas y columnas que empiecen en el número 1 visualmente.

   1 2 3 4 5
  -----------
1 |? ? ? ? ?|
2 |?     ? ?|
3 |?       ?|
4 |? ? ? ? ?|
5 |  ? ? ? ?|
  -----------

* 2: Mostrar la posición del jugador con respecto a la numeración visual del mapa.

Tu posición es (3, 3)  #aunque internamente esté en la posición (2, 2)

* 3: Evitar que en la posición inicial del jugador en el mapa se genere una pista o una trampa.

* 4: Limpiar la consola cada vez que realices un movimiento y dejar el mensaje de la pista o trampa en la zona superior de la consola, justo arriba del mapa.
    Cuando se encuentra el tesoro no debe borrar la consola, el mensaje de la posición en la que se encuentra el tesoro aparecerá abajo y finalizará el juego.

* 5 (DIFÍCIL): Mostrar un símbolo para el jugador. Para ello, una solución es cambiar el código de la función imprimir_mapa_oculto()
"""

import os
import random

DIMENSIONES = 5

# Constantes para el mapa
CELDA_TESORO = "X"
CELDA_TRAMPA = "!"
CELDA_VACIA = " "
CELDA_JUGADOR = "J"
CELDA_CAMINO_JUGADOR = "."

# Constantes para las pistas de los movimientos
ARRIBA = "^"
ABAJO = "v"
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
SALIR = "q"
MOVIMIENTOS = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1), SALIR: (0, 0)}

# Constantes para las posiciones
FILAS = 0
COLUMNAS = 1

# Código oculto del programador para realizar alguna acción que el usuario no sabe que existe. Si encuentras para qué se utiliza igual te sirve en tu aventura...
CODIGO_OCULTO_PROGRAMADOR = "s"


def inicializar_juego() -> tuple:
    """
    Inicializa el juego, mostrando el mapa y la posición del jugador.
    :return: El mapa y la posición del jugador.
    """
    posicion_jugador = posicion_inicial_del_jugador()
    mapa = generar_mapa()
    while mapa[posicion_jugador[FILAS]][posicion_jugador[COLUMNAS]] == CELDA_TESORO:
        mapa = generar_mapa()

    return mapa, posicion_jugador


def posicion_inicial_del_jugador() -> tuple:
    """ Devuelve la posición inicial del jugador. Actualmente es la posición central del mapa.
    :return: La posición inicial del jugador.
    """
    return DIMENSIONES // 2, DIMENSIONES // 2


def crear_camino(posicion_tesoro: tuple, posicion_jugador: tuple) -> set:
    """ Edu???
    Crea un camino desde la posición del jugador al tesoro.
    :param posicion_tesoro: La posición del tesoro.
    :param posicion_jugador: La posición del jugador.
    :return: El camino desde la posición del jugador al tesoro.
    """
    camino = set()
    jugador_x, jugador_y = posicion_jugador[FILAS], posicion_jugador[COLUMNAS]
    tesoro_x, tesoro_y = posicion_tesoro[FILAS], posicion_tesoro[COLUMNAS]
    # Agregar la posición inicial del jugador al camino para garantizar que el tesoro sea alcanzable
    camino.add((jugador_x, jugador_y))
    while (jugador_x, jugador_y) != (tesoro_x, tesoro_y):
        if jugador_x < tesoro_x:
            jugador_x += 1
        elif jugador_x > tesoro_x:
            jugador_x -= 1
        elif jugador_y < tesoro_y:
            jugador_y += 1
        elif jugador_y > tesoro_y:
            jugador_y -= 1
        camino.add((jugador_x, jugador_y))
    return camino


def generar_mapa_con_solucion():
    """ Edu???
    Genera un mapa de la isla con pistas y trampas correctamente colocadas. Crea un camino desde la posición
    del jugador al tesoro antes de llenar el resto del mapa con pistas y trampas. Al hacerlo, se asegura de que siempre
    haya un camino viable hasta el tesoro. El camino se agrega a un conjunto para evitar que se coloquen trampas en él
    y para que al final se asegure de que todas las posiciones del camino tienen una pista que apunta en la
    dirección correcta (excepto la posición inicial del jugador, que debe permanecer como está)

    Con el siguiente contenido:
    - "X" indica el tesoro, y es única en el mapa.
    - "!" indica una trampa, y puede haber varias.
    - ^: indica que el tesoro esta una o mas filas arriba.
    - <: indica que el tesoro esta una o mas columnas a la izquierda.
    - >: indica que el tesoro esta una o mas columnas a la izquierda.
    - v: indica que el tesoro esta una o mas filas abajo.

    """

    mapa = [[CELDA_VACIA for _ in range(DIMENSIONES)] for _ in range(DIMENSIONES)]
    tesoro_x, tesoro_y = random.randint(0, DIMENSIONES - 1), random.randint(0, DIMENSIONES - 1)
    mapa[tesoro_x][tesoro_y] = CELDA_TESORO  # Colocar el tesoro

    # Crear un camino garantizado al tesoro
    camino = crear_camino((tesoro_x, tesoro_y), posicion_inicial_del_jugador())

    # Rellenar el mapa con pistas y trampas, solo si la celda no está en el camino y no es el tesoro
    for i in range(DIMENSIONES):
        for j in range(DIMENSIONES):
            if (i, j) not in camino and (i, j) != (tesoro_x, tesoro_y):
                # Decidir aleatoriamente si colocar una pista, una trampa o vacia.
                opciones = [genera_pista((tesoro_x, tesoro_y), (i, j))]
                opciones += [CELDA_TRAMPA]
                opciones += [CELDA_VACIA]
                mapa[i][j] = random.choice(opciones)

    # Asegurarse de que las celdas del camino tengan pistas correctas
    for pos_x, pos_y in camino:
        # Evitar sobreescribir la posición inicial del jugador y la del tesoro
        if (pos_x, pos_y) != posicion_inicial_del_jugador() and (pos_x, pos_y) != (tesoro_x, tesoro_y):
            mapa[pos_x][pos_y] = genera_pista((tesoro_x, tesoro_y), (pos_x, pos_y))

    return mapa


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

    # Generar el mapa vacio y colocar el tesoro
    mapa = [[CELDA_VACIA for _ in range(DIMENSIONES)] for _ in range(DIMENSIONES)]
    tesoro_x, tesoro_y = random.randint(0, DIMENSIONES - 1), random.randint(0, DIMENSIONES - 1)
    mapa[tesoro_x][tesoro_y] = CELDA_TESORO

    # Colocar pistas y trampas
    for i in range(DIMENSIONES):
        for j in range(DIMENSIONES):
            if mapa[i][j] != CELDA_TESORO and (i, j) != posicion_inicial_del_jugador():
                # Decidir aleatoriamente si colocar una pista, una trampa o vacia.
                opciones = [genera_pista((tesoro_x, tesoro_y), (i, j))]
                opciones += [CELDA_TRAMPA]
                opciones += [CELDA_VACIA]
                mapa[i][j] = random.choice(opciones)

    return mapa


def genera_pista(posicion_tesoro: tuple, posicion: tuple):
    """
    Genera una pista para el mapa, en función de donde se encuentre el tesoro.
    Decidirá si la pista es sobre la fila o la columna basada en la aleatoriedad. Ademas tiene en cuenta que
    si está en la misma fila que el tesoro, generará la pista para las columnas. Y si está en la misma columna
    generará la pista para la fila.
    :param posicion_tesoro: La posición del tesoro.
    :param posicion: La posición para la que se genera la pista.
    :return: La pista generada.
    """
    if random.choice([FILAS, COLUMNAS]) == FILAS:
        return genera_pista_filas(posicion_tesoro, posicion) or genera_pista_columnas(posicion_tesoro, posicion)
    else:
        return genera_pista_columnas(posicion_tesoro, posicion) or genera_pista_filas(posicion_tesoro, posicion)


def genera_pista_filas(posicion_tesoro: tuple, posicion: tuple):
    """Genera una pista basada en la comparación de filas.
    :param posicion_tesoro: La posición del tesoro.
    :param posicion: La posición para la que se genera la pista.
    :return: La pista generada.

    """
    if posicion_tesoro[FILAS] < posicion[FILAS]:
        return ARRIBA
    elif posicion_tesoro[FILAS] > posicion[FILAS]:
        return ABAJO
    return ""


def genera_pista_columnas(posicion_tesoro: tuple, posicion: tuple):
    """Genera una pista basada en la comparación de columnas.
    :param posicion_tesoro: La posición del tesoro.
    :param posicion: La posición para la que se genera la pista.
    :return: La pista generada.
    """
    if posicion_tesoro[COLUMNAS] < posicion[COLUMNAS]:
        return IZQUIERDA
    elif posicion_tesoro[COLUMNAS] > posicion[COLUMNAS]:
        return DERECHA
    return ""


def pedir_movimiento(mapa: list):
    """
    Pide al jugador su próximo movimiento y devuelve las coordenadas de desplazamiento.
    return: el movimiento del jugador
    """
    entrada_correcta = False

    entrada = input("Ingresa tu movimiento (formato: 'u:arriba', 'd:abajo', 'l:izquierda', 'r:derecha', q:salir): ")
    while not entrada_correcta:
        if entrada in MOVIMIENTOS:
            entrada_correcta = True
        elif entrada == CODIGO_OCULTO_PROGRAMADOR:
            imprimir_mapa(mapa)

        if not entrada_correcta:
            entrada = input(
                "Ingresa tu movimiento (formato: 'u:arriba', 'd:abajo', 'l:izquierda', 'r:derecha', q:salir): ")

    return entrada


def obtener_nueva_posicion(posicion_jugador: tuple, movimiento: str) -> tuple:
    """
    Realiza el movimiento del jugador y devuelve la nueva posición.

    :param posicion_jugador: La posición actual del jugador.
    :param movimiento: El movimiento a realizar.
    :return: La nueva posición del jugador.
    """
    direccion = MOVIMIENTOS[movimiento]
    nueva_posicion = (posicion_jugador[FILAS] + direccion[FILAS], posicion_jugador[COLUMNAS] + direccion[COLUMNAS])
    return nueva_posicion


def procesar_movimiento(posicion: tuple, mapa: list) -> int:
    """Procesa el movimiento del jugador y devuelve el código de resultado.
    :param posicion: La posición a la que se mueve el jugador.
    :param mapa: El mapa del juego.
    :return: El código de resultado del movimiento.
    """
    resultado = VACIA_ENCONTRADA
    if not (0 <= posicion[FILAS] < DIMENSIONES and 0 <= posicion[COLUMNAS] < DIMENSIONES):
        resultado = MOVIMIENTO_INVALIDO  # Código de error para movimiento fuera de rango
    elif mapa[posicion[FILAS]][posicion[COLUMNAS]] == CELDA_TESORO:
        resultado = TESORO_ENCONTRADO  # Código para tesoro encontrado
    elif mapa[posicion[FILAS]][posicion[COLUMNAS]] == CELDA_TRAMPA:
        resultado = TRAMPA_ENCONTRADA  # Código para trampa encontrada
    elif mapa[posicion[FILAS]][posicion[COLUMNAS]] != CELDA_VACIA:
        resultado = PISTA_ENCONTRADA  # Código para pista encontrada

    return resultado


def simbolo_celda(mapa, fila, columna, posicion_jugador):
    """ DCS??? Modificado
    Retorna el símbolo a pintar en la celda
    """
    if (fila, columna) == posicion_jugador:
        return CELDA_JUGADOR
    elif mapa[fila][columna] not in {CELDA_VACIA, CELDA_CAMINO_JUGADOR}:
        return DESCONOCIDO
    else:
        return mapa[fila][columna]


def imprimir_mapa_oculto(mapa: list, posicion_jugador):
    """ DCS??? Modificado
    Imprime el mapa sin revelar el tesoro ni las trampas."""
    num_columnas = " ".join(str(i + 1) for i in range(DIMENSIONES))
    print("   " + num_columnas)
    print("  " + "-" * (len(num_columnas) + 2))

    for fila in range(DIMENSIONES):
        print(f"{fila + 1} |", end = "")
        for columna in range(DIMENSIONES):
            if columna < DIMENSIONES - 1:
                print(simbolo_celda(mapa, fila, columna, posicion_jugador), end =" ")
            else:
                print(simbolo_celda(mapa, fila, columna, posicion_jugador) + "|")
    print("  " + "-" * (len(num_columnas) + 2))


def imprimir_mapa_oculto_OLD(mapa: list):
    """ DCS??? Función original
    Imprime el mapa sin revelar el tesoro ni las trampas."""
    for fila in mapa:
        print(" ".join([DESCONOCIDO if celda != CELDA_VACIA else CELDA_VACIA for celda in fila]))


def imprimir_mapa(mapa: list):
    """
    Imprime el mapa.
    :param mapa: El mapa a imprimir.
    """
    for fila in mapa:
        print(fila)


def borrar_consola():
    """ DCS??? Nuevo
    Limpiar la consola."""
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def muestra_resultado_del_movimiento(resultado: int, nueva_posicion: tuple, mapa: list):
    """ DCS??? Modificado
    Muestra en consola el resultado del movimiento del jugador.
    :param resultado: El resultado del movimiento.
    :param nueva_posicion: La nueva posición del jugador.
    :param mapa: El mapa del juego.
    """
    if resultado == TESORO_ENCONTRADO:
        print("¡Has encontrado el tesoro y ganado el juego!")
    else:
        borrar_consola()

        if resultado == MOVIMIENTO_INVALIDO:
            print("Movimiento inválido. Estás intentando salir del mapa.")
        elif resultado == TRAMPA_ENCONTRADA:
            print("Es una trampa. Intenta de nuevo.")
        elif resultado == PISTA_ENCONTRADA:
            pista = mapa[nueva_posicion[FILAS]][nueva_posicion[COLUMNAS]]
            print(f"Hay una pista!!!! La pista es: {pista}")


def posicion_jugador_mapa_visual(mapa: list, posicion_jugador: tuple) -> tuple:
    """ DCS??? Nueva
    Muestra la posición del jugador sumando 1 a filas y columnas internas del mapa
    """
    return posicion_jugador[FILAS] + 1, posicion_jugador[COLUMNAS] + 1


def muestra_estado_mapa(mapa, posicion_jugador):
    """Muestra el mapa y la posición del jugador."""

    imprimir_mapa_oculto(mapa, posicion_jugador)
    print(f"Tu posición es {posicion_jugador_mapa_visual(mapa, posicion_jugador)}")


def jugar():
    """Función principal para iniciar el juego."""

    # Iniciar el mapa y al jugador en el centro del mapa
    mapa, posicion_jugador = inicializar_juego()
    muestra_estado_mapa(mapa, posicion_jugador)

    movimiento = pedir_movimiento(mapa)
    resultado_movimiento = None
    # Loop principal del juego. El juego termina cuando el jugador realizar movimiento SALIR.
    while movimiento != SALIR and resultado_movimiento != TESORO_ENCONTRADO:

        # Obtener la nueva posición del jugador y procesar el movimiento
        nueva_posicion = obtener_nueva_posicion(posicion_jugador, movimiento)
        resultado_movimiento = procesar_movimiento(nueva_posicion, mapa)

        muestra_resultado_del_movimiento(resultado_movimiento, nueva_posicion, mapa)

        if resultado_movimiento != TESORO_ENCONTRADO:
            # Actualizar la posición del jugador si el movimiento es válido
            if resultado_movimiento not in MOVIMIENTOS_NO_PERMITIDO:
                posicion_jugador = nueva_posicion

            muestra_estado_mapa(mapa, posicion_jugador)
            movimiento = pedir_movimiento(mapa)


if __name__ == "__main__":
    jugar()