import copy
import os
import pathlib
from os import path


# Constantes globales
RUTA = pathlib.Path(__file__).parent.absolute()
NOMBRE_FICHERO = 'contactos.csv'
RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)
OPCIONES_MENU = {1, 2, 3, 4, 5, 6, 7, 8}


def borrar_consola():
    """
    Borra la consola según el sistema operativo.
    """
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def cargar_info_contacto(datos: list) -> dict:
    """
    Carga la información de un contacto desde una lista.

    Parámetros:
    - datos (list): Lista con la información del contacto.

    Retorna:
    - dict: Diccionario con la información del contacto.
    """
    return {"nombre": datos[0], "apellido": datos[1], "email": datos[2]}


def cargar_telefonos_contacto(datos: list) -> list:
    """
    Carga los teléfonos de un contacto desde una lista.

    Parámetros:
    - datos (list): Lista con los teléfonos del contacto.

    Retorna:
    - list: Lista de teléfonos del contacto.
    """
    return list(datos[i] for i in range(len(datos)))


def existe_archivo(ruta):
    """
    Verifica si un archivo existe en la ruta especificada.

    Parámetros:
    - ruta (str): Ruta del archivo.

    Retorna:
    - bool: True si el archivo existe, False en caso contrario.
    """
    return path.exists(ruta)
       

def cargar_contactos(contactos: list):
    """
    Carga los contactos desde un archivo CSV y los agrega a la lista.

    Parámetros:
    - contactos (list): Lista de contactos.
    """
    try:
        if existe_archivo(RUTA_FICHERO):
            with open(RUTA_FICHERO, 'r') as fichero:
                for linea in fichero:
                    datos = tuple(linea.rstrip('\n').split(';'))
                    contactos.append(cargar_info_contacto(datos[:3]))
                    contactos[-1]["telefonos"] = cargar_telefonos_contacto(datos[3:])
        else:
            print("El archivo de contactos no existe.")
    except Exception as e:
        print(f"**Error** ({e})")


def pedir_info(dato, msj) -> str:
    """
    Pide información al usuario y valida que no sea una cadena vacía.

    Parámetros:
    - dato (str): Tipo de dato que se está pidiendo.
    - msj (str): Mensaje para el usuario.

    Retorna:
    - str: Información proporcionada por el usuario.
    """
    res = input(msj).strip().title()
    if res == "":
        raise ValueError(f"el {dato} no puede ser una cadena vacía")
    return res


def validar_email(email: str, contactos: list, comprobar_si_existe: bool) -> None:
    """
    Valida el formato del correo electrónico y si ya existe en la agenda.

    Parámetros:
    - email (str): Correo electrónico a validar.
    - contactos (list): Lista de contactos existentes.
    - comprobar_si_existe (bool): Indica si se debe comprobar si el email ya existe en la agenda.

    Levanta:
    - ValueError: Si el email no es válido o ya existe en la agenda.
    """
    if email == "":
        raise ValueError("el email no puede ser una cadena vacía")
    if email.count("@") == 0:
        raise ValueError("el email no es un correo válido")
    if comprobar_si_existe and buscar_contacto(contactos, email) is not None:
        raise ValueError("el email ya existe en la agenda")


def pedir_email(contactos: list, comprobar_si_existe = True) -> str:
    """
    Pide al usuario que ingrese un correo electrónico y realiza validaciones.

    Parámetros:
    - contactos (list): Lista de contactos existentes.
    - comprobar_si_existe (bool): Indica si se debe comprobar si el email ya existe en la agenda.

    Retorna:
    - str: Correo electrónico proporcionado por el usuario.
    """
    email = input("Introduzca su email: ").strip()

    validar_email(email, contactos, comprobar_si_existe)

    return email


def validar_telefono(telefono: str) -> bool:
    """
    Comprueba si un número de teléfono es válido.

    Parámetros:
    - telefono (str): Número de teléfono.

    Retorna:
    - bool: True si el teléfono es válido, False en caso contrario.
    """
    if telefono is "":
        return False
    
    if telefono[:3] == '+34':
        telefono = telefono[3:]
    
    return telefono.isdecimal() and len(telefono) == 9


def pedir_telefonos() -> list:
    """
    Pide al usuario que ingrese números de teléfono y los valida.

    Retorna:
    - list: Lista de números de teléfono.
    """
    telefonos = []
    print("Introduzca los teléfonos (<ENTER> sin información para finalizar):")

    indice = 1
    while indice == 1 or telefono != "":
        telefono = input(f"Teléfono {indice} => ").replace(" ", "")

        if not validar_telefono(telefono):
            raise ValueError(f"**Error** el teléfono no es válido, debe tener 9 posiciones numéricas")

        telefonos.append(telefono)

        indice += 1

    return telefonos


def crear_contacto(contactos: list) -> dict:
    """
    Crea un nuevo contacto solicitando información al usuario.

    Parámetros:
    - contactos (list): Lista de contactos existentes.

    Retorna:
    - dict: Diccionario con la información del nuevo contacto.
    """
    contacto = dict()
    contacto['nombre'] = pedir_info("nombre", "Introduzca su nombre: ")
    contacto['apellido'] = pedir_info("apellido", "Introduzca su apellido: ")
    contacto['email'] = pedir_email(contactos)
    contacto['telefonos'] = pedir_telefonos()
    return contacto


def agregar_contacto(contactos: list):
    """
    Agrega un nuevo contacto a la lista.

    Parámetros:
    - contactos (list): Lista de contactos existentes.
    """
    try:
        contactos.append(crear_contacto(contactos))
        print("Se insertó 1 contacto nuevo")
    except ValueError as e:
        print(f"**Error** {e}")
        print("No se insertó ningún contacto")


def buscar_contacto(contactos: list, email: str) -> int:
    """
    Busca un contacto por su email en la lista de contactos.

    Parámetros:
    - contactos (list): Lista de contactos existentes.
    - email (str): Email a buscar.

    Retorna:
    - int: Posición del contacto en la lista. Si no se encuentra, retorna None.
    """
    for i in range(len(contactos)):
        if str(contactos[i]['email']).lower() == email.lower():
            return i

    return None


def eliminar_contacto(contactos: list, email: str):
    """
    Elimina un contacto de la lista por su email.

    Parámetros:
    - contactos (list): Lista de contactos existentes.
    - email (str): Email del contacto a eliminar.
    """
    try:
        pos = buscar_contacto(contactos, email)
        if pos is not None:
            del contactos[pos]
            print("Se eliminó 1 contacto")
        else:
            print("No se encontró el contacto para eliminar")
    except ValueError as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")


def mostrar_telefonos_contacto(telefonos: list):
    """
    Muestra los teléfonos de un contacto.

    Parámetros:
    - telefonos (list): Lista de teléfonos del contacto.
    """
    if len(telefonos) == 0:
        print(f"Teléfonos: ninguno")
    else:
        print(f"Teléfonos: " + " / ".join(telefonos).replace("+34", "+34-"))


def ordenar_contactos(contactos: list):
    """
    Ordena la lista de contactos por nombre.

    Parámetros:
    - contactos (list): Lista de contactos.
    """
    for i in range(len(contactos) - 1):
        for j in range(i + 1, len(contactos)):
            if contactos[i]['nombre'].lower() > contactos[j]['nombre'].lower():
                contacto_temp = contactos[i]
                contactos[i] = contactos[j]
                contactos[j] = contacto_temp


def mostrar_contacto(contacto: dict, titulo: str = ""):
    """
    Muestra un contacto de la agenda.

    Parámetros:
    - contacto (dict): Datos del contacto.
    - titulo (str): Cadena de texto a mostrar como título previo a la información del contacto si no está vacía.
    """
    if titulo is not "":
        print(titulo)
        print('-' * len(titulo))
    
    print(f"Nombre: {contacto['nombre']} {contacto['apellido']} ({contacto['email']})")
    mostrar_telefonos_contacto(contacto['telefonos'])
    print("......")


def mostrar_contactos(contactos: list):
    """
    Muestra la lista de contactos ordenada por nombre.

    Parámetros:
    - contactos (list): Lista de contactos.
    """
    print(f"AGENDA ({len(contactos)})")
    print("------")

    # Para no modificar la agenda original, podemos hacer una copia profunda...
    # contactos_list = copy.deepcopy(contactos)
    # O la volvemos a crear partiendo de los elementos de la anterior...
    contactos_list = list(contactos)
    ordenar_contactos(contactos_list)

    for contacto in contactos_list:
        mostrar_contacto(contacto)


def modificar_contacto(contactos: list):
    """
    Modifica la información de un contacto existente.

    Parámetros:
    - contactos (list): Lista de contactos existentes.
    """
    try:
        email = pedir_email(contactos, False)
        pos = buscar_contacto(contactos, email)

        if pos is not None:
            print()
            mostrar_contacto(contactos[pos], "Datos actuales del contacto")

            print("\nSeleccione el campo a modificar:")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Email")
            print("4. Teléfonos")
            print("5. Todos los campos")

            opcion = int(input("\nSeleccione el número del criterio de búsqueda: "))
            if opcion not in [1, 2, 3, 4, 5]:
                raise ValueError("Opción no válida.")
            
            if opcion == 5:
                # Modificar todos los campos
                contactos[pos]['nombre'] = pedir_info("nombre", "Nuevo nombre: ")
                contactos[pos]['apellido'] = pedir_info("apellido", "Nuevo apellido: ")
                contactos[pos]['email'] = pedir_email(contactos, False)
                contactos[pos]['telefonos'] = pedir_telefonos()
            else:
                # Modificar un campo específico
                campos = ["nombre", "apellido", "email", "telefonos"]
                campo = campos[opcion - 1]
                if campo == "email":
                    # Si se va a modificar el email, validar que no exista en la agenda
                    nuevo_email = pedir_email(contactos, True)
                    contactos[pos][campo] = nuevo_email
                elif campo == "telefonos":
                    contactos[pos][campo] = pedir_telefonos()
                else:
                    contactos[pos][campo] = pedir_info(campo, f"Nuevo {campo}: ")

            print("\nContacto modificado con éxito.")
        else:
            print("No se encontró el contacto para modificar")
    except ValueError as e:
        print(f"*Error* {e}")


def pedir_opcion() -> int:
    """
    Pide al usuario que seleccione una opción del menú.

    Retorna:
    - int: Opción seleccionada por el usuario.
    """
    try:
        opcion = int(input(">> Seleccione una opción (1-8): "))
        if opcion not in OPCIONES_MENU:
            raise ValueError
    except ValueError:
        opcion = -1
        print("*Error* opción no válida")
        pulse_tecla_para_continuar()

    return opcion


def buscar_contactos_por_criterio(contactos: list, criterio: str, valor_busqueda: str) -> list:
    """
    Busca contactos según un criterio específico.

    Parámetros:
    - contactos (list): Lista de contactos existentes.
    - criterio (str): Criterio de búsqueda ("nombre", "apellido", "email", "telefono").
    - valor_busqueda (str): Valor a buscar.

    Retorna:
    - list: Lista de contactos que cumplen con el criterio de búsqueda.
    """
    resultados = []

    for contacto in contactos:
        if criterio == "telefono":
            if valor_busqueda in contacto.get("telefonos", []):
                resultados.append(contacto)
        elif valor_busqueda in contacto.get(criterio, ""):
            resultados.append(contacto)

    return resultados


def mostrar_resultados_busqueda(resultados: list):
    """
    Muestra los resultados de la búsqueda.

    Parámetros:
    - resultados (list): Lista de contactos que cumplen con el criterio de búsqueda.
    """
    if resultados:
        print(f"\nResultados de la búsqueda ({len(resultados)} contactos encontrados):")
        for resultado in resultados:
            print(f"Nombre: {resultado['nombre']} {resultado['apellido']} ({resultado['email']})")
            mostrar_telefonos_contacto(resultado.get('telefonos', []))
            print("......")
    else:
        print("No se encontraron contactos con el criterio de búsqueda proporcionado.")


def mostrar_contactos_por_criterio(contactos: list):
    """
    Busca y muestra la información de los contactos según el criterio elegido por el usuario.
    """
    print("Criterios de búsqueda")
    print('---------------------')
    print("1. Nombre")
    print("2. Apellido")
    print("3. Email")
    print("4. Teléfono")

    try:
        opcion = int(input("\nSeleccione el número del criterio de búsqueda: "))
        if opcion not in [1, 2, 3, 4]:
            raise ValueError
    except ValueError:
        print("Opción no válida.")
        return

    criterios = ["nombre", "apellido", "email", "telefono"]
    criterio = criterios[opcion - 1]

    valor_busqueda = input(f"\nIngrese el {criterio} a buscar: ").strip().title()

    resultados = buscar_contactos_por_criterio(contactos, criterio, valor_busqueda)
    mostrar_resultados_busqueda(resultados)


def mostrar_menu():
    """
    Muestra el menú de la agenda.
    """
    borrar_consola()

    print("AGENDA")
    print("------")
    print("1. Nuevo contacto")
    print("2. Modificar contacto")
    print("3. Eliminar contacto")
    print("4. Vaciar agenda")
    print("5. Cargar agenda inicial")
    print("6. Mostrar contactos por criterio")
    print("7. Mostrar la agenda completa")
    print("8. Salir\n")


def agenda(contactos: list):
    """
    Función principal que gestiona la agenda.

    Parámetros:
    - contactos (list): Lista de contactos existentes.
    """
    opcion = 0
    while opcion != 8:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion in OPCIONES_MENU ^ {8}:
            if opcion == 1:
                borrar_consola()
                agregar_contacto(contactos)
            elif opcion == 2:
                borrar_consola()
                modificar_contacto(contactos)
            elif opcion == 3:
                borrar_consola()
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
            elif opcion == 6:
                borrar_consola()
                mostrar_contactos_por_criterio(contactos)
            elif opcion == 7:
                borrar_consola()
                mostrar_contactos(contactos)

            pulse_tecla_para_continuar()


def pulse_tecla_para_continuar():
    """
    Pausa la ejecución del programa hasta que el usuario presiona una tecla.
    """
    print("\n")
    os.system("pause")


def main():
    """
    Función principal del programa.
    """
    borrar_consola()

    contactos = []

    cargar_contactos(contactos)

    """ DCS: Comentado para realizar pruebas de la función agenda()
    agregar_contacto(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    eliminar_contacto(contactos, "rciruelo@gmail.com")

    pulse_tecla_para_continuar()
    borrar_consola()

    mostrar_contactos(contactos)
    
    pulse_tecla_para_continuar()
    """

    agenda(contactos)


if __name__ == "__main__":
    main()