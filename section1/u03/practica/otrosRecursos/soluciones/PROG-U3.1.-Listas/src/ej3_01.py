"""
Ejercicio 3.1.1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""

from EjerciciosU2.Pract2_2.ej2_2_01 import borrarConsola


def mostrar_lista(asignaturas):
    print(" - ".join(asignaturas))
    

def main():
    borrarConsola()
    print("Ejercicio 3.1.1")
    print("---------------\n")

    asignaturas = ("Matemáticas", "Física", "Química", "Historia", "Lengua")
    mostrar_lista(asignaturas)
    print()


if __name__ == "__main__":
    main()