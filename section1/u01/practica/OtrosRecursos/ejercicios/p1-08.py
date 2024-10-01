"""
P1.8 - Programa en Python los siguientes algoritmos

    Añade a la carpeta de ejercicios de la U1 de tu repositorio las siguientes tareas:

    Pasa los algoritmos que tienes en el fichero adjunto a un programa de Python.
    Incluye los ejercicios separados en la carpeta ejerciciosU1 de tu repositorio de GitHub.

    IMPORTANTE: Debes realizar la entrega de esta tarea. Para ello añade de nuevo la dirección HTTPS de tu repo de GitHub.

"""
#
# Ejercicio 1.31 - Lee un número hasta que el número esté en el rango 1-10
#
"""
> Introduce un número: 15
> Inténtalo otra vez! (1-10): 0
> Inténtalo otra vez! (1-10): 5
> Correcto!

Inicio

	Escribe "Introduce un número: "
	Lee num
	
	Mientras (num < 1 or num > 10)
		Escribe "Inténtalo otra vez! (1-10): "
		Lee num
	Escribe "Correcto!"
	
Fin
"""
#
# Ejercicio 1.32 - Lee dos números y crea la serie que los une de 1 en 1...
#
"""
> Introduce un número: 4
> Introduce otro: 8
> 4-5-6-7-8

> Introduce un número: 12
> Introduce otro: 3
> 3-4-5-6-7-8-9-10-11-12

Inicio

	Escribe "Introduce un número: "
	Lee x
	Escribe "Introduce otro: "
	Lee y
	
	Si (x >= y) entonces
		numIni = x
		numFin = y
	Sino
		numIni = y
		numFin = x
		
	Mientras (numIni <= numFin) hacer
		Escribe numIni
		Si (numIni != numFin) entonces
			Escribe "-"
                numIni = numIni + 1

Fin
"""
#
# Ejercicio 1.33 - Lee 3 números y dame los números ordenados de menor a mayor.
#
"""
> Dame 3 números:
> 14
> 7
> 10
> Tus números son 7 10 14

Inicio

	Escribe "Dame 3 números: "
	Lee n1
	Lee n2
	Lee n3
	
	Si (n1 < n2 and n1 < n3) entonces
		Si (n2 < n3) entonces
			Escribe n1 + " " + n2 + " " + n3
		Sino
			Escribe n1 + " " + n3 + " " + n2
	Sino
		Si (n2 < n1 and n2 < n3) entonces
			Si (n1 < n3) entonces
				Escribe n2 + " " + n1 + " " + n3
			Sino
				Escribe n2 + " " + n3 + " " + n1
		Sino
			Si (n3 < n1 and n3 < n2) entonces
				Si (n1 < n2) entonces
					Escribe n3 + " " + n1 + " " + n2
				Sino
					Escribe n3 + " " + n2 + " " + n1

Fin
"""
#
# Ejercicio 1.34 - Crea un algoritmo que asigne a una variable el número 3 y después pida un número. Debéis mostrar una serie de 3 en 3 tantos números cómo se hayan leído.
#
"""
> Dime cuantos números debe tener la serie: 6
> 3 6 9 12 15 18
	
Inicio

	num = 3
	
	Escribe "Dime cuantos números debe tener la serie: "
	Lee total

	cont = 1
	Mientras (cont <= total) hacer
		Escribe num
		Si (cont < total) entonces
			Escribe " "
		num = num + 3
		cont = cont + 1
		
Fin
"""
#	
# Ejercicio 1.35 - Pide dos números. Después pide un tercer número del 1 al 4, dependiendo de este número el algoritmo debe hacer lo siguiente:
#	
#	- Si no es un número correcto, escribir un mensaje de error.
#	- Si es un 1, escribir la suma de los dos primeros números.
#	- Si es un 2, escribir la resta de los dos primeros números.
#	- Si es un 3, escribir la multiplicación de los dos primeros números.
#	- Si es un 4, escribir la división de los dos primeros números, siempre que el segundo no sea un 0. Si el segundo número es un 0 escribe un mensaje de error "división por cero no es posible".
"""
> Introduce dos números:
> 5
> 7
> Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): 3
> 5 * 7 = 35

> Introduce dos números:
> 8
> 0
> Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): 4
> La división por cero no es posible

Inicio

	Escribe "Introduce dos números: "
	Lee n1
	Lee n2
	
	opcion = 0
	Mientras (opcion < 1 or opcion > 4) hacer
		Escribe "Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): "
		Lee opcion
		Si (opcion < 1 or opcion > 4) entonces
			Escribe "Error - No es una opción correcta (1-4)"
	
	Segun (opcion) entonces
		1:
			Escribe n1 + " + " + n2 + " = " + (n1+n2)
		2:
			Escribe n1 + " - " + n2 + " = " + (n1-n2)
		3:
			Escribe n1 + " * " + n2 + " = " + (n1*n2)
		4:
			Si (n2 == 0) entonces
				Escribe "La división por cero no es posible"
			Sino
				Escribe n1 + " / " + n2 + " = " + (n1/n2)
	
Fin
"""
#	
# Ejercicio 1.36 - Calcula la media de las notas de un curso.
# Píde el número de notas que va a introducir al principio.
# El número de notas no puede ser un número superior a 100, o inferior a 1.
# Si no introduce un número de notas correcto escribimos el mensaje "Error - el número de notas debe ser un número entero entre 1 y 100"
#
"""
> ¿Cuántas notas vas a introducir? 0
> Error - el número de notas debe ser un número entero entre 1 y 100
> ¿Cuántas notas vas a introducir? 187
> Error - el número de notas debe ser un número entero entre 1 y 100
> ¿Cuántas notas vas a introducir? 3
> Dame las 3 notas del curso:
> 9
> 7.5
> 10
> La media es 8.83
	
Inicio

	Escribe "¿Cuántas notas vas a introducir? "
	Lee total
	
	Mientras (total < 1 o total > 100) hacer
		Escribe "Error - el número de notas debe ser un número entero entre 1 y 100"
		Escribe "¿Cuántas notas vas a introducir? "
		Lee total

	Escribe "Dame las " + total + " notas del curso: "
	
	media = 0
	cont = 1
	Mientras (cont <= 10) hacer
		Lee nota
		media = media + nota
		cont = cont + 1

	media = media / total
	Escribe "La media es " + media
	
Fin
"""