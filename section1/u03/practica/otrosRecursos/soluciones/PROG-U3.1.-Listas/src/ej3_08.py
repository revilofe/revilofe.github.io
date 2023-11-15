"""
Ejercicio 3.1.8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

from EjerciciosU2.Pract2_2.ej2_2_01 import borrarConsola


def pedir_palabra() -> list:
    return list(input("Introduzca una palabra: "))


def palabra_alreves(palabra: list) -> list:
    palabra = list(palabra)
    palabra.reverse()
    return palabra


def comprobar_palindromo(palabra, palabra2) -> bool:
    return "".join(palabra) == "".join(palabra2)


def main():
    borrarConsola()
    print("Ejercicio 3.1.8")
    print("---------------\n")

    palabra = pedir_palabra()

    palabra2 = palabra_alreves(palabra)

    if comprobar_palindromo(palabra, palabra2):
        print("Es un palíndromo => " + "".join(palabra) + " = " + "".join(palabra2))
    else:
        print("NO es un palíndromo => " + "".join(palabra) + " <> " + "".join(palabra2))

    print()


if __name__ == "__main__":
    main()