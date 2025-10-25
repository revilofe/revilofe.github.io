"""
Ejercicio 9: Simulador de Carrera de Caracoles

Descripción:
    Programa que simula una carrera entre 3 caracoles con velocidades diferentes.
    Cada caracol avanza según su velocidad en cada turno hasta que uno llegue a la meta.
    
Autor: Eduardo Fdez
Fecha: 2025-10-25
"""


def simular_carrera(velocidad1: int, velocidad2: int, velocidad3: int, distancia_meta: int) -> tuple[int, int]:
    """
    Simula una carrera de 3 caracoles y determina el ganador y turnos necesarios.
    
    Esta función es la que se evaluará mediante tests automáticos.
    
    Args:
        velocidad1: Velocidad del caracol 1 (cm/turno, 1-10)
        velocidad2: Velocidad del caracol 2 (cm/turno, 1-10)
        velocidad3: Velocidad del caracol 3 (cm/turno, 1-10)
        distancia_meta: Distancia de la meta en cm (debe ser > 0)
        
    Returns:
        tuple[int, int]: (ganador, turnos_necesarios)
            - ganador: Número del caracol ganador (1, 2 o 3), o 0 si hay error
            - turnos_necesarios: Número de turnos que duró la carrera
        
    Nota:
        - Si alguna velocidad < 1 o > 10, devolver (0, 0)
        - Si distancia_meta <= 0, devolver (0, 0)
        - Si hay empate, gana el caracol con número más bajo
        - Todos los caracoles avanzan simultáneamente cada turno
    """
    # Validar datos de entrada
    if velocidad1 < 1 or velocidad1 > 10:
        return (0, 0)
    if velocidad2 < 1 or velocidad2 > 10:
        return (0, 0)
    if velocidad3 < 1 or velocidad3 > 10:
        return (0, 0)
    if distancia_meta <= 0:
        return (0, 0)
    
    # Inicializar posiciones de los caracoles
    posicion1: int = 0
    posicion2: int = 0
    posicion3: int = 0
    
    # Contador de turnos
    turnos: int = 0
    
    # Variable para controlar si hay ganador
    hay_ganador: bool = False
    ganador: int = 0
    
    # Simular la carrera turno por turno
    while not hay_ganador:
        # Incrementar turnos
        turnos += 1
        
        # Cada caracol avanza según su velocidad
        posicion1 += velocidad1
        posicion2 += velocidad2
        posicion3 += velocidad3
        
        # Verificar si alguno llegó a la meta
        # En caso de empate, gana el de menor número
        if posicion1 >= distancia_meta:
            hay_ganador = True
            ganador = 1
        elif posicion2 >= distancia_meta:
            hay_ganador = True
            ganador = 2
        elif posicion3 >= distancia_meta:
            hay_ganador = True
            ganador = 3
    
    return (ganador, turnos)


def solicitar_velocidades() -> tuple[int, int, int]:
    """
    Solicita las velocidades de los 3 caracoles.
    
    Returns:
        tuple[int, int, int]: (velocidad1, velocidad2, velocidad3)
    """
    print("Introduce las velocidades de los caracoles (1-10 cm/turno):")
    
    velocidad1: int = 0
    while velocidad1 < 1 or velocidad1 > 10:
        entrada: str = input("Velocidad caracol 1: ")
        try:
            velocidad1 = int(entrada)
            if velocidad1 < 1 or velocidad1 > 10:
                print("Error: Velocidad debe estar entre 1 y 10")
        except ValueError:
            print("Error: Debe introducir un número entero")
            velocidad1 = 0
    
    velocidad2: int = 0
    while velocidad2 < 1 or velocidad2 > 10:
        entrada: str = input("Velocidad caracol 2: ")
        try:
            velocidad2 = int(entrada)
            if velocidad2 < 1 or velocidad2 > 10:
                print("Error: Velocidad debe estar entre 1 y 10")
        except ValueError:
            print("Error: Debe introducir un número entero")
            velocidad2 = 0
    
    velocidad3: int = 0
    while velocidad3 < 1 or velocidad3 > 10:
        entrada: str = input("Velocidad caracol 3: ")
        try:
            velocidad3 = int(entrada)
            if velocidad3 < 1 or velocidad3 > 10:
                print("Error: Velocidad debe estar entre 1 y 10")
        except ValueError:
            print("Error: Debe introducir un número entero")
            velocidad3 = 0
    
    return (velocidad1, velocidad2, velocidad3)


def solicitar_distancia_meta() -> int:
    """
    Solicita la distancia de la meta.
    
    Returns:
        int: Distancia de la meta en cm (> 0)
    """
    distancia: int = 0
    
    while distancia <= 0:
        entrada: str = input("Distancia de la meta (cm): ")
        try:
            distancia = int(entrada)
            if distancia <= 0:
                print("Error: La distancia debe ser positiva")
        except ValueError:
            print("Error: Debe introducir un número entero")
            distancia = 0
    
    return distancia


def calcular_distancias_finales(vel1: int, vel2: int, vel3: int, turnos: int) -> tuple[int, int, int]:
    """
    Calcula las distancias alcanzadas por cada caracol.
    
    Args:
        vel1, vel2, vel3: Velocidades de los caracoles
        turnos: Número de turnos que duró la carrera
        
    Returns:
        tuple[int, int, int]: Distancias alcanzadas (dist1, dist2, dist3)
    """
    dist1: int = vel1 * turnos
    dist2: int = vel2 * turnos
    dist3: int = vel3 * turnos
    
    return (dist1, dist2, dist3)


def mostrar_resultado(ganador: int, turnos: int, vel1: int, vel2: int, vel3: int, distancia_meta: int) -> None:
    """
    Muestra el resultado de la carrera de forma visual.
    
    Args:
        ganador: Número del caracol ganador
        turnos: Número de turnos que duró la carrera
        vel1, vel2, vel3: Velocidades de los caracoles
        distancia_meta: Distancia de la meta
    """
    print("\n" + "=" * 50)
    print("🐌 RESULTADO DE LA CARRERA 🐌")
    print("=" * 50)
    
    print(f"\nDistancia de la meta: {distancia_meta} cm")
    print(f"Turnos necesarios: {turnos}")
    
    print("\nVelocidades:")
    print(f"  🐌 Caracol 1: {vel1} cm/turno")
    print(f"  🐌 Caracol 2: {vel2} cm/turno")
    print(f"  🐌 Caracol 3: {vel3} cm/turno")
    
    # Calcular distancias alcanzadas por cada caracol
    dist1: int
    dist2: int
    dist3: int
    dist1, dist2, dist3 = calcular_distancias_finales(vel1, vel2, vel3, turnos)
    
    print("\nDistancias alcanzadas:")
    print(f"  Caracol 1: {dist1} cm")
    print(f"  Caracol 2: {dist2} cm")
    print(f"  Caracol 3: {dist3} cm")
    
    print(f"\n🏆 ¡GANADOR: Caracol {ganador}!")


def main() -> None:
    """
    Función principal que coordina la ejecución del programa.
    
    Flujo:
        1. Solicita las velocidades de los 3 caracoles (lectura)
        2. Solicita la distancia de la meta (lectura)
        3. Simula la carrera usando la función obligatoria (procesamiento)
        4. Muestra el resultado de forma visual (salida)
    """
    print("🐌 SIMULADOR DE CARRERA DE CARACOLES 🐌")
    print()
    
    # Paso 1: Lectura - Obtener velocidades
    vel1: int
    vel2: int
    vel3: int
    vel1, vel2, vel3 = solicitar_velocidades()
    
    # Paso 2: Lectura - Obtener distancia de la meta
    distancia: int = solicitar_distancia_meta()
    
    # Paso 3: Procesamiento - Simular carrera usando la función obligatoria
    ganador: int
    turnos: int
    ganador, turnos = simular_carrera(vel1, vel2, vel3, distancia)
    
    # Verificar si hubo error en la simulación
    if ganador == 0:
        print("\nError: Datos inválidos para la simulación")
        return
    
    # Paso 4: Salida - Mostrar resultado
    mostrar_resultado(ganador, turnos, vel1, vel2, vel3, distancia)


if __name__ == "__main__":
    main()
