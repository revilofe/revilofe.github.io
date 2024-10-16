''' **Ejercicio 2.2.14**
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

# 

sumatoria = 0
numero = int(input("Ingrese un número entero: "))

while numero != 0:
    sumatoria += numero
    numero = int(input("Ingrese otro número entero (o 0 para salir): "))

print("La sumatoria de los números ingresados es:", sumatoria)

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

def sumatoria(numeros: list) -> int:
    ''' Devuelve la sumatoria de todos los números de la lista.
    '''
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

def construyeMensaje(total: int ) -> str:
    ''' Construye el mensaje de salida.
    '''
    return "La sumatoria de los números ingresados es: " + str(total)

# Bloque principal del programa
if __name__ == "__main__":    
    # Entrada
    numeros = leerNumerosHastaLeerCero()

    # Proceso
    total = sumatoria(numeros)
    mensaje = construyeMensaje(total)

    # Salida
    print(mensaje)
