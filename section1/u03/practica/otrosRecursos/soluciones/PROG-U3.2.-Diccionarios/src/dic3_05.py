"""
Ejercicio 3.2.5
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""

def main():
    creditos_asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

    print()

    total_creditos = 0
    for asignatura, creditos in creditos_asignaturas.items():
        total_creditos += creditos
        print(f"{asignatura} tiene {creditos} créditos.")

    #Otra forma de hacerlo
    #total_creditos = sum(creditos_asignaturas.values())

    print(f"\nEl número total de créditos del curso es: {total_creditos}\n")


if __name__ == '__main__':
    main()