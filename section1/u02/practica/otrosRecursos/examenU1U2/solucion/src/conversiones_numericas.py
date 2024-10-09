import os

SIMBOLOS = "0123456789ABCDEF"
BASE_BINARIA = 2
BASE_OCTAL = 8
BASE_DECIMAL = 10
BASE_HEXADECIMAL = 16
MENSAJE_ERROR_BASE_GENERAL = "**ERROR** no ha introducido una base correcta!\n"
MENSAJE_ERROR_BASE_IGUAL = "**ERROR** La base de destino no puede ser igual a la base de origen ({base})."
MENSAJE_ERROR_NUMERO = "**ERROR** el número '{numero}' no es válido para la base {base}!\n"


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.
    
    En sistemas Windows utiliza el comando 'cls', en Linux o macOS utiliza 'clear'.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def realiza_pausa():
    """
    Pausa la ejecución del programa hasta que el usuario presione ENTER.
    
    Esta función muestra un mensaje que solicita al usuario presionar ENTER para continuar. 
    Es útil para dar tiempo al usuario a leer la salida antes de que el programa continúe 
    ejecutándose o finalice.
    """
    input("\nPresione ENTER para continuar...")


def es_valido_en_base(valor: str, base: int) -> bool:
    """
    Comprueba si una cadena de caracteres es válida en la base dada.
    
    Args:
        valor (str): El número en formato de cadena de caracteres.
        base (int): La base numérica (2, 8, 10, 16).
    
    Returns:
        bool: True si el valor es válido en la base dada, False en caso contrario.
    """
    if valor.startswith("-"):
        valor = valor[1:]

    if valor == "":
        return False

    for digito in valor:
        valor_numerico = valor_simbolo(digito)
        if valor_numerico == -1 or valor_numerico >= base:
            return False
        
    return True


def comprobar_valor_base(valor: str, base: int) -> bool:
    """
    Comprueba si una cadena de caracteres es válida en una base dada.
    
    Args:
        valor (str): El número a comprobar.
        base (int): La base numérica (2, 8, 10, 16).
    
    Returns:
        bool: True si es válido, False en caso contrario.
    """
    return es_valido_en_base(valor, base)


def dame_simbolo(valor: int) -> str:
    """
    Retorna el símbolo correspondiente a un valor en base hexadecimal.

    Args:
        valor (int): El valor entero entre 0 y 15.

    Returns:
        str: El símbolo correspondiente al valor.

    Raises:
        ValueError: Si el valor está fuera del rango permitido.
    """
    if valor not in range(len(SIMBOLOS)):
        raise ValueError(f"Valor {valor} fuera del rango hexadecimal permitido.")
    
    return SIMBOLOS[valor]


def valor_simbolo(posicion: str) -> int:
    """
    Retorna el valor numérico correspondiente a un símbolo.

    Args:
        posicion (str): El símbolo a convertir.

    Returns:
        int: El valor numérico correspondiente al símbolo, o -1 si no es válido.
    """
    try:
        resultado = SIMBOLOS.index(posicion)
    except ValueError:
        resultado = -1
    
    return resultado


def convertir_decimal_a_otra_base(valor: str, base: int) -> str:
    """
    Convierte un número decimal a una base dada.
    
    Args:
        valor (str): El número decimal en formato de cadena de caracteres.
        base (int): La base a la que se quiere convertir (2, 8, 16).
    
    Returns:
        str: El número convertido a la base dada en formato de cadena,
             o None en caso de error.
    """
    resultado = ""
    cociente = int(valor)

    try:
        while cociente >= base:
            resto = cociente % base
            cociente = cociente // base
            resultado += dame_simbolo(resto)

        resultado += str(dame_simbolo(cociente))
    except ValueError as e:
        print(f"**ERROR** en la conversión: {e}")
        return None

    return resultado[::-1]


def convertir_a_base_decimal(valor: str, base: int) -> int:
    """
    Convierte un número en una base dada a base decimal.
    
    Args:
        valor (str): El número en formato de cadena de caracteres.
        base (int): La base de origen del número (2, 8, 16).
    
    Returns:
        int: El número convertido a decimal, o None en caso de error (como un símbolo no válido).
    """
    resultado = 0
    exponente = 0
    i = len(valor) - 1

    try:
        while i >= 0:
            valor_numerico = valor_simbolo(valor[i])
            if valor_numerico == -1:
                raise ValueError(f"El símbolo '{valor[i]}' no es válido en la base {base}.")
            
            resultado += valor_numerico * base ** exponente
            exponente += 1
            i -= 1

        return resultado
    except ValueError as e:
        print(f"**ERROR** en la conversión a decimal: {e}")
        return None


def convertir_numero_a_otra_base(valor: str, base1: int, base2: int) -> str:
    """
    Convierte un número de una base a otra.
    
    Args:
        valor (str): El número en formato de cadena de caracteres.
        base1 (int): La base de origen del número.
        base2 (int): La base a la que se desea convertir.
    
    Returns:
        str: El número convertido a la base destino, o None en caso de error.
    
    Nota:
        Si la conversión falla (por ejemplo, si el valor no es válido en la base de origen),
        la función devuelve None.
    """
    if valor.startswith("-"):
        simbolo_primera_posicion = "-"
        valor = valor[1:]
    else:
        simbolo_primera_posicion = ""

    # Convertir a base decimal
    if base1 != BASE_DECIMAL:
        valor = convertir_a_base_decimal(valor, base1)
        if valor is None:  # Si hay un error, detener
            return None

    # Convertir a la base de destino
    if base2 != BASE_DECIMAL:
        valor = convertir_decimal_a_otra_base(str(valor), base2)
        if valor is None:  # Si hay un error, detener
            return None

    return simbolo_primera_posicion + valor


def validar_base(base: str) -> bool:
    """
    Verifica si la base introducida es válida.

    Args:
        base (str): Cadena de caracteres que representa la base introducida por el usuario.

    Returns:
        bool: True si la base es válida (2, 8, 10 o 16), False en caso contrario.
    """
    return base in ('2', '8', '10', '16')


def dame_nombre_base(base: int) -> str:
    """
    Retorna el nombre de la base numérica.

    Args:
        base (int): El valor numérico de la base (2, 8, 10, 16).

    Returns:
        str: El nombre descriptivo de la base (por ejemplo, 'binaria').
    """
    if base == BASE_BINARIA:
        return "binaria"
    elif base == BASE_OCTAL:
        return "octal"
    elif base == BASE_DECIMAL:
        return "decimal"
    elif base == BASE_HEXADECIMAL:
        return "hexadecimal"
    else:
        return "desconocida"


def introduce_base(msj: str, permitir_entrada_vacia: bool = False, base_origen: int = None) -> int:
    """
    Solicita al usuario una base numérica válida (2, 8, 10 o 16).

    Args:
        msj (str): El mensaje a mostrar al usuario.
        permitir_entrada_vacia (bool): Si se permite una entrada vacía. (default: False)

    Returns:
        int: La base numérica seleccionada o None si la entrada está vacía.
    """
    base_valida = False
    base = None
    
    while not base_valida:
        base = input(msj).strip()
        
        if permitir_entrada_vacia and base == "":
            return None
        
        base_valida = validar_base(base)
        
        if base_valida and base_origen is not None and int(base) == base_origen:
            print(MENSAJE_ERROR_BASE_IGUAL.format(base = dame_nombre_base(base_origen)))
            base_valida = False 

        if not base_valida:
            print(MENSAJE_ERROR_BASE_GENERAL)

    return int(base)


def introduce_numero(msj: str, base: int) -> str:
    """
    Solicita al usuario un número válido para la base dada.

    Args:
        msj (str): El mensaje a mostrar al usuario.
        base (int): La base numérica en la que debe estar el número.

    Returns:
        str: El número introducido por el usuario.
    """
    numero_valido = False
    valor = None
    
    while not numero_valido:
        valor = input(msj).strip()
        numero_valido = comprobar_valor_base(valor, base)
        
        if not numero_valido:
            print(MENSAJE_ERROR_NUMERO.format(numero = valor, base = dame_nombre_base(base)))

    return valor


def desea_salir() -> bool:
    """
    Pregunta al usuario si desea salir del programa.

    Returns:
        bool: True si el usuario desea salir, False en caso contrario.
    """
    salir = input("\n¿Desea salir del programa? (S/N) ").upper()
    return salir in {'S', 'SI', 'Y', 'YES'}


def realizar_conversion() -> bool:
    """
    Gestiona el proceso de conversión de un número de una base a otra.

    El usuario introduce la base del número a convertir, el número en esa base, 
    y la base de destino. Si la conversión se realiza con éxito, el resultado 
    se muestra. En caso de error (como un número no válido), se indica que la 
    conversión falló. También se realiza una pausa al final para que el usuario 
    pueda ver el resultado antes de que el programa continúe o termine.

    Returns:
        bool: True si la conversión se realizó con éxito, False si hubo algún error.
               Devuelve None si el usuario decide salir del programa al introducir
               una cadena vacía para la base de origen.
    """
    limpiar_pantalla()
    
    base1 = introduce_base("\nIndica la base del número que vas a introducir (2, 8, 10 o 16): ", True)
    if base1 is None:
        return None # Indica que el usuario desea salir de la aplicación

    valor = introduce_numero("\nIntroduce el valor del número a convertir: ", base1)

    base2 = introduce_base("\nIndica la base de numeración a la que quieres convertir el número (2, 8, 10 o 16): ", base_origen = base1)
    
    resultado = convertir_numero_a_otra_base(valor, base1, base2)

    # Comprobamos si la conversión se pudo realizar o por el contrario ocurrió algún error
    estado_conversion = resultado is not None
    
    if estado_conversion:
        print(f"\nEl número \"{valor}\" en base {dame_nombre_base(base1)} es el \"{resultado}\" en base {dame_nombre_base(base2)}.")

    realiza_pausa()

    return estado_conversion


def main():
    """
    Función principal que coordina la interacción con el usuario y la conversión de bases numéricas.
    """
    contador_conversiones = 0
    salir = False

    while not salir:
        exito = realizar_conversion()
        
        if exito:
            contador_conversiones += 1
        elif exito is None:
            salir = desea_salir()
    
    if contador_conversiones > 0:
        print(f"\nHas realizado {contador_conversiones} {'conversión' if contador_conversiones == 1 else 'conversiones'}.\n")
    else:
        print("\nNo has realizado ninguna conversión.\n")



if __name__ == "__main__":
    main()
