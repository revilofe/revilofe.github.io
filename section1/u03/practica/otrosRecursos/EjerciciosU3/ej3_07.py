"""
Ejercicio 3.1.7
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""

from EjerciciosU2.Pract2_2.ej2_2_01 import borrarConsola


def eliminar_pos_multiplos_de_3(abecedario: list):
    for i in range(len(abecedario) - 1, -1, -1):
        if i % 3 == 0:
            del abecedario[i]


def lista_abecedario() -> list:
    #return list(map(chr, range(97, 123)))
    return list(chr(i) for i in range(97, 123))


def main():
    borrarConsola()
    print("Ejercicio 3.1.7")
    print("---------------\n")

    abecedario = lista_abecedario()

    print("Abecedario completo: ")
    print(", ".join(abecedario))
    
    eliminar_pos_multiplos_de_3(abecedario)

    print("\nAbecedario eliminando posiciones múltiplos de 3:")
    print(", ".join(abecedario))
    print()


if __name__ == "__main__":
    main()