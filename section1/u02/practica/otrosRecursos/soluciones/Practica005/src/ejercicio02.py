"""
Ejercicio 2: Clasificador de Temperaturas

Descripción:
    Programa que clasifica una temperatura en categorías y determina
    si es una temperatura extrema.
    
Autor: Eduardo Fdez
Fecha: 2025-10-25
"""


def clasificar_temperatura(temperatura: float) -> tuple[str, bool]:
    """
    Clasifica una temperatura y determina si es extrema.
    
    Esta función es la que se evaluará mediante tests automáticos.
    
    Args:
        temperatura: La temperatura en grados Celsius
        
    Returns:
        tuple[str, bool]: (clasificación, es_extrema)
            - clasificación: "Helada", "Frío", "Templado", "Cálido" o "Caluroso"
            - es_extrema: True si temp < -10 o temp > 40, False en caso contrario
        
    Nota:
        - Si la temperatura está fuera del rango válido (-50 a 60), 
          devolver ("Inválida", False)
    """
    # Validar que la temperatura esté en un rango razonable
    if temperatura < -50 or temperatura > 60:
        return ("Inválida", False)
    
    # Determinar si es una temperatura extrema
    # Una temperatura es extrema si es menor que -10 o mayor que 40
    es_extrema: bool = temperatura < -10 or temperatura > 40
    
    # Clasificar la temperatura según los rangos establecidos
    clasificacion: str = ""
    
    if temperatura < 0:
        clasificacion = "Helada"
    elif temperatura <= 10:  # 0 <= temp <= 10
        clasificacion = "Frío"
    elif temperatura <= 20:  # 11 <= temp <= 20
        clasificacion = "Templado"
    elif temperatura <= 30:  # 21 <= temp <= 30
        clasificacion = "Cálido"
    else:  # temperatura > 30
        clasificacion = "Caluroso"
    
    return (clasificacion, es_extrema)


def solicitar_temperatura() -> float:
    """
    Solicita al usuario una temperatura y valida que esté en el rango correcto.
    
    Returns:
        float: La temperatura validada (entre -50 y 60)
    """
    temperatura: float = -100.0  # Valor inicial fuera de rango para entrar al bucle
    
    # Bucle que se ejecuta mientras la temperatura no sea válida
    while temperatura < -50 or temperatura > 60:
        entrada: str = input("Introduce la temperatura en °C: ")
        
        try:
            temperatura = float(entrada)
            
            # Validar el rango
            if temperatura < -50 or temperatura > 60:
                print("Error: La temperatura debe estar entre -50°C y 60°C")
        except ValueError:
            print("Error: Debe introducir un número válido.")
            temperatura = -100.0  # Mantener fuera de rango para continuar
    
    return temperatura


def mostrar_resultado(temperatura: float, clasificacion: str, es_extrema: bool) -> None:
    """
    Muestra el resultado de la clasificación de manera formateada.
    
    Args:
        temperatura: La temperatura analizada
        clasificacion: La clasificación obtenida
        es_extrema: Si la temperatura es extrema o no
    """
    print(f"\nTemperatura: {temperatura}°C")
    print(f"Clasificación: {clasificacion}")
    
    # Mostrar alerta según si es extrema o no
    if es_extrema:
        print("¡ALERTA! Temperatura EXTREMA")
    else:
        print("Temperatura NO extrema")


def main() -> None:
    """
    Función principal que coordina la ejecución del programa.
    
    Flujo:
        1. Solicita la temperatura al usuario (con validación)
        2. Clasifica la temperatura usando la función obligatoria
        3. Muestra el resultado formateado
    """
    # Paso 1: Obtener temperatura del usuario
    temperatura: float = solicitar_temperatura()
    
    # Paso 2: Clasificar usando la función obligatoria
    clasificacion: str
    es_extrema: bool
    clasificacion, es_extrema = clasificar_temperatura(temperatura)
    
    # Paso 3: Mostrar resultado
    mostrar_resultado(temperatura, clasificacion, es_extrema)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
