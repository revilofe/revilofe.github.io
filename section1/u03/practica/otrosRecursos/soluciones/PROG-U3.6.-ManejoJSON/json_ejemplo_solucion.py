import json
import os


def limpiar_consola():
    os.system("clear" if os.name == "posix" else "cls")


def pausar():
    input("Presione ENTER para continuar...") if os.name == "posix" else os.system("pause")
    print()
    

def cargar_json(nombre_fichero: str) -> dict:
    """
    Carga el contenido de un fichero JSON.

    Args:
        nombre_fichero (str): Nombre del fichero JSON.

    Returns:
        (dict): Contenido del archivo JSON como un diccionario, o None si no se pudo cargar.
    """
    try:
        with open(nombre_fichero, "r") as archivo:
            return json.load(archivo)
        
    except FileNotFoundError:
        print(f"*ERROR* El archivo {nombre_fichero} no existe.")
    
    except json.JSONDecodeError:
        print("*ERROR* El archivo JSON tiene un formato incorrecto.")

    except Exception as e:
        print(f"*ERROR* Problemas al cargar los datos {e}.")

    return None


def guardar_json(nombre_fichero: str, datos: dict):
    """
    Guarda los datos en un fichero JSON.

    Args:
        nombre_fichero (str): Nombre del fichero JSON.
        datos (dict): Datos a guardar.
    """
    try:
        with open(nombre_fichero, "w") as archivo:
            json.dump(datos, archivo, indent = 4)

    except PermissionError:
        print(f"*ERROR* No tienes permisos para escribir en el archivo '{nombre_fichero}'.")

    except TypeError as e:
        print(f"*ERROR* Los datos no son serializables a JSON. Detalle: {e}")        

    except Exception as e:
        print(f"*ERROR* Problemas al guardar los datos: {e}")


def actualizar_usuario(datos: dict, id_usuario: int, nueva_edad: int):
    """
    Actualiza la edad de un usuario dado su ID.

    Args:
        datos (dict): Diccionario con los datos actuales.
        id_usuario (int): ID del usuario a actualizar.
        nueva_edad (int): Nueva edad del usuario.
    """
    for usuario in datos["usuarios"]:
        if usuario["id"] == id_usuario:
            usuario["edad"] = nueva_edad
            print(f"Usuario con ID {id_usuario} actualizado.")
            return
    
    print(f"Usuario con ID {id_usuario} no encontrado.")


def insertar_usuario(datos: dict, nuevo_usuario: dict):
    """
    Inserta un nuevo usuario.

    Args:
        datos (dict): Diccionario con los datos actuales.
        nuevo_usuario (dict): Diccionario con los datos del nuevo usuario.
    """
    datos["usuarios"].append(nuevo_usuario)
    print(f"Usuario {nuevo_usuario['nombre']} añadido con éxito.")


def eliminar_usuario(datos: dict, id_usuario: int):
    """
    Elimina un usuario dado su ID.

    Args:
        datos (dict): Diccionario con los datos actuales.
        id_usuario (int): ID del usuario a eliminar.
    """
    for usuario in datos["usuarios"]:
        if usuario["id"] == id_usuario:
            datos["usuarios"].remove(usuario)
            print(f"Usuario con ID {id_usuario} eliminado.")
            return
    
    print(f"Usuario con ID {id_usuario} no encontrado.")



def inicializar_datos(archivo_origen: str, archivo_destino: str):
    """
    Copia el contenido de un archivo origen a un archivo destino.

    Args:
        archivo_origen (str): Nombre del archivo original que será copiado.
        archivo_destino (str): Nombre del archivo destino donde se copiarán los datos.
    """
    try:
        # Comprobar si el archivo origen existe
        with open(archivo_origen, "r") as archivo:
            # Leer los datos del archivo origen
            datos_origen = json.load(archivo)
        
        # Guardar los datos en el archivo destino
        with open(archivo_destino, "w") as archivo:
            json.dump(datos_origen, archivo, indent = 4)
        
        print(f"Datos inicializados desde '{archivo_origen}' a '{archivo_destino}'.")
    
    except FileNotFoundError:
        print(f"*ERROR* El archivo origen '{archivo_origen}' no existe. No se realizó la copia.")

    except json.JSONDecodeError:
        print(f"*ERROR* El archivo origen '{archivo_origen}' tiene un formato JSON inválido.")

    except Exception as e:
        print(f"*ERROR* Problemas al inicializar los datos: {e}")


def mostrar_datos(datos: dict):
    """
    Muestra los datos contenidos en el diccionario de forma organizada.

    Args:
        datos (dict): Diccionario con los datos actuales.
    """
    print("\n--- Contenido Actual del JSON ---")
    if "usuarios" in datos and datos["usuarios"]:
        for usuario in datos["usuarios"]:
            print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")
    else:
        print("*ERROR* El archivo JSON no contiene usuarios!")

    print("--- Fin del Contenido ---\n")

    pausar()


def main():
    """
    Función principal que realiza las operaciones de gestión de un archivo JSON.
    """
    # Nombre del fichero JSON
    nombre_fichero_orig = "datos_usuarios_orig.json"
    nombre_fichero = "datos_usuarios.json"

    limpiar_consola()

    # Inicializar datos desde archivo origen a destino
    inicializar_datos(nombre_fichero_orig, nombre_fichero)

    # 1. Cargar datos desde el fichero JSON
    datos = cargar_json(nombre_fichero)
    
    if datos is None:
        # Inicializamos datos vacíos si hay error
        datos = {"usuarios": []}

    # Mostrar los datos iniciales
    mostrar_datos(datos)

    # 2. Actualizar la edad de un usuario
    actualizar_usuario(datos, id_usuario = 1, nueva_edad = 31)

    # Mostrar datos después de actualizar
    mostrar_datos(datos)    

    # 3. Insertar un nuevo usuario
    nuevo_usuario = {"id": 3, "nombre": "Pedro", "edad": 40}
    insertar_usuario(datos, nuevo_usuario)

    # Mostrar datos después de insertar
    mostrar_datos(datos)

    # 4. Eliminar un usuario
    eliminar_usuario(datos, id_usuario = 2)

    # Mostrar datos después de eliminar
    mostrar_datos(datos)

    # 5. Guardar los datos de nuevo en el fichero JSON
    guardar_json(nombre_fichero, datos)

    print("Operaciones completadas. Archivo actualizado.\n")


if __name__ == "__main__":
    main()
