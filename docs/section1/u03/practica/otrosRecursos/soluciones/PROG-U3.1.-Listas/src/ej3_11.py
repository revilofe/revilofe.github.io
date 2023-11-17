"""
Ejercicio 3.1.11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
"""

from EjerciciosU2.Pract2_2.ej2_2_01 import borrarConsola


def producto(vector_1: tuple, vector_2: tuple) -> tuple:
    return tuple(vector_1[i] * vector_2[i] for i in range(0, 3))


def main():
    borrarConsola()
    print("Ejercicio 3.1.11")
    print("---------------\n")

    vector_1 = (1,2,3)
    vector_2 = (-1,0,2)

    vector_3 = producto(vector_1, vector_2)

    print(f"{vector_1} x {vector_2} = {vector_3}")
    print()


if __name__ == "__main__":
    main()