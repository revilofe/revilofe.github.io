"""
Ejercicio 3.1.4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
6 números de 1 a 49 + reintegro de 0 a 9
Los 6 números deben ser únicos
"""

from EjerciciosU2.Pract2_2.ej2_2_01 import borrarConsola


def pedir_numero(indice: int, numeros_loteria: list):
    error = True
    while error:
        try:
            numero = int(input(f"({indice}) => "))
            if not (1 <= numero <= 49):
                raise ValueError
            if numeros_loteria.count(numero) >= 1:
                raise Exception("**Error** número repetido (ya lo introdujo anteriormente)")
            error = False
        except ValueError:
            print("**Error** número no válido (solo números enteros del rango 1-49)")
        except Exception as e:
            print(e)
    
    numeros_loteria.append(numero)


def pedir_reintegro() -> int:
    error = True
    while error:
        try:
            numero = int(input("(Reintegro) => "))
            if not (0 <= numero <= 9):
                raise ValueError
            error = False
        except ValueError:
            print("**Error** número no válido (solo un número entero del rango 0-9)")

    return numero


def introducir_numeros_loteria() -> tuple:
    numeros_loteria = []
    for i in range(1, 7):
        pedir_numero(i, numeros_loteria)
    
    numeros_loteria.sort()
    numeros_loteria.append(pedir_reintegro())
    
    return tuple(numeros_loteria)


def mostar_loteria(numeros_loteria):
    lista_numeros = ""
    for i in range(6):
        lista_numeros += str(numeros_loteria[i]) + ", "
    
    print("\nNúmeros: " + lista_numeros[:len(lista_numeros) - 2])
    print("Reintegro: " + str(numeros_loteria[6]))


def main():
    borrarConsola()
    print("Ejercicio 3.1.4")
    print("---------------\n")

    print("Introduzca los números de la lotería: ")
    numeros_loteria = introducir_numeros_loteria()
    
    mostar_loteria(numeros_loteria)

    print()
    print(numeros_loteria)
    print()


if __name__ == "__main__":
    main()