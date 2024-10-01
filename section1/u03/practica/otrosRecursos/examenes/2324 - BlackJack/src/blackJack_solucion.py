
import os

PALOS = ('Corazones', 'Picas', 'Treboles', 'Diamantes')

CARTAS = ('As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

VALORES = {'As':(1, 11), '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

PUNTOS_OBJETIVO = 21
CARTAS_AL_INICIO = 1


def borrar_consola():
    """ Limpiar la consola.
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def pulse_tecla_para_continuar():
    """ Mostrar el mensaje Presione una tecla para continuar y hacer una pausa hasta que se realice la acción.
    """
    os.system("pause")


def crear_baraja() -> set:
    """ Crear la baraja de 52 cartas
    """
    return set((carta, palo) for carta in CARTAS for palo in PALOS)


def reparte_carta(baraja: set) -> tuple:
    """ Reparte una carta de la baraja
    """
    try:
        return baraja.pop()
    except KeyError:
        print("*Error* la baraja no tiene cartas")
        return None
    

def dame_carta(baraja: set, cartas_jugador: list) -> bool:
    """ Pide una carta, la guarda en la lista del jugador y retorna True si la baraja se ha quedado sin cartas
    """
    carta = reparte_carta(baraja)
    if carta == None:
        #No existen más cartas en la baraja
        return False
    else:
        cartas_jugador.append(carta)
        return True


def contesta_a_pregunta(mensaje: str) -> bool:
    """ Hace una pregunta de si o no
    """
    respuesta = None
    while respuesta not in {'s', 'si', 'n', 'no'}:
        if respuesta != None:
            print("*Error* respuesta no válida (s, si, n, no)")
        respuesta = input(mensaje).strip().lower()

    return respuesta in {'s' ,'si'}


def pedir_carta(baraja: set, cartas_jugador: list) -> bool:
    """ Pregunta si quiere una carta o se planta
    """
    if contesta_a_pregunta("¿Quieres una carta? (s/n) "):
        return dame_carta(baraja, cartas_jugador)
    else:
        return False


def actualizar_puntos_comodines(cartas_jugador: list, puntos: int) -> int:
    """ Actualizar los puntos con las cartas que tengan más de un valor
    """
    for carta in cartas_jugador:       
        if puntos < puntos - valor_carta(carta[0]) + valor_carta(carta[0], False) <= PUNTOS_OBJETIVO:
            puntos = puntos - valor_carta(carta[0]) + valor_carta(carta[0], False)
    return puntos


def calcular_puntos(cartas_jugador: list) -> int:
    """ Calcular los puntos de las cartas del jugador
    """
    puntos = 0
    for carta in cartas_jugador:
        puntos += valor_carta(carta[0])

    puntos = actualizar_puntos_comodines(cartas_jugador, puntos)

    return puntos > PUNTOS_OBJETIVO, puntos


def valor_carta(carta: tuple, valor_minimo = True) -> int:
    """ Retornar el valor de una carta, si tiene más de uno retornará el valor mínimo o máximo dependiendo de valor_minimo
    """
    if type(VALORES[carta]) == tuple and len(VALORES[carta]) == 2:
        if valor_minimo:
            return int(min(VALORES[carta]))
        else:
            return int(max(VALORES[carta]))
    else:
        return int(VALORES[carta])
   

def mostrar_cartas(jugador, puntos, cartas_jugador: list):
    """ Mostrar los puntos y cartas de un jugador
    """
    print(jugador)
    print("-" * len(jugador))
    print(f"\t{puntos} puntos >>\n" + "\n".join(f"\t{carta[0]} de {carta[1]}" for carta in cartas_jugador)) 


def mostrar_resultado(cartas_jugador1, puntosJ1, cartas_jugador2, puntosJ2):
    """ Mostrar el resultado final del juego
    """
    borrar_consola()
    mostrar_cartas("Jugador 1", puntosJ1, cartas_jugador1)
    mostrar_cartas("\nJugador 2", puntosJ2, cartas_jugador2)
    print()

    if puntosJ1 > PUNTOS_OBJETIVO and puntosJ2 > PUNTOS_OBJETIVO:
        print("¡Los dos os habéis pasado!")
    elif puntosJ2 > PUNTOS_OBJETIVO:
        print("¡Jugador 1 GANA!")
    elif puntosJ1 > PUNTOS_OBJETIVO:
        print("¡Jugador 2 GANA!")
    elif puntosJ1 > puntosJ2:
        print("¡Jugador 1 GANA!")
    elif puntosJ2 > puntosJ1:
        print("¡Jugador 2 GANA!")
    else:
        print("¡Habéis empatado!")

    print()
    pulse_tecla_para_continuar()
    borrar_consola()


def jugar(baraja: set):
    """ Jugar al black jack entre dos jugadores
    """
    ronda = 1
    cartas_jugador1 = []
    cartas_jugador2 = []
    puntosJ1 = puntosJ2 = 0

    for _ in range(CARTAS_AL_INICIO):
        finJ1 = not dame_carta(baraja, cartas_jugador1)
        finJ2 = not dame_carta(baraja, cartas_jugador2)
  
    while not (finJ1 and finJ2):

        ronda += 1
        borrar_consola()
        print(f"RONDA: {ronda}\n")

        if not finJ1:
            finJ1, puntosJ1 = calcular_puntos(cartas_jugador1)

        if not finJ2:
            finJ2, puntosJ2 = calcular_puntos(cartas_jugador2)

        if not finJ1:
            mostrar_cartas("Jugador 1", puntosJ1, cartas_jugador1)
            finJ1 = not pedir_carta(baraja, cartas_jugador1)

        if not finJ2:
            mostrar_cartas("\nJugador 2", puntosJ2, cartas_jugador2)
            finJ2 = not pedir_carta(baraja, cartas_jugador2)

    mostrar_resultado(cartas_jugador1, puntosJ1, cartas_jugador2, puntosJ2)


def main():
    baraja = crear_baraja()

    seguir_jugando = True

    while seguir_jugando:
        jugar(baraja)
        seguir_jugando = contesta_a_pregunta("¿Quieres jugar otra partida? (s/n) ")


if __name__ == "__main__":
    main()