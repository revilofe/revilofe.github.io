

# 3.3.4

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

"""
Resultado:
Números pares: {2, 4, 6, 8, 10}
Múltiplos de tres: {3, 6, 9}
Intersección entre pares y múltiplos de tres: {6}
Estas son las soluciones al ejercicio 2. Si necesitas más ayuda o tienes alguna otra pregunta, no dudes en decírmelo.
"""