""" **Ejercicio 2.2.15** Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la
sumatoria de todos los números positivos ingresados.


"""


def leer_numeros_hasta_leer_cero() -> list:
    """ Lee números enteros de teclado, hasta que el usuario ingrese el 0.
        Devuelve una lista con los números ingresados.
    """
    numeros_leidos = []
    numero = int(input("Ingrese un número entero: "))
    while numero != 0:
        numeros_leidos.append(numero)
        numero = int(input("Ingrese otro número entero (o 0 para salir): "))
    return numeros_leidos


def sumatoria_de_positivos(numeros_a_sumar: list) -> int:
    """ Devuelve la sumatoria de todos los números de la lista.
    """
    suma = 0
    for numero in numeros_a_sumar:
        if numero > 0:
            suma += numero
    return suma


def construye_mensaje(total_sumatoria: int) -> str:
    """ Construye el mensaje de salida.
    """
    return "La sumatoria de los números ingresados es: " + str(total_sumatoria)


# Bloque principal del programa
if __name__ == "__main__":
    # Entrada
    numeros = leer_numeros_hasta_leer_cero()

    # Proceso
    total = sumatoria_de_positivos(numeros)
    mensaje = construye_mensaje(total)

    # Salida
    print(mensaje)



