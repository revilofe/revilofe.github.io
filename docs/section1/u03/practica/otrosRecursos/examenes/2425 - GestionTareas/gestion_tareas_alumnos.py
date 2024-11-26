
import os


OPCIONES = {"1", "2", "3", "4"}
ESTADOS = {"Pendiente", "En Proceso", "Completada"}


def limpiar_pantalla():
    """
    Limpia la consola dependiendo del sistema operativo.
    """    
    os.system("clear" if os.name == "posix" else "cls")


def pausar():
    """
    Pausa la ejecución del programa.
    """    
    if os.name == "posix":
        input("\nPresione ENTER para continuar...")
    else:
        print()
        os.system("pause")


def crear_tareas_ejemplo() -> list:
    """
    Genera una lista de tareas predefinidas para el ejercicio.

    Returns:
        list: Lista de diccionarios con información de tareas.    
    """
    return [
        {"ID": 1, "Descripción": "Estudiar Python", "Estado": "Pendiente"},
        {"ID": 2, "Descripción": "Terminar proyecto", "Estado": "En Proceso"},
        {"ID": 3, "Descripción": "Revisar correos", "Estado": "Completada"},
        {"ID": 4, "Descripción": "Planificar reunión", "Estado": "Pendiente"},
        {"ID": 5, "Descripción": "Comprar libros", "Estado": "Pendiente"},
        {"ID": 6, "Descripción": "Actualizar currículum", "Estado": "En Proceso"},
        {"ID": 7, "Descripción": "Organizar escritorio", "Estado": "Completada"},
        {"ID": 8, "Descripción": "Preparar presentación", "Estado": "Pendiente"},
    ]


def obtener_tareas(tareas: list) -> str:
    """
    Genera una cadena que contiene todas las tareas formateadas.

    Args:
        tareas (list): Lista de tareas.

    Returns:
        str: Cadena formateada con todas las tareas.
    """
    # TODO: Utiliza join.
    # Ejemplo de cadena de caracteres que debe retornar:
    """
    ID: 1, Descripción: Estudiar Python, Estado: Pendiente
    ID: 2, Descripción: Terminar proyecto, Estado: En Proceso
    ID: 3, Descripción: Revisar correos, Estado: Completada
    ID: 4, Descripción: Planificar reunión, Estado: Pendiente
    ID: 5, Descripción: Comprar libros, Estado: Pendiente
    ID: 6, Descripción: Actualizar currículum, Estado: En Proceso
    ID: 7, Descripción: Organizar escritorio, Estado: Completada
    ID: 8, Descripción: Preparar presentación, Estado: Pendiente    
    """



def mostrar_tarea(tarea: dict):
    """
    Muestra una tarea en formato legible.
    
    Args:
        tarea (dict): Diccionario con la información de la tarea.
    """
    # TODO: Debe mostrar por consola la tarea como en el siguiente ejemplo:
    # ID: 1, Descripción: Estudiar Python, Estado: Pendiente



def filtrar_tareas_por_estado(tareas: list, estado: str) -> tuple:
    """
    Filtra las tareas por el estado especificado.

    Args:
        tareas (list): Lista de tareas.
        estado (str): Estado por el cual filtrar las tareas.

    Returns:
        tuple: Tareas que coinciden con el estado indicado.
    """
    # TODO: No podéis usar el método filter() para filtrar en la lista



def mostrar_menu(estado = ""):
    """
    Muestra el menú de opciones. Indica el filtro actual si está activo.

    Args:
        estado (str): Estado actual del filtro.
    """
    limpiar_pantalla()
    print("\nMenú:\n----")
    print("1. Filtrar tareas " + (f"({estado})" if estado else ""))
    print("2. Mostrar todas las tareas")
    print("3. Mostrar siguiente tarea")
    print("4. Salir")



def elegir_opcion():
    """
    Solicita al usuario que elija una opción del menú.

    Returns:
        str: Opción seleccionada por el usuario.
    """
    opcion = None
    
    while opcion not in OPCIONES:
    
        if opcion is not None:
            print("*ERROR* Opción no válida, inténtalo de nuevo.")
        
        opcion = input("Elige una opción: ").strip()

    return opcion


def pedir_estado() -> str:
    """
    Solicita al usuario un estado para filtrar las tareas.

    Returns:
        str: Estado seleccionado o cadena vacía si no se aplica un filtro.
    """
    estado = None
    while not (estado == "" or estado in ESTADOS):

        if estado is not None:
            print("*ERROR* Estado no válido, inténtalo de nuevo.")

        estado = input("Introduce un estado para filtrar (ENTER para eliminar el filtro): ").strip().title()

    return estado


def main():
    """
    Función principal que administra el programa.
    """
    tareas_todas = crear_tareas_ejemplo()
    
    # Por defecto, cargamos todas las tareas y creamos el iterador...
    tareas = list(tareas_todas)
    iterador_tareas = iter(tareas)

    # Asignamos el estado vacío para indicar que no existe ningún filtro activo...
    estado = ""
    salir = False

    while not salir:
        mostrar_menu(estado)
        opcion = elegir_opcion()

        if opcion == "1":
            estado = pedir_estado()
            # TODO: Asignar tareas... debéis filtrar las tareas si existe un estado y sino volver a cargar todas las tareas.
            # TODO: Después de asignar correctamente tareas, debéis crear el iterador con la nueva lista.


        elif opcion == "2":
            print("\nTodas las tareas:")
            # TODO: Mostrar TODAS las tareas (usad la lista tareas_todas)


        elif opcion == "3":
            # TODO: Debe mostrar la siguiente tarea en las tareas filtradas con el iterador
            # si no hay más tareas, debe reiniciar el iterador para que muestre de nuevo la
            # primera tarea la próxima vez que seleccionen esta opción del menú.
            """
            Si existe una tarea debe mostrar lo siguiente:

                Siguiente tarea:
                ID: 1, Descripción: Estudiar Python, Estado: Pendiente

                Presione una tecla para continuar . . . 

            Si no existen más tareas debe reiniciar el iterador y mostrar los siguiente:

                No hay más tareas! Se ha reiniciado el iterador...

                Presione una tecla para continuar . . . 
            """



        elif opcion == "4":
            salir = True      


if __name__ == "__main__":
    main()
