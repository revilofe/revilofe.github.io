
import os
import random
import time


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.
    
    En sistemas Windows utiliza el comando 'cls', en Linux o macOS utiliza 'clear'.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pausa():
    input("\nPresione ENTER para continuar...")
    limpiar_pantalla()


def dame_pista(numero: int, numero_oculto: int, intentos: int, frio: int, caliente: int) -> str:
    pista = "el número oculto es "
    
    if numero_oculto > numero:
        pista += f"MAYOR... ¡te quedan {intentos} intentos!\n"
    else:
        pista += f"MENOR... ¡te quedan {intentos} intentos!\n"

    diferencia = abs(numero_oculto - numero)
    
    if diferencia > frio:
        pista = "\n* FRÍO, FRÍO, " + pista
    elif diferencia > caliente:
        pista = "\n* CALIENTE, CALIENTE, " + pista
    else:
        pista = "\n* TE QUEMAS, " + pista

    return pista


def adivina_el_numero(numero_oculto: int, total_intentos: int, frio: int, caliente: int):
    numero = numero_oculto - 1
    intentos_realizados = 0
    numero_adivinado = False
    salir = False

    while not salir:
        intentos_realizados += 1
        total_intentos -= 1
        numero = introduce_numero_entero(f"¿Qué número es? ")
        if numero != numero_oculto and total_intentos > 0:
            print(dame_pista(numero, numero_oculto, total_intentos, frio, caliente))
        elif numero == numero_oculto:
            numero_adivinado = True
            salir = True
        else:
            salir = True

    return numero_adivinado, intentos_realizados


def comprobar_numero_entero(valor: str) -> bool:
    if valor.startswith("-"):
        valor = valor[1:]
    
    return valor.isdigit()


def introduce_numero_entero(msj: str) -> int:
    valor = input(msj).strip()
    
    while not comprobar_numero_entero(valor):
        print("\n*ERROR* Ha introducido un número entero no válido!")
        valor = input(msj).strip()

    return int(valor)


def genera_numero_oculto(min: int, max: int) -> int:
    return random.randint(min, max)


def configurar_juego():
    limpiar_pantalla()
    print(f"--- CONFIGURA EL JUEGO DE ADIVINA EL NÚMERO OCULTO ---\n\n")
    
    salir = False

    while not salir:
        minimo = introduce_numero_entero("Introduce el mínimo número posible: ")
        maximo = introduce_numero_entero("Introduce el máximo número posible: ")
        if not (minimo < maximo and (maximo - minimo) >= 100):
            print("\n*ERROR* Debe haber por lo menos 100 números de diferencia entre ellos...\n")
        else:
            salir = True

    salir = False
 
    while not salir:
        frio = introduce_numero_entero("Introduce la diferencia para mostrar la pista FRÍO, FRÍO: ")
        caliente = introduce_numero_entero("Introduce la diferencia para mostrar la pista CALIENTE, CALIENTE: ")
        if not (frio > caliente and minimo <= frio <= maximo and minimo <= caliente <= maximo):
            print(f"\n*ERROR* Deben estar dentro del rango ({minimo}.{maximo}) y no ser iguales...\n")
        else:
            salir = True

    intentos = introduce_numero_entero("Introduce el número de intentos: ")

    return minimo, maximo, intentos, frio, caliente


def mostrar_configuracion(minimo, maximo, intentos, frio, caliente):
    limpiar_pantalla()
    print(f"--- CONFIGURACIÓN ACTUAL DE ADIVINA EL NÚMERO OCULTO ---\n\n")
    print(f"* El número oculto será un número entero entre {minimo} y {maximo}.")
    print(f"* El número de intentos posibles son {intentos}.")
    print(f"* La diferencia mayor de {frio}, mostrará la pista FRÍO, FRÍO...")
    print(f"* La diferencia mayor de {caliente}, mostrará la pista CALIENTE, CALIENTE...")
    print(f"* Si la diferencia es menor, mostrará la pista TE QUEMAS...")
    pausa()


def mostrar_menu():
    limpiar_pantalla()
    print(f"--- MENÚ DE ADIVINA EL NÚMERO OCULTO ---\n\n")
    print("1. Jugar.")
    print("2. Configurar.")
    print("3. Mostrar configuración.")
    print("4. Salir.\n")


def elegir_opcion_menu() -> int:
    mostrar_menu()
    salir = False
    while not salir:
        opcion = introduce_numero_entero("Elije => ")

        if not comprobar_opcion(opcion):
            print("\n*ERROR* Opción {opcion} incorrecta! (1-3)")
        else:
            salir = True
    
    return opcion


def comprobar_opcion(opcion: int) -> bool:
    return 1 <= opcion <= 4


def jugar(numero_oculto, intentos, frio, caliente):
    limpiar_pantalla()
    print(f"--- ADIVINA EL NÚMERO OCULTO EN {intentos} INTENTOS ---\n\n")
    numero_adivinado, intentos_realizados = adivina_el_numero(numero_oculto, intentos, frio, caliente)

    if numero_adivinado:
        print(f"\n¡Bravo! ¡Lo conseguiste en {intentos_realizados} intentos!")
    else:
        print(f"\nGAME OVER - ¡Otra vez será! (#{numero_oculto}#)")

    pausa()



def main():
    limpiar_pantalla()
    print("--- BIENVENIDOS AL JUEGO DE ADIVINAR EL NÚMERO OCULTO ---\n\n")
    time.sleep(2)

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
