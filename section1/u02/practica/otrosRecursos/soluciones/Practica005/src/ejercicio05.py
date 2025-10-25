"""
Ejercicio 5: Conversor de Tiempo

Descripción:
    Programa que convierte una cantidad de segundos a formato legible
    en días, horas, minutos y segundos.
    
Autor: Eduardo Fdez
Fecha: 2025-10-25
"""


def convertir_segundos(segundos_totales: int) -> tuple[int, int, int, int]:
    """
    Convierte una cantidad de segundos a días, horas, minutos y segundos.
    
    Esta función es la que se evaluará mediante tests automáticos.
    
    Args:
        segundos_totales: Cantidad total de segundos (debe ser >= 0)
        
    Returns:
        tuple[int, int, int, int]: (dias, horas, minutos, segundos)
        
    Nota:
        - Si segundos_totales < 0, devolver (0, 0, 0, 0)
        - 1 día = 86400 segundos
        - 1 hora = 3600 segundos
        - 1 minuto = 60 segundos
    """
    # Validar que los segundos no sean negativos
    if segundos_totales < 0:
        return (0, 0, 0, 0)
    
    # Constantes de conversión
    SEGUNDOS_POR_DIA: int = 86400   # 24 * 60 * 60
    SEGUNDOS_POR_HORA: int = 3600   # 60 * 60
    SEGUNDOS_POR_MINUTO: int = 60
    
    # Calcular días y obtener el resto
    dias: int = segundos_totales // SEGUNDOS_POR_DIA
    resto: int = segundos_totales % SEGUNDOS_POR_DIA
    
    # Calcular horas y obtener el resto
    horas: int = resto // SEGUNDOS_POR_HORA
    resto = resto % SEGUNDOS_POR_HORA
    
    # Calcular minutos y obtener el resto
    minutos: int = resto // SEGUNDOS_POR_MINUTO
    segundos: int = resto % SEGUNDOS_POR_MINUTO
    
    return (dias, horas, minutos, segundos)


def solicitar_segundos() -> int:
    """
    Solicita al usuario una cantidad de segundos.
    
    Returns:
        int: Cantidad de segundos validada (>= 0)
    """
    segundos: int = -1
    
    while segundos < 0:
        entrada: str = input("Introduce el número de segundos: ")
        
        try:
            segundos = int(entrada)
            
            if segundos < 0:
                print("Error: Los segundos deben ser un valor positivo o cero")
        except ValueError:
            print("Error: Debe introducir un número entero válido")
            segundos = -1
    
    return segundos


def formatear_plural(cantidad: int, singular: str, plural: str) -> str:
    """
    Devuelve la forma correcta (singular o plural) según la cantidad.
    
    Args:
        cantidad: La cantidad a evaluar
        singular: Palabra en singular
        plural: Palabra en plural
        
    Returns:
        str: La forma correcta con la cantidad
    """
    if cantidad == 1:
        return f"{cantidad} {singular}"
    else:
        return f"{cantidad} {plural}"


def mostrar_resultado(segundos_totales: int, dias: int, horas: int, 
                      minutos: int, segundos: int) -> None:
    """
    Muestra el resultado de la conversión formateado.
    
    Args:
        segundos_totales: Los segundos totales introducidos
        dias: Días calculados
        horas: Horas calculadas
        minutos: Minutos calculados
        segundos: Segundos calculados
    """
    print(f"\n{segundos_totales} segundos equivalen a:")
    
    # Construir el resultado parte por parte
    resultado: str = ""
    
    # Añadir días si hay
    if dias > 0:
        resultado = resultado + formatear_plural(dias, "día", "días")
    
    # Añadir horas si hay
    if horas > 0:
        if resultado != "":
            resultado = resultado + ", "
        resultado = resultado + formatear_plural(horas, "hora", "horas")
    
    # Añadir minutos si hay
    if minutos > 0:
        if resultado != "":
            resultado = resultado + ", "
        resultado = resultado + formatear_plural(minutos, "minuto", "minutos")
    
    # Añadir segundos si hay
    if segundos > 0:
        if resultado != "":
            resultado = resultado + ", "
        resultado = resultado + formatear_plural(segundos, "segundo", "segundos")
    
    # Si todo es 0, mostrar "0 segundos"
    if resultado == "":
        resultado = "0 segundos"
    
    print(resultado)


def main() -> None:
    """
    Función principal que coordina la ejecución del programa.
    
    Flujo:
        1. Solicita la cantidad de segundos
        2. Convierte usando la función obligatoria
        3. Muestra el resultado formateado con plurales
    """
    # Paso 1: Obtener segundos del usuario
    segundos_totales: int = solicitar_segundos()
    
    # Paso 2: Convertir usando la función obligatoria
    dias: int
    horas: int
    minutos: int
    segundos: int
    dias, horas, minutos, segundos = convertir_segundos(segundos_totales)
    
    # Paso 3: Mostrar resultado
    mostrar_resultado(segundos_totales, dias, horas, minutos, segundos)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
