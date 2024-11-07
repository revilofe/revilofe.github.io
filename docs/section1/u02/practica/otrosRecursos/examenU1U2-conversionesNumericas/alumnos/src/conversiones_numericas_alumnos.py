import os

SIMBOLOS = "0123456789ABCDEF"
BASE_BINARIA = 2
BASE_OCTAL = 8
BASE_DECIMAL = 10
BASE_HEXADECIMAL = 16
MENSAJE_ERROR_BASE = "**ERROR** no ha introducido una base correcta!\n"
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


def comprobar_entero(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres representa un número entero.

    Args:
        valor (str): La cadena de caracteres a comprobar.

    Returns:
        bool: True si es un número entero válido, False en caso contrario.
    """
    if valor.startswith("-"):
        return False

    return valor.isdigit() or (valor.startswith("-") and valor[1:].isdigit())


def es_hexadecimal(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres es un número en base hexadecimal.

    Args:
        valor (str): La cadena de caracteres a comprobar.

    Returns:
        bool: True si es hexadecimal, False en caso contrario.
    """
    if valor.startswith("-"):
        return False

    for i in range(len(valor)):
        if valor_simbolo(valor[i]) == -1:
            return False
    return True


def es_decimal(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres es un número en base decimal.

    Args:
        valor (str): La cadena de caracteres a comprobar.

    Returns:
        bool: True si es decimal, False en caso contrario.
    """
    return comprobar_entero(valor)


def es_octal(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres es un número en base octal.

    Args:
        valor (str): La cadena de caracteres a comprobar.

    Returns:
        bool: True si es octal, False en caso contrario.
    """
    if valor.startswith("-"):
        return False

    for i in range(len(valor)):
        valor_numerico = valor_simbolo(valor[i])
        if valor_numerico > 7 or valor_numerico == -1:
            return False
    return True


def es_binario(valor: str) -> bool:
    """
    Comprueba si una cadena de caracteres es un número en base binaria.

    Args:
        valor (str): La cadena de caracteres a comprobar.

    Returns:
        bool: True si es binario, False en caso contrario.
    """
    if valor.startswith("-"):
        return False

    for i in range(len(valor)):
        valor_numerico = valor_simbolo(valor[i])
        if valor_numerico > 1 or valor_numerico == -1:
            return False
    return True


def comprobar_valor_base(valor: str, base) -> bool:
    """
    Comprueba si una cadena de caracteres es válida en una base dada.

    Args:
        valor (str): La cadena de caracteres a comprobar.
        base (int): La base numérica (2, 8, 10, 16).

    Returns:
        bool: True si el valor es válido en la base dada, False en caso contrario.
    """
    if valor == "" or valor == "-":
        return False
    elif base == BASE_BINARIA:
        return es_binario(valor)
    elif base == BASE_OCTAL:
        return es_octal(valor)
    elif base == BASE_DECIMAL:
        return es_decimal(valor)
    elif base == BASE_HEXADECIMAL:
        return es_hexadecimal(valor)
    else:
        return False


def dame_simbolo(valor: int) -> str:
    pass


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


def introduce_base(msj: str) -> int:
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
        
        base_valida = validar_base(base)
        
        if not base_valida:
            print(MENSAJE_ERROR_BASE)

    return int(base)


def introduce_numero(msj: str, base: int) -> str:
    numero_valido = False
    valor = None
    
    while not numero_valido:
        valor = input(msj).strip()
        numero_valido = comprobar_valor_base(valor, base)
        
        if not numero_valido:
            print(MENSAJE_ERROR_NUMERO.format(numero = valor, base = dame_nombre_base(base)))

    return valor


def realizar_conversion():
    """
    Gestiona el flujo de conversión de un número introducido por el usuario.
    """   
    base1 = introduce_base("\nIndica la base del número que vas a introducir (2, 8, 10 o 16): ")

    valor = introduce_numero("\nIntroduce el valor del número a convertir: ", base1)

    base2 = introduce_base("\nIndica la base de numeración a la que quieres convertir el número (2, 8, 10 o 16): ")
    
    resultado = convertir_numero_a_otra_base(valor, base1, base2)

    # Comprobamos si la conversión se pudo realizar o por el contrario ocurrió algún error
    estado_conversion = resultado is not None
    
    if estado_conversion:
        print(f"\nEl número \"{valor}\" en base {dame_nombre_base(base1)} es el \"{resultado}\" en base {dame_nombre_base(base2)}.")


def main():
    """
    Función principal que coordina la interacción con el usuario y la conversión de bases numéricas.
    """
    realizar_conversion()



if __name__ == "__main__":
    main()
