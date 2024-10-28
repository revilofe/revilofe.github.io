import os
import random
import time


def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pausa():
    """Realiza una pausa hasta que el usuario presione ENTER."""
    input("\nPresione ENTER para continuar...")
    limpiar_pantalla()


def evaluar_diferencia(numero: int, numero_oculto: int, frio: int, caliente: int) -> int:
    """
    Evalúa la distancia entre el número oculto y el ingresado, y devuelve un código numérico
    basado en la cercanía.
    """
    diferencia = abs(numero_oculto - numero)
    
    if diferencia > frio:
        return 0  # Frío
    elif diferencia > caliente:
        return 1  # Caliente
    else:
        return 2  # Te Quemas


def mostrar_pista(numero: int, numero_oculto: int, intentos: int, frio: int, caliente: int):
    """
    Muestra una pista combinando la distancia (frío, caliente, te quemas) y si el número oculto
    es mayor o menor.
    """
    diferencia_code = evaluar_diferencia(numero, numero_oculto, frio, caliente)

    # Determinamos el mensaje según el código de diferencia
    if diferencia_code == 0:
        pista = "* FRÍO, FRÍO,"
    elif diferencia_code == 1:
        pista = "* CALIENTE, CALIENTE,"
    else:
        pista = "* TE QUEMAS,"

    pista += " el número oculto es "

    if numero_oculto > numero:
        pista += "MAYOR... "
    else:
        pista += "MENOR... "

    if intentos > 1:
        pista += f"¡te quedan {intentos} intentos!\n"
    else:
        pista += f"¡te queda {intentos} intento!\n"

    print(f"\n{pista}")


def adivina_el_numero(numero_oculto: int, total_intentos: int, frio: int, caliente: int):
    """Gestiona el proceso de adivinación del número oculto."""
    intentos_realizados = 0
    numero_adivinado = False
    salir = False

    while not salir and total_intentos > 0:
        numero = pedir_numero_usuario("¿Qué número es? ")
        intentos_realizados += 1
        total_intentos -= 1

        if numero != numero_oculto:
            mostrar_pista(numero, numero_oculto, total_intentos, frio, caliente)
        else:
            numero_adivinado = True
            salir = True

    return numero_adivinado, intentos_realizados


def comprobar_numero_entero(valor: str) -> bool:
    """Comprueba si el valor dado es un número entero."""
    if valor.startswith("-"):
        valor = valor[1:]
    return valor.isdigit()


def pedir_numero_usuario(mensaje: str) -> int:
    """Pide al usuario que introduzca un número entero, validándolo."""
    salir = False
    
    while not salir:
        valor = input(mensaje).strip()
        salir = comprobar_numero_entero(valor)
        
        if not salir:
            print("\n*ERROR* Ha introducido un número entero no válido!")

    return int(valor)


def configurar_rangos_numeros() -> tuple:
    """Configura el rango de números válidos para el juego."""
    salir = False

    while not salir:
        minimo = pedir_numero_usuario("Introduce el mínimo número posible: ")
        maximo = pedir_numero_usuario("Introduce el máximo número posible: ")
        
        salir = (minimo < maximo) and ((maximo - minimo) >= 100)

        if not salir:
            print("\n*ERROR* Debe haber por lo menos 100 números de diferencia entre ellos...")

    return minimo, maximo


def configurar_pistas(minimo: int, maximo: int) -> tuple:
    """Configura los valores de frío y caliente para las pistas."""
    salir = False

    while not salir:
        frio = pedir_numero_usuario("Introduce la diferencia para mostrar la pista FRÍO, FRÍO: ")
        caliente = pedir_numero_usuario("Introduce la diferencia para mostrar la pista CALIENTE, CALIENTE: ")
        
        salir = (frio > caliente) and (minimo <= frio <= maximo) and (minimo <= caliente <= maximo)

        if not salir:
            print(f"\n*ERROR* Deben estar dentro del rango ({minimo}.{maximo}) y no ser iguales...")

    return frio, caliente


def configurar_intentos() -> int:
    """Configura el número de intentos para adivinar el número oculto."""
    salir = False

    while not salir:
        intentos = pedir_numero_usuario("Introduce el número de intentos: ")
        salir = intentos > 0
        if not salir:
            print("\n*ERROR* El número de intentos debe ser un entero positivo...")

    return intentos

def configurar_juego() -> tuple:
    """Configura todos los parámetros del juego: rango, pistas e intentos."""
    limpiar_pantalla()
    print("--- CONFIGURA EL JUEGO DE ADIVINA EL NÚMERO OCULTO ---\n\n")
    
    minimo, maximo = configurar_rangos_numeros()
    frio, caliente = configurar_pistas(minimo, maximo)
    intentos = configurar_intentos()

    return minimo, maximo, intentos, frio, caliente


def mostrar_configuracion(minimo, maximo, intentos, frio, caliente):
    """Muestra la configuración actual del juego."""
    limpiar_pantalla()
    print(f"--- CONFIGURACIÓN ACTUAL DE ADIVINA EL NÚMERO OCULTO ---\n\n")
    print(f"* El número oculto será un número entre {minimo} y {maximo}.")
    print(f"* El número de intentos es {intentos}.")
    print(f"* Pista FRÍO si la diferencia es mayor a {frio}.")
    print(f"* Pista CALIENTE si la diferencia es mayor a {caliente}.")
    print(f"* Pista TE QUEMAS si la diferencia es menor.")
    pausa()


def mostrar_menu():
    """Muestra el menú principal."""
    limpiar_pantalla()
    print(f"--- MENÚ DE ADIVINA EL NÚMERO OCULTO ---\n\n")
    print("1. Jugar.")
    print("2. Configurar.")
    print("3. Mostrar configuración.")
    print("4. Salir.\n")


def comprobar_opcion(opcion: int) -> bool:
    """Comprueba si la opción elegida está en el rango permitido."""
    return 1 <= opcion <= 4


def elegir_opcion_menu() -> int:
    """Permite al usuario elegir una opción del menú."""
    mostrar_menu()
    opcion = pedir_numero_usuario("Elije => ")

    while not comprobar_opcion(opcion):
        print(f"\n*ERROR* Opción {opcion} incorrecta! (1-4)")
        opcion = pedir_numero_usuario("Elije => ")

    return opcion


def jugar(numero_oculto, intentos, frio, caliente):
    """Gestiona el proceso de juego y muestra los resultados."""
    limpiar_pantalla()
    print(f"--- ADIVINA EL NÚMERO OCULTO EN {intentos} INTENTOS ---\n\n")
    numero_adivinado, intentos_realizados = adivina_el_numero(numero_oculto, intentos, frio, caliente)

    if numero_adivinado:
        print(f"\n¡Bravo! ¡Lo conseguiste en {intentos_realizados} intentos!")
    else:
        print(f"\nGAME OVER - ¡Otra vez será! (#{numero_oculto}#)")
    
    pausa()


def genera_numero_oculto(minimo: int, maximo: int) -> int:
    """Genera un número oculto aleatorio dentro de un rango."""
    return random.randint(minimo, maximo)
    

def main():
    """Función principal del juego."""
    limpiar_pantalla()
    print("--- BIENVENIDOS AL JUEGO DE ADIVINAR EL NÚMERO OCULTO ---\n\n")
    time.sleep(2)

    # Configuración inicial por defecto
    minimo = 0
    maximo = 100
    frio = 15
    caliente = 5
    intentos = 5

    salir = False

    while not salir:
        opcion = elegir_opcion_menu()

        if opcion == 1:
            numero_oculto = genera_numero_oculto(minimo, maximo)
            jugar(numero_oculto, intentos, frio, caliente)
        elif opcion == 2:
            minimo, maximo, intentos, frio, caliente = configurar_juego()
        elif opcion == 3:
            mostrar_configuracion(minimo, maximo, intentos, frio, caliente)
        else:
            salir = True

    limpiar_pantalla()
    print("Bye, bye...\n\n")


if __name__ == "__main__":
    main()
