
# 3.3.4

# Dadas las listas
frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

# 1. Crea conjuntos a partir de estas listas
set_frutas1 = set(frutas1)
set_frutas2 = set(frutas2)

# 2. Encuentra las frutas que están en ambas listas
frutas_comunes = set_frutas1.intersection(set_frutas2)

# 3. Encuentra las frutas que están en frutas1 pero no en frutas2
frutas_solo_en_frutas1 = set_frutas1.difference(set_frutas2)

# 4. Encuentra las frutas que están en frutas2 pero no en frutas1
frutas_solo_en_frutas2 = set_frutas2.difference(set_frutas1)

print("Frutas comunes:", frutas_comunes)
print("Frutas solo en frutas1:", frutas_solo_en_frutas1)
print("Frutas solo en frutas2:", frutas_solo_en_frutas2)

"""Resultado:

Frutas comunes: {'manzana', 'pera', 'uva'}
Frutas solo en frutas1: {'naranja', 'plátano'}
Frutas solo en frutas2: {'sandía', 'durazno'}
Estas son las soluciones al ejercicio 1. Si necesitas más ayuda o tienes alguna otra pregunta, no dudes en decírmelo.
"""