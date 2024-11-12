
import os

# Mensajes de error predefinidos
MENSAJES_ERROR = (
    "Problemas al intentar limpiar la pantalla {error}",
    "Error al configurar los decimales. Formato: decimales <n>.",
    "Entrada no válida. Ingrese número, operador, 'resultado', 'cancelar' o <ENTER> para finalizar el cálculo.",
    "Error: Introduzca un operador antes de otro número.",
    "Comando no reconocido. Escriba 'lista' para ver las operaciones disponibles.",
    "Error: no es posible la división por 0! Introduzca otro valor diferente a 0...",
    "Se produjo un error: {error}"
)

# Operadores soportados por la calculadora
OPERADORES = ('+', '-', 'x', '*', '/', ':', '**', 'exp')
OPERADORES_SUMAR = ('+')
OPERADORES_RESTAR = ('-')
OPERADORES_MULTIPLICAR = ('x', '*')
OPERADORES_DIVIDIR = ('/', ':')
OPERADORES_POTENCIA = ('**', 'exp')



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
    """Suma dos números.

    Args:
        num1 (float): El primer número a sumar.
        num2 (float): El segundo número a sumar.

    Returns:
        float: El resultado de la suma de num1 y num2.
    """
    return num1 + num2


def restar(num1: float, num2: float) -> float:
    """Resta dos números.

    Args:
        num1 (float): El número del que se resta (minuendo).
        num2 (float): El número a restar (sustraendo).

    Returns:
        float: El resultado de la resta de num1 y num2.
    """
    return num1 - num2


def es_resultado_negativo(num1: float, num2: float) -> bool:
    """Determina si el resultado de una operación de multiplicación o división entre num1 y num2 debe ser negativo.

    Args:
        num1 (float): El primer número de la operación.
        num2 (float): El segundo número de la operación.
        es_potencia (bool, optional): Indica si la operación es una potencia. 

    Returns:
        bool: `True` si el resultado debería ser negativo, `False` en caso contrario. 
              Valor por defecto es `False`.
    """
    return (num1 != 0) and (num2 != 0) and (num1 < 0) != (num2 < 0)


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
    resultado_negativo = es_resultado_negativo(num1, num2)

    # Redondeo a enteros
    num1 = round(abs(num1))
    num2 = round(abs(num2))

    # Inicializa el resultado a 0, por si alguno de los números es 0
    resultado = 0

    if num1 != 0 and num2 != 0:
        # Para optimizar, usamos el menor número en el rango de iteraciones
        num_a_sumar = max(num1, num2)
        num_rango = min(num1, num2)

        # Calcula el resultado usando solo sumas
        for _ in range(num_rango):
            resultado += num_a_sumar

        # También podríamos haber utilizado la función sumar:
        # for _ in range(num_rango):
        #     resultado = sumar(resultado, num_a_sumar)

        # Ajuste de signo si el resultado es negativo
        if resultado_negativo:
            resultado = 0 - resultado

        # También podríamos haber utilizado la función restar:
        # if resultado_negativo:
        #     resultado = restar(0, resultado)

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
    resultado_negativo = es_resultado_negativo(num1, num2)

    # Redondeo a enteros
    num1 = round(abs(num1))
    num2 = round(abs(num2))

    if num2 == 0:
        raise ZeroDivisionError("No es posible dividir por cero!")

    # Inicializa el resultado a 0, por si num1 es 0
    resultado = 0

    if num1 != 0:
        # Realiza la división entera restando repetidamente el divisor
        while num1 >= num2:
            num1 -= num2
            resultado += 1

        # También podríamos haber utilizado la función restar
        # while num1 >= num2:
        #     num1 = restar(num1, num2)
        #     resultado = sumar(resultado, 1)

        # Ajuste de signo si el resultado es negativo
        if resultado_negativo:
            resultado = 0 - resultado

        # También podríamos haber utilizado la función restar:
        # if resultado_negativo:
        #     resultado = restar(0, resultado)

    return resultado


def potencia(base: float, exponente: float) -> int:
    """
    Calcula la potencia de un número usando multiplicaciones sucesivas.

    Args:
        base (float): La base que se va a elevar.
        exponente (float): El exponente al que se elevará la base.
    
    Returns:
        int: El resultado de elevar la base al exponente.
    
    Note:
        Utiliza la función multiplicar para realizar la operación de potencia.
        Este método está diseñado para exponentes enteros no negativos.
    """
    # Redondeamos a entero
    exponente = round(exponente)
    base = round(base)

    # Cualquier número elevado a 0 es 1
    if exponente == 0:
        resultado = 1

    # Premisa de resultado 0 con exponente negativo
    elif exponente < 0: 
        resultado = 0

    else:
        # Inicializa el resultado como la base y realiza la potencia mediante multiplicaciones sucesivas
        resultado = base
        for _ in range(exponente - 1):
            resultado = multiplicar(resultado, base)
        
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

    Raises:
        ZeroDivisionError: Si el divisor es cero.
    """    
    if operador in OPERADORES_MULTIPLICAR:
        resultado = multiplicar(num1, num2)
    elif operador in OPERADORES_DIVIDIR:
        resultado = dividir(num1, num2)
    elif operador in OPERADORES_SUMAR:
        resultado = sumar(num1, num2)
    elif operador in OPERADORES_POTENCIA:
        resultado = potencia(num1, num2)
    elif operador in OPERADORES_RESTAR:
        resultado = restar(num1, num2)
    else:
        # En principio no sería necesario controlar este error, ya que nunca va
        # a llamar a esta función con un operador que no esté en la constante 
        # OPERADORES (ver realizar_calculo()).
        raise ValueError

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
          ** o exp => Potencia
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

    Note:
        * Dentro de esta función el usuario puede realizar cálculos secuenciales, es decir, 
          comenzará introduciendo un número, después un operador, y otro número... a partir 
          de aquí sobre el resultado acumulado, introducirá operador y número para seguir 
          realizando cálculos (ver ejemplos en README.md de la tarea en el repositorio de GitHub).
        * El usuario es guiado para introducir números y operadores secuencialmente 
          para realizar operaciones básicas.
        * El usuario puede utilizar "resultado" en la secuencia de cálculo para reutilizar el 
          resultado almacenado en la calculadora.
        * El cálculo finaliza al pulsar <ENTER>, volviendo y actualizando el resultado almacenado 
          de la calculadora con el cálculo realizado.
        * También podemos escribir "cancelar", volviendo sin realizar ningún cambio en el 
          resultado almacenado de la calculadora.    
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
            # Cogemos el último operador ingresado (si antes había otro, lo reemplaza)
            # De esta manera, si ingresamos varios operadores seguidos, se realizará 
            # la operación que indique el último operador introducido.
            operador = entrada
        
        else:
            # Si se ingresó el comando resultado, reemplazamos el valor de entrada por
            # el valor del resultado de la calculadora.
            if entrada == "resultado":
                entrada = resultado_almacenado

            try:
                # Si estamos aquí es porque esperamos un número, pero siempre con el 
                # control de excepciones, para capturar errores de conversión.
                numero = float(entrada)

                # Si existe un operador, debemos realizar un cálculo.
                if operador is not None:
                    # Si el resultado aún no se ha asignado, tomamos 0 cómo el valor 
                    # inicial del cálculo. Esto se produce cuando solo ingresamos un
                    # operador y después un número.
                    if resultado is None:
                        resultado = 0

                    # Realizamos el cálculo y ajustamos el resultado a las posiciones
                    # decimales adecuadas.
                    resultado = round(calcular_operacion(resultado, numero, operador), decimales)

                    # Importante! Debemos reiniciar el operador después de realizar un 
                    # cálculo, para que lo siguiente válido sea un operador y no un 
                    # número.
                    operador = None

                elif resultado is None:
                    resultado = numero

                else:
                    mostrar_error(3)

            except ValueError:
                mostrar_error(2)
            except ZeroDivisionError:
                mostrar_error(5)
            except Exception as e:
                mostrar_error(6, e)
    
    return resultado


def ajustar_decimales(decimales: int, entrada: str) -> int:
    """
    Ajusta el número de posiciones decimales según la entrada proporcionada.

    Args:
        decimales (int): El número de posiciones decimales actual.
        entrada (str): Una cadena de texto que se espera contenga, en la segunda palabra,
            el número deseado de posiciones decimales. La primera palabra se ignora.

    Returns:
        (int): El número de posiciones decimales ajustado. Si ocurre un error en la conversión, devuelve el valor original de `decimales`.
    """
    posiciones_decimales = decimales
    
    try:
        posiciones_decimales = int(entrada.split()[1])
    except (IndexError, ValueError):
        mostrar_error(1)

    return posiciones_decimales


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

        elif entrada == "ce":
            resultado = 0

        elif entrada.startswith("decimales"):
            decimales = ajustar_decimales(decimales, entrada)
            print(f"Decimales configurados a {decimales}.")

        elif entrada == "calculo":
            resultado_ultimo_calculo = realizar_calculo(decimales, resultado)

            if resultado_ultimo_calculo != None:
                resultado = resultado_ultimo_calculo

        else:
            mostrar_error(4)


        if not desea_salir and entrada != "ce":
            pausa()


    limpiar_pantalla()
    print("\n\nBye, bye...\n\n")



if __name__ == "__main__":
    main()
