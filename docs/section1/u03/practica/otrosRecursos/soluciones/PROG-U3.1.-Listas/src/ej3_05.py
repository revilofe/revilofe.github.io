"""
Ejercicio 3.1.5
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""

from EjerciciosU2.Pract2_2.ej2_2_01 import borrarConsola


def obtener_numeros_orden_inverso(numeros):
    res = ""
    for i in range(len(numeros) - 1, -1, -1):
        res += str(numeros[i])
        if i != 0:
            res += ", "
    return res

def main():
    borrarConsola()
    print("Ejercicio 3.1.5")
    print("---------------\n")

    numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    print(obtener_numeros_orden_inverso(numeros) + "\n")


if __name__ == "__main__":
    main()