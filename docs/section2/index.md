---
title: "Incidentes de ciberseguridad"
description: Presentación del módulo de incidentes de seguridad. 
icon: 
permalink: /incidentes/presentacion
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


Se describe el módulo profesional de Incidentes de ciberseguridad. Esta información se divide en: 

* Una primera sección de **Información** general en la que se hace una propuesta de temario, con la relación de unidades y los resultados de aprendizaje asociados, asi como las posibles fechas en las que se impartirían. 
* Una segunda sección con **Materiales** relacionados con el modulo, como Fuentes de información, libros recomendados, recursos y herramientas para aplicar conceptos. 

Todo el contenido está supeditado a mejora, pues es solo una propuesta que irá cambiando, espero que a mejor. Si tienes una propuesta de mejora, no te cortes y pasamela ;-).

## Presentaciones

### Unidad 0 - Presentación
* [IS-U0.1.1 - Presentación](https://revilofe.github.io/slides/IS-U0.1.1.-Presentacion.html)

### Unidad 1 - Planes de prevención y concienciación
* [IS-U1.1.1 - Principios Generales](https://revilofe.github.io/slides/IS-U1.1.1.-PrincipiosGenerales.html)
* [IS-U1.2.1 - Plan Director de Seguridad](https://revilofe.github.io/slides/IS-U1.2.1.-PlanDirectorDeSeguridad.html)
* [IS-U1.2.2 - Análisis de Riesgos](https://revilofe.github.io/slides/IS-U1.2.2.-AnalisiDeRiesgos.html)
* [IS-U1.3.1 - Protección del Puesto de Trabajo](https://revilofe.github.io/slides/IS-U1.3.1.-ProteccionDelPuestoDeTrabajo.html)
* [IS-U1.4.1 - Plan de Concienciación](https://revilofe.github.io/slides/IS-U1.4.1.-PlanDeConcienciacion.html)

### Unidad 2 - Análisis de incidentes
* [IS-U2.1.1 - Taxonomía de Incidentes](https://revilofe.github.io/slides/IS-U2.1.1.-TaxonomiaDeIncidentes.html)
* [IS-U2.2 - SOC](https://revilofe.github.io/slides/IS-U2.2.-SOC.html)
* [IS-U2.2.1 - Detección de Incidentes](https://revilofe.github.io/slides/IS-U2.2.1.-DeteccionDeIncidentes.html)

### Unidad 3 - Investigación de incidentes
* [IS-U3.1.1 - Recopilación de Evidencias](https://revilofe.github.io/slides/IS-U3.1.1.-RecopilacionDeEvidencias.html)

## Información

### Propuesta de temario

En los siguientes enlaces se encuentran los contenidos, resultados de aprendizaje, criterios de evaluación y herramientas para trabajarlos y poder evaluarlos. Es solo una propuesta, pero puede servir de punto de partida inicial.

1. [Planes de ciberseguridad](page-1/)
2. [Análisis de incidentes de ciberseguridad](page-2/)
3. [Construcción de un CyberSOC](page-3/)
4. [Investigación de incidentes de ciberseguridad](page-4/)
5. [Implementación de medidas](page-5/)
6. [Documentación y notificación de incidentes](page-6/)

### Relación de unidades y resultados de aprendizaje

| Unidad | UD 1 | UD 2 | UD 3 | UD 4 | UD 5 | UD 6 |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- |
| RA 1   | X    |      |      |      |      |      |
| RA 2   |      | X    | X    |      |      |      |
| RA 3   |      |      |      | X    |      |      |
| RA 4   |      |      |      |      | X    |      |
| RA 5   |      |      |      |      |      | X    |

### Relación de unidades y fechas

El curso tiene un total de 24 semanas (720 horas). La relación propuesta entre unidades y semanas es la siguiente:

| Unidad | Semanas        |
| ------ | -------------- |
| 1      | Semana 1 - 4   |
| 2      | Semana 5 - 7   |
| 3      | Semana 8 - 12  |
| 4      | Semana 13 - 16 |
| 5      | Semana 17 - 20 |
| 6      | Semana 21 - 24 |

## Materiales

### Fuentes

- Parte de la organización/contenido esta tomado de [Rafael del Rio](https://rafaeldelrio.github.io/)


### Libros

- [El libro de Ra-Ma de gestión de incidentes](https://www.ra-ma.es/libro/gestion-de-incidentes-de-ciberseguridad_139033/) puede ser un buen punto de partida para organizar la estructura del temario.


### Recursos

- [Incibe](https://www.incibe.es/protege-tu-empresa/tematicas/gestion-incidentes-seguridad): el instituto nacional de ciberseguridad pone a nuestra disposición bastantes materiales para la gestión de incidentes de ciberseguridad.
- [Awesome Incident Response](https://github.com/meirwah/awesome-incident-response): repositorio de github con muchas herramientas para la detección y gestión de incidentes.
- [Cyberdefenders](https://cyberdefenders.org/)
- [Let's Defend](https://letsdefend.io/)

### Herramientas

- [Gophish](https://getgophish.com/): nos permite realizar entrenamientos para mejorar la concienciación frente a ataques de phishing.
- [Suite ELK con docker](https://hub.docker.com/r/sebp/elk/tags): nos permite montar un SIEM de forma sencilla. Para recolectar datos para el SIEM podemos emplear [Filebeat](https://www.elastic.co/es/beats/filebeat), [Winlogbeat](https://www.elastic.co/es/beats/winlogbeat), [Heartbeat](https://www.elastic.co/es/beats/heartbeat), [Metricbeat](https://www.elastic.co/es/beats/metricbeat), [Packetbeat](https://www.elastic.co/es/beats/packetbeat), [etc...](https://www.elastic.co/es/beats/)

## Contenido

Típicamente se intenta tener los siguientes apartados en cada uno de los módulos profesionales:

- Teoría: en formato editable (como libreoffice, un .odt), o en documentos PDF
- Presentaciones: en formato editable (como libreoffice, un .odp), o en documentos PDF
- Ejercicios: un boletín de ejercicios para practicar en clases.
- Prácticas evaluables: una serie de prácticas evaluables.
- Exámenes: una serie de exámenes
