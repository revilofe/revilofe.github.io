---
title: "UD 2 - 2.5 Ejecutables en IDEs"
description: Ejecutables en IDEs
summary: Ejecutables en IDEs
authors:
    - Eduardo Fdez
date: 2024-10-21
icon: "material/file-document-outline"
permalink: /edes/unidad2/2.5
categories:
    - EDES
tags:
    - EDES
    - IDE
    - Actualizacion
---

## 2.5. Ejecutables en IDEs

La generación de **ejecutables** es una tarea fundamental en el desarrollo de software, ya que permite distribuir aplicaciones de manera sencilla y eficiente. En este punto, veremos cómo generar ejecutables en distintos lenguajes de programación en varios entornos de desarrollo integrado (IDE)

### 1. Introducción
En esta sección, aprenderemos cómo generar ejecutables a partir del código fuente en diferentes lenguajes y entornos de desarrollo. Veremos cómo utilizar **IntelliJ IDEA** para ejecutar un mismo programa en **Kotlin** y **Java**, y cómo ejecutar el mismo código en **Python** utilizando **PyCharm** y **Visual Studio Code**. Esto te permitirá comprender cómo generar y ejecutar programas en distintos lenguajes y en varios entornos de desarrollo.

Este punto es totalmente práctico y te permitirá experimentar con la generación de ejecutables en distintos lenguajes y entornos, lo que te ayudará a comprender cómo manejar proyectos en múltiples lenguajes y entornos de desarrollo.

### 2. Generación de ejecutables a partir de código fuente en distintos lenguajes en un mismo IDE (CE 2.e)

#### 2.1. Descripción de la actividad
Vamos a crear un programa sencillo en **Kotlin** y **Java** que cuenta del 10 al 0 y luego imprime "¡Despegue!". Lo ejecutaremos dentro del mismo IDE, en este caso **IntelliJ IDEA**, para demostrar cómo podemos manejar varios lenguajes en un mismo entorno.

#### 2.2. Crear y ejecutar el programa en **Kotlin** en IntelliJ IDEA
1. **Crear un proyecto en Kotlin**:
      - Abre **IntelliJ IDEA** y selecciona `File > New > Project`.
      - Elige **Kotlin** como lenguaje y asegúrate de tener seleccionado **JVM** (Java Virtual Machine).
      - Asigna un nombre al proyecto, por ejemplo, "CuentaAtrasKotlin".

2. **Escribir el código en Kotlin**:
      - Dentro del proyecto, crea un archivo llamado `Main.kt` y añade el siguiente código:
      ```kotlin
      fun main() {
          for (i in 10 downTo 0) {
              println(i)
          }
          println("¡Despegue!")
      }
      ```
      - Este programa utiliza un bucle que cuenta del 10 al 0 e imprime "¡Despegue!" al final.

3. **Ejecutar el código**:
      - Para ejecutar el código, selecciona el archivo `Main.kt`, haz clic en el botón **Run** en la parte superior o usa el atajo `Shift + F10`.
      - El programa se ejecutará en la consola integrada de IntelliJ IDEA, mostrando la cuenta regresiva seguida de "¡Despegue!".

   **Resultado esperado**:
   ```
   10
   9
   8
   7
   6
   5
   4
   3
   2
   1
   0
   ¡Despegue!
   ```

#### 2.3. Crear y ejecutar el programa en **Java** en IntelliJ IDEA
1. **Crear un proyecto en Java**:  
      - En IntelliJ IDEA, selecciona `File > New > Project`.   
      - Esta vez elige **Java** como lenguaje y nombra el proyecto "CuentaAtrasJava".   

2. **Escribir el código en Java**:    
      - Crea un archivo llamado `Main.java` en el proyecto y escribe el siguiente código:
      ```java
      public class Main {
          public static void main(String[] args) {
              for (int i = 10; i >= 0; i--) {
                  System.out.println(i);
              }
              System.out.println("¡Despegue!");
          }
      }
      ```   
      - Este programa hace lo mismo que el de Kotlin, pero utilizando la sintaxis de Java.   

3. **Ejecutar el código**:
      - Selecciona el archivo `Main.java`, haz clic en **Run** o usa el atajo `Shift + F10`.
      - El programa se ejecutará y mostrará la misma salida que el programa en Kotlin.

   **Resultado esperado**:
   ```
   10
   9
   8
   7
   6
   5
   4
   3
   2
   1
   0
   ¡Despegue!
   ```

#### 2.4. Conclusión
Al utilizar **IntelliJ IDEA**, puedes gestionar proyectos en **Kotlin** y **Java** fácilmente en el mismo IDE. Hemos visto cómo crear y ejecutar el mismo programa en ambos lenguajes sin necesidad de cambiar de entorno, lo que facilita el manejo de múltiples lenguajes en un solo lugar.

### 3. Generación de ejecutables con diferentes IDEs a partir del mismo código fuente (CE 2.f)

#### 3.1. Descripción de la actividad
Ahora vamos a escribir un programa en **Python** que cuenta desde 10 hasta 0 y muestra "¡Despegue!". El mismo código se ejecutará en dos IDEs diferentes: **PyCharm** y **Visual Studio Code**. Esto te permitirá comparar cómo funcionan distintos entornos con el mismo código fuente.    

#### 3.2. Crear y ejecutar el programa en **PyCharm** (Python)
1. **Crear un proyecto en PyCharm**:   
      - Abre **PyCharm** y selecciona `File > New Project`.   
      - Asegúrate de que el proyecto esté configurado para usar **Python** como lenguaje y asígnale un nombre, por ejemplo, "CuentaAtrasPython".   

2. **Escribir el código en Python**:
      - Dentro del proyecto, crea un archivo llamado `main.py` y añade el siguiente código:
      ```python
      for i in range(10, -1, -1):
          print(i)
      print("¡Despegue!")
      ```
      - Este código utiliza un bucle `for` que cuenta de 10 a 0 y luego imprime "¡Despegue!".

3. **Ejecutar el código en PyCharm**:
      - Haz clic derecho sobre `main.py` y selecciona **Run 'main'** o usa el atajo `Shift + F10`.
      - El programa se ejecutará en la consola integrada de PyCharm y mostrará la cuenta atrás seguida de "¡Despegue!".

   **Resultado esperado**:
   ```
   10
   9
   8
   7
   6
   5
   4
   3
   2
   1
   0
   ¡Despegue!
   ```

#### 3.3. Crear y ejecutar el programa en **Visual Studio Code** (Python)
1. **Abrir Visual Studio Code y configurar Python**:   
      - Si no lo has hecho ya, instala la extensión de **Python** desde la sección de extensiones (`Ctrl + Shift + X`) buscando "Python" y haciendo clic en **Instalar**.    
      - Abre Visual Studio Code y crea una nueva carpeta de proyecto o abre la carpeta donde está guardado el archivo `main.py`.   

2. **Escribir o abrir el código en Python**:
      - Si no lo tienes aún, crea el archivo `main.py` con el mismo código:   
      ```python
      for i in range(10, -1, -1):
          print(i)
      print("¡Despegue!")
      ```

3. **Ejecutar el código en Visual Studio Code**:
      - Haz clic en el botón de **ejecución** en la esquina superior derecha o usa el atajo `Ctrl + F5`.   
      - El programa se ejecutará en la terminal integrada de Visual Studio Code, mostrando el mismo resultado.   

   **Resultado esperado**:
   ```
   10
   9
   8
   7
   6
   5
   4
   3
   2
   1
   0
   ¡Despegue!
   ```

#### 3.4. Conclusión
Hemos visto cómo el mismo programa en **Python** puede ejecutarse tanto en **PyCharm** como en **Visual Studio Code**, proporcionando los mismos resultados en ambos entornos. Esto demuestra la flexibilidad de los entornos de desarrollo para ejecutar el mismo código fuente, lo que permite a los desarrolladores adaptarse a las preferencias o requisitos del equipo.

#### 4. Conclusión general
En este punto, hemos explorado la generación de ejecutables o la ejecución de código en distintos lenguajes utilizando un mismo IDE, como **IntelliJ IDEA** para **Kotlin** y **Java**, y cómo ejecutar el mismo código Python en diferentes IDEs como **PyCharm** y **Visual Studio Code**. Esto te proporciona una visión clara de cómo gestionar proyectos en múltiples lenguajes y entornos de desarrollo, una habilidad clave para cualquier desarrollador.
