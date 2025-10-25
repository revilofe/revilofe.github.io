"""
Ejercicio 4: Calculadora de Índice de Masa Corporal (IMC)

Descripción:
    Programa que calcula el IMC y determina la categoría de peso según los
    estándares de salud establecidos.
    
Autor: Eduardo Fdez
Fecha: 2025-10-25
"""


def calcular_imc(peso: float, altura: float) -> tuple[float, str]:
    """
    Calcula el IMC y determina la categoría de peso.
    
    Esta función es la que se evaluará mediante tests automáticos.
    
    Args:
        peso: Peso en kilogramos
        altura: Altura en metros
        
    Returns:
        tuple[float, str]: (imc, categoria)
            - imc: El índice de masa corporal calculado
            - categoria: "Bajo peso", "Normal", "Sobrepeso" u "Obesidad"
        
    Nota:
        - Si peso <= 0 o altura <= 0, devolver (0.0, "Datos inválidos")
        - Si peso < 20 o peso > 300, devolver (0.0, "Peso fuera de rango")
        - Si altura < 0.5 o altura > 2.5, devolver (0.0, "Altura fuera de rango")
    """
    # Validar que los datos sean positivos
    if peso <= 0 or altura <= 0:
        return (0.0, "Datos inválidos")
    
    # Validar rangos razonables de peso
    if peso < 20 or peso > 300:
        return (0.0, "Peso fuera de rango")
    
    # Validar rangos razonables de altura
    if altura < 0.5 or altura > 2.5:
        return (0.0, "Altura fuera de rango")
    
    # Calcular IMC: peso / altura²
    imc: float = peso / (altura * altura)
    
    # Determinar la categoría según el IMC
    categoria: str = ""
    
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:  # 18.5 <= imc < 25
        categoria = "Normal"
    elif imc < 30:  # 25 <= imc < 30
        categoria = "Sobrepeso"
    else:  # imc >= 30
        categoria = "Obesidad"
    
    return (imc, categoria)


def solicitar_peso() -> float:
    """
    Solicita el peso al usuario y valida que esté en rango.
    
    Returns:
        float: Peso validado entre 20 y 300 kg
    """
    peso: float = 0.0
    
    while peso < 20 or peso > 300:
        entrada: str = input("Peso en kg: ")
        
        try:
            peso = float(entrada)
            
            if peso < 20 or peso > 300:
                print("Error: El peso debe estar entre 20 y 300 kg")
        except ValueError:
            print("Error: Debe introducir un número válido")
            peso = 0.0
    
    return peso


def solicitar_altura() -> float:
    """
    Solicita la altura al usuario y valida que esté en rango.
    
    Returns:
        float: Altura validada entre 0.5 y 2.5 metros
    """
    altura: float = 0.0
    
    while altura < 0.5 or altura > 2.5:
        entrada: str = input("Altura en metros: ")
        
        try:
            altura = float(entrada)
            
            if altura < 0.5 or altura > 2.5:
                print("Error: La altura debe estar entre 0.5 y 2.5 metros")
        except ValueError:
            print("Error: Debe introducir un número válido")
            altura = 0.0
    
    return altura


def mostrar_resultado(peso: float, altura: float, imc: float, categoria: str) -> None:
    """
    Muestra el resultado del cálculo de IMC formateado.
    
    Args:
        peso: El peso introducido
        altura: La altura introducida
        imc: El IMC calculado
        categoria: La categoría de peso determinada
    """
    print(f"\nPeso: {peso:.1f} kg")
    print(f"Altura: {altura:.2f} m")
    print(f"IMC: {imc:.2f}")
    print(f"Categoría: {categoria}")


def main() -> None:
    """
    Función principal que coordina la ejecución del programa.
    
    Flujo:
        1. Solicita peso y altura al usuario (con validación)
        2. Calcula el IMC usando la función obligatoria
        3. Muestra el resultado formateado
    """
    # Paso 1: Obtener datos del usuario
    peso: float = solicitar_peso()
    altura: float = solicitar_altura()
    
    # Paso 2: Calcular IMC y categoría
    imc: float
    categoria: str
    imc, categoria = calcular_imc(peso, altura)
    
    # Paso 3: Mostrar resultado
    mostrar_resultado(peso, altura, imc, categoria)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
