"""
Ejercicio 3.3.6
Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}
Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.
"""

def main():
    # Dado el conjunto de letras
    vocales = {'a', 'e', 'i', 'o', 'u'}

    # 1. Crea un conjunto consonantes que contenga las letras que no son vocales
    # alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    alfabeto = set(chr(i) for i in range(97, 123))
    consonantes = alfabeto.difference(vocales)

    # 2. Crea un conjunto letras_comunes que contenga las letras en común entre vocales y consonantes
    letras_comunes = vocales.intersection(consonantes)

    print("Consonantes:", consonantes)
    print("Letras comunes entre vocales y consonantes:", letras_comunes)


if __name__ == "__main__":
    main()