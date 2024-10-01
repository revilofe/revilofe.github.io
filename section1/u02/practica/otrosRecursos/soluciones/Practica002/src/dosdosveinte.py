"""Ejercicio 2.2.20 Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase).
Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no
hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en
qué posición se encontró y finalizar la ejecución.

"""


def leer_frase() -> str:
    """
    Lee una frase desde la entrada estándar. Se asegura de que la frase sea mas de una palabra.

    :return: La frase leída.
    """
    frase_leida = input("Ingrese una frase, minimo 2 palabras: ").strip()
    while len(frase_leida.split()) < 2:
        frase_leida = input("Ingrese una frase, minimo 2 palabras: ").strip()
    return frase_leida


def leer_letra() -> str:
    """
    Lee una letra desde la entrada estándar. Se asegura que la letra tiene tamaño y es un caracter visible.

    :return: La letra leída.
    """
    letra_leida = input("Ingrese una letra: ").strip()
    while len(letra_leida) != 1:
        letra_leida = input("Ingrese una letra: ").strip()
    return letra_leida


def encontrar_posicion_de_caracter_en_frase(letra_buscada: str, frase_de_busqueda: str) -> int:
    """
    Recorrer la frase, carácter a carácter, comparando con la letra buscada.
    Si encuentra el caracter, devolver la posición en la frase, el tamaño de la frase no encuentra el caracter.
    """
    posicion_en_frase = 0
    no_encontrado = True
    while posicion_en_frase < len(frase_de_busqueda) and no_encontrado:
        if frase_de_busqueda[posicion_en_frase] == letra_buscada:
            no_encontrado = False
        else:
            posicion_en_frase += 1
    return posicion_en_frase


def mensaje_de_caracter_en_frase(posicion: int, longitud: int, letra_buscada: str) -> str:
    """
    Genera mensaje a sacar por pantalla.
    """

    mensaje_salida = ''
    for posicion_en_frase in range(0, posicion + 1):
        if posicion_en_frase == posicion and posicion_en_frase < longitud:
            mensaje_salida += f"La letra {letra_buscada} se encuentra en la posicion {posicion_en_frase}\n"
        elif posicion_en_frase < longitud:
            mensaje_salida += f"La letra {letra_buscada} no se encuentra en la posicion {posicion_en_frase}\n"
    return mensaje_salida


if __name__ == "__main__":
    # Ingreso y lectura de datos
    frase = leer_frase()
    letra = leer_letra()

    # Procesamiento de datos
    posicion_encontrada = encontrar_posicion_de_caracter_en_frase(letra, frase)
    mensaje = mensaje_de_caracter_en_frase(posicion_encontrada, len(frase), letra)

    # Salida de datos
    print(mensaje)
