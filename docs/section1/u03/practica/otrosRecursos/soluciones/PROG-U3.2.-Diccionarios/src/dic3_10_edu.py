
"""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor `True` si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
3. Preguntar por el NIF del cliente y mostrar sus datos.
4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
6. Terminar el programa.

## Ejemplo de ejecución del programa

Bienvenido al programa de gestión de clientes
¿Qué desea hacer? Escriba el número de la opción:
(1) Añadir cliente
(2) Eliminar cliente
(3) Mostrar cliente
(4) Listar todos los clientes
(5) Listar clientes preferentes
(6) Terminar

1
Introduzca el NIF del cliente: 12345678A
Introduzca el nombre del cliente: Perico de los Palotes
Introduzca la dirección del cliente: C/ Falsa, 123
Introduzca el teléfono del cliente: 123456789
Introduzca el correo electrónico del cliente: perico@gmail.com
¿Es un cliente preferente (S/N)? s

¿Qué desea hacer? Escriba el número de la opción: 2
"""

import os


# Funciones que interactuan con el usuario
def menu():
    opciones = ("1","2", "3", "4", "5", "6")
    opcion = ""
    limpiar_pantalla()
    while opcion not in opciones:
        print("Bienvenido al programa de gestión de clientes")
        print("(1) Añadir cliente")
        print("(2) Eliminar cliente")
        print("(3) Mostrar cliente")
        print("(4) Listar todos los clientes")
        print("(5) Listar clientes preferentes")
        print("(6) Terminar")

        opcion = input("¿Qué desea hacer? Escriba el número de la opción:")
    return opcion

def limpiar_pantalla():
    """
    Limpia la pantalla, difenrente en windows y linux
    """
    os.system("clear")


def pause():
    """
    Pausa el programa hasta que el usuario pulse intro
    """
    input("Pulse intro para continuar...")

def pedir_datos_cliente():
    """
    Pide los datos de un cliente y devuelve un diccionario con los datos y el nif
    """
    nif = input("Introduzca el NIF del cliente: ")
    nombre = input("Introduzca el nombre del cliente: ")
    direccion = input("Introduzca la dirección del cliente: ")
    telefono = input("Introduzca el teléfono del cliente: ")
    correo = input("Introduzca el correo electrónico del cliente: ")
    preferente = input("¿Es un cliente preferente (S/N)? ")
    if preferente == "S":
        preferente = True
    else:
        preferente = False
    cliente = {"nombre": nombre, "direccion": direccion, "telefono": telefono, "correo": correo,
               "preferente": preferente}
    return cliente, nif

def pedir_nif():
    """
    Pide el nif de un cliente
    """
    return input("Introduzca el NIF del cliente: ")

def imprimir_cliente_multilinea(nif, cliente):
    """Imprimer los datos del cliente en varias lineas"""
    print("NIF:", nif)
    print("######################")
    print("Nombre:", cliente["nombre"])
    print("Dirección:", cliente["direccion"])
    print("Teléfono:", cliente["telefono"])
    print("Correo:", cliente["correo"])
    print("Preferente:", cliente["preferente"])

# Funciones que trabajar con mi base de datos, en este caso es un diccionario.
def anadir_cliente(clientes, nif, cliente):
    """
    Añade un cliente a la base de datos
    :param clientes: diccionario con los clientes
    :param nif: nif del cliente
    :param cliente: diccionario con los datos del cliente
    :return: None
    """
    clientes[nif] = cliente


def obtener_todos_clientes(clientes):
    """
    Devuelve un diccionario con todos los clientes
    :param clientes: diccionario con los clientes
    :return: diccionario con todos los clientes
    """
    return clientes.copy()

def obtener_cliente_por_nif(clientes, nif):
    """
    Devuelve el cliente con el nif indicado o None si no existe
    :param clientes: diccionario con los clientes
    :param nif: nif del cliente a buscar
    :return: cliente con el nif indicado o None si no existe
    """
    return clientes.get(nif)

def eliminar_cliente(clientes, nif):
    """
    Elimina un cliente de la base de datos
    :param clientes: diccionario con los clientes
    :param nif: nif del cliente a eliminar
    :return: cliente eliminado o None si no existe
    """
    cliente = obtener_cliente_por_nif(clientes, nif)
    del clientes[nif]
    return cliente


# Funciones que implementan las opciones del programa
def opcion_anadir_cliente(clientes:dict):
    """
    Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    """
    # Entrada
    cliente, nif = pedir_datos_cliente()

    # Proceso
    anadir_cliente(clientes, nif, cliente)

    # Salida
    print("Cliente añadido correctamente.")



def opcion_mostrar_todos_clientes(clientes):
    """
    Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    """
    #Entrada
    #Proceso
    todos_clientes = obtener_todos_clientes(clientes)

    #Salida
    print("Lista de clientes")
    print("-----------------")
    for nif, cliente in todos_clientes.items():
        imprimir_cliente_multilinea(nif, cliente)


def opcion_mostrar_clientes_preferentes(clientes):
    """
    Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
    """
    #Entrada
    #Proceso
    todos_clientes = obtener_todos_clientes(clientes)

    #Salida
    print("Lista de clientes preferentes")
    print("------------------------------")
    for nif, cliente in todos_clientes.items():
        if cliente["preferente"]:
            imprimir_cliente_multilinea(nif, cliente)


def opcion_mostrar_cliente(clientes):
    """
    Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    :param clientes: diccionario con los clientes
    """
    #Entrada

    nif = pedir_nif()

    #Proceso
    cliente = obtener_cliente_por_nif(clientes, nif)

    #Salida
    if cliente != None:
        imprimir_cliente_multilinea(nif, cliente)
    else:
        print("No existe el cliente con el nif", nif)

def opcion_eliminar_cliente(clientes):
    """
    Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    """
    #Entrada
    nif = pedir_nif()

    #Proceso
    cliente = eliminar_cliente(clientes, nif)

    #Salida
    if cliente != None:
        print("Cliente eliminado correctamente.")
    else:
        print("No existe el cliente con el nif", nif)



def main():
    clientes = {}
    opcion = menu()
    while opcion != "6":
        if opcion == "1":
            # 1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
            opcion_anadir_cliente(clientes)
            pause()
        elif opcion == "2":
            opcion_eliminar_cliente(clientes)
            pause()
        elif opcion == "3":
            opcion_mostrar_cliente(clientes)
            pause()
        elif opcion == "4":
            opcion_mostrar_todos_clientes(clientes)
            pause()
        elif opcion == "5":
            opcion_mostrar_clientes_preferentes(clientes)
            pause()
        opcion = menu()
    print("Fin del programa")

if __name__ == "__main__":
    main()
