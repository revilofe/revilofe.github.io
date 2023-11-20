"""
Ejercicio 3.2.10
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
"""

def mostrar_menu():
    print("\nMenú:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")


def agregar_cliente(base_datos):
    nif = input("Ingrese el NIF del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    preferente = input("¿Es cliente preferente? (Sí/No): ").lower() == 'sí'

    #TODO: Crear un diccionario cliente con toda la información...
    ???

    #TODO: Añadir el diccionario cliente que previamente has creado al 
    # diccionario principal que hemos llamado base_datos...
    ???

    print(f"Cliente {nombre} añadido correctamente.")


def eliminar_cliente(base_datos):
    nif = input("Ingrese el NIF del cliente que desea eliminar: ")
    #TODO: eliminar el cliente con nif que se ha introducido
    #Si existe mostrar por consola "Cliente con NIF XXXXXXXXX eliminado correctamente."
    #Sino mostrar "No se encontró un cliente con NIF XXXXXXXXX en la base de datos."
    ???


def mostrar_cliente(base_datos):
    nif = input("Ingrese el NIF del cliente que desea mostrar: ")
    cliente = base_datos.get(nif)
    if cliente:
        print("\nDatos del cliente:")
        #TODO: Mostrar todos los datos del cliente
        #en cada línea de consola mostrar el par clave: valor de sus datos...
        ???
    else:
        print(f"No se encontró un cliente con NIF {nif} en la base de datos.")


def listar_clientes(base_datos):
    print("\nListado de todos los clientes:")
    for nif, cliente in base_datos.items():
        print(f"NIF: {nif}, Nombre: {cliente['Nombre']}")


def listar_clientes_preferentes(base_datos):
    print("\nListado de clientes preferentes:")
    for nif, cliente in base_datos.items():
        if cliente['Preferente']:
            print(f"NIF: {nif}, Nombre: {cliente['Nombre']}")


def main():
    base_datos_clientes = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            agregar_cliente(base_datos_clientes)
        elif opcion == '2':
            eliminar_cliente(base_datos_clientes)
        elif opcion == '3':
            mostrar_cliente(base_datos_clientes)
        elif opcion == '4':
            listar_clientes(base_datos_clientes)
        elif opcion == '5':
            listar_clientes_preferentes(base_datos_clientes)
        elif opcion == '6':
            print("Programa terminado.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 6.")


if __name__ == "__main__":
    main()