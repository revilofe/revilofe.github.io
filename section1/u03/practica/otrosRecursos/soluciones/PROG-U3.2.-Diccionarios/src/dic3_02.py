"""
Ejercicio 3.2.2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""

def obtener_informacion_usuario() -> dict:
    """ Obtener la información del usuario
    """

    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    direccion = input("Ingrese su dirección: ")
    telefono = input("Ingrese su número de teléfono: ")

    informacion_usuario = {
        'Nombre': nombre,
        'Edad': edad,
        'Dirección': direccion,
        'Teléfono': telefono
    }

    return informacion_usuario


def mostrar_informacion_usuario(usuario: dict):
    """ Mostrar la información del usuario
    """
    mensaje = f"{usuario['Nombre']} tiene {usuario['Edad']} años, vive en {usuario['Dirección']} y su número de teléfono es {usuario['Teléfono']}."
    print(mensaje)


def main():
    mostrar_informacion_usuario(obtener_informacion_usuario())


if __name__ == '__main__':
    main()