---
title: "UD 1 - 2.1 Plan director de seguridad (guía práctica)"
description: Guía paso a paso para diseñar e implantar un Plan Director de Seguridad alineado con el negocio.
summary: Pasos, roles, entregables y métricas para un Plan Director de Seguridad efectivo.
authors:
    - Eduardo Fdez
date: 2025-11-02
icon:
permalink: /is/unidad1/2.1/plan-director
categories:
    - IS
tags:
    - plan director
    - ciberseguridad
    - gestion
---

## 2.1. Plan director de seguridad

El Plan Director de Seguridad (PDS) es la hoja de ruta que permite mejorar de forma
ordenada la ciberseguridad de una organización. Se centra en identificar qué proteger,
cómo hacerlo y en qué orden, alineando la inversión con los objetivos estratégicos y
el nivel de riesgo aceptable. A continuación desarrollamos todo su contenido siguiendo
la guía oficial de INCIBE para que podáis replicarlo en cualquier organización.

### 1. Introducción al contexto del PDS

Las tecnologías de la información se han convertido en la base del negocio:
gestión de pedidos, facturación, bases de datos de clientes o la web corporativa dependen
de sistemas que deben protegerse con el mismo rigor que cualquier proceso productivo.

#### 1.1. Escenarios que muestran la necesidad del PDS

- Sufrimos un virus informático y nadie conoce el procedimiento de respuesta.
- Se pierde información crítica y no existen copias de seguridad recuperables.
- Desaparece un portátil con datos sensibles sin cifrar.
- La tienda online recibe un ataque de denegación de servicio y queda inoperativa.
- Se avería un servidor o la red, dejando al equipo sin correo ni aplicaciones clave.

#### 1.2. Preguntas clave que la dirección debe responder

- ¿Gestionamos información corporativa en móviles con medidas suficientes?
- ¿Funcionan nuestras copias de seguridad? ¿Están completos los datos respaldados?
- ¿Conocemos los riesgos reales que amenazan a la empresa?
- ¿Debemos externalizar servicios TIC o disponer de recursos internos?

Responder a estas preguntas evidencia que la protección del negocio requiere un enfoque
planificado y avalado por la dirección.

### 2. ¿Qué es un Plan Director de Seguridad?

> Un PDS define y prioriza proyectos de seguridad de la información para reducir los riesgos
> a niveles aceptables a partir del análisis de la situación inicial.

Un buen PDS debe:

- Alinear la estrategia de seguridad con la estrategia corporativa y TIC.
- Delimitar un alcance claro y asignar responsabilidades a personal interno y proveedores.
- Incorporar buenas prácticas y obligaciones legales para plantilla y terceros.
- Contar con patrocinio explícito de la dirección para garantizar recursos.

#### 2.1. Factores que condicionan su magnitud

- Tamaño y madurez digital de la organización.
- Sector y requisitos regulatorios (RGPD, ENS, PCI-DSS, etc.).
- Naturaleza de la información tratada y criticidad de los procesos de negocio.
- Alcance del proyecto (departamentos, procesos, sistemas específicos).
- Estructura organizativa y recursos disponibles.

El PDS es un ciclo de mejora continua: una vez finalizado un plan se vuelve a iniciar
para mantener el nivel de protección actualizado frente a nuevas amenazas o cambios
en la empresa.

### 3. Visión general de las fases del PDS

1. Conocer la situación actual de la organización.
2. Conocer la estrategia corporativa.
3. Definir proyectos e iniciativas.
4. Clasificar y priorizar los proyectos.
5. Aprobar el Plan Director de Seguridad.
6. Poner en marcha el plan y hacer seguimiento.

### 4. Fase 1. Conocer la situación actual de la organización

Es la fase más extensa y crítica. Requiere coordinación entre áreas, datos fiables
para evaluar la madurez en seguridad y, sobre todo, el apoyo explícito de la dirección
para acceder a información, recursos y personal.

#### 4.1. Actividades previas

**Acotar y establecer el alcance**

- Determinad si el PDS cubrirá toda la empresa o un subconjunto (por ejemplo,
  procesos críticos como facturación o un departamento TIC).
- Analizad qué activos y procesos son esenciales para la continuidad del negocio.
- Documentad lo que queda fuera del plan para retomarlo en ciclos posteriores.

**Designar responsables de la gestión de los activos**

- Elaborad un inventario de activos de información (personas, procesos, hardware,
  software, instalaciones o ficheros).
- Asignad roles concretos:
  - Responsable de Seguridad para coordinar iniciativas.
  - Responsables de Información para activos/datos específicos.
  - Responsables de ámbito (lógico, físico, legal, organizativo) según el tipo de control.
- En pymes varias funciones podrán recaer en una misma persona; lo importante es
  dejar clara la responsabilidad.

**Valoración inicial de la situación**

- Evaluad qué controles están implantados y qué requisitos aplican.
- Usad ISO/IEC 27002:2017 como referencia para seleccionar controles pertinentes
  (no es obligatorio implantar todos, solo los que aplican a la empresa).
- Elaborad el *Documento de Selección de Controles* o *Declaración de Aplicabilidad (SoA)*,
  indicando el grado de implantación y madurez de cada control.
- A modo orientativo, aplicad una escala de madurez tipo CMM:
  - Inexistente: no se realiza el control (p. ej. no hay copias de seguridad).
  - Inicial: el control existe pero sin formalidad ni planificación.
  - Repetible: se ejecuta de forma informal y depende de la experiencia individual.
  - Definido: hay procedimiento documentado pero sin aprobación formal.
  - Administrado: procedimiento documentado y aprobado, con gestión activa.
  - Optimizado: procedimiento aprobado y medido periódicamente mediante indicadores.

**Análisis de cumplimiento**

1. Realizad entrevistas con responsables de cada área (Personal, Jurídico, Administración,
   Servicios Generales, Calidad, TIC) para comprobar la aplicación de controles.
2. Incluid revisiones físicas de instalaciones (CPD, accesos, condiciones medioambientales).
3. Registrad problemas y evidencias con checklists y formularios que recojan cada control revisado.
4. Asignad puntuaciones (por ejemplo, de 0 a 5) para visualizar el grado de cumplimiento
   y poder comparar la evolución en el tiempo.
5. Solicitad que la dirección comunique formalmente la importancia del proyecto
   para garantizar la colaboración de todas las áreas.

**Establecer objetivos a cumplir**

- Definid metas realistas por dominio (actual, objetivo a medio/largo plazo y nivel óptimo).
- Usad gráficos de radar o tablas para visualizar brechas entre el estado actual y el deseado.
- Centrad los objetivos en las áreas con mayor impacto en el negocio (copias de seguridad,
  control de accesos, gestión de incidentes, continuidad, etc.).

#### 4.2. Análisis técnico de seguridad

- Revisad la infraestructura: segmentación de red, protección perimetral, cortafuegos, IDS/IPS,
  antivirus, políticas de contraseñas y estado de parcheo.
- Comprobad la seguridad de la página web, los servidores internos y los equipos de usuario.
- Preparad procedimientos de recuperación antes de las pruebas para minimizar el impacto
  sobre los servicios evaluados.
- Realizad auditorías técnicas desde el exterior e interior de la organización para simular
  amenazas internas y externas.
- Documentad hallazgos, vulnerabilidades y deficiencias de control junto con las evidencias.

#### 4.3. Análisis de riesgos dentro del PDS

!!! note "Relación con la unidad 1.2.2"
    La metodología para identificar, evaluar y tratar riesgos ya se desarrolló en detalle
    en la unidad [1.2.2](/is/unidad1/1.2.2). Aquí la integramos dentro del PDS y resaltamos
    los puntos clave de la guía.

**Etapas del análisis de riesgos**

1. Identificar los activos susceptibles de sufrir amenazas, recogiendo su valor para el negocio.
2. Catalogar las amenazas más relevantes para cada activo crítico (por ejemplo, DDoS,
   acceso indebido, errores humanos, desastres físicos).
3. Determinar las consecuencias de la amenaza (impacto) y la probabilidad de que ocurra.
4. Evaluar los controles existentes que reducen la probabilidad o el impacto.
5. Estimar el riesgo residual al que la organización sigue expuesta tras aplicar controles.

**Pasos prácticos**

1. Inventariad activos, amenazas y vulnerabilidades (p. ej. un servidor web vulnerable
   a saturación de tráfico).
2. Calculad el riesgo intrínseco antes de controles específicos.
3. Estimad probabilidad e impacto para obtener el nivel de riesgo.
4. Decidid qué riesgos son aceptables y cuáles requieren tratamiento, valorando coste
   y eficacia de las salvaguardas.
5. Documentad el riesgo residual tras aplicar controles y revisadlo periódicamente,
   ya que puede variar con cambios de infraestructura o nuevas amenazas.

También podéis adaptar metodologías existentes o combinarlas para crear un enfoque
propio ajustado a la organización.

##### 4.3.1. Nivel de riesgo aceptable y estrategias de tratamiento

- **Transferir**: traspasar parte del riesgo a un tercero (seguros, acuerdos con proveedores).
- **Eliminar**: suprimir procesos o servicios innecesarios para que el riesgo desaparezca.
- **Asumir**: aceptar un riesgo de manera justificada cuando el coste del control es demasiado alto
  (por ejemplo, mantener la actividad sin generador eléctrico durante cortes prolongados).
- **Mitigar**: implantar salvaguardas que reduzcan probabilidad o impacto
  (SAI, replicación, acuerdos de respaldo, planes de continuidad).

Sea cual sea la estrategia, documentad quién decide y por qué, con el aval de la dirección.

### 5. Fase 2. Conocer la estrategia de la organización

- Analizad proyectos en curso y futuros, planes de crecimiento, reorganizaciones o fusiones.
- Considerad si la empresa apostará por centralizar servicios, externalizarlos o iniciar nuevas líneas de negocio
  con requisitos regulatorios específicos.
- Contrastad la estrategia con responsables de cada departamento y con la dirección para lograr
  una visión global y objetiva.
- El objetivo es alinear la seguridad tanto con la estrategia TIC como con la estrategia general de negocio.

### 6. Fase 3. Definir proyectos e iniciativas

A partir del análisis anterior, proponed acciones concretas en tres bloques:

1. Mejora de métodos de trabajo y cumplimiento normativo/organizativo.
2. Refuerzo de controles técnicos y físicos detectados como insuficientes.
3. Gestión de riesgos que superan el nivel aceptable acordado.

Estimad para cada iniciativa el esfuerzo temporal, coste económico y recursos necesarios
(internos y externos). A modo de referencia, la guía propone los siguientes proyectos tipo:

| ID | Proyecto | Descripción |
| --- | --- | --- |
| 01 | Desarrollar e implementar una política de seguridad | Política que cubra, como mínimo, el compromiso de la dirección, el uso del correo e Internet, el uso de dispositivos móviles y la protección de datos personales. |
| 02 | Plan de concienciación en seguridad de la información | Sesiones de formación y sensibilización para personal operativo y dirección. |
| 03 | Mejora en la gestión de incidentes y atención al usuario | Definir, documentar e implantar el proceso integral de gestión de incidentes de seguridad. |
| 04 | Adecuación al RGPD | Proyecto para adaptar la organización a la normativa de protección de datos. |
| 05 | Cooperación RR. HH. – TIC | Establecer mecanismos de coordinación que agilicen altas, bajas y cambios de personal y acceso. |
| 06 | Plan de continuidad TIC | Incrementar la capacidad de respuesta ante contingencias tecnológicas críticas. |
| 07 | Seguridad de la red corporativa | Segmentar la red y desplegar sistemas de detección de intrusos (IDS/IPS). |
| 08 | Política de copias de seguridad | Analizar la información copiada, definir periodicidades y verificar restauraciones periódicas. |
| 09 | Clasificación de la información | Sistema de clasificación con niveles (público, privado, confidencial) que regule etiquetado, acceso, cifrado, destrucción, etc. |
| 10 | Regulación de servicios TIC prestados por terceros | Revisar y homogeneizar contratos con proveedores críticos e incorporar acuerdos de nivel de servicio (SLA). |

Recordad valorar la estrategia de la organización para evitar inversiones que pronto
quedarían obsoletas (por ejemplo, si se centralizarán los servicios TIC en un grupo empresarial).

### 7. Fase 4. Clasificar y priorizar los proyectos

- Agrupad iniciativas según su origen (cumplimiento, auditoría técnica, riesgos) o según el tipo de acción.
- Ordenad los proyectos atendiendo al esfuerzo y al tiempo requerido: corto, medio o largo plazo.
- Identificad proyectos «quick wins» de bajo esfuerzo con un alto impacto inmediato.
- Homogeneizad el nivel de detalle de cada iniciativa para facilitar la comparación.

### 8. Fase 5. Aprobar el Plan Director de Seguridad

- Consolidada la versión preliminar del plan, sometedla a revisión de la dirección.
- Aceptad ajustes de alcance, plazos o prioridades y reiterad la revisión si fuese necesario.
- Una vez aprobado formalmente, comunicad el respaldo de la dirección a toda la organización
  (reuniones, comunicados, correo) resaltando la importancia de la colaboración de todas las áreas.

### 9. Fase 6. Puesta en marcha y seguimiento

- Realizad una presentación inicial del proyecto a todas las personas implicadas para alinear expectativas.
- Asignad responsables o coordinadores a cada iniciativa y dotadles de recursos.
- Considerad la creación de un comité de gestión que supervise los avances.
- Definid la periodicidad de seguimiento individual y global del plan (mensual, semestral, anual) y documentad resultados.
- Confirmad que cada objetivo alcanzado resuelve la brecha detectada en el análisis inicial.
- Revisad el plan cuando se produzcan cambios significativos en la organización o en su entorno.

### 10. Entregables clave del PDS

1. Inventario de activos y responsables asociados.
2. Documento de Selección de Controles / Declaración de Aplicabilidad.
3. Evaluaciones de madurez y objetivos por dominio de seguridad.
4. Informes de auditoría técnica con evidencias y recomendaciones.
5. Registro de riesgos, estrategia de tratamiento y riesgo residual aceptado.
6. Catálogo priorizado de iniciativas con costes y recursos.
7. Acta de aprobación de la dirección y plan de seguimiento.

### 11. Buenas prácticas y errores frecuentes

- Asegurad el apoyo de la dirección en todas las fases para obtener información y recursos.
- Combinad controles técnicos, organizativos, legales y físicos: la seguridad debe ser integral.
- Evitad sobrecargar la organización con demasiados proyectos simultáneos.
- Involucrad a RR. HH., Jurídico y Servicios Generales desde el inicio para alinear responsabilidades.
- Documentad incidencias y lecciones aprendidas para alimentar la mejora continua del plan.

### 12. Referencias recomendadas

- INCIBE. *Plan director de seguridad*. [Documento guía](OtrosRecursos/metad_plan-director-seguridad.pdf).
- ISO/IEC 27002:2017. *Código de buenas prácticas para controles de seguridad de la información*.
- INCIBE. *Gestión de riesgos: una guía de aproximación para el empresario*.
- INCIBE. *Copias de seguridad: una guía de aproximación para el empresario*.
