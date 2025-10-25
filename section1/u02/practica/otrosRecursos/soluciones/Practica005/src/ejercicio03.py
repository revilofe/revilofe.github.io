"""
Ejercicio 3: Contador de Dígitos Pares e Impares

Descripción:
    Programa que cuenta cuántos dígitos pares e impares tiene un número entero,
    trabajando exclusivamente con operaciones matemáticas (sin conversión a string).
    
Autor: Eduardo Fdez
Fecha: 2025-10-25
"""


def contar_digitos_pares_impares(numero: int) -> tuple[int, int]:
    """
    Cuenta la cantidad de dígitos pares e impares en un número.
    
    Esta función es la que se evaluará mediante tests automáticos.
    
    Args:
        numero: Un número entero (puede ser positivo o negativo)
        
    Returns:
        tuple[int, int]: (cantidad_pares, cantidad_impares)
        
    Nota:
        - El 0 se considera par
        - Si el número es negativo, se trabaja con su valor absoluto
        - Si el número es 0, devolver (1, 0)
    """
    # Caso especial: si el número es 0
    if numero == 0:
        return (1, 0)
    
    # Trabajar con el valor absoluto para manejar números negativos
    numero_absoluto: int = numero
    if numero < 0:
        numero_absoluto = -numero
    
    # Contadores para dígitos pares e impares
    cantidad_pares: int = 0
    cantidad_impares: int = 0
    
    # Extraer dígitos usando operaciones matemáticas
    # Mientras queden dígitos por procesar
    while numero_absoluto > 0:
        # Obtener el último dígito usando módulo 10
        digito: int = numero_absoluto % 10
        
        # Verificar si el dígito es par o impar
        if digito % 2 == 0:
            cantidad_pares = cantidad_pares + 1
        else:
            cantidad_impares = cantidad_impares + 1
        
        # Eliminar el último dígito dividiendo entre 10 (división entera)
        numero_absoluto = numero_absoluto // 10
    
    return (cantidad_pares, cantidad_impares)


def extraer_digitos_pares(numero: int) -> str:
    """
    Extrae y devuelve una cadena con los dígitos pares del número.
    
    Args:
        numero: El número a analizar
        
    Returns:
        str: Cadena con los dígitos pares separados por comas
    """
    if numero == 0:
        return "0"
    
    # Trabajar con valor absoluto
    numero_absoluto: int = numero if numero >= 0 else -numero
    
    digitos_pares: str = ""
    
    # Extraer dígitos de derecha a izquierda
    while numero_absoluto > 0:
        digito: int = numero_absoluto % 10
        
        if digito % 2 == 0:
            # Añadir el dígito (convertido a string)
            if digitos_pares == "":
                digitos_pares = str(digito)
            else:
                # Añadir al principio para mantener el orden original
                digitos_pares = str(digito) + ", " + digitos_pares
        
        numero_absoluto = numero_absoluto // 10
    
    return digitos_pares


def extraer_digitos_impares(numero: int) -> str:
    """
    Extrae y devuelve una cadena con los dígitos impares del número.
    
    Args:
        numero: El número a analizar
        
    Returns:
        str: Cadena con los dígitos impares separados por comas
    """
    if numero == 0:
        return ""
    
    # Trabajar con valor absoluto
    numero_absoluto: int = numero if numero >= 0 else -numero
    
    digitos_impares: str = ""
    
    # Extraer dígitos de derecha a izquierda
    while numero_absoluto > 0:
        digito: int = numero_absoluto % 10
        
        if digito % 2 != 0:
            # Añadir el dígito (convertido a string)
            if digitos_impares == "":
                digitos_impares = str(digito)
            else:
                # Añadir al principio para mantener el orden original
                digitos_impares = str(digito) + ", " + digitos_impares
        
        numero_absoluto = numero_absoluto // 10
    
    return digitos_impares


def solicitar_numero() -> int:
    """
    Solicita al usuario un número entero.
    
    Returns:
        int: El número introducido por el usuario
    """
    numero: int = 0
    valido: bool = False
    
    # Bucle hasta obtener un número válido
    while not valido:
        entrada: str = input("Introduce un número entero: ")
        
        try:
            numero = int(entrada)
            valido = True
        except ValueError:
            print("Error: Debe introducir un número entero válido.")
    
    return numero


def mostrar_resultado(numero: int, pares: int, impares: int, 
                      digitos_pares: str, digitos_impares: str) -> None:
    """
    Muestra el resultado del análisis de forma formateada.
    
    Args:
        numero: El número analizado
        pares: Cantidad de dígitos pares
        impares: Cantidad de dígitos impares
        digitos_pares: String con los dígitos pares
        digitos_impares: String con los dígitos impares
    """
    print(f"\nNúmero analizado: {numero}")
    
    # Mostrar dígitos pares
    if pares > 0:
        print(f"Dígitos pares: {pares} ({digitos_pares})")
    else:
        print("Dígitos pares: 0")
    
    # Mostrar dígitos impares
    if impares > 0:
        print(f"Dígitos impares: {impares} ({digitos_impares})")
    else:
        print("Dígitos impares: 0")


def main() -> None:
    """
    Función principal que coordina la ejecución del programa.
    
    Flujo:
        1. Solicita un número al usuario
        2. Cuenta los dígitos pares e impares usando la función obligatoria
        3. Extrae los dígitos para mostrarlos
        4. Muestra el resultado formateado
    """
    # Paso 1: Obtener número del usuario
    numero: int = solicitar_numero()
    
    # Paso 2: Contar dígitos usando la función obligatoria
    cantidad_pares: int
    cantidad_impares: int
    cantidad_pares, cantidad_impares = contar_digitos_pares_impares(numero)
    
    # Paso 3: Extraer los dígitos para mostrar
    digitos_pares: str = extraer_digitos_pares(numero)
    digitos_impares: str = extraer_digitos_impares(numero)
    
    # Paso 4: Mostrar resultado
    mostrar_resultado(numero, cantidad_pares, cantidad_impares, 
                     digitos_pares, digitos_impares)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
