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


def cargar_info_contacto(datos: list) -> dict:
    return {"nombre": datos[0], "apellido": datos[1], "email": datos[2]}


def cargar_telefonos_contacto(datos: list) -> list:
    return list(datos[i] for i in range(len(datos)))


def cargar_contactos(contactos: list):
    try:

        with open(RUTA_FICHERO, 'r') as fichero:
            for linea in fichero:
                datos = tuple(linea[:len(linea) - 1].split(';'))
                contactos.append(cargar_info_contacto(datos[:3]))
                contactos[len(contactos) - 1]["telefonos"] = cargar_telefonos_contacto(datos[3:])

    except FileNotFoundError as e:
        print(f"**Error** ({e})")
    except Exception as e:
        print(f"**Error** ({e})")


def pedir_info(dato, msj) -> str:
    res = input(msj).strip()
    if res == "":
        raise ValueError(f"el {dato} no puede ser una cadena vacía")
    return res


def pedir_email() -> str:
    res = input("Introduzca su email: ").strip()
    if res == "":
        raise ValueError("el email no puede ser una cadena vacía")
    if res.count("@") == 0:
        raise ValueError("el email no es un correo válido")
    return res


def pedir_telefonos() -> list:
    telefonos = []
    print("Introduzca los teléfonos:")

    indice = 1
    while indice == 1 or res != "":
        res = input(f"{indice}. ").strip()
        
        if res != "" and (not res.isnumeric() or len(res) != 9):
            raise ValueError(f"**Error** el teléfono no es válido, debe tener 9 posiciones numéricas")
        
        if res != "":
            telefonos.append(res)
        indice += 1

    return telefonos


def crear_contacto() -> dict:
    contacto = dict()
    contacto['nombre'] = pedir_info("nombre", "Introduzca su nombre: ")
    contacto['apellido'] = pedir_info("apellido", "Introduzca su apellido: ")
    contacto['email'] = pedir_email()
    contacto['telefonos'] = pedir_telefonos()
    return contacto


def agregar_contacto(contactos: list):
    try:
        contactos.append(crear_contacto())
        print("Se insertó 1 contacto nuevo")
    except ValueError as e:
        print(f"**Error** {e}")
        print("No se insertó ningún contacto")


def buscar_contacto(contactos: list, email: str) -> int:
    for i in range(len(contactos)):
        if str(contactos[i]['email']).lower() == email.lower():
            return i
        
    return None


def eliminar_contacto(contactos: list, email: str):
    try:
        pos = buscar_contacto(contactos, email)
        if pos != None:
            del contactos[pos]
            print("Se eliminó 1 contacto")
        else:
            print("No se encontró el contacto para eliminar")
    except ValueError as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")


def mostrar_telefonos_contacto(telefonos: list):
    if len(telefonos) == 0:
        print(f"Teléfonos: ninguno")
    else:
        print(f"Teléfonos: " + " / ".join(telefonos))


def mostrar_contactos(contactos: list):
    print(f"AGENDA ({len(contactos)})")
    print("------")

    for contacto in contactos:
        print(f"Nombre: {contacto['nombre']} {contacto['apellido']} ({contacto['email']})")
        mostrar_telefonos_contacto(contacto['telefonos'])
        print("......")


def pulse_tecla_para_continuar():
    print("\n")
    os.system("pause")


def main():
    borrar_consola()

    #asignar una estructura de datos vacía para trabajar con la agenda
    contactos = []

    #modificar la función cargar_contactos para que almacene todos los contactos del fichero en una lista con un diccionario por contacto (claves: nombre, apellido, email y telefonos)
    cargar_contactos(contactos)

    #crear función para añadir un contacto y llamarla
    #el nombre y apellido no pueden ser una cadena vacía o solo espacios
    #el email no puede ser una cadena vacía y debe contener el carácter @
    #pedir teléfonos hasta que el usuario introduzca la cadena vacía
    #un teléfono debe estar compuestos por 9 números
    agregar_contacto(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    #crear función buscar_contacto para que la función eliminar_contacto sea correcta y llamarla eliminando al contacto con el email rciruelo@gmail.com
    eliminar_contacto(contactos, "rciruelo@gmail.com")

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
    mostrar_contactos(contactos)


if __name__ == "__main__":
    main()