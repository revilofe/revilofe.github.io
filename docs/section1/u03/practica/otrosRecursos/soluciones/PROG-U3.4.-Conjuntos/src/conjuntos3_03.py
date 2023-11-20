"""
Ejercicio 3.3.3
El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.

Por ejemplo, el conjunto potencia de {1,2,3} es:

{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s y retorne su «lista potencia» (la lista de todos sus subconjuntos):

>>> conjunto_potencia({6, 1, 4})
[set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]
"""

def conjunto_potencia(conjunto_original: set) -> list:
    # Inicializar la lista potencia con el conjunto vacío
    potencia = [set()]

    # Generar el conjunto potencia
    for elemento in conjunto_original:
        # Crear nuevos conjuntos agregando el elemento actual a los conjuntos existentes
        nuevos_subconjuntos = []
        for subconjunto in potencia:
            nuevos_subconjuntos.append(subconjunto | {elemento})
        
        # Agregar los nuevos subconjuntos a la lista potencia
        potencia.extend(nuevos_subconjuntos)

    return potencia


def main():
    conjunto_original = {6, 1, 4}
    resultado = conjunto_potencia(conjunto_original)
    print(resultado)


if __name__ == "__main__":
    main()
