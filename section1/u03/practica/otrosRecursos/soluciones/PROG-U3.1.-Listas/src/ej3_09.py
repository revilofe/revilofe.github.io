"""
Ejercicio 3.1.9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""

from EjerciciosU2.Pract2_2.ej2_2_01 import borrarConsola


def pedir_palabra() -> list:
    palabra = input("Introduzca una palabra: ").strip().lower()

    palabra = palabra.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')

    return list(palabra)


def contar_vocales(palabra) -> tuple:
    return tuple((vocal, palabra.count(vocal)) for vocal in ('a', 'e', 'i', 'o', 'u'))


def mostrar_resultado(vocales):
    for vocal in vocales:
        print(vocal[0] + " = " + str(vocal[1]))


def main():
    borrarConsola()
    print("Ejercicio 3.1.9")
    print("---------------\n")

    palabra = pedir_palabra()

    vocales = contar_vocales(palabra)

    mostrar_resultado(vocales)

    print()
    print(vocales)
    print()


if __name__ == "__main__":
    main()