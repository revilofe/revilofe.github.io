
import os

# Mensajes de error predefinidos
MENSAJES_ERROR = (
    "Problemas al intentar limpiar la pantalla {error}",
    "Error al configurar los decimales. Formato: decimales <n>.",
    "Entrada no válida. Ingrese número, operador, 'resultado', 'cancelar' o <ENTER> para finalizar el cálculo.",
    "Error: Introduzca un operador antes de otro número.",
    "Comando no reconocido. Escriba 'lista' para ver las operaciones disponibles.",
)

# Operadores soportados por la calculadora
OPERADORES = ('+', '-', 'x', '*', '/', ':', '**', 'exp')


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.
    """
    try:
        os.system('clear' if os.name == 'posix' else 'cls')
    except Exception as e:
        mostrar_error(0, e)


def pausa():
    """
    Pausa la ejecución del programa hasta que se pulse ENTER.
    """
    input("\nPresione ENTER para continuar...")


def mostrar_error(indice_error: int, msj_error = None):
    """
    Muestra un mensaje de error en la consola.
    
    Args:
        indice_error (int): Índice del mensaje de error en MENSAJES_ERROR.
        msj_error (str, opcional): Texto adicional para personalizar el mensaje de error.
    """
    try:
        if msj_error != None:
            print(f"\n*ERROR* {MENSAJES_ERROR[indice_error].format(error = msj_error)}\n")
        else:
            print(f"\n*ERROR* {MENSAJES_ERROR[indice_error]}\n")
    except IndexError:
        print("\n*ERROR* Mensaje de error no definido.\n")
    except Exception as e:
        print(f"\n*ERROR* Problemas al mostrar error!\n{e}\n")


def sumar(num1: float, num2: float) -> float:
    """Devuelve la suma de num1 y num2."""
    return num1 + num2


def restar(num1: float, num2: float) -> float:
    """Devuelve la resta de num1 y num2."""
    return num1 - num2


def es_resultado_negativo(num1: float, num2: float) -> bool:
    """Determina si el resultado de una operación entre num1 y num2 debe ser negativo."""
    return (num1 < 0) != (num2 < 0)


def multiplicar(num1: float, num2: float) -> int:
    """
    Realiza la multiplicación ENTERA de dos números usando solo sumas y restas.
    
    Args:
        num1 (float): Primer número.
        num2 (float): Segundo número.
    
    Returns:
        int: Resultado de la multiplicación.

    Note:
        Debe redondear los números recibidos a enteros para trabajar.
    """
    
    if num2 == 0:
        resultado = 0
    else:
        resultado_negativo = es_resultado_negativo(num1, num2)

        num1 = round(abs(num1))
        num2 = round(abs(num2))

        # Para optimizar el menor número de iteraciones del bucle for, seleccionamos el rango del número menor
        num_a_sumar = max(num1, num2)
        num_rango = min(num1, num2)

        resultado = 0
        for _ in range(num_rango):
            resultado += num_a_sumar

        if resultado_negativo:
            resultado = resultado - (resultado + resultado)

    return resultado
   

def dividir(num1: float, num2: float) -> int:
    """
    Realiza la división ENTERA de dos números usando solo sumas y restas.
    
    Args:
        num1 (float): Dividendo.
        num2 (float): Divisor.
    
    Returns:
        int: Resultado de la división.
    
    Raises:
        ZeroDivisionError: Si el divisor es cero.

    Note:
        Debe redondear los números recibidos a enteros para trabajar.        
    """
    
    if num2 == 0:
        raise ZeroDivisionError("No es posible dividir por cero!")
    else:    
        resultado_negativo = es_resultado_negativo(num1, num2)

        num1 = round(abs(num1))
        num2 = round(abs(num2))

        resultado = 0
        while num1 >= num2:
            num1 -= num2
            resultado += 1

        if resultado_negativo:
            resultado = resultado - (resultado + resultado)

    return resultado


def potencia(base: float, exponente: float) -> int:
    """
    Calcula la potencia de un número usando multiplicaciones sucesivas.

    Args:
        base (float): La base que se va a elevar.
        exponente (int): El exponente al que se elevará la base.
    
    Returns:
        int: El resultado de elevar la base al exponente.
    
    Note:
        Utiliza la función multiplicar para realizar la operación de potencia.
        Este método está diseñado para exponentes enteros no negativos.
    """
    # Cualquier número elevado a 0 es 1
    if exponente == 0:
        resultado = 1

    # Para esta práctica vamos a suponer que un número elevado a un exponente 
    # negativo siempre dará 0 (aunque en realidad no es así matemáticamente)
    elif exponente < 0: 
        resultado = 0

    else:
        # Comprobamos si el signo del resultado debe ser negativo: 
        # Solo para bases negativas con exponentes impares...
        resultado_negativo = base < 0 and exponente % 2 != 0

        # Tomamos el valor absoluto de la base y exponente como entero
        exponente = round(abs(exponente))
        base = round(abs(base))
        resultado = base

        for _ in range(exponente - 1):
            resultado = multiplicar(resultado, base)
        
        if resultado_negativo:
            resultado = resultado - (resultado + resultado)

    return resultado


def pedir_entrada(msj: str) -> str:
    """
    Pide al usuario una entrada, la limpia y convierte a minúsculas.
    
    Args:
        msj (str): Mensaje para solicitar la entrada.
    
    Returns:
        str: Entrada del usuario.
    """    
    return input(msj).strip().lower()


def calcular_operacion(num1: float, num2: float, operador: str) -> float:
    """
    Realiza la operación especificada entre num1 y num2 dependiendo del valor del operador.
    
    Args:
        num1 (float): Primer número.
        num2 (float): Segundo número.
        operador (str): Operador de la operación.
    
    Returns:
        float: Resultado de la operación.
    """    
    if operador in "x*":
        resultado = multiplicar(num1, num2)
    elif operador in "/:":
        resultado = dividir(num1, num2)
    elif operador == "+":
        resultado = sumar(num1, num2)
    elif operador in "**exp":
        resultado = potencia(num1, num2)
    else:
        resultado = restar(num1, num2)

    return resultado


def obtener_operaciones() -> str:
    """Devuelve una cadena con la lista de operaciones disponibles en la calculadora."""
    return """
    Operaciones disponibles:
      ce => Reiniciar resultado a 0
      decimales <n> => Establecer decimales en resultado
      cadena vacía + <ENTER> => Pregunta si desea salir
      calculo => Iniciar cálculo secuencial
          + => Suma
          - => Resta
          x o * => Multiplicación
          / o : => División
          ** exp => Potencia
          cancelar => vovler sin actualizar resultado de la calculadora
          cadena vacía + <ENTER> => volver actualizando resultado de la calculadora
    """


def realizar_calculo(decimales: int, resultado_almacenado: float) -> float:
    """
    Realiza una secuencia de cálculos solicitando números y operadores al usuario.
    
    Args:
        decimales (int): Número de decimales para el resultado.
        resultado_almacenado (float): Valor almacenado en la calculadora.
    
    Returns:
        float: Resultado final del cálculo o None si se cancela.
    """
    operador = None
    resultado = None
    realizando_calculos = True

    print("\n## Ingrese número, operador, 'resultado', 'cancelar' o <ENTER> para finalizar el cálculo ##\n")

    while realizando_calculos:
        entrada = pedir_entrada(f"\t (Cálculo = {resultado if resultado != None else 0:.{decimales}f}) >> ")
        
        if entrada == "cancelar":
            resultado = None
            realizando_calculos = False
        
        elif entrada == "":
            realizando_calculos = False
        
        elif entrada in OPERADORES:
            operador = entrada
        
        else:
            if entrada == "resultado":
                entrada = resultado_almacenado

            try:
                numero = float(entrada)

                if operador is not None:
                    if resultado is None:
                        resultado = 0
                    resultado = round(calcular_operacion(resultado, numero, operador), decimales)
                    operador = None

                elif resultado is None:
                    resultado = numero

                else:
                    mostrar_error(3)

            except ValueError:
                mostrar_error(2)
    
    return resultado


def main():
    """
    Función principal de la calculadora. Gestiona la entrada del usuario y coordina las operaciones.
    
    Note:
        El flujo del programa es el siguiente:

        1. Inicia la calculadora mostrando el resultado almacenado por defecto (0.00).
        
        2. El usuario ingresa un comando, que puede ser:
            - "lista" para ver todas las operaciones disponibles.
            - "ce" para reiniciar el resultado almacenado a 0.
            - "decimales <n>" para establecer el número de decimales mostrados en el resultado.
            - "calculo" para iniciar una secuencia de cálculo paso a paso.
            - Una entrada vacía y pulsa la tecla <ENTER> para salir de la calculadora.
        
        3. Según el comando ingresado:
            - El programa realiza la operación o ejecuta la acción indicada.
            - Al ingresar "calculo":
                * El usuario es guiado para introducir números y operadores secuencialmente para realizar operaciones básicas.
                * El usuario puede utilizar "resultado" en la secuencia de cálculo para reutilizar el resultado almacenado en la calculadora.
                * El cálculo finaliza al pulsar <ENTER>, volviendo y actualizando el resultado almacenado de la calculadora con el cálculo realizado.
                * También podemos escribir "cancelar", volviendo sin realizar ningún cambio en el resultado almacenado de la calculadora.
        
        4. La calculadora sigue ejecutándose hasta que el usuario confirma la salida al ingresar una entrada vacía y pulsar <ENTER>.
        
        5. Finalmente, se limpia la pantalla, el programa se despide y termina.
    """

    decimales = 2
    resultado = 0.0
    desea_salir = False

    while not desea_salir:
        limpiar_pantalla()
        print("### CALCULADORA ###\n    -----------\n\n")

        entrada = pedir_entrada(f"Operación (RES => {resultado:.{decimales}f}) >> ")

        if entrada == "":
            desea_salir = pedir_entrada("¿Desea salir de la calculadora? (s/n) ") == "s"

        elif entrada == "lista":
            print(obtener_operaciones())
            pausa()

        elif entrada == "ce":
            resultado = 0

        elif entrada.startswith("decimales"):
            try:
                decimales = int(entrada.split()[1])
                print(f"Decimales configurados a {decimales}.")
            except (IndexError, ValueError):
                mostrar_error(1)
            
            pausa()                

        elif entrada == "calculo":
            resultado_ultimo_calculo = realizar_calculo(decimales, resultado)

            if resultado_ultimo_calculo != None:
                resultado = resultado_ultimo_calculo

            pausa()

        else:
            mostrar_error(4)
            pausa()


    limpiar_pantalla()
    print("\n\nBye, bye...\n\n")


if __name__ == "__main__":
    main()
