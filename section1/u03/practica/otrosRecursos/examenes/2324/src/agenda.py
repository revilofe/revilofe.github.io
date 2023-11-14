"""
Propuesta de examen
"""

import os
import pathlib
from os import path


RUTA = pathlib.Path(__file__).parent.absolute() 
NOMBRE_FICHERO = 'contactos.csv'
RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)


def borrar_consola():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def cargar_contactos(contactos: list):
    try:

        with open(RUTA_FICHERO, 'r') as fichero:
            for linea in fichero:
                print(linea)

    except FileNotFoundError as e:
        print(f"**Error** ({e})")
    except Exception as e:
        print(f"**Error** ({e})")


def eliminar_contacto(contactos: list, email: str):
    try:
        #pos = buscar_contacto(?)
        if pos != None:
            del contactos[pos]
            print("Se eliminó 1 contacto")
        else:
            print("No se encontró el contacto para eliminar")
    except ValueError as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")


def pulse_tecla_para_continuar():
    print("\n")
    os.system("pause")


def main():
    borrar_consola()

    #asignar una estructura de datos vacía para trabajar con la agenda
    contactos = ?

    #modificar la función cargar_contactos para que almacene todos los contactos del fichero en una lista con un diccionario por contacto (claves: nombre, apellido, email y telefonos)
    cargar_contactos(?)

    #crear función para añadir un contacto y llamarla
    #el nombre y apellido no pueden ser una cadena vacía o solo espacios
    #el email no puede ser una cadena vacía y debe contener el carácter @
    #pedir teléfonos hasta que el usuario introduzca la cadena vacía
    #un teléfono debe estar compuestos por 9 números
    agregar_contacto(?)

    pulse_tecla_para_continuar()
    borrar_consola()

    #crear función buscar_contacto para que la función eliminar_contacto sea correcta y llamarla eliminando al contacto con el email rciruelo@gmail.com
    eliminar_contacto(?)

    pulse_tecla_para_continuar()
    borrar_consola()

    #crear función mostrar_contactos para que muestre la agenda resultante con el formato:
    #
    # AGENDA (6)
    # ------
    # Nombre: Laura Iglesias (liglesias@gmail.com)
    # Teléfonos: 666777333 / 666888555 / 607889988
    # ......
    # Nombre: Antonio Amargo (aamargo@gmail.com)
    # Teléfonos: niguno
    # ......
    mostrar_contactos(?)


if __name__ == "__main__":
    main()