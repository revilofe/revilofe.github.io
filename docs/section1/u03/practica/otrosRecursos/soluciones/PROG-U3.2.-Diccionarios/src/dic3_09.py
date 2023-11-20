"""
Ejercicio 3.2.9
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""

def pedir_importe(msj: str) -> float:
    importe = None
    while importe == None:
        try:
            importe = float(input("Ingrese el coste de la factura: ").replace(',', '.'))
        except ValueError:
            importe = None
            print("*Error* importe no válido")
    return importe


def mostrar_estado_cobros(facturas):
    total_cobrado = sum(facturas.values())
    total_pendiente = sum(facturas.values())
    print("\nEstado de cobros:")
    print(f"Cantidad cobrada hasta el momento: {total_cobrado}")
    print(f"Cantidad pendiente de cobro: {total_pendiente}\n")


def agregar_factura(facturas):
    numero_factura = input("Ingrese el número de factura: ")
    coste_factura = pedir_importe("Ingrese el coste de la factura: ")
    facturas[numero_factura] = coste_factura
    print(f"¡Nueva factura añadida! Coste: {coste_factura}")
    mostrar_estado_cobros(facturas)


def pagar_factura(facturas):
    numero_factura = input("Ingrese el número de factura que desea pagar: ")
    if numero_factura in facturas:
        coste_pagado = facturas.pop(numero_factura)
        print(f"¡Factura {numero_factura} pagada! Coste: {coste_pagado}")
        mostrar_estado_cobros(facturas)
    else:
        print(f"No existe una factura con el número {numero_factura}.")


def main():
    # Inicializar el diccionario de facturas
    facturas = {}

    opcion = 0
    while opcion != '3':
        # Mostrar opciones al usuario
        print("1. Añadir nueva factura")
        print("2. Pagar factura existente")
        print("3. Terminar")

        # Solicitar la elección del usuario
        opcion = input(">> Seleccione una opción: ")

        if opcion == '1':
            # Añadir nueva factura
            agregar_factura(facturas)
        elif opcion == '2':
            # Pagar factura existente
            pagar_factura(facturas)
        elif opcion not in {'1', '2', '3'}:
            print("Opción no válida. Por favor, elija una opción válida.")



if __name__ == "__main__":
    main()