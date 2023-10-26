"""
Ejercicio 2.2.20
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

"""


def leer_frase() -> str:
    """
    Lee una frase desde la entrada estándar. Se asegura de que la frase sea mas de una palabra.

    :return: La frase leída.
    """
    frase = input("Ingrese una frase, minimo 2 palabras: ").strip()
    while len(frase.split()) < 2:
        frase = input("Ingrese una frase, minimo 2 palabras: ").strip()
    return frase


def leer_letra() -> str:
    """
    Lee una letra desde la entrada estándar. Se asegura que la letra tiene tamaño y es un caracter visible.

    :return: La letra leída.
    """
    letra = input("Ingrese una letra: ").strip()
    while len(letra) != 1:
        letra = input("Ingrese una letra: ").strip()
    return letra


def mensaje_de_caracter_en_frase(letra: str, frase: str) -> str:
    '''
     Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (a añadiendo al mensaje final ese mensaje con la posición) y continuar. Si se encuentra una coincidencia, añadir al mensaje final en qué posición se encontró y devolver el mensaje completo.
    '''

    mensaje = ''

    posicion_en_frase = 0
    no_encontrado = True
    while posicion_en_frase < len(frase) and no_encontrado:
        if frase[posicion_en_frase] == letra:
            mensaje += f"La letra {letra} se encuentra en la posicion {posicion_en_frase}\n"
            no_encontrado = False
        else:
            mensaje += f"La letra {letra} no se encuentra en la posicion {posicion_en_frase}\n"
        posicion_en_frase += 1
    return mensaje


if __name__ == "__main__":
    # Ingreso y lectura de datos
    frase = leer_frase()
    letra = leer_letra()

    # Procesamiento de datos
    mensaje = mensaje_de_caracter_en_frase(letra, frase)

    # Salida de datos
    print(mensaje)
