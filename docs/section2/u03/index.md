---
title: "UD 3 - Detección de incidentes"
description: Detección de incidentes. SOC, CERT, CSIRT.
icon: material/security
permalink: /incidentes/unidad3
categories:
  - IC
tags:
  - Incidentes
  - Ciberseguridad
# Relacionado con la tabla de contenidos
toc: true
toc_label: "Contenido"
toc_icon: "file-code"
---

Cada unidad contendrá una serie de contenidos, resultados de aprendizaje (desglosados en criterios de evaluación), una práctica o prácticas para evaluar la adquisición de dichos criterios de evaluación y una prueba teórica para evaluar la asimilación de contenido.

## Normativa que respalda la unidad

### Contenidos

En esta sección se incluyen los contenidos mínimos a impartir en esta unidad, teniendo en cuenta [la normativa del curso](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2020-4963).

Bloque 2 - Auditoría de incidentes de ciberseguridad:

- Controles, herramientas y mecanismos de monitorización, identificación, detección y alerta de incidentes: tipos y fuentes
- Clasificación, valoración, documentación, seguimiento inicial de incidentes de ciberseguridad.

### Resultados de aprendizaje a trabajar

En esta sección se relaciona la unidad con el resultado de aprendizaje a trabajar en esta unidad, teniendo en cuenta [la normativa del curso](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2020-4963).

RA 2. Analiza incidentes de ciberseguridad utilizando herramientas, mecanismos de detección y alertas de seguridad.

#### Criterios de evaluación

En esta sección se relaciona la unidad con los criterios de evaluación concretos, del resultado de aprendizaje a trabajar en esta unidad, teniendo en cuenta [la normativa del curso](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2020-4963).

- b) Se han establecido controles, herramientas y mecanismos de monitorización, identificación, detección y alerta de incidentes
- e) Se ha realizado una clasificación, valoración, documentación y seguimiento de los incidentes detectados dentro de la organización.

## Cómo impartir la unidad

Esta es la sección más interesante, y se incluye cómo trabajar la unidad, haciendo referencia a herramientas, guías, materiales y recursos, de manera individual para cada criterio.

- **Criterio de evaluación b**: se puede montar un SIEM, con el stack de Elastic (ElasticSearch, Logstash y Kibana) para la monitorización de incidentes. Dado que el montaje del sistema es complejo, se recomienda emplear [la siguiente imagen de docker para ello](https://elk-docker.readthedocs.io/).
- **Criterio de evaluación e**: se puede montar [una herramienta de ticketing, como FIR,](https://github.com/certsocietegenerale/FIR/) para llevar el control de los incidentes, desde su origen hasta su resolución. Recomiendo que se despliegue con Docker, por lo que los alumnos deben haber visto Docker en este momento (aunque sea a nivel básico).

### Teoría

Por hacer.

### Ejercicios

Por hacer.

## Cómo evaluar la unidad

### Práctica de la unidad

En esta sección se incluye una propuesta de práctica o prácticas con los que evaluar la unidad.

### Controles de ejemplo

En esta sección se incluyen controles de ejemplo para evaluar la unidad.
