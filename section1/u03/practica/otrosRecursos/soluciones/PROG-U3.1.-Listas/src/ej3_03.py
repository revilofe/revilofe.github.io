"""
Ejercicio 3.1.3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""

from EjerciciosU2.Pract2_2.ej2_2_01 import borrarConsola


def pedirNota(asignatura: str) -> float:
    nota = float(input(asignatura + ": ").replace(",", "."))
    if not (0 <= nota <= 10):
        raise ValueError
    return nota


def introducirNotas(asignaturas: tuple):
    for i in range(0, len(asignaturas)):
        todo_ok = False
        while not todo_ok:
            try:
                asignaturas[i][1] = pedirNota(asignaturas[i][0])
                todo_ok = True
            except ValueError:
                print("**Error** la nota debe ser un número entre 0 y 10 con o sin deicmales")
  

def mostrarAsignaturas(asignaturas):
    for asignatura in asignaturas:
        print("En {} he sacado {:.2f}".format(asignatura[0], asignatura[1]))


def main():
    borrarConsola()
    print("Ejercicio 3.1.3")
    print("---------------\n")

    asignaturas = (["Matemáticas", 0], ["Física", 0], ["Química", 0], ["Historia", 0], ["Lengua", 0])

    print("Introduzca las notas de sus asignaturas: ")
    introducirNotas(asignaturas)
    
    mostrarAsignaturas(asignaturas)

    print()
    print(asignaturas)
    print()


if __name__ == "__main__":
    main()