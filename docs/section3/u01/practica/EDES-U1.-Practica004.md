---
title: "UD 1 - P4: Relación software y hardware"
description: Relación software y hardware
summary: Relación software y hardware
authors:
    - Eduardo Fdez
date: 2022-10-06
icon:   
permalink: /edes/unidad1/p1.4
categories:
    - EDES
tags:
    - Software
---

## P 1.4: Relación software y hardware

### 1. Desarrollo de la Actividad A: Comparativa lenguaje C vs Ensamblador

Para esta actividad se propone una comparativa entre C y Ensamblador y cómo se relacionan con el hardware. :

#### 1. Introducción al uso del simulador      
   * Presenta a los estudiantes la herramienta **TinkerCAD**. En TinkerCAD, pueden crear un circuito simple con un microcontrolador (por ejemplo, un **Arduino**) y observar cómo el código que cargan en el sistema interactúa con el procesador y los periféricos.
   * Explica que cada componente del sistema (procesador, memoria y periféricos) tiene un papel importante en la ejecución de un programa.

#### 2. Primera parte    
Simulación de la relación Software-Hardware con TinkerCAD:
   * Los estudiantes crearán un proyecto en **TinkerCAD** con un circuito que contenga un microcontrolador **Arduino** y algunos componentes adicionales como un **LED** y un **sensor** (botón).    
   * Cargarán un código simple que, por ejemplo, encienda o apague el LED cuando se presiona el botón.     
   * **Ejemplo de código** para Arduino:
          * [Explicación Arduino](https://www.youtube.com/watch?v=hf1LOwpnwEw)     
          * [Ejecutar y compilar un programa](https://www.tinkercad.com/things/ht2v0BF9AuW-encender-y-apagar-un-led-utilizando-un-boton-pulsador-?sharecode=JNLiMzkxWhyTlgjBj3s64i31APyBzvzo4Sf1At2E6to)    
          * Los estudiantes podrán ver cómo el botón (periférico) envía señales al procesador y cómo el **software** (el código cargado) controla el **hardware** (el LED).    
   * Pueden intentar modificar el programa para que encienda el LED cuando se presiona el botón dos veces y lo apague cuando se presione el botón una sola vez.

#### 3. Segunda parte    
Simulación del funcionamiento del procesador con el emulador LC3 Machines:

  * Presenta a los estudiantes el **Emulador LC3**, una herramienta que simula el funcionamiento de un procesador **LC3** (una arquitectura de computadora simple). Se puede usar la [opción 1 ](https://spacetech.github.io/LC3Simulator/) u [opción 2](https://wchargin.com/lc3web/)    
  * Los estudiantes utilizarán el **Emulador LC3** para cargar un programa en código ensamblador o un programa muy básico en una máquina virtual.    
  * Observarán cómo el **software** (en este caso, el código en ensamblador o un programa simple en C) se convierte en **instrucciones** que el procesador ejecuta. 
  * Con el emulador, podrán ver la interacción entre el código, el procesador y la memoria en tiempo real.    

    Ejemplo básico de código ensamblador (LC3):
  
      ```nasm
      .ORIG x3000          
  
      LD R0, NUM1          ; Cargar el valor de NUM1 en R0
      LD R1, NUM2          ; Cargar el valor de NUM2 en R1
      ADD R2, R0, R1       ; Sumar R0 y R1, guardar el resultado en R2
  
      ; Convertir el resultado a ASCII
      LD R3, ASCII_ZERO    ; Cargar el valor ASCII de '0' en R3 (48)
      ADD R0, R2, R3       ; Sumar el valor de R2 al valor ASCII de '0'
  
      ; Mostrar el resultado
      TRAP x21             ; Mostrar el carácter en pantalla
  
      HALT                 ; Finalizar el programa
  
      NUM1    .FILL x0005          ; Primer número (5)
      NUM2    .FILL x0003          ; Segundo número (3)
      ASCII_ZERO .FILL x0030       ; Valor ASCII de '0' (48 en decimal)
  
      .END                 ; Fin del programa
  
      ```
  
    Explicación del código:
  
      1. **LD R3, ASCII_ZERO**: Carga el valor **48** (que es el valor ASCII del carácter **'0'**) en el registro **R3**. Este valor se almacena en la etiqueta **ASCII_ZERO**.
      2. **ADD R0, R2, R3**: Suma el valor de **R2** (resultado de la suma de 5 + 3) con **48** para convertir el número en un carácter ASCII.
      3. *TRAP x21**: Muestra el carácter ASCII resultante en la pantalla (en este caso, el carácter **'8'**).    
  
    Resultado esperado:    
  Al ejecutar este programa, se mostrará el carácter **'8'** en la pantalla, que es el resultado de la suma de **5 + 3**.

#### 4. Conclusión
Los estudiantes finalizarán la actividad conectando lo aprendido a la realidad de los sistemas informáticos actuales. Deberán ser capaces de identificar claramente la **relación entre el software y el hardware**, y cómo las instrucciones del software controlan los diferentes componentes del hardware.

### 2. Desarrollo de la Actividad B: Funcionamiento de una CPU   
Esta actividad se centra en el funcionamiento de un procesador y cómo se relaciona con el software. Se utilizará un simulador   

#### 1. Introducción al Simulador y Explicación del Contexto:
- Antes de comenzar con la simulación, introduce el **Little Man Computer (LMC)** como una metáfora sencilla para explicar cómo funciona una CPU. El **"pequeño hombre"** en la simulación es el procesador, que sigue instrucciones escritas en un formato muy básico y que puede interactuar con un conjunto limitado de recursos: una memoria de números, un buzón para entradas (teclado) y otro para salidas (pantalla o impresora).    
- Explica a los estudiantes que utilizarán este simulador para entender cómo se comunican el **software** (las instrucciones que ellos escribirán) y el **hardware** (la CPU y la memoria). Así podrán ver cómo el procesador toma decisiones, lee datos de la memoria y los devuelve como salida.    

#### 2. Creación de un Programa Simple en LMC    

- Los estudiantes usarán el simulador LMC para escribir un programa simple que sume dos números introducidos por el usuario y muestre el resultado en pantalla. Aqui tienes el acceso al [simulador](https://peterhigginson.co.uk/lmc/?F5=17-Sep-24_17:48:41)      

  **Ejemplo de código en LMC** para sumar dos números:    

    ```nasm
    INP           ; Entrada del primer número
    STA NUM1      ; Guardar el número en la memoria
    INP           ; Entrada del segundo número
    ADD NUM1      ; Sumar el segundo número al primero
    OUT           ; Mostrar el resultado
    HLT           ; Terminar el programa
    NUM1 DAT 0    ; Variable para almacenar el número
    
    ```

#### 3. Ejecución y Análisis del Programa    

- Una vez escrito el programa, los estudiantes lo ejecutarán paso a paso en el simulador. A medida que se ejecute el programa, el simulador mostrará cómo las instrucciones van siendo procesadas por la **CPU** (el pequeño hombre), cómo se almacenan los números en la **memoria** y cómo se realiza la salida.

#### 4. Ampliación: Simulación del Hardware Completo en PCjs Machines

Si deseas una actividad más avanzada para alumnos con mayor comprensión, puedes complementar el uso de LMC con una simulación en **PCjs Machines** (https://www.pcjs.org/). Aquí, los estudiantes pueden cargar un programa en un sistema operativo antiguo, como MS-DOS, y ver cómo el software controla el hardware en una simulación de un ordenador completo.

#### 5. Resultados Esperados   

- Los estudiantes entenderán de forma visual y práctica cómo el software que escriben (instrucciones) interactúa con la CPU (procesador), la memoria y los periféricos (entrada/salida).
- Lograrán ver cómo las operaciones básicas de un procesador se relacionan con las instrucciones del software, lo que facilita la comprensión de cómo los programas controlan el hardware.
- Podrán identificar el rol de cada componente del sistema (procesador, memoria y periféricos) y cómo su correcta interacción es esencial para el funcionamiento del software en cualquier entorno.

