---
title: "UD 3 - Diseño y diagramas de clases"
description: Diseño y diagramas de clases
summary: Diseño y diagramas de clases
authors:
    - Eduardo Fdez
date: 2025-11-03
icon: 
permalink: /edes/unidad3
categories:
    - EDES
tags:
    - EDES
    - UML
    - Diseño

# Relacionado con la tabla de contenidos
toc: true
toc_label: "Contenido"
toc_icon: "file-code"

#hide:
#  - footer
---

## **Unidad 3: Diseño y Diagramas de Clases**

### 1. Normativa que Respalda la Unidad

Esta unidad está alineada con la normativa del curso **"Entornos de Desarrollo"** del ciclo formativo de **Desarrollo de Aplicaciones Web**, teniendo como base el **Resultado de Aprendizaje (RA) 5** y sus **Criterios de Evaluación (CE)**. El objetivo principal es que los estudiantes generen diagramas de clases valorando su importancia en el desarrollo de aplicaciones y empleando herramientas específicas.

**Referencias normativas**:
- [Real Decreto 686/2010, de 20 de mayo](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2010-9269) - Título de Técnico Superior en Desarrollo de Aplicaciones Web
- [Orden de 16 de junio de 2011](https://www.todofp.es/dam/jcr:c198771c-775e-469b-936f-5f5ef6af165a/andtsdesarrollo-aplicaciones-web-pdf.pdf) - Currículo del ciclo formativo

---

### 2. Resultado de Aprendizaje a Trabajar

- **RA 5**: **Genera diagramas de clases valorando su importancia en el desarrollo de aplicaciones y empleando herramientas específicas**.

Este resultado de aprendizaje se enfoca en proporcionar al estudiante las competencias necesarias para:
- Comprender los fundamentos de la programación orientada a objetos
- Utilizar UML como lenguaje de modelado estándar
- Elaborar e interpretar diagramas de clases
- Aplicar principios de diseño de software (cohesión y acoplamiento)

---

### 3. Criterios de Evaluación

En esta unidad se trabajarán los siguientes **criterios de evaluación** relacionados con el **RA 5**:

1. **CE 5.a**: **Se han identificado los conceptos básicos de la programación orientada a objetos**.

    - **Contenido asociado**: Introducción a UML, conceptos fundamentales de la orientación a objetos: clases, objetos, atributos, métodos, encapsulación, herencia, polimorfismo.

2. **CE 5.b**: **Se han utilizado herramientas para la elaboración de diagramas de clases**.

    - **Contenido asociado**: Herramientas de modelado UML (PlantUML, Draw.io, Visual Paradigm, StarUML), notación estándar de diagramas de clases.

3. **CE 5.c**: **Se ha interpretado el significado de diagramas de clases**.

    - **Contenido asociado**: Lectura e interpretación de diagramas de clases existentes, comprensión de relaciones, multiplicidades y visibilidad.

4. **CE 5.d**: **Se han trazado diagramas de clases a partir de las especificaciones de las mismas**.

    - **Contenido asociado**: Técnicas de identificación de clases a partir de requisitos, elaboración de diagramas desde especificaciones textuales, aplicación de principios de diseño.

5. **CE 5.e**: **Se ha generado código a partir de un diagrama de clases**.

    - **Contenido asociado**: Generación automática de código (forward engineering), implementación en Kotlin de diagramas de clases.

6. **CE 5.f**: **Se ha generado un diagrama de clases mediante ingeniería inversa**.

    - **Contenido asociado**: Ingeniería inversa (reverse engineering), extracción de diagramas desde código existente, herramientas para ingeniería inversa.

---

### 4. Contenidos

En esta sección se describen los contenidos que se impartirán en la Unidad 3, teniendo en cuenta la normativa del curso y los criterios de evaluación.

- La unidad pertenece al **Bloque 5: Elaboración de diagramas de clases**.

**U3: Diseño y Diagramas de Clases**

Durante la **Unidad 3**, trabajaremos los siguientes contenidos:

#### 4.1. Introducción a UML (CE 5.a)

- ¿Qué es UML? Definición y propósito
- Historia y evolución de UML
- Los 14 tipos de diagramas UML
- Diagramas estructurales vs diagramas de comportamiento
- Alternativas a UML (SysML, BPMN, ERD, etc.)
- Mejores prácticas en modelado
- UML en metodologías ágiles

#### 4.2. Diagrama de Clases (CE 5.b, 5.c, 5.d)

**Elementos fundamentales**:
- Clases: estructura (nombre, atributos, métodos)
- Visibilidad (+, -, #, ~)
- Atributos: tipos, valores iniciales, atributos estáticos
- Métodos: parámetros, tipos de retorno, métodos estáticos
- Clases abstractas e interfaces

**Tipos de relaciones**:
- Asociación: binaria, reflexiva, n-aria
- Agregación (◇): relación "tiene un" (partes independientes)
- Composición (♦): relación "es parte de" (partes dependientes)
- Herencia (▷): generalización/especialización
- Dependencia (- - →): uso temporal
- Implementación (- - ▷): realización de interfaces

**Conceptos adicionales**:
- Multiplicidad y cardinalidad (1, 0..1, *, 1..*)
- Roles en las relaciones
- Navegabilidad

#### 4.3. Identificación de Clases (CE 5.d)

**Técnicas de identificación**:
- Análisis de sustantivos en requisitos
- Identificación de clases candidatas
- Descarte de candidatas inapropiadas:
  - Clases redundantes
  - Nombres imprecisos
  - Eventos u operaciones
  - Metalenguaje
  - Fuera del alcance
  - Atributos simples

**Proceso de selección**:
- Relevancia al problema
- Eliminación de redundancias
- Agrupación de características
- Consideración de clases implícitas

**Representación UML**:
- Notación gráfica estándar
- Ejemplos prácticos en Kotlin

#### 4.4. Acoplamiento y Cohesión (CE 5.a, 5.d)

**Cohesión** (7 niveles de menor a mayor calidad):
1. Cohesión coincidental (la peor)
2. Cohesión lógica
3. Cohesión temporal
4. Cohesión procedimental
5. Cohesión comunicacional
6. Cohesión secuencial
7. Cohesión funcional (la mejor)

**Acoplamiento** (5 tipos de mayor a menor):
1. Acoplamiento de contenido (el peor)
2. Acoplamiento común
3. Acoplamiento externo
4. Acoplamiento de control
5. Acoplamiento de datos (el mejor)

**Principios de diseño**:
- Alta cohesión: módulos con propósito único y bien definido
- Bajo acoplamiento: minimizar dependencias entre módulos
- Métricas: LCOM, Ca, Ce, Inestabilidad (I)
- Estrategias de refactorización

#### 4.5. Herramientas de Modelado (CE 5.b, 5.e, 5.f)

**Herramientas de diagramación**:
- **Online**: Draw.io, Lucidchart, PlantUML Online
- **Desktop**: Visual Paradigm, StarUML, Enterprise Architect
- **Integradas en IDEs**: IntelliJ IDEA, Eclipse, Visual Studio

**Generación de código** (Forward Engineering):
- Generación automática desde diagramas
- Configuración de plantillas
- Mantenimiento de sincronización

**Ingeniería inversa** (Reverse Engineering):
- Extracción de diagramas desde código Kotlin/Java
- Herramientas de análisis estático
- Actualización de modelos

---

### 5. Actividades de Evaluación

Para evaluar la adquisición de los criterios de evaluación, se propondrán las siguientes **actividades**:

#### Actividad 1: Conceptos de POO y UML (CE 5.a)
- **Descripción**: Cuestionario sobre conceptos básicos de orientación a objetos y UML
- **Objetivo**: Identificar y comprender los fundamentos de la programación orientada a objetos
- **Entregables**: Respuestas argumentadas con ejemplos

#### Actividad 2: Uso de Herramientas de Modelado (CE 5.b)
- **Descripción**: Instalación y uso de al menos dos herramientas de modelado UML (ej: PlantUML y Draw.io)
- **Objetivo**: Familiarizarse con diferentes herramientas de diagramación
- **Entregables**: Diagramas creados con ambas herramientas y comparativa de funcionalidades

#### Actividad 3: Interpretación de Diagramas (CE 5.c)
- **Descripción**: Análisis de diagramas de clases existentes de sistemas reales
- **Objetivo**: Comprender e interpretar diagramas de clases complejos
- **Entregables**: Documento explicando el significado de cada elemento del diagrama

#### Actividad 4: Diseño de Diagramas de Clases (CE 5.d)
- **Descripción**: Elaboración de diagramas de clases a partir de especificaciones de requisitos de un sistema (ej: biblioteca, tienda online, clínica veterinaria)
- **Objetivo**: Aplicar técnicas de identificación de clases y crear diagramas completos
- **Entregables**: Diagrama de clases UML completo con todas las relaciones

#### Actividad 5: Generación de Código (CE 5.e)
- **Descripción**: Implementación en Kotlin de un diagrama de clases previamente diseñado
- **Objetivo**: Transformar modelos UML en código ejecutable
- **Entregables**: Código fuente en Kotlin con todas las clases, atributos, métodos y relaciones

#### Actividad 6: Ingeniería Inversa (CE 5.f)
- **Descripción**: Generación de diagramas de clases a partir de código Kotlin existente usando herramientas de IDE
- **Objetivo**: Aplicar técnicas de ingeniería inversa para documentar código
- **Entregables**: Diagrama UML generado y comparativa con el código original

#### Actividad 7: Acoplamiento y Cohesión (CE 5.a, 5.d)
- **Descripción**: Análisis y refactorización de código aplicando principios de alta cohesión y bajo acoplamiento
- **Objetivo**: Mejorar la calidad del diseño identificando problemas de acoplamiento y cohesión
- **Entregables**: Código refactorizado con justificación de los cambios realizados

---

### 6. Prueba de Evaluación de Contenidos

Al final de la unidad, se realizará una **prueba de evaluación** que incluirá:

**Parte teórica** (40%):
- Conceptos fundamentales de UML y POO
- Tipos de relaciones en diagramas de clases
- Principios de cohesión y acoplamiento
- Interpretación de notación UML

**Parte práctica** (60%):
- Elaboración de diagrama de clases a partir de requisitos
- Identificación de errores en diagramas existentes
- Análisis de código para determinar niveles de cohesión y acoplamiento
- Generación de código Kotlin desde un diagrama
- Preguntas de opción múltiple sobre herramientas y mejores prácticas

Los estudiantes deberán demostrar su comprensión de:
- Los conceptos básicos de la programación orientada a objetos
- La notación UML para diagramas de clases
- Las técnicas de identificación de clases
- Los principios de diseño (cohesión y acoplamiento)
- El uso de herramientas de modelado

---

### 7. Recursos y Materiales

#### Documentación de la unidad:
- **3.1.-Introducción a UML**: Fundamentos, historia, tipos de diagramas

    - [Ver slides](https://revilofe.github.io/slides/section3-ed/ED-U3.1.-UML.html)

- **3.2.-Diagrama de clases**: Notación, elementos, relaciones

     - [Ver slides](https://revilofe.github.io/slides/section3-ed/ED-U3.2.-DiagramaClases.html)

- **3.3.-Identificación de clases**: Técnicas y ejemplos prácticos

    - [Ver slides](https://revilofe.github.io/slides/section3-ed/ED-U3.3.-IdentifClases.html)

- **3.4.-Acoplamiento y cohesión**: Principios de diseño de software

#### Herramientas recomendadas:
- [PlantUML](https://plantuml.com/) - Diagramas mediante código
- [Draw.io](https://app.diagrams.net/) - Editor online gratuito
- [Visual Paradigm Community Edition](https://www.visual-paradigm.com/download/community.jsp) - Herramienta profesional gratuita
- IntelliJ IDEA - Con plugin de diagramas UML

#### Referencias bibliográficas:
- **UML Distilled** - Martin Fowler (Guía práctica de UML)
- **Applying UML and Patterns** - Craig Larman (Diseño orientado a objetos)
- **Clean Code** - Robert C. Martin (Principios de código limpio)
- **Design Patterns** - Gang of Four (Patrones de diseño)

#### Recursos online:
- [UML.org](https://www.uml.org/) - Especificación oficial
- [DiagramasUML.com](https://diagramasuml.com/) - Tutoriales en español
- [Refactoring.guru](https://refactoring.guru/) - Patrones y refactorización

---

### 8. Temporalización

**Duración estimada**: 12-15 horas lectivas

| Sesión | Contenido                                 | Horas  |
|--------|-------------------------------------------|--------|
| 1      | Introducción a UML                        | 1h     |
| 1      | Diagrama de clases: elementos y notación  | 1h     |
| 2      | Diagrama de clases: relaciones            | 1h     |
| 2      | Identificación de clases                  | 1h     |
| 3      | Acoplamiento y cohesión                   | 1h     |
| 3      | Herramientas y práctica                   | 1h     |
| 4      | Prueba de evaluación                      | 1h     |

---

### 9. Conexión con Otras Unidades

**Unidades previas**:
- **U1**: Fundamentos del desarrollo de software → Base conceptual
- **U2**: Entornos de desarrollo integrado → Herramientas de modelado en IDEs

**Unidades posteriores**:
- **U4**: Control de versiones y documentación → Documentar diseños
- **U5**: Pruebas y depuración → Diseñar para facilitar pruebas
- **U6**: Diagramas de comportamiento → Complemento al diseño estático

---

### 10. Competencias Profesionales Desarrolladas

Esta unidad contribuye al desarrollo de las siguientes **competencias profesionales**:

- **d)** Gestionar bases de datos, interpretando su diseño lógico
- **e)** Desarrollar aplicaciones con acceso a bases de datos
- **n)** Elaborar y mantener la documentación de los procesos de desarrollo

Y los siguientes **objetivos generales del ciclo**:

- **e)** Interpretar el diseño lógico, verificando los parámetros establecidos
- **o)** Utilizar herramientas específicas, cumpliendo los estándares establecidos, para elaborar y mantener la documentación

---

Con este enfoque, se abordan claramente los **RA 5** y sus **CE** específicos, proporcionando una base sólida para el diseño orientado a objetos y la creación de diagramas de clases profesionales.
