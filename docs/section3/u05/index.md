---
title: "UD 5 - Diseño y Realización de Pruebas"
description: Unidad dedicada a pruebas de software, TDD, herramientas de automatización y depuración.
summary: Introducción a la verificación del software mediante tipos de pruebas, diseño de casos, automatización y depuración.
authors:
  - Eduardo Fdez
date: 2026-03-27
icon: "material/file-document-multiple-outline"
permalink: /edes/unidad5
categories:
  - EDES
tags:
  - EDES
  - testing
  - calidad
  - depuracion

toc: true
toc_label: "Contenido"
toc_icon: "file-code"
---

## Unidad 5: Diseño y realización de pruebas

En esta unidad trabajamos un bloque fundamental del desarrollo profesional: comprobar si el software funciona como debe, detectar defectos con criterio y utilizar herramientas que permitan validar cambios con más seguridad.

La unidad combina tres ideas que en la práctica suelen ir de la mano:

- entender los fundamentos de las pruebas de software;
- aprender a diseñar y automatizar pruebas útiles;
- utilizar el entorno de desarrollo para depurar y analizar comportamientos.

## Normativa que respalda la unidad

Esta unidad se alinea con el módulo **Entornos de Desarrollo** del ciclo de **Desarrollo de Aplicaciones Web**, tomando como referencia principal el **Resultado de Aprendizaje 3**.

### Resultado de aprendizaje

**RA 3. Verifica el funcionamiento de programas diseñando y realizando pruebas.**

### Criterios de evaluación

Tomando como referencia literal `docs/section3/recursos/EDES Normativa.txt`, los criterios de evaluación asociados a este resultado de aprendizaje son:

- **CE a)** Se han identificado los diferentes tipos de pruebas.
- **CE b)** Se han definido casos de prueba.
- **CE c)** Se han identificado las herramientas de depuración y prueba de aplicaciones ofrecidas por el entorno de desarrollo.
- **CE d)** Se han utilizado herramientas de depuración para definir puntos de ruptura y seguimiento.
- **CE e)** Se han utilizado las herramientas de depuración para examinar y modificar el comportamiento de un programa en tiempo de ejecución.
- **CE f)** Se han efectuado pruebas unitarias de clases y funciones.
- **CE g)** Se han implementado pruebas automáticas.
- **CE h)** Se han documentado las incidencias detectadas.
- **CE i)** Se han utilizado dobles de prueba para aislar los componentes durante las pruebas.

### Referencias de currículo

- [Currículo del ciclo formativo en TodoFP](https://www.todofp.es/dam/jcr:c198771c-775e-469b-936f-5f5ef6af165a/andtsdesarrollo-aplicaciones-web-pdf.pdf)
- `docs/section3/recursos/EDES Normativa.txt`

## Contenidos de la unidad

La unidad pertenece al bloque de **pruebas y calidad**. Los contenidos mínimos y su aterrizaje en el repositorio quedan organizados así:

### 1. Fundamentos de pruebas

- tipos de pruebas;
- niveles de prueba;
- técnicas dinámicas y estáticas;
- diseño de casos de prueba;
- planificación y documentación de pruebas.

Material principal:

- [5.1 Pruebas](teoria/EDES-U5.1.-Pruebas.md)

### 2. Pruebas unitarias y automatización

- pruebas unitarias y su valor dentro del desarrollo;
- desarrollo guiado por pruebas (*TDD*);
- automatización de pruebas;
- dobles de prueba;
- herramientas del ecosistema Kotlin para testing.

Material principal:

- [5.2 Test de unidad y TDD](teoria/EDES-U5.2.-TestUnidadYTDD.md)
- [5.2.1 Kotest](teoria/EDES-U5.2.1.-Kotest.md)
- [5.2.2 MockK](teoria/EDES-U5.2.2.-Mockk.md)

### 3. Depuración y análisis de ejecución

- uso del depurador del IDE;
- puntos de ruptura y seguimiento;
- inspección de variables y flujo de ejecución;
- trazas y *logging* para analizar comportamiento.

Material principal:

- [5.3 Depuración](teoria/EDES-U5.3.-Depuracion.md)
- [5.3.1 Logging Code](teoria/EDES-U5.3.1.-LoggingCode.md)

## Secuencia orientativa de trabajo

Una forma razonable de impartir la unidad es esta:

1. Empezar por los fundamentos del testing y la planificación.
2. Pasar a pruebas unitarias y al enfoque TDD.
3. Introducir herramientas concretas para automatizar pruebas en Kotlin.
4. Cerrar la unidad con depuración, análisis de ejecución y trazas.

## Materiales disponibles

### Teoría

- [5.1 Pruebas](teoria/EDES-U5.1.-Pruebas.md)
- [5.2 Test de unidad y TDD](teoria/EDES-U5.2.-TestUnidadYTDD.md)
- [5.2.1 Kotest](teoria/EDES-U5.2.1.-Kotest.md)
- [5.2.2 MockK](teoria/EDES-U5.2.2.-Mockk.md)
- [5.3 Depuración](teoria/EDES-U5.3.-Depuracion.md)
- [5.3.1 Logging Code](teoria/EDES-U5.3.1.-LoggingCode.md)


### Presentaciones

En el módulo aparecen asociadas actualmente estas presentaciones públicas:

- [ED-U5.1 - Pruebas](https://revilofe.github.io/slides/section3-ed/ED-U5.1.-Pruebas.html)
- [ED-U5.2.1 - Kotest](https://revilofe.github.io/slides/section3-ed/ED-U5.2.1.-Kotest.html)
- [ED-U5.3 - Depuración](https://revilofe.github.io/slides/section3-ed/ED-U5.3.-Depuracion.html)
- [ED-U5.3.1 - Logging Code](https://revilofe.github.io/slides/section3-ed/ED-U5.3.1.-LoggingCode.html)

### Recursos y herramientas

Para esta unidad tiene sentido trabajar con herramientas como:

- IntelliJ IDEA o un IDE equivalente;
- framework de pruebas de Kotlin;
- bibliotecas de *mocking*;
- depurador integrado del IDE;
- utilidades de *logging* y trazas;
- herramientas de análisis estático y cobertura.

## Qué se espera que aprenda el alumnado

Al terminar la unidad, el alumnado debería ser capaz de:

- diferenciar niveles, técnicas y tipos de prueba;
- diseñar casos de prueba con criterio;
- escribir y ejecutar pruebas unitarias;
- automatizar comprobaciones básicas del código;
- usar el depurador para localizar y comprender errores;
- interpretar la relación entre pruebas y calidad del software.

## Evaluación orientativa

Esta unidad puede evaluarse combinando varias evidencias:

- ejercicios de análisis y diseño de casos de prueba;
- pruebas prácticas de automatización;
- actividades de depuración guiada;
- práctica de unidad;
- revisión de calidad y documentación básica de incidencias.

## Observaciones

La unidad 5 tiene ya teoría consolidada, pero todavía puede ampliarse con:

- una práctica específicamente alineada con testing y depuración;
- más presentaciones asociadas a `5.2`, `5.2.2`, `5.3` y `5.3.1`;
- materiales de evaluación o cuestionarios GIFT para reforzar conceptos.
