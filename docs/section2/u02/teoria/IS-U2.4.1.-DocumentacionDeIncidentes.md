---
title: "UD 2 - 2.4.1 Documentación de incidentes"
description: "Aprende qué documentar en un incidente de seguridad, por qué es crucial y cómo esta práctica mejora la respuesta y previene futuros ataques."
summary: "Esta guía explica la importancia de documentar los incidentes de seguridad, detallando qué información es esencial registrar para una gestión eficaz. Se enfoca en la motivación y los beneficios de una buena documentación, enlazando a recursos adicionales sobre cómo elaborar los informes técnicos."
authors:
    - Eduardo Fdez
date: 2025-11-25
icon: "material/file-document-outline"
permalink: /is/unidad-2/2.4.1-documentacion-de-incidentes
categories:
    - "Incidentes de seguridad"
tags:
    - "Incidentes"
    - "Documentación"
    - "Seguridad"
---

# 2.4.1. Documentación de incidentes

## 1. Introducción

La correcta **clasificación, valoración, documentación y seguimiento** de los incidentes de ciberseguridad es un pilar fundamental para garantizar una respuesta eficaz y una mejora continua en las prácticas de seguridad de cualquier organización. En este documento, nos centraremos en el **QUÉ** documentar y en la importancia de hacerlo, sentando las bases para una gestión de incidentes robusta y bien fundamentada.

Un incidente de seguridad es cualquier suceso que afecte a la **confidencialidad, integridad o disponibilidad** de los activos de información de la empresa. La gestión de incidentes no solo consiste en resolver estos sucesos, sino también en aprender de ellos para fortalecer nuestras defensas.

## 2. ¿Por qué es tan importante documentar?

La documentación de incidentes no es un mero trámite burocrático, sino una herramienta estratégica que aporta un valor incalculable a la organización. A continuación, se detallan las razones clave por las que documentar es esencial:

-   **Generación de inteligencia**: La información recopilada permite identificar **indicadores de compromiso (IOCs)** y las **tácticas, técnicas y procedimientos (TTPs)** de los atacantes. Esta inteligencia es crucial para ajustar y mejorar las herramientas de detección.
-   **Lecciones aprendidas**: Cada incidente es una oportunidad de aprendizaje. Documentar lo bueno y lo malo de la respuesta permite a la organización fortalecer sus defensas y optimizar sus planes.
-   **Análisis y parametrización de sistemas**: Conocer la naturaleza del incidente, sus características y los vectores de ataque es fundamental para configurar adecuadamente los sistemas de seguridad.
-   **Campañas de sensibilización**: La documentación de incidentes reales proporciona material de gran valor para crear campañas de concienciación y formación dirigidas, enfocadas en las amenazas y vulnerabilidades específicas de la organización.
-   **Cumplimiento normativo y legal**: Una documentación detallada es indispensable para cumplir con las obligaciones legales de notificación (como al INCIBE) y para gestionar las implicaciones legales del incidente.
-   **Conocimiento del adversario**: Permite conocer a los atacantes, sus estrategias y sus patrones, ayudando a prevenir y solucionar futuros incidentes.

## 3. ¿Qué debemos documentar?

Para que la documentación sea útil, debe ser detallada y precisa. A continuación, se presenta un listado de los elementos clave que se deben registrar, basados en la "Guía Nacional de Notificación y Gestión de Ciberincidentes".

### 3.1. Información General del Incidente

-   **Asunto**: Una descripción breve y clara. (Ej: "Incidente de ransomware en el servidor de ficheros").
-   **Identificación del afectado**: Nombre de la organización o particular.
-   **Sector estratégico**: Si aplica (energía, financiero, sanidad, etc.).
-   **Fechas y horas clave**:
    -   **Del incidente**: ¿Cuándo ocurrió?
    -   **De la detección**: ¿Cuándo nos dimos cuenta?
-   **Descripción detallada**: Una narración completa de lo sucedido, incluyendo el `origen` si se conoce (phishing, malware, explotación de vulnerabilidad, etc.).

### 3.2. Clasificación y Valoración

-   **Taxonomía**: Clasificar el incidente según una taxonomía estándar (ej. malware, DoS, phishing, fuga de información).
-   **Nivel de Peligrosidad**: Se refiere a la **amenaza** en sí misma. ¿Es un malware muy sofisticado? ¿Un ataque DDoS masivo? Se valora la capacidad intrínseca de la amenaza para causar daño.
-   **Nivel de Impacto**: Se refiere a las **consecuencias** reales o potenciales en la organización. ¿Se han perdido datos sensibles? ¿Se ha interrumpido un servicio crítico? ¿Hay daño reputacional?
-   **Impacto transfronterizo**: Indicar si el incidente afecta a otros estados miembros de la UE.

!!! note "Peligrosidad vs. Impacto"
    Es crucial no confundir estos dos términos. Un malware muy **peligroso** (una nueva cepa de ransomware) puede tener un **impacto** bajo si se detecta y contiene a tiempo en un solo equipo no crítico. Por el contrario, un ataque poco sofisticado (baja **peligrosidad**) puede tener un **impacto** muy alto si afecta a un sistema vital para la empresa.

### 3.3. Detalles Técnicos

-   **Recursos tecnológicos afectados**: Listado de IPs, sistemas operativos, aplicaciones, versiones, etc.
-   **Indicadores de Compromiso (IOCs)**: Hashes de ficheros, dominios y IPs maliciosas, URLs de phishing, etc.
-   **Indicadores de Ataque (IACs)**: Tácticas y técnicas utilizadas por los atacantes, a menudo mapeadas con el framework MITRE ATT&CK.

### 3.4. Gestión y Respuesta

-   **Plan de acción y contramedidas**: ¿Qué se ha hecho hasta ahora? Ej: "Se ha aislado el servidor afectado de la red", "Se han bloqueado las IPs de los atacantes en el firewall". Es importante detallar cada paso.
-   **Herramientas utilizadas**: Software y hardware empleado. Ej. SIEM, EDR, herramientas forenses.
-   **Colaboraciones**: Equipos internos (sistemas, legal) o externos (proveedores, INCIBE-CERT) que han participado en la gestión del incidente. Ej: "Colaboración con el equipo de respuesta a incidentes del proveedor X".
-   **Línea temporal de acciones**: Un registro cronológico detallado de todas las acciones realizadas por el equipo de respuesta. Ej: "10:15 - Detección del incidente", "10:30 - Aislamiento del sistema afectado", etc.
-   **Medios necesarios para la resolución**: Esfuerzo empleado, medido en jornadas-persona (JP). Ej: "5 JP del equipo de seguridad", "2 JP del equipo de sistemas".

### 3.5. Consecuencias y Análisis Post-Incidente

-   **Afectación**: ¿Quién ha sido el afectado final? (la empresa, clientes, particulares).
-   **Impacto económico estimado**: Costes directos (horas de trabajo, sustitución de equipos) e indirectos (pérdida de negocio, multas).
-   **Extensión geográfica**: Local, autonómico, nacional, supranacional.
-   **Daños reputacionales**: Afectación a la imagen y confianza en la organización.
-   **Regulación afectada**: ¿Implica al ENS, RGPD, directiva NIS, Ley PIC?
-   **Actuación de FFCCSE**: ¿Se ha requerido la intervención de las Fuerzas y Cuerpos de Seguridad del Estado?
-   **Adjuntos**: Evidencias como capturas de pantalla, logs, correos electrónicos, etc.

## 4. ¿Cómo documentar un incidente?

Saber **qué** documentar es el primer paso. El segundo, y no menos importante, es saber **cómo** plasmar toda esa información en un informe técnico que sea claro, útil y profesional.

Un buen informe no es solo una colección de datos; es una narración estructurada que permite a diferentes audiencias (desde técnicos hasta directivos) entender lo que ha pasado, cómo se ha actuado y qué se debe hacer para evitar que vuelva a ocurrir.

Para aprender a redactar informes técnicos de calidad, desde la estructura y el lenguaje hasta consejos específicos para incidentes de seguridad, te recomendamos consultar la siguiente guía detallada:

-   [**2.4.2 Cómo escribir informes técnicos**](IS-U2.4.2.-ComoEscribirInformesTecnicos.md)

## 5. Bibliografía y Actividad

### Bibliografía

-   [Guía Nacional de Notificación y Gestión de Ciberincidentes](https://www.incibe-cert.es/guias-y-estudios/guias/guia-nacional-notificacion-y-gestion-ciberincidentes)
-   [Guía de Gestión de Ciberincidentes para el Sector Privado](https://www.incibe-cert.es/sites/default/files/contenidos/guias/doc/incibe-cert_gestion_ciberincidentes_sector_privado.pdf)

### Actividad

Para poner en práctica lo aprendido, realiza la siguiente actividad:

1.  Elige un incidente de seguridad real que haya sido noticia recientemente.
2.  Busca información sobre el mismo en fuentes abiertas (noticias, blogs de seguridad, informes de fabricantes).
3.  Utilizando la estructura y los campos descritos en este documento, elabora un borrador de la documentación del incidente.
4.  **Evaluación**: Se valorará la completitud de la documentación (80%), la correcta clasificación del incidente según la taxonomía vista (10%) y la justificación de la valoración de peligrosidad e impacto (10%). El documento no debe exceder las 6 páginas.