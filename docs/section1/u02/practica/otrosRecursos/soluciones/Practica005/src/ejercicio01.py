"""
Ejercicio 1: Calculadora de Propinas

Descripción:
    Programa que calcula la propina y el total a pagar en un restaurante
    según la calidad del servicio proporcionada por el usuario.
    
Autor: Eduardo Fdez
Fecha: 2025-10-25
"""


def calcular_propina(importe: float, calidad: str) -> tuple[float, float]:
    """
    Calcula la propina y el total a pagar según el importe y la calidad del servicio.
    
    Esta función es la que se evaluará mediante tests automáticos.
    
    Args:
        importe: El importe de la cuenta (debe ser positivo)
        calidad: Calidad del servicio ("excelente" = 20%, "bueno" = 15%, "regular" = 10%)
        
    Returns:
        tuple[float, float]: Una tupla con (propina, total_a_pagar)
        
    Nota:
        - Si el importe es <= 0, devuelve (0.0, 0.0)
        - Si la calidad no es válida, devuelve (0.0, importe)
        - La calidad se compara en minúsculas
    """
    # Validación: si el importe no es positivo, devolver valores en 0
    if importe <= 0:
        return (0.0, 0.0)
    
    # Convertir la calidad a minúsculas para comparación case-insensitive
    calidad_lower: str = calidad.lower()
    
    # Inicializar el porcentaje en 0 (caso de calidad no válida)
    porcentaje: int = 0
    
    # Determinar el porcentaje según la calidad
    # Usamos if-elif en lugar de diccionarios ya que aún no se han visto
    if calidad_lower == "excelente":
        porcentaje = 20
    elif calidad_lower == "bueno":
        porcentaje = 15
    elif calidad_lower == "regular":
        porcentaje = 10
    else:
        # Calidad no válida: devolver propina 0 y el importe original
        return (0.0, importe)
    
    # Calcular la propina aplicando el porcentaje
    propina: float = importe * porcentaje / 100
    
    # Calcular el total (importe + propina)
    total: float = importe + propina
    
    # Devolver ambos valores como tupla
    return (propina, total)


def solicitar_importe() -> float:
    """
    Solicita al usuario el importe de la cuenta y valida que sea positivo.
    
    Returns:
        float: El importe de la cuenta validado (siempre > 0)
    """
    importe: float = -1.0
    
    # Bucle que se ejecuta mientras el importe no sea válido
    # Usamos una condición explícita en lugar de while True
    while importe <= 0:
        entrada: str = input("Importe de la cuenta: ")
        
        # Intentar convertir la entrada a float
        # Si hay error, el importe queda en -1 y se repite el bucle
        try:
            importe = float(entrada)
            
            # Validar que sea positivo
            if importe <= 0:
                print("Error: El importe debe ser un valor positivo.")
        except ValueError:
            print("Error: Debe introducir un número válido.")
            importe = -1.0  # Asegurar que continúa el bucle
    
    return importe


def solicitar_calidad_servicio() -> str:
    """
    Solicita al usuario la calidad del servicio y valida que sea una opción correcta.
    
    Returns:
        str: La calidad del servicio en minúsculas ("excelente", "bueno" o "regular")
    """
    calidad: str = ""
    
    # Bucle que se ejecuta mientras la calidad no sea válida
    # Verificamos con una condición explícita
    while calidad != "excelente" and calidad != "bueno" and calidad != "regular":
        entrada: str = input("Calidad del servicio (excelente/bueno/regular): ")
        calidad = entrada.lower()
        
        # Si la calidad no es válida, mostrar mensaje y continuar el bucle
        if calidad != "excelente" and calidad != "bueno" and calidad != "regular":
            print("Error: Debe introducir 'excelente', 'bueno' o 'regular'.")
    
    return calidad


def obtener_porcentaje_texto(calidad: str) -> str:
    """
    Obtiene el texto del porcentaje para mostrar según la calidad.
    
    Args:
        calidad: La calidad del servicio (ya validada)
        
    Returns:
        str: El texto del porcentaje ("20%", "15%" o "10%")
    """
    # Determinar el porcentaje según la calidad
    if calidad == "excelente":
        return "20%"
    elif calidad == "bueno":
        return "15%"
    else:  # calidad == "regular"
        return "10%"


def mostrar_resumen(importe: float, propina: float, total: float, calidad: str) -> None:
    """
    Muestra el resumen de la cuenta con el formato requerido.
    
    Args:
        importe: El importe de la cuenta
        propina: El valor de la propina
        total: El total a pagar (importe + propina)
        calidad: La calidad del servicio (para mostrar el porcentaje)
    """
    porcentaje_texto: str = obtener_porcentaje_texto(calidad)
    
    print(f"\nCuenta: {importe:.2f}€")
    print(f"Propina ({porcentaje_texto}): {propina:.2f}€")
    print(f"Total a pagar: {total:.2f}€")


def main() -> None:
    """
    Función principal que coordina la ejecución del programa.
    
    Flujo:
        1. Solicita el importe de la cuenta (con validación)
        2. Solicita la calidad del servicio (con validación)
        3. Llama a la función calcular_propina para obtener los resultados
        4. Muestra el resumen formateado
    """
    # Paso 1: Obtener datos del usuario con validación
    importe: float = solicitar_importe()
    calidad: str = solicitar_calidad_servicio()
    
    # Paso 2: Calcular propina y total usando la función obligatoria
    # Esta función devuelve una tupla, la desempaquetamos en dos variables
    propina: float
    total: float
    propina, total = calcular_propina(importe, calidad)
    
    # Paso 3: Mostrar resultado formateado
    mostrar_resumen(importe, propina, total, calidad)


# Punto de entrada del programa
# Este bloque solo se ejecuta si el archivo se ejecuta directamente
# No se ejecuta si el archivo se importa (útil para los tests)
if __name__ == "__main__":
    main()

