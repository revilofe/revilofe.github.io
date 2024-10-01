"""
Ejercicio 3.1.12
Escribir un programa que almacene las matrices A=(123456) y B=(−100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
A:
     1 2
     3 4
     5 6
B:
    -1 0
     0 1
     1 1
"""

from EjerciciosU2.Pract2_2.ej2_2_01 import borrarConsola


def producto_fila(vector_1: tuple, vector_2: tuple) -> tuple:
    return tuple(vector_1[i] * vector_2[i] for i in range(0, 2))


def producto(matriz_1: tuple, matriz_2: tuple) -> tuple:
    return tuple(producto_fila(matriz_1[i], matriz_2[i]) for i in range(0, 3))


def pintar_matriz(matriz: list) -> str:
    res = ""
    for vector in matriz:
        res += f"{vector[0]}, {vector[1]}\n"

    return res

def main():
    borrarConsola()
    print("Ejercicio 3.1.12")
    print("---------------\n")

    matriz_1 = ((1, 2), (3, 4), (5, 6))
    matriz_2 = ((-1, 0), (0, 1), (1, 1))

    matriz_3 = producto(matriz_1, matriz_2)

    print(pintar_matriz(matriz_3))

    print()
    print(f"{matriz_1} x {matriz_2} = {matriz_3}")
    print()


if __name__ == "__main__":
    main()