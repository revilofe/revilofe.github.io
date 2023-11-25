"""
27/11/2023

Práctica del examen para realizar en casa
-----------------------------------------

* El programa debe estar correctamente documentado.

* Debes intentar ajustarte lo máximo que puedas a lo que se pide en los comentarios TODO.

* Tienes libertad para desarrollar los métodos o funciones que consideres, pero estás obligado a usar como mínimo todos los que se solicitan en los comentarios TODO.

* Además, tu programa deberá pasar correctamente las pruebas unitarias que se adjuntan en el fichero test_agenda.py, por lo que estás obligado a desarrollar los métodos que se importan y prueban en la misma: pedir_email(), validar_email() y validar_telefono()

"""

import os
import pathlib
from os import path

# Constantes globales
RUTA = pathlib.Path(__file__).parent.absolute() 

NOMBRE_FICHERO = 'contactos.csv'

RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)

#TODO: Crear un conjunto con las posibles opciones del menú de la agenda
OPCIONES_MENU = ?
#TODO: Utiliza este conjunto en las funciones agenda() y pedir_opcion()


def borrar_consola():
    """ Limpia la consola
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def cargar_contactos(contactos: list):
    """ Carga los contactos iniciales de la agenda desde un fichero
    ...
    """
    #TODO: Controlar los posibles problemas derivados del uso de ficheros...

    with open(RUTA_FICHERO, 'r') as fichero:
        for linea in fichero:
            print(linea)


def eliminar_contacto(contactos: list, email: str):
    """ Elimina un contacto de la agenda
    ...
    """
    try:
        #TODO: Crear función buscar_contacto para recuperar la posición de un contacto con un email determinado

        if pos != None:
            del contactos[pos]
            print("Se eliminó 1 contacto")
        else:
            print("No se encontró el contacto para eliminar")
    except Exception as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")


def agenda(contactos: list):
    """ Ejecuta el menú de la agenda con varias opciones
    ...
    """
    #TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...

    while opcion != 7:
        mostrar_menu()
        opcion = pedir_opcion()

        #TODO: Se valorará que utilices la diferencia simétrica de conjuntos para comprobar que la opción es un número entero del 1 al 6
        if opcion in ?:



def pulse_tecla_para_continuar():
    """ Muestra un mensaje y realiza una pausa hasta que se pulse una tecla
    """
    print("\n")
    os.system("pause")


def main():
    """ Función principal del programa
    """
    borrar_consola()

    #TODO: Asignar una estructura de datos vacía para trabajar con la agenda
    contactos = ?

    #TODO: Modificar la función cargar_contactos para que almacene todos los contactos del fichero en una lista con un diccionario por contacto (claves: nombre, apellido, email y telefonos)
    #TODO: Realizar una llamada a la función cargar_contacto con todo lo necesario para que funcione correctamente.
    cargar_contactos(?)

    #TODO: Crear función para agregar un contacto. Debes tener en cuenta lo siguiente:
    # - El nombre y apellido no pueden ser una cadena vacía o solo espacios y se guardarán con la primera letra mayúscula y el resto minúsculas (ojo a los nombre compuestos)
    # - El email debe ser único en la lista de contactos, no puede ser una cadena vacía y debe contener el carácter @.
    # - El email se guardará tal cuál el usuario lo introduzca, con las mayúsculas y minúsculas que escriba. 
    #  (CORREO@gmail.com se considera el mismo email que correo@gmail.com)
    # - Pedir teléfonos hasta que el usuario introduzca una cadena vacía, es decir, que pulse la tecla <ENTER> sin introducir nada.
    # - Un teléfono debe estar compuesto solo por 9 números, aunque debe permitirse que se introduzcan espacios entre los números.
    # - Además, un número de teléfono puede incluir de manera opcional un prefijo +34.
    # - De igual manera, aunque existan espacios entre el prefijo y los 9 números al introducirlo, debe almacenarse sin espacios.
    # - Por ejemplo, será posible introducir el número +34 600 100 100, pero guardará +34600100100 y cuando se muestren los contactos, el telófono se mostrará como +34-600100100. 
    #TODO: Realizar una llamada a la función agregar_contacto con todo lo necesario para que funcione correctamente.
    agregar_contacto(?)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Realizar una llamada a la función eliminar_contacto con todo lo necesario para que funcione correctamente, eliminando el contacto con el email rciruelo@gmail.com
    eliminar_contacto(?)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Crear función mostrar_contactos para que muestre todos los contactos de la agenda con el siguiente formato:
    # ** IMPORTANTE: debe mostrarlos ordenados según el nombre, pero no modificar la lista de contactos de la agenda original **
    #
    # AGENDA (6)
    # ------
    # Nombre: Antonio Amargo (aamargo@gmail.com)
    # Teléfonos: niguno
    # ......
    # Nombre: Daniela Alba (danalba@gmail.com)
    # Teléfonos: +34-600606060 / +34-670898934
    # ......
    # Nombre: Laura Iglesias (liglesias@gmail.com)
    # Teléfonos: 666777333 / 666888555 / 607889988
    # ......
    # ** resto de contactos **
    #
    #TODO: Realizar una llamada a la función mostrar_contactos con todo lo necesario para que funcione correctamente.
    mostrar_contactos(?)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Crear un menú para gestionar la agenda con las funciones previamente desarrolladas y las nuevas que necesitéis:
    # AGENDA
    # ------
    # 1. Nuevo contacto
    # 2. Modificar contacto
    # 3. Eliminar contacto
    # 4. Vaciar agenda
    # 5. Cargar agenda inicial
    # 6. Mostrar contactos por criterio
    # 7. Mostrar la agenda completa
    # 8. Salir
    #
    # >> Seleccione una opción: 
    #
    #TODO: Para la opción 3, modificar un contacto, deberás desarrollar las funciones necesarias para actualizar la información de un contacto.
    #TODO: También deberás desarrollar la opción 6 que deberá preguntar por el criterio de búsqueda (nombre, apellido, email o telefono) y el valor a buscar para mostrar los contactos que encuentre en la agenda.
    agenda(?)


if __name__ == "__main__":
    main()