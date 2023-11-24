"""
En esta ocasión la documentación no está completa y solo existe una descripción funcional de qué realiza cada bloque de código del juego.

Este programa desarrolla el juego del black jack entre dos jugadores:
- Inicialmente se reparte una carta a cada jugador.
- Posteriormente se pregunta en cada ronda si desea una carta más o se planta.
- Gana el jugador que más se acerque a 21 sin pasarse.
- El programa te permite jugar una partida tras otra hasta que tú decidas parar o se acaben las cartas de la baraja.
- El valor de las cartas es el siguiente:
    * El número de la misma en las cartas del 2 al 10.
    * As puede valer 1 u 11.
    * J, Q y K valen 10.

    
Algún profe despistado ha desarrollado con prisas el juego y debéis darle solución vosotros...

- Para empezar nos falta una constante muy VALIOSA, que recoje los puntos de cada CARTA en un diccionario. El As es una carta que actúa de comodín y puede valer 1 u 11, según mejor convenga a nuestra mano. Esta carta especial debe tener un valor de una tupla de dos valores enteros y no un solo valor entero cómo el resto de cartas.

- Soluciona los errores evidentes que ya os está marcando Visual Studio.

- Al proporcionar las cartas a los jugadores, aunque parece que tiene buena pinta, cuando se acaba la baraja se produce un "problemilla" no muy controlado, está claro que el profe no jugó mucho...

- Al desarrollar el juego seguramente existan argumentos o parámetros que no se hayan pasado o definido correctamente... en fin, las prisas :-P

- En la función valor_carta se intenta controlar que si el tipo del valor de la carta es una tupla y tiene 2 elementos pueda recuperar su valor mínimo o máximo según indique su parámetro de entrada valor_minimo.

- jugar() debe tener algún problema porque no me deja JUGAR...

- Me gustaría que el programa funcionara cómo se describe al principio y poder jugar las partidas que yo quiera hasta que se acabe la baraja.

- Si ves alguna mejora posible, adelante y realizala, siempre que la documentes correctamente y no cómo ha hecho el vago del profesor.

"""
import os

PALOS = ('Corazones', 'Picas', 'Treboles', 'Diamantes')

CARTAS = ('As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

VALORES = ???

PUNTOS_OBJETIVO = 21
CARTAS_AL_INICIO = 21


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
    return set((carta, palo) for carta in CARTAS, PALOS)


def reparte_carta(baraja: set) -> tuple:
    """ Reparte una carta de la baraja
    """
    return baraja.pop()
    

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

    return respuesta in ???


def pedir_carta(baraja: set, cartas_jugador: list) -> bool:
    """ Pregunta si quiere una carta o se planta
    """
    if contesta_a_pregunta("¿Quieres una carta? (s/n) "):
        return dame_carta()
    else:
        return False


def actualizar_puntos_comodines(cartas_jugador: list) -> int:
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

    puntos = actualizar_puntos_comodines(cartas_jugador)

    return puntos > PUNTOS_OBJETIVO, puntos


def valor_carta(carta: tuple, valor_minimo = True) -> int:
    """ Retornar el valor de una carta, si tiene más de uno retornará el valor mínimo o máximo dependiendo de valor_minimo
    """
    if VALORES[carta] == tuple and VALORES[carta] == 2:
        if valor_minimo:
            return ???
        else:
            return ???
    else:
        return int(VALORES[carta])
   

def mostrar_cartas(jugador, puntos, cartas_jugador: list):
    """ Mostrar los puntos y cartas de un jugador
    """
    print(jugador)
    print("-" * len(puntos))
    print(f"\t{puntos} puntos >>\n" + "\n".(f"\t{carta[0]} de {carta[1]}" for )) 


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


def jugar():
    """ Jugar al black jack entre dos jugadores
    """
    ronda = 1
    cartas_jugador1 = 0
    cartas_jugador2 = 0
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
        jugar()
        seguir_jugando = not contesta_a_pregunta("¿Quieres jugar otra partida? (s/n) ")


if __name__ == "__main__":
    main()