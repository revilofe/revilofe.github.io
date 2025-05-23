''' **Ejercicio 2.2.15**
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

'''

def leerNumerosHastaLeerCero() -> list:
    ''' Lee números enteros de teclado, hasta que el usuario ingrese el 0. 
        Devuelve una lista con los números ingresados.
    '''
    numeros = []
    numero = int(input("Ingrese un número entero: "))
    while numero != 0:
        numeros.append(numero)
        numero = int(input("Ingrese otro número entero (o 0 para salir): "))
    return numeros

def maximo(numeros: list) -> int:
    ''' Devuelve el máximo de todos los números de la lista.
    '''
    if len(numeros) == 0: raise ValueError("La lista no puede ser vacía")
    
    numeroMaximo = numeros[0]
    for numero in numeros:
        if numeroMaximo < numero:
            numeroMaximo = numero
    return numeroMaximo

def construyeMensaje(total: int ) -> str:
    ''' Construye el mensaje de salida.
    '''
    return "La sumatoria de los números ingresados es: " + str(total)

# Bloque principal del programa
if __name__ == "__main__":    
    # Entrada
    numeros = leerNumerosHastaLeerCero()

    # Proceso
    try:
        total = maximo(numeros)
    except:
        print("Error en la lista de valores")
        exit()
    
    mensaje = construyeMensaje(total)

    # Salida
    print(mensaje)
