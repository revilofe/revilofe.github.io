---
title: "UD 2 - P2: Iterativas"
summary: Condicionales
description: Condicionales
authors:
    - Eduardo Fdez
date: 2022-09-18
icon: "material/file-document-edit"
permalink: /prog/unidad2/p2.2
categories:
    - PROG
tags:
    - Software
    - Ejercicios

# https://aprendeconalf.es/docencia/python/ejercicios/bucles/
# http://patriciaemiguel.com/ejercicios/python/2019/03/10/ejercicios-buclewhile-python.html
---

> Durante la realización de estos ejercicios, no debes usar ninguna función (método) de las clases para ayudarte a realizarlo. Es decir, evita hacer uso de las funciones `len`, `count` de `str`, etc. La reaización de estas funciones forman parte de la realización del ejercicio.  

## P2.2 - Ejercicios

#### **Ejercicio 2.2.1**
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.


#### **Ejercicio 2.2.2**
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


#### **Ejercicio 2.2.3**
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


#### **Ejercicio 2.2.4**
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.


#### **Ejercicio 2.2.5**
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

```Python
# Formula para calcular El capital tras un año.
amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 
```

#### **Ejercicio 2.2.6**
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
```
*
**
***
****
*****
```


#### **Ejercicio 2.2.7**
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


#### **Ejercicio 2.2.8**
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
```
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
```

#### **Ejercicio 2.2.9**
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


#### **Ejercicio 2.2.10**
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.


#### **Ejercicio 2.2.11**
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.


#### **Ejercicio 2.2.12**
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.


#### **Ejercicio 2.2.13**
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.


#### **Ejercicio 2.2.14**
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.


#### **Ejercicio 2.2.15**
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.


#### **Ejercicio 2.2.16**
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.


#### **Ejercicio 2.2.17**
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.


#### **Ejercicio 2.2.18**
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.


#### **Ejercicio 2.2.19**
Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.


#### **Ejercicio 2.2.20**
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.


#### **Ejercicio 2.2.21**
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.


#### **Ejercicio 2.2.22**
Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.


#### **Ejercicio 2.2.23**
Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.
```
Ejemplo de ejecución:
Libro: Los 3 mosqueteros
Libro: Historia de 2 ciudades
Libro: /
Línea completa. Aparecen 2 dígitos numéricos.
Libro: 20000 leguas de viaje submarino
Libro: El señor de los anillos
Libro: /
Línea completa. Aparecen 5 dígitos numéricos.
Libro: 20 años después
Libro: *
Fin. Se leyeron 2 líneas completas.
```


#### **Ejercicio 2.2.24**
Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.


#### **Ejercicio 2.2.25**
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
