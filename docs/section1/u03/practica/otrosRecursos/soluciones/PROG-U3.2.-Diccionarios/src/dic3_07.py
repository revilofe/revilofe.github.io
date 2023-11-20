"""
Ejercicio 3.2.7
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
"""

def pedir_precio(articulo: str) -> float:
    """ Solicitar un precio del artículo hasta que sea un formato válido
    """
    precio = None
    while precio == None:
        try:
            precio = float(input(f"Ingrese el precio para '{articulo}': ").replace(',', '.'))
        except ValueError:
            print("*Error* precio no válido")
            precio = None

    return precio


def pedir_articulo(cesta_compra: dict) -> bool:
    """ Solicitar un artículo y su precio para añadirlo al diccionario
    """
    articulo = input("Ingrese el nombre del artículo (o escriba 'fin' para finalizar): ")

    # Verificar si el usuario desea finalizar la entrada de datos...
    if articulo.lower() == 'fin':
        return True

    cesta_compra[articulo] = pedir_precio(articulo)

    return False


def mostrar_cesta(cesta_compra: dict):
    """ Mostrar la lista de la compra y el coste total
    """
    print("\nCESTA:")
    print("{:<15} {:<10}".format("Artículo", "Precio"))
    print("-" * 25)

    total_coste = 0

    for articulo, precio in cesta_compra.items():
        print("{:<15} {:<10.2f}".format(articulo, precio))
        total_coste += precio

    print("-" * 25)
    print("{:<15} {:<10.2f}".format("Total", total_coste))



def main():
    cesta_compra = {}
    fin = False

    while not fin:
        fin = pedir_articulo(cesta_compra)

    mostrar_cesta(cesta_compra)


if __name__ == '__main__':
    main()