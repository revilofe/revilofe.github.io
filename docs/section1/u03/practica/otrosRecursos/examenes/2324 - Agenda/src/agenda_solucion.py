import copy
import os
import pathlib
from os import path


#Constantes globales
RUTA = pathlib.Path(__file__).parent.absolute() 
NOMBRE_FICHERO = 'contactos.csv'
RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)
OPCIONES_MENU = {1, 2, 3, 4, 5, 6}


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
    res = input(msj).strip().title()
    if res == "":
        raise ValueError(f"el {dato} no puede ser una cadena vacía")
    return res


def pedir_email(contactos: list, comprobar_si_existe = True) -> str:
    email = input("Introduzca su email: ").strip()
    if email == "":
        raise ValueError("el email no puede ser una cadena vacía")
    if email.count("@") == 0:
        raise ValueError("el email no es un correo válido")
    if comprobar_si_existe and buscar_contacto(contactos, email) != None:
        raise ValueError("el email ya existe en la agenda")
    return email


def comprobar_telefono(telefono: str) -> bool:
    if telefono[:3] == '+34':
        telefono = telefono[3:]  
    return (telefono.isdecimal() and len(telefono) == 9)
    

def pedir_telefonos() -> list:
    telefonos = []
    print("Introduzca los teléfonos (<ENTER> sin información para finalizar):")

    indice = 1
    while indice == 1 or telefono != "":
        telefono = input(f"Teléfono {indice} => ").replace(" ", "")
        
        if telefono != "" and not comprobar_telefono(telefono):
            raise ValueError(f"**Error** el teléfono no es válido, debe tener 9 posiciones numéricas")
        
        if telefono != "":
            telefonos.append(telefono)

        indice += 1

    return telefonos


def crear_contacto(contactos: list) -> dict:
    contacto = dict()
    contacto['nombre'] = pedir_info("nombre", "Introduzca su nombre: ")
    contacto['apellido'] = pedir_info("apellido", "Introduzca su apellido: ")
    contacto['email'] = pedir_email(contactos)
    contacto['telefonos'] = pedir_telefonos()
    return contacto


def agregar_contacto(contactos: list):
    try:
        contactos.append(crear_contacto(contactos))
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
        print(f"Teléfonos: " + " / ".join(telefonos).replace("+34", "+34-"))


def ordenar_contactos(contactos: list):
    for i in range(len(contactos) - 1):
        for j in range(i + 1, len(contactos)):
            if contactos[i]['nombre'].lower() > contactos[j]['nombre'].lower():
                contacto_temp = contactos[i]
                contactos[i] = contactos[j]
                contactos[j] = contacto_temp


def mostrar_contactos(contactos: list):
    print(f"AGENDA ({len(contactos)})")
    print("------")

    #Para no modificar la agenda original, podemos hacer una copia profunda...
    #contactos_list = copy.deepcopy(contactos)
    #O la volvemos a crear partiendo de los elementos de la anterior...
    contactos_list = list(contactos)
    ordenar_contactos(contactos_list)

    for contacto in contactos_list:
        print(f"Nombre: {contacto['nombre']} {contacto['apellido']} ({contacto['email']})")
        mostrar_telefonos_contacto(contacto['telefonos'])
        print("......")


def modificar_contacto(contactos: list):
    print("")
    

def pedir_opcion() -> int:
    try:
        opcion = int(input(">> Seleccione una opción (1-6): "))
        if opcion not in OPCIONES_MENU:
            raise ValueError
    except ValueError:
        opcion = -1
        print("*Error* opción no válida")
        pulse_tecla_para_continuar()
    
    return opcion


def mostrar_menu():
    borrar_consola()

    print("AGENDA")
    print("------")
    print("1. Nuevo contacto")
    print("2. Modificar contacto")
    print("3. Eliminar contacto")
    print("4. Vaciar agenda")
    print("5. Cargar agenda inicial")
    print("6. Salir\n")


def agenda(contactos: list):
    opcion = 0
    while opcion != 6:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion in OPCIONES_MENU ^ {6}:
            if opcion == 1:
                agregar_contacto(contactos)
            elif opcion == 2:
                modificar_contacto(contactos)
            elif opcion == 3:
                try:
                    email = pedir_email(contactos, False)
                except ValueError as e:
                    print(f"*Error* {e}")
                else:
                    eliminar_contacto(contactos, email)
            elif opcion == 4:
                contactos.clear()
            elif opcion == 5:
                cargar_contactos(contactos)

        if opcion != 6:
            pulse_tecla_para_continuar()


def pulse_tecla_para_continuar():
    print("\n")
    os.system("pause")


def main():
    borrar_consola()

    contactos = []

    cargar_contactos(contactos)

    agregar_contacto(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    eliminar_contacto(contactos, "rciruelo@gmail.com")

    pulse_tecla_para_continuar()
    borrar_consola()

    mostrar_contactos(contactos)


if __name__ == "__main__":
    main()