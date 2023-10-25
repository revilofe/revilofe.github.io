''' **Ejercicio 2.2.25**
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
'''

def leeFraseDeUsuario() -> str:
    frase = input("Introduzca una frase:").strip()
    
    while frase == "":
        frase = input("Introduzca una frase:").strip()
    return frase


def idetificaPalabraMasLarga(frase:str) -> str:
    palabras = frase.split(" ")
    palabraMasLarga = palabras[0]
    for palabra in palabras:
        if len(palabra) > len(palabraMasLarga):
            palabraMasLarga = palabra
    return palabraMasLarga

def contarPalabras(frase:str) -> str:
    return len(frase.split(" "))


def generaMensaje(palabraMasLarga, numeroPalabras):
    return "La palabra más larga es "+palabraMasLarga+" y hay "+str(numeroPalabras)+" palabras"

if __name__ == "__main__":
    # Entrada: El usuario ingresa una frase
    frase = leeFraseDeUsuario()

    # Proceso: Identicar la palabra más larga y el numero de palabras
    palabraMasLarga = identificarPalabraMasLarga(frase)
    numeroPalabras = contarPalabras(frase)

    mensaje = generaMensaje(palabraMasLarga, numeroPalabras)

    # Salida: Informar de la primera palabra más larga y cuantas palabras había
    print(mensaje)

