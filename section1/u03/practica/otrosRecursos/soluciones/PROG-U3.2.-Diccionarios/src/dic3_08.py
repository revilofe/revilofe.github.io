"""
Ejercicio 3.2.8
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""

def pedir_palabras_traducidas() -> dict:
    """ Solicitar al usuario las palabras y sus traducciones
    """
    entrada = input("Ingrese las palabras y sus traducciones (palabra1:traduccion1, palabra2:traduccion2, ...): ")

    # Dividir la entrada del usuario en pares palabra:traducción y agregar al diccionario...
    pares_palabra_traduccion = [par.split(':') for par in entrada.split(',')]

    # Crear el diccionario a partir de las palabras introducidas...
    traductor = {palabra.strip(): traduccion.strip() for palabra, traduccion in pares_palabra_traduccion}


def traducir_frase(traductor: dict, frase_espanol: str) -> str:
    """ Traducir la frase palabra a palabra utilizando el diccionario
    """
    palabras_frase = frase_espanol.split()
    return ' '.join(traductor.get(palabra, palabra) for palabra in palabras_frase)


def main():
    traductor = pedir_palabras_traducidas()
    pedir_palabras_traducidas(traductor)
    frase_espanol = input("Ingrese una frase en español: ")
    print("Frase traducida:", traducir_frase(traductor, frase_espanol))



if __name__ == '__main__':
    main()


