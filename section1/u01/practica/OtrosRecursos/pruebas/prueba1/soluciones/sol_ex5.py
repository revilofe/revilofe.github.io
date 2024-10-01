"""
Crea un algoritmo en pseudocódigo y pásalo también a un programa en Python que pida los días totales trabajados en la vida laboral y te transforme esos días a años, meses y días.

Para este programa vamos a considerar que todos los años tienen 360 días y todos los meses 30 días.

Debe cumplir lo siguiente:

- La palabra año, mes y día irá en plural o singular dependiendo de su cantidad.

- No puede introducir un valor negativo para los días. Si lo hace, debéis dar un mensaje de error y volver a pedir los días trabajados hasta que introduzca un número positivo (el 0 también es válido).

Ejemplo 1:

> Introduzca los días trabajados: 1347
> Ha cotizado 3 años, 8 meses y 27 días.

Ejemplo 2:

> Introduzca los días trabajados: 31
> Ha cotizado 0 años, 1 mes y 1 día.

Ejemplo 3:

> Introduzca los días trabajados: -230
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: -33
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: 0
> Ha cotizado 0 años, 0 meses y 0 días.


Inicio

    Escribe "Introduzca los días trabajados:"
    Lee dias
    
    Mientras (dias < 0) hacer
        Escribe "*** Error - el valor no puede ser negativo ***"
        Escribe "Introduzca los días trabajados:"
        Lee dias
    
    annios = dias // 365
    dias = dias % 365

    meses = dias // 30
    dias = dias % 30

    resultado = "Ha cotizado " + annios

    Si (annios != 1) entonces
        resultado = resultado + " años, " + meses
    Sino
        resultado = resultado + " año, " + meses

    Si (meses != 1) entonces
        resultado = resultado + " meses y " + dias
    Sino
        resultado = resultado + " mes y " + dias

    Si (dias != 1) entonces
        resultado = resultado + " días."
    Sino
        resultado = resultado + " día."    

    Escribe resultado

Fin
"""

dias = int(input("Introduzca los días trabajados: "))

while (dias < 0):
    print("*** Error - el valor no puede ser negativo ***")
    dias = int(input("Introduzca los días trabajados: "))

annios = dias // 365
dias = dias % 365

meses = dias // 30
dias = dias % 30

resultado = "Ha cotizado " + str(annios)

if annios != 1:
    resultado += " años, " + str(meses)
else:
    resultado += " año, " + str(meses)

if meses != 1:
    resultado += " meses y " + str(dias)
else:
    resultado += " mes y " + str(dias)

if dias != 1:
    resultado += " días."
else:
    resultado += " día."

print(resultado)
