---
title: "UD 1 - Introducción al desarrollo de software"
description: Introducción al desarrollo de software
summary: Introducción al desarrollo de software
authors:
    - Eduardo Fdez
date: 2022-09-17
icon: 
permalink: /edes/unidad1
categories:
    - EDES
tags:
    - EDES
    - Software

# Relacionado con la tabla de contenidos
toc: true
toc_label: "Contenido"
toc_icon: "file-code"

#hide:
#  - footer

# Enlace en el que trabajar:
# https://revilofe.notion.site/Unidad-1-Fundamentos-del-Desarrollo-de-Software-Elementos-Herramientas-y-Lenguajes-e21494c5b49f478c8167ce2c08e9ceda?pvs=4

---

## **Unidad 1: Introducción al Desarrollo de Software**

### 1. Normativa que Respalda la Unidad

Esta unidad está alineada con la normativa del curso **"Entornos de Desarrollo"** del ciclo formativo de **Desarrollo de Aplicaciones Web**, teniendo como base el **Resultado de Aprendizaje (RA) 1** y sus **Criterios de Evaluación (CE)**. El objetivo principal es que los estudiantes reconozcan y comprendan los elementos y herramientas esenciales que intervienen en el desarrollo de software, desde la planificación hasta la puesta en funcionamiento.

---

### 2. Resultado de Aprendizaje a Trabajar

- **RA 1**: **Reconoce los elementos y herramientas que intervienen en el desarrollo de un programa informático**, analizando sus características y las fases en las que actúan hasta llegar a su puesta en funcionamiento.

  Este resultado de aprendizaje se logrará desglosando el contenido en cinco puntos, cada uno enfocado en un criterio de evaluación específico.

---

### 3. Criterios de Evaluación

En esta unidad se trabajarán los siguientes **criterios de evaluación** relacionados con el **RA 1**:

1. **CE 1.a**: **Se ha reconocido la relación de los programas con los componentes del sistema informático**, como la memoria, procesador, periféricos, entre otros.

    - **Contenido asociado**: Relación entre software y hardware. Cómo interactúan los componentes físicos del ordenador (memoria RAM, procesador, dispositivos de entrada/salida) con el software durante la ejecución de programas.

2. **CE 1.c**: **Se han diferenciado los conceptos de código fuente, objeto y ejecutable**.

    - **Contenido asociado**: Explicación detallada sobre cómo el código fuente se transforma en un archivo ejecutable, incluyendo la etapa intermedia de generación de código objeto. Se abordarán ejemplos prácticos con compiladores y su salida generada.

3. **CE 1.d**: **Se han reconocido las características de la generación de código intermedio para su ejecución en máquinas virtuales**.

    - **Contenido asociado**: Análisis de cómo se genera el código intermedio (por ejemplo, bytecode en Java) y su ejecución en máquinas virtuales como la JVM. Comparación entre código intermedio y código ejecutable tradicional.

4. **CE 1.e**: **Se han clasificado los lenguajes de programación, identificando sus características**.

    - **Contenido asociado**: Clasificación de los lenguajes en compilados vs interpretados, alto nivel vs bajo nivel y paradigmas de programación. Análisis de características y ejemplos de lenguajes como Python, Java, C y Assembly.

5. **CE 1.f**: **Se ha evaluado la funcionalidad ofrecida por las herramientas utilizadas en el desarrollo de software**.

    - **Contenido asociado**: Evaluación de herramientas específicas como editores de texto, compiladores, intérpretes, sistemas de control de versiones, depuradores y frameworks. Se discutirán las ventajas y desventajas de cada herramienta según su funcionalidad.

---

### 4. Contenidos

En esta sección se describen los contenidos que se impartirán en la Unidad 1, teniendo en cuenta la normativa del curso y los criterios de evaluación.

- La unidad pertenece al **Bloque 1: Desarrollo de Software**.

**U1: Introducción al Desarrollo de Software**

Durante la **Unidad 1**, trabajaremos los siguientes contenidos:

1. **Relación entre el Software y el Hardware** (CE 1.a):
    - Análisis de cómo el software interactúa con los componentes físicos del sistema, como el procesador, la memoria y los periféricos.
    - Ejemplos prácticos de cómo se ejecuta un programa en la CPU y cómo se almacenan los datos en la RAM.

2. **Diferenciación entre Código Fuente, Código Objeto y Ejecutable** (CE 1.c):
    - Definición de cada concepto y ejemplos de cómo se realiza la compilación de un programa en C.
    - Análisis de la estructura del código objeto y el ejecutable generado por el compilador.

3. **Generación de Código Intermedio para Máquinas Virtuales** (CE 1.d):
    - Explicación de cómo lenguajes como Java generan bytecode que se ejecuta en una máquina virtual.
    - Comparativa de rendimiento y portabilidad entre código intermedio y ejecutable tradicional.

4. **Clasificación y Características de los Lenguajes de Programación** (CE 1.e):
    - Clasificación de los lenguajes de programación en función de su nivel de abstracción (alto nivel vs bajo nivel), paradigma (imperativo, funcional, orientado a objetos) y modo de ejecución (compilado vs interpretado).
    - Ejemplos prácticos de lenguajes representativos como Python, C, Java y Assembly.

5. **Evaluación de Herramientas Utilizadas en el Desarrollo de Software** (CE 1.f):
    - Evaluación de herramientas utilizadas en el desarrollo de software como editores de texto (Sublime Text), compiladores (GCC), intérpretes (Python), herramientas de documentación (JSDoc, Doxygen), depuradores (GDB, PDB), sistemas de control de versiones (Git), frameworks (Django, Spring), y herramientas de pruebas y calidad (SonarQube, JUnit).
    - Discusión sobre las ventajas y desventajas de cada herramienta según el contexto de uso y el tipo de proyecto.

---

### 5. Actividades de Evaluación

Para evaluar la adquisición de los criterios de evaluación, se propondrán las siguientes **actividades**:

1. **Actividad 1: Relación entre Software y Hardware (CE 1.a)**.
    - **Descripción**: Simulación del ciclo de ejecución en el hardware y análisis de cómo interactúa con el software.
    - **Objetivo**: Identificar cómo el software se comunica con el hardware durante la ejecución y cómo se gestionan las operaciones de entrada/salida.

2. **Actividad 2: Diferenciación entre Código Fuente, Objeto y Ejecutable (CE 1.c)**.
    - **Descripción**: Compilación de un programa sencillo en C para observar cada etapa del proceso y comparar los resultados generados.
    - **Objetivo**: Analizar la transformación del código fuente en código objeto y, finalmente, en un ejecutable.

3. **Actividad 3: Generación de Código Intermedio para Máquinas Virtuales (CE 1.d)**.
    - **Descripción**: Creación y ejecución de un programa en Java, analizando la generación de bytecode y su ejecución en la JVM.
    - **Objetivo**: Entender cómo se ejecuta el código intermedio en una máquina virtual y su independencia de la plataforma.

4. **Actividad 4: Clasificación de Lenguajes de Programación (CE 1.e)**.
    - **Descripción**: Clasificación y comparación de diferentes lenguajes de programación (Python, C, Java, Assembly) y sus características principales.
    - **Objetivo**: Identificar en qué contextos y proyectos se utilizaría cada tipo de lenguaje según su clasificación y características.

5. **Actividad 5: Evaluación de Herramientas de Desarrollo (CE 1.f)**.
    - **Descripción**: Evaluación y comparación de herramientas de desarrollo (compiladores, intérpretes, sistemas de gestión de versiones, etc.). Los estudiantes crearán una tabla comparativa con ventajas y desventajas.
    - **Objetivo**: Comprender el uso de cada herramienta en el ciclo de desarrollo del software y su aplicación práctica.

---

### 6. Prueba de Evaluación de Contenidos

Al final de la unidad, se realizará una pruebas  incluirán preguntas teóricas y prácticas sobre los conceptos tratados. Los estudiantes deberán demostrar su comprensión de:

- La relación entre software y hardware.
- La diferenciación entre tipos de código.
- La clasificación de lenguajes de programación.
- La funcionalidad de las herramientas utilizadas en el desarrollo de software.

---

Con este enfoque, se abordan claramente los **RA** y **CE** específicos para cada punto tratado en la unidad, y se detallan las actividades que permitirán evaluar su adquisición de manera práctica.
