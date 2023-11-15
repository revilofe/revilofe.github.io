"""
Ejercicio 3.1.6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

from EjerciciosU2.Pract2_2.ej2_2_01 import borrarConsola


def pedirNota(asignatura: str) -> float:
    todo_ok = False
    while not todo_ok:
        try:
            nota = float(input(asignatura + ": ").replace(",", "."))
            if not (0 <= nota <= 10):
                raise ValueError
            return nota
        except ValueError:
            print("**Error** la nota debe ser un número entre 0 y 10 con o sin deicmales")


def eliminar_asignaturas_aprobadas(asignaturas: list):
    for i in range(len(asignaturas) - 1, -1, -1):
        if asignaturas[i][1] >= 5:
            del asignaturas[i]


def introducirNotas(asignaturas: list):
    for i in range(0, len(asignaturas)):
        asignaturas[i][1] = pedirNota(asignaturas[i][0])


def mostrarAsignaturas(asignaturas):
    for asignatura in asignaturas:
        print("\t{} = {:.2f}".format(asignatura[0], asignatura[1]))


def main():
    borrarConsola()
    print("Ejercicio 3.1.6")
    print("---------------\n")

    asignaturas = [["Matemáticas", 0], ["Física", 0], ["Química", 0], ["Historia", 0], ["Lengua", 0]]

    print("Introduzca las notas de sus asignaturas: ")
    introducirNotas(asignaturas)
    eliminar_asignaturas_aprobadas(asignaturas)
    
    print("\nAsignaturas que repite:")
    mostrarAsignaturas(asignaturas)

    print()
    print(asignaturas)
    print()


if __name__ == "__main__":
    main()