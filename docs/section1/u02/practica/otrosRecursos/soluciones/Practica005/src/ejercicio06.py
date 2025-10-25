"""
Ejercicio 6: Detector de Años Bisiestos

Descripción:
    Programa que determina si un año es bisiesto según las reglas del
    calendario gregoriano.
    
Autor: Eduardo Fdez
Fecha: 2025-10-25
"""


def es_bisiesto(anio: int) -> tuple[bool, int]:
    """
    Determina si un año es bisiesto y devuelve un código de razón.
    
    Esta función es la que se evaluará mediante tests automáticos.
    
    Args:
        anio: El año a verificar
        
    Returns:
        tuple[bool, int]: (es_bisiesto, codigo_razon)
            - es_bisiesto: True si es bisiesto, False si no
            - codigo_razon: Código que indica la razón:
                * 0: Año fuera de rango (< 1582 o > 3000)
                * 1: Es bisiesto - divisible por 400
                * 2: No es bisiesto - divisible por 100 pero no por 400
                * 3: Es bisiesto - divisible por 4 pero no por 100
                * 4: No es bisiesto - no divisible por 4
        
    Nota:
        - Si año < 1582 o año > 3000, devolver (False, 0)
        - 1582 es el año de adopción del calendario gregoriano
    """
    # Validar que el año esté en el rango válido
    if anio < 1582 or anio > 3000:
        return (False, 0)  # Código 0: Año fuera de rango
    
    # Aplicar las reglas del año bisiesto:
    # 1. Si es divisible por 400 -> ES bisiesto (código 1)
    # 2. Si es divisible por 100 (pero no por 400) -> NO es bisiesto (código 2)
    # 3. Si es divisible por 4 (pero no por 100) -> ES bisiesto (código 3)
    # 4. En cualquier otro caso -> NO es bisiesto (código 4)
    
    if anio % 400 == 0:
        # Es divisible por 400: ES bisiesto (año secular bisiesto)
        return (True, 1)
    elif anio % 100 == 0:
        # Es divisible por 100 pero NO por 400: NO es bisiesto
        return (False, 2)
    elif anio % 4 == 0:
        # Es divisible por 4 pero NO por 100: ES bisiesto
        return (True, 3)
    else:
        # No es divisible por 4: NO es bisiesto
        return (False, 4)


def solicitar_anio() -> int:
    """
    Solicita al usuario un año y valida el rango.
    
    Returns:
        int: Año validado (entre 1582 y 3000)
    """
    anio: int = 0
    
    while anio < 1582 or anio > 3000:
        entrada: str = input("Introduce un año: ")
        
        try:
            anio = int(entrada)
            
            if anio < 1582 or anio > 3000:
                print("Error: El año debe estar entre 1582 y 3000")
        except ValueError:
            print("Error: Debe introducir un número entero válido")
            anio = 0
    
    return anio


def calcular_dias_febrero(es_bisiesto_valor: bool) -> int:
    """
    Calcula cuántos días tiene febrero según si es bisiesto o no.
    
    Args:
        es_bisiesto_valor: True si el año es bisiesto
        
    Returns:
        int: 29 si es bisiesto, 28 si no
    """
    if es_bisiesto_valor:
        return 29
    else:
        return 28


def calcular_dias_anio(es_bisiesto_valor: bool) -> int:
    """
    Calcula cuántos días tiene el año.
    
    Args:
        es_bisiesto_valor: True si el año es bisiesto
        
    Returns:
        int: 366 si es bisiesto, 365 si no
    """
    if es_bisiesto_valor:
        return 366
    else:
        return 365


def obtener_mensaje_razon(codigo: int) -> str:
    """
    Convierte un código de razón a un mensaje legible.
    
    Args:
        codigo: El código de razón (0-4)
        
    Returns:
        str: Mensaje explicativo
    """
    if codigo == 0:
        return "Año fuera de rango"
    elif codigo == 1:
        return "Es divisible por 400 (año secular bisiesto)"
    elif codigo == 2:
        return "Es divisible por 100 pero no por 400 (año secular no bisiesto)"
    elif codigo == 3:
        return "Es divisible por 4 y no es un año secular"
    elif codigo == 4:
        return "No es divisible por 4"
    else:
        return "Código de razón desconocido"


def mostrar_resultado(anio: int, es_bisiesto_valor: bool, codigo_razon: int) -> None:
    """
    Muestra el resultado del análisis del año.
    
    Args:
        anio: El año analizado
        es_bisiesto_valor: Si el año es bisiesto
        codigo_razon: Código que indica la razón (0-4)
    """
    # Mostrar si es o no bisiesto
    if es_bisiesto_valor:
        print(f"\nEl año {anio} SÍ es bisiesto")
    else:
        print(f"\nEl año {anio} NO es bisiesto")
    
    # Convertir código a mensaje y mostrar
    mensaje_razon: str = obtener_mensaje_razon(codigo_razon)
    print(f"Razón: {mensaje_razon}")
    
    # Mostrar información adicional solo si el año es válido
    if codigo_razon != 0:  # 0 = Año fuera de rango
        dias_febrero: int = calcular_dias_febrero(es_bisiesto_valor)
        dias_anio: int = calcular_dias_anio(es_bisiesto_valor)
        print(f"Tendrá {dias_anio} días (febrero con {dias_febrero} días)")


def main() -> None:
    """
    Función principal que coordina la ejecución del programa.
    
    Flujo:
        1. Solicita un año al usuario
        2. Determina si es bisiesto usando la función obligatoria
        3. Muestra el resultado con explicación
    """
    # Paso 1: Obtener año del usuario
    anio: int = solicitar_anio()
    
    # Paso 2: Determinar si es bisiesto
    es_bisiesto_valor: bool
    codigo_razon: int
    es_bisiesto_valor, codigo_razon = es_bisiesto(anio)
    
    # Paso 3: Mostrar resultado
    mostrar_resultado(anio, es_bisiesto_valor, codigo_razon)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
