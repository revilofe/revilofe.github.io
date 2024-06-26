
import os
from msvcrt import getch

#Símbolos que se mostrarán en el tablero
FICHAS = (' ', 'X', 'O')

#Matriz con los conjuntos de posiciones permitidas desde cada par fila, columna del tablero
POSICIONES_PERMITIDAS = (
    ({(0, 1), (1, 0), (1, 1)}, 
    {(0, 0), (2, 0), (1, 1)}, 
    {(0, 1), (1, 2), (1, 1)}),
    ({(0, 0), (2, 0), (1, 1)}, 
    {(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)}, 
    {(0, 2), (2, 2), (1, 1)}),
    ({(1, 0), (2, 1), (1, 1)}, 
    {(2, 0), (2, 2), (1, 1)}, 
    {(2, 1), (1, 2), (1, 1)})
)


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
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != 0:
            return tablero[i][0], True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != 0:
            return tablero[0][i], True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != 0:
        return tablero[0][0], True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != 0:
        return tablero[0][2], True

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
    #ronda <= 3 solo colocar ficha => comprobar si podemos colocar la ficha del jugador en la posición fila y columna siempre que sea una casilla vacía.
    #ronda > 3 mover ficha => 
    #   si solo ha seleccionado la posición de la ficha que va a mover => comprobar si en dicha posición existe una ficha del jugador
    #   si seleccionó también la posición dónde mover => comprobar si la nueva posición es accesible desde su posición anterior y que la posición destino esté vacía.
    if ronda <= 3:
        return tablero[pos_ficha['fila']][pos_ficha['columna']] == 0
    else:
        if pos_ficha['fila'] == pos_ficha['columna'] == None:
            return tablero[pos_ficha_a_mover['fila']][pos_ficha_a_mover['columna']] == jugador
        else:
            return (pos_ficha['fila'], pos_ficha['columna']) in POSICIONES_PERMITIDAS[pos_ficha_a_mover['fila']][pos_ficha_a_mover['columna']] and tablero[pos_ficha['fila']][pos_ficha['columna']] == 0


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
        if ronda > 3: #ronda mayor que 3, debe mover una ficha del tablero
            pos_ficha_a_mover['fila'] = pedir_posicion("fila", f"\nJugador {jugador}, seleccione una ficha para MOVER...")
            pos_ficha_a_mover['columna'] = pedir_posicion("columna")
            pos_correcta = comprobar_casilla(tablero, jugador, ronda, pos_ficha, pos_ficha_a_mover)

        if pos_correcta or ronda <= 3:
            pos_ficha['fila'] = pedir_posicion("fila", f"\nJugador {jugador}, seleccione una posición para COLOCAR su ficha...")
            pos_ficha['columna'] = pedir_posicion("columna")
            pos_correcta = comprobar_casilla(tablero, jugador, ronda, pos_ficha, pos_ficha_a_mover)

        if pos_correcta:
            if ronda > 3:
                tablero[pos_ficha_a_mover['fila']][pos_ficha_a_mover['columna']] = 0    
            tablero[pos_ficha['fila']][pos_ficha['columna']] = jugador
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

        ganador, hay_ganador = verificar_ganador(tablero)
        if hay_ganador:
            print(f"\n¡El jugador {ganador} ha ganado!\n")


def main():
    tablero = crear_tablero()
    mostrar_tablero(tablero)
    jugar(tablero)


if __name__ == "__main__":
    main()