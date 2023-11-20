"""
Ejercicio 3.2.6
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

def pedir_datos(informacion_persona: dict) -> bool:
    """ Solicitar el nombre de la clave (atributo)
    """
    clave = input("Ingrese un atributo (o escriba 'fin' para finalizar): ").lower()

    # Verificar si el usuario desea finalizar la entrada de datos...
    if clave == 'fin':
        return True

    valor = input(f"Ingrese el valor para '{clave}': ")
    informacion_persona[clave] = valor

    return False


def mostrar_info(msj: str, informacion_persona: dict):
    """ Mostrar el contenido actualizado del diccionario
    """
    print(msj)
    for atributo, valor in informacion_persona.items():
        print(f"{atributo}: {valor}")
    print()


def main():
    
    informacion_persona = {}
    fin = False

    while not fin:
        fin = pedir_datos(informacion_persona)
        mostrar_info("\nContenido actualizado del diccionario:", informacion_persona)

    mostrar_info("Diccionario final:", informacion_persona)


if __name__ == '__main__':
    main()