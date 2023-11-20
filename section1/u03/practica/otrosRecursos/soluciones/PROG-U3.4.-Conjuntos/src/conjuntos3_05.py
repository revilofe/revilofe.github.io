"""
Ejercicio 3.3.5
Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
"""

def main():
    # Dado el conjunto de números enteros
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    # 1. Crea un conjunto pares que contenga los números pares
    pares = {num for num in numeros if num % 2 == 0}

    # 2. Crea un conjunto multiplos_de_tres que contenga los múltiplos de tres
    multiplos_de_tres = {num for num in numeros if num % 3 == 0}

    # 3. Encuentra la intersección entre los conjuntos pares y multiplos_de_tres
    pares_y_multiplos_de_tres = pares.intersection(multiplos_de_tres)

    print("Números pares:", pares)
    print("Múltiplos de tres:", multiplos_de_tres)
    print("Intersección entre pares y múltiplos de tres:", pares_y_multiplos_de_tres)


if __name__ == "__main__":
    main()