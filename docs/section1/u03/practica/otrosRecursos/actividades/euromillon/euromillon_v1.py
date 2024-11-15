
import os
import random

# Configuración del juego...
CONFIG = {
    "bombo": {
        "min": 1,       # Número mínimo para el bombo
        "max": 50,      # Número máximo para el bombo
        "total": 5      # Total de números seleccionados en el bombo
    },
    "estrellas": {
        "min": 1,       # Número mínimo para las estrellas
        "max": 12,      # Número máximo para las estrellas
        "total": 2      # Total de estrellas seleccionadas
    }
}



def limpiar_pantalla():
    """
    Limpia la consola dependiendo del sistema operativo.
    """
    os.system('clear' if os.name == 'posix' else 'cls')


def pausa():
    """
    Pausa la ejecución del programa hasta que el usuario presione ENTER.
    """
    input("\nPresione ENTER para continuar...")


def pedir_numero(msj: str, minimo: int, maximo: int) -> int:
    """
    Solicita al usuario un número dentro de un rango definido.

    Args:
        msj (str): Mensaje que se mostrará al usuario.
        minimo (int): Valor mínimo permitido.
        maximo (int): Valor máximo permitido.

    Returns:
        int: Número válido ingresado por el usuario dentro del rango.
    """    
    numero = None
    while numero is None:
        try:
            numero = int(input(msj).strip())

            if not (minimo <= numero <= maximo):
                raise ValueError(f"El número debe estar entre el {minimo} y el {maximo}!")
            
        except ValueError as e:
            if numero is None:
                print("*ERROR* Número no válido!")
            else:
                numero = None
                print(f"*ERROR* {e}")

    return numero


def solicitar_numeros(desc: str, total: int, min: int, max: int) -> set:
    """
    Solicita al usuario una cantidad específica de números únicos dentro de un rango.

    Args:
        desc (str): Descripción del tipo de número ("el número", "la estrella").
        total (int): Cantidad total de números que el usuario debe ingresar.
        min (int): Valor mínimo permitido.
        max (int): Valor máximo permitido.

    Returns:
        set: Conjunto de números ingresados por el usuario.
    """    
    numeros = set()
    while len(numeros) < total:
        numeros.add(pedir_numero(f"Dame {desc} #{len(numeros) + 1}#>> ", min, max))
        print(f"{sorted(numeros) if len(numeros) > 0 else []}")

    return numeros


def preguntar_total(desc: str, min: int) -> int:
    """
    Pregunta al usuario cuántos elementos quiere jugar, dentro de un rango predefinido.

    Args:
        desc (str): Descripción del tipo de elemento ("números", "estrellas").
        min (int): Valor mínimo permitido.

    Returns:
        int: Cantidad seleccionada por el usuario.

    Note:
        El rango máximo no se pasa por parámetro a la función, sino que se establece como 
        el doble del valor mínimo que se pasa cómo segundo argumento de la función.
    """
    max = min * 2
    return pedir_numero(f"Total de {desc} a jugar ({min}-{max})? >> ", min, max)


def sacar_bolas(min: int, max: int, total: int) -> set:
    """
    Selecciona al azar una cantidad de números enteros únicos dentro de un rango.

    Args:
        min (int): Valor mínimo del rango.
        max (int): Valor máximo del rango.
        total (int): Cantidad de elementos a seleccionar.

    Returns:
        set: Conjunto de números enteros seleccionados al azar.
    """
    return set(random.sample(range(min, max + 1), total))


def generar_euromillon(premiados: set, estrellas: set):
    """
    Genera los números y estrellas premiados para el sorteo del Euromillón.

    Args:
        premiados (set): Conjunto donde se almacenarán los números premiados.
        estrellas (set): Conjunto donde se almacenarán las estrellas premiadas.
    """
    premiados.update(sacar_bolas(CONFIG["bombo"]["min"], CONFIG["bombo"]["max"], CONFIG["bombo"]["total"]))
    estrellas.update(sacar_bolas(CONFIG["estrellas"]["min"], CONFIG["estrellas"]["max"], CONFIG["estrellas"]["total"]))


def obtener_aciertos(jugados: set, premiados: set) -> int:
    """
    Calcula la cantidad de aciertos comparando dos conjuntos de elementos.

    Args:
        jugados (set): Conjunto de elementos seleccionados por el usuario.
        premiados (set): Conjunto de elementos premiados.

    Returns:
        int: Número de elementos comunes entre los dos conjuntos.
    """
    # Cuenta los aciertos mediante la intersección de conjuntos
    return len(jugados & premiados)


def mostrar_resultados(numeros_premiados: set, 
                       estrellas_premiadas: set, 
                       numeros: set, 
                       estrellas: set):
    """
    Muestra los resultados del sorteo y los aciertos del jugador.

    Args:
        numeros_premiados (set): Conjunto de números premiados.
        estrellas_premiadas (set): Conjunto de estrellas premiadas.
        numeros (set): Números seleccionados por el jugador.
        estrellas (set): Estrellas seleccionadas por el jugador.
    """
    limpiar_pantalla()
    print("RESULTADOS DEL EUROMILLÓN\n-------------------------\n\n")

    print(f"Números premiados = {sorted(numeros_premiados)}")
    print(f"Estrellas premiadas = {sorted(estrellas_premiadas)}")
    
    print(f"Números jugados = {sorted(numeros)}")
    print(f"Estrellas jugadas = {sorted(estrellas)}")

    # Comprobar los resultados, obteniendo el número de aciertos que ha tenido...
    aciertos_numeros = obtener_aciertos(numeros, numeros_premiados)
    aciertos_estrellas = obtener_aciertos(estrellas, estrellas_premiadas)

    print("\n\nTotal de números acertados = " + 
          f"{aciertos_numeros}\n" + 
          "Total de estrellas acertadas = " + 
          f"{aciertos_estrellas}")


def main():
    limpiar_pantalla()
    print("JUEGA AL EUROMILLÓN\n-------------------\n\n")

    # Preguntar cuantos números y estrellas puede el jugador introducir...
    total_numeros = preguntar_total("números", CONFIG["bombo"]["total"])
    total_estrellas = preguntar_total("estrellas", CONFIG["estrellas"]["total"])

    # Pedir los números y estrellas del euromillón...
    print(f"\n### Seleccione {total_numeros} números del {CONFIG["bombo"]["min"]} al {CONFIG["bombo"]["max"]} ###")
    numeros = solicitar_numeros("el número", total_numeros, CONFIG["bombo"]["min"], CONFIG["bombo"]["max"])
    print(f"\n### Seleccione {total_estrellas} estrellas del {CONFIG["estrellas"]["min"]} al {CONFIG["estrellas"]["max"]} ###")
    estrellas = solicitar_numeros("la estrella", total_estrellas, CONFIG["estrellas"]["min"], CONFIG["estrellas"]["max"])

    pausa()

    # Sacar de los bombos los números y las estrellas premiadas...
    numeros_premiados = set()
    estrellas_premiadas = set()
    generar_euromillon(numeros_premiados, estrellas_premiadas)

    mostrar_resultados(numeros_premiados, estrellas_premiadas, numeros, estrellas)


if __name__ == "__main__":
    main()
