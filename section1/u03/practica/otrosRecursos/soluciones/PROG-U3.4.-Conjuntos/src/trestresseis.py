# 3.3.4

# Dado el conjunto de letras
vocales = {'a', 'e', 'i', 'o', 'u'}

# 1. Crea un conjunto consonantes que contenga las letras que no son vocales
alfabeto = set('abcdefghijklmnopqrstuvwxyz')
consonantes = alfabeto.difference(vocales)

# 2. Crea un conjunto letras_comunes que contenga las letras en común entre vocales y consonantes
letras_comunes = vocales.intersection(consonantes)

print("Consonantes:", consonantes)
print("Letras comunes entre vocales y consonantes:", letras_comunes)

"""
Resultado:

Consonantes: {'c', 'm', 'd', 'n', 'j', 'y', 'x', 'f', 'z', 'w', 'p', 'v', 's', 'q', 't', 'l', 'g', 'r', 'b', 'h', 'k'}
Letras comunes entre vocales y consonantes: set()
En este caso, no hay letras en común entre las vocales y las consonantes.

Estas son las soluciones al ejercicio 3. Si necesitas más ayuda o tienes alguna otra pregunta, no dudes en decírmelo.
"""