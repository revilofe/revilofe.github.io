"""
Ejercicio 3.1.10
Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.
"""

from EjerciciosU2.Pract2_2.ej2_2_01 import borrarConsola


def ordenar_precios(precios: tuple) -> list:
    lista_precios = list(precios)
    lista_precios.sort()
    return lista_precios


def obtener_mayor(precios: tuple) -> int:
    mayor = None
    for precio in precios:
        if mayor == None or precio > mayor:
            mayor = precio
    
    return mayor


def obtener_menor(precios: tuple) -> int:
    menor = None
    for precio in precios:
        if menor == None or precio < menor:
            menor = precio
    
    return menor


def main():
    borrarConsola()
    print("Ejercicio 3.1.10")
    print("---------------\n")

    precios = (50, 75, 46, 22, 80, 65, 8)

    print("Opción 1")
    print("Menor: " + str(obtener_menor(precios)))
    print("Mayor: " + str(obtener_mayor(precios)))

    print("\nOpción 2")
    lista_precios = ordenar_precios(precios)
    print("Menor: " + str(lista_precios[0]))
    print("Mayor: " + str(lista_precios[len(lista_precios) - 1]))

    print()
    print(precios)
    print()


if __name__ == "__main__":
    main()