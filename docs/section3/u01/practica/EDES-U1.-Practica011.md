---
title: "UD 1 - P11: Elementos de desarrollo"
description: Elementos de desarrollo
summary: Elementos de desarrollo
authors:
    - Eduardo Fdez
date: 2024-10-07
icon:   
permalink: /edes/unidad1/p1.11
categories:
    - EDES
tags:
    - Software
---

## P 1.11: Elementos de desarrollo

### 1. Objetivo
Evaluar la relación entre **software y hardware**, clasificar lenguajes de programación y comprender los diferentes procesos de ejecución (compilación, interpretación y máquinas virtuales), utilizando ejemplos de lenguajes interpretados, compilados y que generan código intermedio para su ejecución en una máquina virtual.

### 2. Dinámica
- Individual o en grupo. Queda a elección del profesor.
- Cada individuo/grupo deberá trabajar con **tres lenguajes** de programación diferentes:
    - **Lenguajes interpretados** (Python).
    - **Lenguajes compilados** (C).
    - **Lenguajes que generan código intermedio ejecutado en una máquina virtual** (Java).

### 3. Tarea
Escribir un pequeño programa en cada lenguaje y responder a las preguntas en el README.md, usando capturas de pantalla para ilustrar las respuestas y el lenguaje de marcas markdown para formatear el texto.

Deberá escribirse un programa por cada uno de los tres lenguajes elegidos que:

1. Pregunte el nombre del usuario.
2. Pregunte el año de nacimiento. Y obtenga la edad del usuario.
3. Muestre un mensaje que diga: `"Hola [nombre del usuario], tienes [x] años. Este programa está hecho en el lenguaje de programación: [lenguaje]"`.    

---

### 5. Preguntas y Actividades para Evaluar Cada Criterio de Evaluación

Contesta a estas preguntas de forma concisa y clara. Las respuestas deben estar bien estructuradas e ir al grano. Realiza capturas de pantalla para ilustrar tus respuestas.

Las respuestas deberán responderse por cada uno de los lenguajes utilizados (interpretado, compilado y en máquina virtual), siempre que aplique. Si no aplica, indícalo claramente.

#### 5.1. Criterio de Evaluación 1.a: Relación entre Software y Hardware    

**Pregunta**:    

1. Describe cómo el software que has creado se ha relacionado con los componentes físicos del dispositivo (memoria RAM, procesador, periféricos, etc.) durante la ejecución de los tres lenguajes (interpretado, compilado y en máquina virtual).    
     - **Puntos a incluir**:    
         - Cómo se almacenaron los datos en memoria.    
         - Qué hizo el procesador con el código.    
         - Si se interactuó con periféricos, como la pantalla para mostrar la salida.    


#### 5.2. Criterio de Evaluación 1.c: Diferenciación entre Código Fuente, Código Objeto y Ejecutable    

**Preguntas**:    

1. Explica cómo el código fuente que escribiste se transformó en código objeto y ejecutable en el caso de los lenguajes compilados. ¿Generaste archivos intermedios (código objeto)? ¿Qué nombres tomaron estos archivos?    
2. Para los lenguajes interpretados, describe cómo el código fuente se ejecutó directamente, sin generar archivos de código objeto o ejecutable.    
3. Para el lenguaje que genera código intermedio (Java, C#), explica cómo el código fuente se transformó en código intermedio (bytecode) y cómo este fue ejecutado por la máquina virtual.    


#### 5.3. Criterio de Evaluación 1.d: Generación de Código Intermedio para Máquinas Virtuales    

**Preguntas**:    

1. Describe el proceso de generación de código intermedio (bytecode) en el lenguaje que utilizaste que emplea una máquina virtual (por ejemplo, Java o C#).    
2. Explica qué rol juega la máquina virtual en la ejecución del código y cómo difiere de la ejecución directa en un sistema operativo como ocurre con los lenguajes compilados e interpretados.    


#### 5.4. Criterio de Evaluación 1.e: Clasificación de Lenguajes de Programación   

**Preguntas**:    

1. Clasifica los tres lenguajes utilizados (interpretado, compilado y en máquina virtual) según su:
     - **Modo de ejecución** (interpretado vs compilado vs máquina virtual).   
     - **Nivel de abstracción** (alto nivel vs bajo nivel).   
     - **Paradigma de programación** (imperativo, orientado a objetos, funcional,...).   

2. Explica qué características de estos lenguajes influyeron en su clasificación. Es decir, ahonde en las razones por las que cada lenguaje pertenece a una categoría específica. 


#### 5.5. Criterio de Evaluación 1.f: Evaluación de Herramientas Utilizadas en el Desarrollo    

**Preguntas**:    

1. Para cada uno de los tres lenguajes (interpretado, compilado y en máquina virtual), describe las herramientas que utilizaste en el proceso de desarrollo:    
     - **Sistema operativo** (¿en qué sistema ejecutaste el programa?).   
     - **Editor de texto o IDE** (¿dónde escribiste el código?).    
     - **Compilador o intérprete** (¿cómo se transformó o ejecutó el código?).   
     - **Depurador** (si lo usaste, ¿cómo lo empleaste para encontrar errores?).     
     - **Sistema de gestión de versiones** (si lo usaste, ¿cómo guardaste las versiones del código?).     
     - **Otras herramientas** Añade alguna herramienta más a la lista. ¿Cómo te ayudó en el desarrollo?

---

### 6. Entrega

Cada individuo/grupo deberá entregar:    

1. **El código fuente** de los tres lenguajes elegidos (interpretado, compilado y en máquina virtual).    
2. **Capturas de pantalla** de la ejecución del programa en cada lenguaje.    
3. **Respuestas** a todas las preguntas planteadas, agrupadas por criterio de evaluación.    

---

### 7. Conclusión Final
Al final del trabajo, se deberá reflexionar y entregar una **conclusión**, de no más de 10 líneas, que compare las diferencias entre los tres lenguajes (interpretado, compilado y en máquina virtual), destacando:     

- Las diferencias de rendimiento.    
- La facilidad o complejidad de cada proceso de ejecución.    
- Las ventajas y desventajas de cada tipo de lenguaje (interpretado vs compilado vs intermedio).    

---

### 8. Evaluación

Esta actividad permite evaluar los siguientes **Criterios de Evaluación**:     

- **CE 1.a**: Relación entre software y hardware.    
- **CE 1.c**: Diferencias entre código fuente, objeto y ejecutable.    
- **CE 1.d**: Generación de código intermedio en lenguajes con máquinas virtuales.    
- **CE 1.e**: Clasificación de lenguajes de programación.    
- **CE 1.f**: Evaluación de las herramientas utilizadas en el desarrollo de software.    
