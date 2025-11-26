---
title: "UD 1 - 1.1.1 Pseudocódigo"
description: Pseudocódigo
summary: Un programa informático
authors:
    - Diego Cano
    - Eduardo Fdez
date: 2023-09-20
icon: "material/file-document-outline"
permalink: /prog/unidad1/1.1.1
categories:
    - PROG
tags:
    - Software
---
## 1.1.1. El pseudocódigo

El pseudocódigo es una forma de representar algoritmos de forma que sean fácilmente entendibles por cualquier persona, independientemente de su formación en programación. Se trata de un lenguaje de programación simplificado que utiliza expresiones y estructuras de control propias de la programación estructurada.

### 1. Pseudocódigo. Características

* Lenguaje cercano a un lenguaje de programación cuyo objetivo es el desarrollo de algoritmos fácilmente interpretables por un programador.
* Es independiente del lenguaje de programación en el que vayamos a realizar posteriormente nuestra aplicación.
* Debe utilizar un conjunto limitado de expresiones, pero no existe una sintaxis estandarizada.
* Pueden escribir algoritmos que tengan una solución finita y que comiencen desde un único punto de partida.

### 2. Elementos de un programa en pseudocódigo

A pesar de que no existe una norma rígida que establezca cómo realizar la escritura de programas en pseudocódigo, es recomendable seguir una serie de recomendaciones que permitan transcribir el programa al lenguaje de programación que va a usarse con la mayor facilidad.

A la hora de realizar programas en pseudocódigo, podemos utilizar los siguientes elementos:

* Inicio
* Fin
* Escribe "un texto a escribir"
* Lee X
* Si (condición) entonces
* Si (condición) entonces ... Sino ....
* Según (valor) entonces ... opcion1: ... opcion2: ...
* Mientras (condición) hacer ....
* Para X en (1...N) hacer ....
* Operadores matemáticos básicos: +, -, *, /, // y % (módulo).
* Operadores relacionales: == (igual), >, <, >=, <= y != (distinto).
* Operadores lógicos: and, or y not (negación).
* La asignación de valores a una variable la realizaremos con el símbolo =

#### 2.1. Inicio y Fin

Todo algoritmo va a empezar por un paso o instrucción  `Inicio` y va a terminar con la palabra reservada `Fin`.

Ejemplo:

```
Inicio
	Escribe “¿Cómo te llamas?”
	Lee nombre
	Escribe “Hola, ” + nombre
Fin
```

#### 2.2. Variables

* Una variable va a ser básicamente un contenedor de información al que le vamos a asignar un nombre en minúsculas.
* Podrá contener los siguientes tipos de datos: Cadena de caracteres (se representa con comillas dobles `"Una cadena"`), números (enteros `5`y decimales `5.4`) y valores lógicos (`verdadero`/`falso`).
* Su valor podrá ser modificado a lo largo del algoritmo.
* El tipo de datos que contiene no vamos a especificarlo explícitamente simplemente al asignar un valor, estaremos definiendo de forma implícita su tipo de datos.
* Podemos concatenar el valor de una variable a una cadena de caracteres con el símbolo `+`.
* No será necesario realizar conversiones de tipos de datos para trabajar (ya veréis posteriormente lo necesario que esto es en la programación). Se trata de simplificar al máximo la construcción y manejo de las variables en un algoritmo.

Ejemplo:

```
Inicio
    num1 = 10
    Escribe “Introduce un número: ”
    Lee num2

    suma = num1 + num2
    Escribe “La suma de ” + num1 + “ + “ + num2 + “ es ” + suma

    iva = 0.21
    Escribe “Introduce un precio: ”
    Lee precio

    Escribe “El precio con IVA es ” + (precio * iva)
Fin
```

#### 2.3. Estructuras de control

El pseudocódigo utiliza las estructuras de control propias de la programación estructurada.
  * Estructuras de control secuencial.
  * Estructuras de control condicional.
  * Estructuras de control iterativa.  

Para la construcción de un algoritmo vamos a simplificar estas estructuras lo máximo posible para su mejor entendimiento, ya posteriormente según el lenguaje de programación, veremos todas las opciones que nos proporciona.

##### 2.3.1. Estructuras de control secuencial.

Describen bloques de instrucciones que son ejecutadas en orden de aparición (secuencialmente).
Los bloques pueden estar delimitados por las expresiones `Inicio`-`Fin` o bien estar contenidos en otras estructuras.

```
Inicio
    Instrucción1
    …
    InstrucciónN
Fin
```

##### 2.3.2. Estructuras de control condicional.

La estructura de control condicional,  nos permite ejecutar instrucciones de forma alternativa o selectiva, es decir encauza el flujo de ejecución hacia un bloque de instrucciones u otro en función de la evaluación que se realiza sobre una condición determinada.

El bloque o secuencia de instrucciones que ejecutará debe estar tabulado y acabará cuando esa indentación finalice, es decir, vuelva a encontrar una instrucción a la misma altura de la expresión `Si (condición) entonces`.

Vamos a utilizar: simple, doble, múltiple, anidados.

###### 2.3.2.1 Condicional simple:

Establece un conjunto de instrucciones que se ejecutarán si se cumple una condición que retornará un valor lógico.

Ejemplo:

```
Si (condición) entonces
    Instrucción1
    …
    InstrucciónN
```
###### 2.3.2.2 Condicional doble:

Añade otro bloque de instrucciones que se ejecuta en caso de que no se cumpla la condición.

Ejemplo:

```
Si (condición) entonces
    Instrucción1
    …
    InstrucciónN
Sino
    Instrucción1
    …
    InstrucciónN
```

###### 2.3.2.3 Condicional múltiple:

Permite definir multiple bloques de instrucciones que se ejecutarán en función de la opción que sea verdadera:

```
Según valor_selector entonces 
    opcion1:
        Instrucción1
        …
        InstrucciónI  
    opcion2:
        InstrucciónJ
        …
        InstrucciónN
```

###### 2.3.2.3 Estructuras anidados:

Permite ejecutar diferentes bloques de instrucciones mediante el anidamiento de diferentes estructuras de control, cuyas condiciones son excluyentes.

Ejemplo:

```
Si (condición) entonces
    Instrucciones1
Sino
    Si (condición) entonces
        InstruccionesI
    Sino
        Si (condición) entonces
            InstruccionesJ
        Sino
            InstruccionesN
```

##### 2.3.3. Estructuras de control iterativa.

La estructura de control iterativa permite que un bloque de instrucciones sea ejecutado mientras se cumpla una condición.

Solo vamos a contemplar dos tipos de bucles: `Mientras` y `Para`.

###### 2.3.3.1. Estructura iterativa `Mientras`.

Iteración con salida al principio (Mientras): primero se evalúa la condición y en caso de cumplirse ejecuta el bloque de instrucciones. Las instrucciones contenidas deben actuar sobre los valores usados en la condición para evitar bucles infinitos.

> ![](assets/book.png)
> En algunos lenguajes suele existir otra estructura similar que podrías asemejarse a `Hacer ... Hasta (condición)` en donde primero se ejecutan las instrucciones y antes de proseguir se evalúa la condición, por tanto, siempre se ejecutará el bloque de instrucciones una vez.
    
Ejemplos:
    
```
Mientras (condición) hacer
    Instrucción1
    …
    InstrucciónN
```
    
```
Mientras (cont > 0) hacer
    Escribe cont
    cont = cont - 1
```
    
> ![](assets/rayo.png)
> Actividad: ¿Cuál es el resultado del algoritmo anterior?

###### 2.3.3.2. Estructura iterativa `Para`.

Ejecutará el bloque de instrucciones un número determinado de veces. Hace uso de una variable que irá incrementando o decrementando su valor de uno en uno en función de un rango de valores.

Ejemplos:
    
```
Para i en (1…N) hacer
    Instrucción1
    …
    InstrucciónN
```
```
Para i en (N…0) hacer
    Instrucción1
    …
    InstrucciónN
```
    
```
Inicio
    suma = 0 
    Para i en (1…10) hacer
        suma = suma + 1
    Escribe “La suma de los primeros 10 números enteros es ” + suma
Fin
```

> ![](assets/rayo.png)
> Actividad: ¿Cuál es el resultado del algoritmo anterior?
   
    

> ![](assets/rayo.png)
> Actividad: Realiza un algoritmo que lea dos números y muestre cuál es el mayor.
    
    

```
Inicio
    Lee num1
    Lee num2

    Si (num1 > num2) Entonces
        Escribe num1 + “ es mayor que ” + num2
    Sino
        Escribe num2 + “ es mayor que ” + num1

Fin
```
    
    

> ![](assets/rayo.png)
> Actividad: Muestra la relación entre dos numeros que introduce el usuario.
    
    
```
Inicio
    Lee num1
    Lee num2

    Si (num1 == num2) entonces
        Escribe num1 + “ es igual que ” + num2
    Sino    
        Si (num1 > num2) entonces
            Escribe num1 + “ es mayor que ” + num2
        Sino
            Escribe num2 + “ es mayor que ” + num1

Fin
```
   
    

> ![](assets/rayo.png)
> Actividad: Lee un número, si es mayor que 0 muestra la serie decrementando su valor hasta 0. Por ej:  `7 => 7 6 5 4 3 2 1 0`
    
    
```
Inicio
    Lee num

    Si (num > 0) entonces
        Escribe num + “ => ”
        Mientras (num >= 0) hacer
            Escribe num + “ ”
            num = num - 1
Fin
```
```
Inicio
    Lee num

    Si (num > 0) entonces
        Escribe num + “ => ”
        Para i en (num...0) hacer
            Escribe i + “ ”
Fin
```
    
    

> ![](assets/rayo.png)
> Actividad: Lee un número, si es mayor que 0 muestra la serie decrementando su valor hasta 0. Por ej: `7 => 7, 6, 5, 4, 3, 2, 1, 0`
    
    
```
Inicio
    Lee num

    Si (num > 0) entonces
        Escribe num + “ => ”
        
        Mientras (num >= 0) hacer
            Escribe num
            Si (num != 0) entonces
                Escribe “, ”
            num = num - 1
Fin
```
    
    

> ![](assets/rayo.png)
> Actividad: Lee un número, si es mayor que 0 muestra la serie decrementando su valor hasta 0 *(usa el bucle Para)*. Por ej: `7 => 7, 6, 5, 4, 3, 2, 1, 0`
    
    
```
Inicio
    Lee num

    Si (num > 0) entonces
        Escribe num + “ => ”

        Para i en (num...0) hacer
            Escribe i
            Si (i != 0) entonces
                Escribe “, ”
Fin
```
    
    

> ![](assets/rayo.png)
> Ejercicio 1: Lee un número hasta que el número esté en el rango 1-10
> ``` 
> Introduce un número: 15
> Inténtalo otra vez! (1-10): 0
> Inténtalo otra vez! (1-10): 5
> Correcto!
> ```
    
    

> ![](assets/rayo.png)
> Ejercicio 2: Lee dos números y crea la serie que los une de 1 en 1...
> ``` 
> Introduce un número: 4
> Introduce otro: 8
> 4-5-6-7-8
>
> Introduce un número: 12
> Introduce otro: 3
> 3-4-5-6-7-8-9-10-11-12
> ```
    
    

> ![](assets/rayo.png)
> Ejercicio 3: Lee 3 números y dame los números ordenados de menor a mayor.
> ``` 
> Dame 3 números:
> 14
> 7
> 10
> Tus números son 7 10 14
> ```
