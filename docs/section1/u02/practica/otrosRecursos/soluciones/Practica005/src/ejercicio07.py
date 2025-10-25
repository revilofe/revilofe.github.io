"""
Ejercicio 7: Calculadora de Descuentos Progresivos

Descripción:
    Programa que calcula el precio final de una compra aplicando descuentos
    progresivos por volumen y descuento adicional para clientes premium.
    
Autor: Eduardo Fdez
Fecha: 2025-10-25
"""


def calcular_precio_final(importe: float, es_premium: bool) -> tuple[float, float, float]:
    """
    Calcula el precio final aplicando descuentos por volumen y premium.
    
    Esta función es la que se evaluará mediante tests automáticos.
    
    Args:
        importe: Importe original de la compra (debe ser > 0)
        es_premium: True si el cliente es premium, False si no
        
    Returns:
        tuple[float, float, float]: (descuento_volumen, descuento_premium, precio_final)
            - descuento_volumen: Cantidad descontada por volumen
            - descuento_premium: Cantidad descontada por ser premium
            - precio_final: Precio final a pagar
        
    Nota:
        - Si importe <= 0, devolver (0.0, 0.0, 0.0)
        - El descuento premium se aplica DESPUÉS del descuento por volumen
        - Descuentos por volumen:
            * < 100€: 0%
            * 100-199€: 10%
            * 200-499€: 15%
            * >= 500€: 20%
        - Descuento premium: 5% adicional sobre el precio ya descontado
    """
    # Validar que el importe sea positivo
    if importe <= 0:
        return (0.0, 0.0, 0.0)
    
    # Determinar porcentaje de descuento por volumen
    porcentaje_volumen: float = 0.0
    
    if importe >= 500:
        porcentaje_volumen = 0.20
    elif importe >= 200:
        porcentaje_volumen = 0.15
    elif importe >= 100:
        porcentaje_volumen = 0.10
    # else: sin descuento (0%)
    
    # Calcular descuento por volumen
    descuento_volumen: float = importe * porcentaje_volumen
    
    # Calcular subtotal tras descuento de volumen
    subtotal: float = importe - descuento_volumen
    
    # Calcular descuento premium (5% sobre el subtotal)
    descuento_premium: float = 0.0
    if es_premium:
        descuento_premium = subtotal * 0.05
    
    # Calcular precio final
    precio_final: float = subtotal - descuento_premium
    
    return (descuento_volumen, descuento_premium, precio_final)


def solicitar_importe() -> float:
    """
    Solicita al usuario el importe de la compra.
    
    Returns:
        float: Importe validado (> 0)
    """
    importe: float = 0.0
    
    while importe <= 0:
        entrada: str = input("Importe de la compra: ")
        try:
            importe = float(entrada)
            if importe <= 0:
                print("Error: El importe debe ser positivo")
        except ValueError:
            print("Error: Debe introducir un número válido")
            importe = 0.0
    
    return importe


def solicitar_es_premium() -> bool:
    """
    Pregunta al usuario si el cliente es premium.
    
    Returns:
        bool: True si es premium, False si no
    """
    respuesta: str = ""
    
    while respuesta != "si" and respuesta != "no":
        respuesta = input("¿Cliente premium? (si/no): ").lower()
        if respuesta != "si" and respuesta != "no":
            print("Error: Debe responder 'si' o 'no'")
    
    return respuesta == "si"


def mostrar_resultado(importe: float, desc_vol: float, desc_prem: float, final: float) -> None:
    """
    Muestra el resultado de los descuentos aplicados de forma detallada.
    
    Args:
        importe: Importe original de la compra
        desc_vol: Descuento aplicado por volumen
        desc_prem: Descuento aplicado por ser premium
        final: Precio final a pagar
    """
    # Calcular valores para mostrar
    ahorro_total: float = desc_vol + desc_prem
    porcentaje_ahorro: float = (ahorro_total / importe) * 100 if importe > 0 else 0.0
    subtotal: float = importe - desc_vol
    
    print(f"\nImporte original: {importe:.2f}€")
    
    if desc_vol > 0:
        porc_vol: float = (desc_vol / importe) * 100
        print(f"Descuento por volumen ({porc_vol:.0f}%): -{desc_vol:.2f}€")
        print(f"Subtotal: {subtotal:.2f}€")
    
    if desc_prem > 0:
        print(f"Descuento premium (5%): -{desc_prem:.2f}€")
    
    print(f"Total a pagar: {final:.2f}€")
    
    if ahorro_total > 0:
        print(f"Ahorro total: {ahorro_total:.2f}€ ({porcentaje_ahorro:.2f}%)")


def main() -> None:
    """
    Función principal que coordina la ejecución del programa.
    
    Flujo:
        1. Solicita el importe de la compra
        2. Pregunta si el cliente es premium
        3. Calcula descuentos usando la función obligatoria
        4. Muestra el resultado detallado
    """
    # Paso 1: Obtener importe del usuario
    importe: float = solicitar_importe()
    
    # Paso 2: Preguntar si es cliente premium
    es_premium: bool = solicitar_es_premium()
    
    # Paso 3: Calcular descuentos usando la función obligatoria
    desc_vol: float
    desc_prem: float
    final: float
    desc_vol, desc_prem, final = calcular_precio_final(importe, es_premium)
    
    # Paso 4: Mostrar resultado
    mostrar_resultado(importe, desc_vol, desc_prem, final)


if __name__ == "__main__":
    main()
