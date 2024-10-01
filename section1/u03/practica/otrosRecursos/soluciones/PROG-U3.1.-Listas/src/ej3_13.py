"""
Ejercicio 3.1.13
Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

https://www.superprof.es/apuntes/escolar/matematicas/estadistica/descriptiva/desviacion-tipica.html

"""

import math
from EjerciciosU2.Pract2_2.ej2_2_01 import borrarConsola


def pedir_lista_numeros() -> tuple:
    error = True
    while error:
        try:
            entrada = input("Lista de números separados por coma:\n").split(',')
            lista = tuple(int(valor) for valor in entrada)
            error = False
        except Exception:
            print("**Error** debe introducir una lista de números enteros separados por una coma")

    return lista


def calcular_media(lista_numeros: tuple) -> float:
    media: float = 0
    for num in lista_numeros:
        media += num
    
    return media/len(lista_numeros)


def calcular_desviacion_tipica(lista_numeros: tuple, media: float) -> float:
    desviacion: float = 0
    for num in lista_numeros:
        desviacion = (num - media) ** 2

    desviacion /= len(lista_numeros)
    return math.sqrt(desviacion)
    #return desviacion ** (0.5)


def main():
    borrarConsola()
    print("Ejercicio 3.1.13")
    print("---------------\n")

    lista_numeros = pedir_lista_numeros()

    media = calcular_media(lista_numeros)

    desviacion_tipica = calcular_desviacion_tipica(lista_numeros, media)

    print()
    print(lista_numeros)
    print()
    print(f"La media es {media:.2f}")
    print(f"La desviación típica es {desviacion_tipica:.2f}")


if __name__ == "__main__":
    main()