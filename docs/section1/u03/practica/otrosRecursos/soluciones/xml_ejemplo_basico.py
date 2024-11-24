import xml.etree.ElementTree as ET


def cargar_xml(nombre_fichero: str) -> ET.ElementTree:
    """
    Carga el contenido de un archivo XML.

    Args:
        nombre_fichero (str): Nombre del archivo XML.

    Returns:
        ET.ElementTree: Árbol del XML.
    """
    try:
        return ET.parse(nombre_fichero)
    
    except FileNotFoundError:
        print(f"*ERROR* El archivo {nombre_fichero} no existe.")

    except ET.ParseError:
        print("*ERROR* El archivo XML tiene un formato incorrecto.")

    except Exception as e:
        print(f"*ERROR* Problemas al cargar el XML: {e}")
    
    return None


def guardar_xml(arbol: ET.ElementTree, nombre_fichero: str) -> bool:
    """
    Guarda un árbol XML en un archivo.

    Args:
        arbol (ET.ElementTree): Árbol XML.
        nombre_fichero (str): Nombre del archivo de salida.

    Returns:
        (bool): True si se guardó correctamente y False si se produjo algún problema.
    """
    try:
        arbol.write(nombre_fichero, encoding = "utf-8", xml_declaration = True)

        return True

    except FileNotFoundError:
        print(f"*ERROR* La ruta especificada '{nombre_fichero}' no existe.")

    except PermissionError:
        print(f"*ERROR* No tienes permisos para escribir en el archivo '{nombre_fichero}'.")

    except Exception as e:
        print(f"*ERROR* Problemas al guardar el archivo XML: {e}")

    return False


def actualizar_usuario(raiz: ET.Element, id_usuario: int, nueva_edad: int):
    """
    Actualiza la edad de un usuario dado su ID.

    Args:
        raiz (ET.Element): Nodo raíz del XML.
        id_usuario (int): ID del usuario a actualizar.
        nueva_edad (int): Nueva edad.
    """
    for usuario in raiz.findall("usuario"):
        if usuario.find("id").text == str(id_usuario):
            usuario.find("edad").text = str(nueva_edad)
            print(f"Usuario con ID {id_usuario} actualizado.")
            return
    
    print(f"Usuario con ID {id_usuario} no encontrado.")


def insertar_usuario(raiz: ET.Element, nuevo_usuario: dict):
    """
    Inserta un nuevo usuario en el XML.

    Args:
        raiz (ET.Element): Nodo raíz del XML.
        nuevo_usuario (dict): Datos del nuevo usuario.
    """
    usuario = ET.SubElement(raiz, "usuario")
    ET.SubElement(usuario, "id").text = str(nuevo_usuario["id"])
    ET.SubElement(usuario, "nombre").text = nuevo_usuario["nombre"]
    ET.SubElement(usuario, "edad").text = str(nuevo_usuario["edad"])

    print(f"Usuario {nuevo_usuario['nombre']} añadido con éxito.")


def eliminar_usuario(raiz: ET.Element, id_usuario: int):
    """
    Elimina un usuario por su ID.

    Args:
        raiz (ET.Element): Nodo raíz del XML.
        id_usuario (int): ID del usuario a eliminar.
    """
    for usuario in raiz.findall("usuario"):
        if usuario.find("id").text == str(id_usuario):
            raiz.remove(usuario)
            print(f"Usuario con ID {id_usuario} eliminado.")
            return
    
    print(f"Usuario con ID {id_usuario} no encontrado.")


def main():
    """
    Función principal.
    """
    nombre_fichero = "src/otros/datos_usuarios.xml"

    # 1. Cargar XML
    arbol = cargar_xml(nombre_fichero)

    if arbol is None:
        # Inicializamos datos vacíos si hay error
        raiz = ET.Element("usuarios")
        arbol = ET.ElementTree(raiz)
    
    # Obtenemos el nodo principal y padre de todos
    raiz = arbol.getroot()

    # 2. Actualizar la edad de un usuario
    actualizar_usuario(raiz, id_usuario = 1, nueva_edad = 31)

    # 3. Insertar un nuevo usuario
    nuevo_usuario = {"id": 3, "nombre": "Pedro", "edad": 40}
    insertar_usuario(raiz, nuevo_usuario)

    # 4. Eliminar un usuario
    eliminar_usuario(raiz, id_usuario=2)

    # 5. Guardar los datos de nuevo en el fichero XML
    guardar_xml(arbol, nombre_fichero)

    print("Operaciones completadas. Archivo actualizado.\n")


if __name__ == "__main__":
    main()
