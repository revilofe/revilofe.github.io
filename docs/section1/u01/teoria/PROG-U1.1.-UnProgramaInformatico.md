---
title: "UD 1 - 1.1 Un programa informático"
description: Un programa informático
summary: Un programa informático
authors:
    - Eduardo Fdez
date: 2022-09-18
icon: material/sofware
permalink: /prog/unidad1/1.1
categories:
    - PROG
tags:
    - Software
    
---

## La programación
* [Definición](https://es.wikipedia.org/wiki/Programaci%C3%B3n): Es el **proceso** por el cual se desarrolla un **programa**, haciendo uso de herramientas como un **lenguajes de programación** y de otra que sea capaz de “traducirlo” a lo que se conoce como lenguaje de máquina, que puede "comprender" el microprocesador.
* **Ciclo de vida**: Entender el problema, recopilar requisitos, Planificar, Diseñar, Programar, Probar, Desplegar, Mantener.

![](assets/PROG-U1-CicloVida.png)

## Ordenador 
* **Máquina** electrónica, analógica o digital, dotada de una memoria de gran capacidad y de métodos de tratamiento de la información, capaz de resolver problemas matemáticos y lógicos mediante la utilización de programas informáticos.
* Un ordenador **ejecuta programas**, que son un conjunto de instrucciones representadas mediante un lenguaje de programación y datos que se ejecutan de forma secuencial y que a partir de unos datos de entrada producen una salida. Para ejecutar esos programas el ordenador sigue esta estructura básica:

![](assets/PROG-U1-VonNeuman.png)

## ¿Qué es un programa o software?
El *software*, por su parte, de acuerdo con el IEEE: “es el conjunto de los programas de cómputo, procedimientos, reglas, documentación y datos asociados, que forman parte de las operaciones de un sistema de computación”.

Dicho en otras palabras, son todos los programas o aplicaciones que integran un dispositivo y que le permiten realizar tareas específicas gracias al lenguaje de programación.

El *software* le da instrucciones al hardware de la forma como debe realizar una tarea, por esta razón, todos los programas que usamos en un dispositivo son software, por ejemplo:

* Navegador web como Google Chrome o Mozilla Firefox.
* Sistemas operativos como Windows, Mac OS, Linux, entre otros.
* Antivirus.
* Aplicaciones de ofimática como Microsoft Word.
* Sistemas empresariales como un BPMS, ERP, CRM, entre otros.

#### Tipos de software
* **De sistema** (Sistema operativo, drivers -controladores-)
* **De aplicación** (Suite ofimática, Navegador, Edición de imagen, ...)
* **De desarrollo** (Editores, compiladores, interpretes, ...)

> Los drivers son los controladores de dispositivos.


## Relación Hardware-Software
La relación entre el *software* y el *hardware* se pueden describir de la siguiente forma:
* **Disco duro**: almacena de forma permanente los archivos ejecutables y los archivos de datos.  
* **Memoria RAM**: almacena de forma temporal el código binario de los archivos ejecutables y los archivos de datos necesarios. 
* **CPU**: lee y ejecuta instrucciones almacenadas en memoria RAM, así como los datos necesarios. 
* **E/S**: recoge nuevos datos desde la entrada, se muestran los resultados, se leen/guardan a disco. 

El disco duro se considera un periférico de E/S (Entrada/Salida).

La CPU se llama también UCP (en inglés), procesador o microprocesador.

## Algoritmos
Como decíamos, la programación es el proceso que se utiliza para la creación de programas que se ejecutan en dispositivos con capacidad de cómputo. Estos programas son creados para satisfacer unas necesidades o resolver problemas.

Para que este proceso sea exitoso, se ha de analizar el problema que se quiere satisfacer y describir cada paso que se va a realizar, es decir, se ha de diseñar el algoritmo (secuencia de pasos) que se va a seguir para llegar a la solución.

**Algoritmo**: En términos de programación, un algoritmo es una secuencia de pasos lógicos que permiten solucionar un problema.

Una vez se tenga el algoritmo, se podrá pasar a su codificación traduciendo el algoritmo a un lenguaje de programación y por último se generará el programa que se ejecutará en el ordenador para poder depurarse antes de darlo por finalizado.
![](assets/PROG-U1-CicloAlgoritmo.png)


### Características de los algoritmos

Las algoritmos son independientes del lenguaje en el que se implementan y del dispositivo en el que se ejecutan.
Según Joyanes en su libro “Fundamentos de la programación”, las características que debe tener cualquier algoritmo son: 
* **Preciso**: se debe indicar el orden de realización de cada paso 
* **Definido**: si se sigue un algoritmo dos veces con las mismas entradas, se debe obtener el mismo resultado. 
* **Finito**: todo algoritmo debe terminar en algún momento.

### Ejemplo de algoritmo

El **pseudocódigo** se puede considerar como un lenguaje intermedio entre el lenguaje humano y el lenguaje de programación y las palabras reservadas de este. También permite la representación de las estructuras de control y la asignación de manera muy fácil.

Supongamos que queremos resolver un problema, sobre como realizar el mantenimiento de una lámpara.


```  

Si la lampara funciona entonces
    fin. # (1)
Si no
    Si la lampara NO está enchufada entonces
        Enchufarla.
    Si el foco está quemado entonces
        Reemplazar el foco.
    Si sigue sin funcionar entonces
        Comprar nueva lámpara.
fin. # (1)      

``` 

1.  :man_raising_hand: Con la palabra `fin`, __finaliza__ el programa.

Los **diagramas de flujo** son representaciones gráficas de la secuencia de operaciones que se realizan dentro de un algoritmo.
Se representan mediante un conjunto de formas unidas por flechas. Para indicar el inicio del diagrama, se representa en un óvalo la palabra “inicio”. Una secuencia de operaciones se representan mediante una secuencia (lo más detallada posible) de rectángulos de arriba-abajo o derecha-izquierda. Un rombo representa una operación condicional con dos posibles caminos a seguir.


![](assets/PROG-U1-DiagramaFlujo.png)

## Lenguajes de programación
- [TIOBE](https://www.tiobe.com/tiobe-index/)
- [Encuesta stackoverflow](https://insights.stackoverflow.com/survey/2021#overview)
- ¿Que lenguajes de programación conoces?
- ¿Tienes alguna preferencia?
- ¿Cuál crees que se adapta mejor a:
    * [multiplataforma](https://kotlinlang.org/docs/mpp-intro.html)?
    * [desarrollo web](https://keepcoding.io/blog/lenguajes-desarrollo-web/)?