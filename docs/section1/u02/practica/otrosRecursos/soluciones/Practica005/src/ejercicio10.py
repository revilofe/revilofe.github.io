"""
Ejercicio 10: Calculadora de Estadísticas Básicas

Descripción:
    Programa que calcula estadísticas básicas (suma, promedio, máximo, mínimo)
    de una serie de números positivos introducidos por el usuario.
    
Autor: Eduardo Fdez
Fecha: 2025-10-25
"""


def calcular_promedio(suma_total: int, cantidad: int) -> float:
    """
    Calcula el promedio a partir de la suma y cantidad.
    
    Esta función es la que se evaluará mediante tests automáticos.
    
    Args:
        suma_total: Suma total de todos los números
        cantidad: Cantidad de números procesados
        
    Returns:
        float: Promedio (suma / cantidad), o 0.0 si hay error
        
    Nota:
        - Si cantidad <= 0, devolver 0.0
        - Si suma_total < 0, devolver 0.0
        - El promedio debe tener precisión de float
    """
    # Validar datos de entrada
    if cantidad <= 0:
        return 0.0
    if suma_total < 0:
        return 0.0
    
    # Calcular promedio
    promedio: float = suma_total / cantidad
    
    return promedio


def encontrar_maximo_minimo(numeros_texto: str) -> tuple[int, int]:
    """
    Encuentra el máximo y mínimo de una serie de números separados por espacios.
    
    Esta es una función auxiliar para demostrar procesamiento de datos.
    
    Args:
        numeros_texto: String con números separados por espacios (ej: "5 10 3 8")
        
    Returns:
        tuple[int, int]: (maximo, minimo)
    """
    # Si está vacío, devolver valores por defecto
    if numeros_texto == "":
        return (0, 0)
    
    # Inicializar con valores extremos
    maximo: int = -999999
    minimo: int = 999999
    
    # Procesar cada número en el texto
    numero_actual: str = ""
    i: int = 0
    
    while i <= len(numeros_texto):
        # Si llegamos al final o encontramos un espacio
        if i == len(numeros_texto) or numeros_texto[i] == " ":
            # Si tenemos un número acumulado
            if numero_actual != "":
                # Convertir a entero
                valor: int = int(numero_actual)
                
                # Actualizar máximo y mínimo
                if valor > maximo:
                    maximo = valor
                if valor < minimo:
                    minimo = valor
                
                # Resetear número actual
                numero_actual = ""
        else:
            # Acumular dígitos
            numero_actual += numeros_texto[i]
        
        i += 1
    
    return (maximo, minimo)


def solicitar_numeros() -> tuple[int, int, str]:
    """
    Solicita números al usuario hasta que ingrese 0.
    
    Returns:
        tuple[int, int, str]: (cantidad, suma_total, numeros_como_texto)
    """
    print("Introduce números positivos (0 para terminar):")
    
    cantidad: int = 0
    suma_total: int = 0
    numeros_texto: str = ""
    
    numero: int = -1
    
    while numero != 0:
        try:
            numero = int(input(f"Número {cantidad + 1}: "))
            
            if numero < 0:
                print("Error: Solo se aceptan números positivos")
            elif numero > 0:
                # Agregar a la suma
                suma_total += numero
                cantidad += 1
                
                # Guardar en texto para calcular máximo/mínimo
                if numeros_texto == "":
                    numeros_texto = str(numero)
                else:
                    numeros_texto += " " + str(numero)
            # Si es 0, terminamos el bucle
        except ValueError:
            print("Error: Debe introducir un número entero")
    
    return (cantidad, suma_total, numeros_texto)


def mostrar_resultado(cantidad: int, suma: int, promedio: float, maximo: int, minimo: int) -> None:
    """
    Muestra las estadísticas calculadas de forma clara.
    
    Args:
        cantidad: Cantidad de números procesados
        suma: Suma total de los números
        promedio: Promedio de los números
        maximo: Valor máximo
        minimo: Valor mínimo
    """
    print("\n" + "=" * 50)
    print("📊 ESTADÍSTICAS DE LOS NÚMEROS INTRODUCIDOS 📊")
    print("=" * 50)
    
    print(f"\nCantidad de números: {cantidad}")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Número máximo: {maximo}")
    print(f"Número mínimo: {minimo}")
    
    # Calcular rango
    rango: int = maximo - minimo
    print(f"Rango (máx - mín): {rango}")


def main() -> None:
    """
    Función principal que coordina la ejecución del programa.
    
    Flujo:
        1. Solicita números al usuario hasta que ingrese 0
        2. Calcula promedio usando la función obligatoria
        3. Encuentra máximo y mínimo
        4. Muestra todos los resultados
    """
    print("📊 CALCULADORA DE ESTADÍSTICAS BÁSICAS 📊")
    print()
    
    # Paso 1: Obtener números del usuario
    cantidad: int
    suma_total: int
    numeros_texto: str
    cantidad, suma_total, numeros_texto = solicitar_numeros()
    
    # Validar que se hayan introducido números
    if cantidad == 0:
        print("\nNo se introdujeron números válidos.")
        return
    
    # Paso 2: Calcular promedio usando la función obligatoria
    promedio: float = calcular_promedio(suma_total, cantidad)
    
    # Paso 3: Encontrar máximo y mínimo
    maximo: int
    minimo: int
    maximo, minimo = encontrar_maximo_minimo(numeros_texto)
    
    # Paso 4: Mostrar resultados
    mostrar_resultado(cantidad, suma_total, promedio, maximo, minimo)


if __name__ == "__main__":
    main()
