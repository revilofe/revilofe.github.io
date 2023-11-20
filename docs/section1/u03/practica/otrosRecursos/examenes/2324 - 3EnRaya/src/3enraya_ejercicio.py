
import os
from msvcrt import getch

#Símbolos que se mostrarán en el tablero
FICHAS = (' ', 'X', 'O')

#TODO: Matriz 3x3 con los conjuntos de posiciones permitidas desde cada par fila, columna del tablero:
# Una tupla que contendrá 3 tuplas (filas), cada una tendrá 3 conjuntos (columnas), 
# donde cada elemento de un conjunto es una posición accesible en forma de tupla (fila, columna)
POSICIONES_PERMITIDAS = ???


def borrarConsola():
    """ Limpiar la consola."""
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def pulse_tecla_para_continuar():
    """ Mostrar el mensaje Presione una tecla para continuar y 
    hacer una pausa hasta que se realice la acción."""
    os.system("pause")


def mostrar_fila(fila: list):
    """ Mostrar una fila del tablero
    :param fila: lista con la información de la fila a mostrar
    """
    contenido_fila = "| "
    for celda in fila:
        contenido_fila += str(FICHAS[celda]) + " | "
    print(contenido_fila)


def mostrar_tablero(tablero: tuple):
    """ Mostrar en consola el tablero con las fichas.
    :param tablero: matriz de 3x3 con la información del tablero.
    """
    borrarConsola()
    print("-------------")
    for fila in tablero:
        mostrar_fila(fila)
        print("-------------")


def crear_fila(num_columnas = 3) -> list:
    """ Crear las columnas de una fila
    :param num_columnas: número de columnas del tablero.
        (por defecto se establece el valor 3)
    :return: lista con la fila generada con los valores por defecto (0 = casilla vacía)
    """
    return list(0 for _ in range(num_columnas))


def crear_tablero(num_filas = 3) -> tuple:
    """ Crear las filas del tablero
    :param num_filas: número de filas del tablero.
        (por defecto se establece el valor 3)
    :return: tupla con la matriz num_filas x num_columnas
    """
    return tuple(crear_fila() for _ in range(num_filas))


def verificar_ganador(tablero) -> tuple:
    """ Comprobar si algún jugador ha ganado.
    :param tablero: matriz de 3x3 con la información del tablero.
    :return: tupla con dos elementos:
        - el número del jugador si alguno ganó o None si no ganó aún nadie
        - un valor lógico indicando si el juego ha terminado
    """
    # TODO: Verificar filas y columnas
    # Si el contenido de las celdas de una fila o columna es igual y distinto de cero
    # retornar una de las celdas (jugador) y True
    ???

    # TODO: Verificar diagonales
    # Igual en las diagonales...
    ???

    # Si no retorno nada, quiere decir que aún no ganó nadie...
    return None, False


def pedir_posicion(fila_col, msj = "") -> int:
    """ Pedir la posición de la fila o columna al jugador.
    :param fila_col: str con la palabra 'fila' o 'columna'.
    :param msj: frase que se mostrará si es distinta a la cadena vacía 
    (se usa para mostrar una descripción de lo que se va a solicitar solo al insertar la fila)
    :return: número con la posición del tablero seleccionado.
    """
    pos = None
    if msj != "": print(msj)
    while pos == None:
        try:
            pos = int(input(f'Elige la {fila_col} (1, 2, 3): ')) - 1
            if not 0 <= pos <= 2:
                raise ValueError
        except ValueError:
            pos = None
            print(f"**Error** {fila_col} no válida")
    
    return pos


def comprobar_casilla(tablero: tuple, 
                      jugador: int, 
                      ronda: int, 
                      pos_ficha: list, 
                      pos_ficha_a_mover: list) -> bool:
    """ Comprobar si la casilla seleccionada es correcta para colocar la ficha del jugador.
    :param tablero: matriz de 3x3 con la información del tablero.
    :param jugador: número del jugador
    :param ronda: número de la ronda en la que estamos
    :param pos_ficha: diccionario con la posición de la fila y columna dónde desea colocar la ficha
    :param pos_ficha_a_mover: diccionario con la posición de la fila y columna desde dónde desea mover la ficha
    :return: True si la posición es correcta / False si no lo es.
    """
    # TODO:
    # ronda <= 3: solo colocar ficha => comprobar si podemos colocar la ficha del jugador en la posición fila y columna siempre que sea una casilla vacía.
    # ronda > 3: mover ficha => 
    #   si solo ha seleccionado la posición de la ficha que va a mover => comprobar si en dicha posición existe una ficha del jugador
    #   si seleccionó también la posición dónde mover => comprobar si la nueva posición es accesible desde su posición anterior y que la posición destino esté vacía.
    ???


def colocar_ficha(tablero: tuple, jugador: int, ronda: int):
    """ Solicitar a un jugador las posiciones de la ficha que va a colocar.
    :param tablero: matriz de 3x3 con la información del tablero.
    :param jugador: número del jugador
    :param ronda: número de la ronda en la que estamos
    """
    pos_ficha = {'fila': None, 'columna': None}
    pos_ficha_a_mover = {'fila': None, 'columna': None}
    pos_correcta = False

    while not pos_correcta:
        #TODO: Si ronda es mayor que 3, debe pedir la fila y columna de la ficha a mover y comprobar que la casilla es del jugador con el turno...
        if ronda > 3:
            ???

        if pos_correcta or ronda <= 3:
            pos_ficha['fila'] = pedir_posicion("fila", f"\nJugador {jugador}, seleccione una posición para COLOCAR su ficha...")
            pos_ficha['columna'] = pedir_posicion("columna")
            pos_correcta = comprobar_casilla(tablero, jugador, ronda, pos_ficha, pos_ficha_a_mover)

        if pos_correcta:
            # TODO: Si la ronda es mayor que 3, poner la celda de la ficha que se ha movido vacía
            ???

            #TODO: Establecer la posición del tablero según pos_ficha al jugador que tiene el turno
            ???
        else:
            pos_ficha['fila'] = pos_ficha['columna'] = None
            pos_ficha_a_mover['fila'] = pos_ficha_a_mover['columna'] = None
            print("**Error** movimiento inválido")
            pulse_tecla_para_continuar()
            mostrar_tablero(tablero)


def cambiar_turno(turno: int) -> int:
    """ Modificar el turno.
    :param turno: jugador que tiene el turno anterior.
    :return: jugador que tiene el turno actual.
    """
    if turno % 2 == 0:
        return 1
    return 2


def jugar(tablero: tuple):
    """ Pedir a cada jugador la posición de una ficha hasta que uno de ellos gane.
    :param tablero: matriz de 3x3 con la información del tablero.
    """
    # TODO: Aquí también hay algún problema que debes arreglar...

    turno = 0
    ronda = 0
    hay_ganador = False
    ganador = ""

    while not hay_ganador:

        turno = cambiar_turno(turno)
        if turno == 1:
            ronda += 1

        print(f"\nRONDA {ronda}")
        print("-" * len(f"RONDA {ronda}"))

        colocar_ficha(tablero, turno, ronda)
        mostrar_tablero(tablero)

        verificar_ganador(tablero)
        if hay_ganador:
            print(f"\n¡El jugador {ganador} ha ganado!\n")


def main():
    tablero = crear_tablero()
    mostrar_tablero(tablero)
    jugar(tablero)


if __name__ == "__main__":
    main()