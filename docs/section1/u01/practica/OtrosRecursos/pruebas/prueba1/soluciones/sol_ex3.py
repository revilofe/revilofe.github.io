"""
Escribe un programa en Python que lea una palabra y la encripte:

    1. Pedir la palabra hasta que cumpla que tiene un mínimo de 8 letras.
    
    2. Después, transformar o encriptar la palabra de la siguiente manera:
        - Sin bucles, pero escribiendo varias instrucciones si lo necesitáis.
        - Eliminar espacios.
        - Consonantes a mayúsculas
        - La vocal a pasa a ser una @.
        - La vocal e pasa a ser un 3.
        - La vocal i pasa a ser un 1.
        - El resto de vocales serán minúsculas.
        - Si tiene solo 8 letras, añade un * al principio y un # al final.

    3. Ejemplos:

    > Introduzca una palabra: Pedro PAblO    1984
    > Su palabra encriptada es P3DRoP@BLo1984

    > Introduzca una palabra: ArIADNa2
    > Su palabra encriptada es *@R1@DN@2#

    > Introduzca una palabra: USER       89
    > Introduzca una palabra *mínimo 8 letras*: USER  893465
    > Su palabra encriptada es uS3R893465

"""

palabra = input("Introduzca una palabra: ").replace(" ", "")
while (len(palabra) < 8):
    palabra = input("Introduzca una palabra *mínimo 8 letras*: ").replace(" ", "")

palabra = palabra.upper()
palabra = palabra.replace("A", "@")
palabra = palabra.replace("E", "3")
palabra = palabra.replace("I", "1")
palabra = palabra.replace("O", "o")
palabra = palabra.replace("U", "u")

if (len(palabra) == 8):
    palabra = "*" + palabra + "#"

print("Su palabra encriptada es " + palabra)