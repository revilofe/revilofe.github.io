import json


def cargar_datos(ruta: str) -> list:
    """
    Carga los datos desde un archivo JSON.

    Args:
        ruta (str): Ruta al archivo JSON.

    Returns:
        list: Lista de diccionarios con los datos cargados.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        json.JSONDecodeError: Si el archivo no tiene un formato JSON válido.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"*ERROR* Archivo no encontrado: {ruta}")
    except json.JSONDecodeError:
        print("*ERROR* El archivo no tiene un formato JSON válido.")
    except Exception as e:
        print(f"*ERROR* Se ha producido un problema inesperado: {e}.")

    return []


def obtener_ciudades_unicas(datos: list) -> set:
    """
    Obtiene el conjunto de ciudades únicas de los datos.

    Args:
        datos (list): Lista de diccionarios con los datos del censo.

    Returns:
        set: Conjunto de ciudades únicas.
    """
    return {persona["ciudad"] for persona in datos}


def contar_profesiones(datos: list) -> dict:
    """
    Cuenta el número de personas por profesión.

    Args:
        datos (list): Lista de diccionarios con los datos del censo.

    Returns:
        dict: Diccionario con las profesiones como claves y las cantidades como valores.
    """
    profesiones = {}
    for persona in datos:
        profesion = persona["profesion"]
        if profesion not in profesiones:
            profesiones[profesion] = 0
        profesiones[profesion] += 1
    return profesiones


def agrupar_personas_por_edad(datos: list) -> dict:
    """
    Agrupa las personas por edad.

    Args:
        datos (list): Lista de diccionarios con los datos del censo.

    Returns:
        dict: Diccionario con las edades como claves y conjuntos de nombres como valores.
    """
    personas_por_edad = {}
    for persona in datos:
        edad = persona["edad"]
        if edad not in personas_por_edad:
            personas_por_edad[edad] = set()
        personas_por_edad[edad].add(persona["nombre"])
    return personas_por_edad


def buscar_personas_por_ciudad(datos: list, ciudad: str) -> set:
    """
    Busca las personas que viven en una ciudad específica.

    Args:
        datos (list): Lista de diccionarios con los datos del censo.
        ciudad (str): Ciudad en la que buscar personas.

    Returns:
        set: Conjunto de nombres de personas que viven en la ciudad.
    """
    return {persona["nombre"] for persona in datos if persona["ciudad"] == ciudad}


def mostrar_ciudades(ciudades: set):
    ciudades = sorted(ciudades)
    total_ciudades = len(ciudades)
    
    if total_ciudades > 1:
        resultado = ', '.join(ciudades[:-1]) + " y " + ciudades[-1] + '.'
    elif total_ciudades == 1:
        resultado = ciudades[0] + "."
    else:
        resultado = "No existen!"
    
    print(f"\n1. Ciudades únicas:\n   {resultado}")


def ordenar_diccionario_por_clave(diccionario: dict) -> dict:
    return {clave: diccionario[clave] for clave in sorted(diccionario)}


def mostrar_profesiones(profesiones: dict):
    profesiones_ordenado = ordenar_diccionario_por_clave(profesiones)

    print("\n2. Número de personas por profesión:\n")
    for profesion, cantidad in profesiones_ordenado.items():
        print(f"   {profesion}: {cantidad}")


def mostrar_personas_por_edad(personas: dict):
    personas_ordenadas = ordenar_diccionario_por_clave(personas)

    print("\n3. Personas agrupadas por edad:\n")
    for edad, nombres in personas_ordenadas.items():
        print(f"   {edad}: {" - ".join(nombres) + "."}")


def mostrar_estadisticas(datos: list):
    """
    Muestra las estadísticas generadas a partir de los datos.

    Args:
        datos (list): Lista de diccionarios con los datos del censo.
    """
    # Mostrar ciudades únicas
    mostrar_ciudades(obtener_ciudades_unicas(datos))

    # Mostrar número de personas por profesión
    mostrar_profesiones(contar_profesiones(datos))

    # Mostrar personas agrupadas por edad
    mostrar_personas_por_edad(agrupar_personas_por_edad(datos))

    # Búsqueda por ciudad
    ciudad = input("\nIntroduce una ciudad para buscar personas: ").strip().title()
    personas_en_ciudad = buscar_personas_por_ciudad(datos, ciudad)
    if personas_en_ciudad:
        print(f"\n4. Personas en {ciudad}:\n   {"\n   ".join(sorted(personas_en_ciudad))}\n")
    else:
        print(f"\n4. No se encontraron personas en {ciudad}.\n")


def main():
    """
    Función principal del programa.
    """
    archivo = "examenes/censo_info.json"
    datos = cargar_datos(archivo)

    if datos:
        mostrar_estadisticas(datos)
    else:
        print("\nNo se pudieron cargar los datos. Verifica el archivo JSON.")


if __name__ == "__main__":
    main()
