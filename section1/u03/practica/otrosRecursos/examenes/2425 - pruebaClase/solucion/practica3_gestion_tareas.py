
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


def obtener_tareas(tareas: list) -> str:
    """
    Genera una cadena que contiene todas las tareas formateadas.

    Args:
        tareas (list): Lista de tareas.

    Returns:
        str: Cadena formateada con todas las tareas.
    """
    return "\n".join(
        f"ID: {tarea['ID']}, Descripción: {tarea['Descripción']}, Estado: {tarea['Estado']}"
        for tarea in tareas
    )


def mostrar_tarea(tarea: dict):
    """
    Muestra una tarea en formato legible.
    
    Args:
        tarea (dict): Diccionario con la información de la tarea.
    """
    print(f"ID: {tarea['ID']}, Descripción: {tarea['Descripción']}, Estado: {tarea['Estado']}")


def filtrar_tareas_por_estado(tareas: list, estado: str) -> tuple:
    """
    Filtra las tareas por el estado especificado.

    Args:
        tareas (list): Lista de tareas.
        estado (str): Estado por el cual filtrar las tareas.

    Returns:
        tuple: Tareas que coinciden con el estado indicado.
    """
    return (tarea for tarea in tareas if tarea["Estado"] == estado)



def main():
    """
    Función principal que administra el programa.
    """
    tareas_todas = crear_tareas_ejemplo()
    tareas = list(tareas_todas)
    
    iterador_tareas = iter(tareas)
    estado = ""
    salir = False

    while not salir:
        mostrar_menu(estado)
        opcion = elegir_opcion()

        if opcion == "1":
            estado = pedir_estado()
            
            if estado:
                tareas = filtrar_tareas_por_estado(tareas_todas, estado)
            else:
                tareas = list(tareas_todas)

            iterador_tareas = iter(tareas)

        elif opcion == "2":
            print("\nTodas las tareas:")
            print(obtener_tareas(tareas))
            pausar()

        elif opcion == "3":
            try:
                tarea = next(iterador_tareas)
                print("\nSiguiente tarea:")
                mostrar_tarea(tarea)
            except StopIteration:
                print("\nNo hay más tareas! Se ha reiniciado el iterador...")
                iterador_tareas = iter(tareas)
            
            pausar()

        elif opcion == "4":
            salir = True      


if __name__ == "__main__":
    main()
