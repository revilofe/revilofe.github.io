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
    - PDS
    - ciberseguridad
    - gestion
    - riesgos
    - plan director de seguridad
---

## 2.1. Plan director de seguridad

El Plan Director de Seguridad (PDS) es la hoja de ruta que organiza de manera ordenada
las actuaciones de ciberseguridad que una empresa necesita para proteger la continuidad
del negocio. En este tema aprenderemos a diseñarlo paso a paso siguiendo la guía de
INCIBE, incorporando ejemplos reales y conectando cada fase con el análisis de riesgos
estudiado en la unidad. El objetivo es que, al finalizar, podáis
trabajar en la elaboración de un PDS adaptándolo a cualquier organización.

### 1. Introducción: la necesidad de planificar la seguridad

La digitalización ha convertido la información en un activo imprescindible: facturación,
relación con clientes y proveedores, stock, datos personales o propiedad intelectual
dependen de sistemas y redes. Cuando esos sistemas fallan, el negocio se detiene.
Por eso, proteger la información es proteger la empresa. Pensemos en estas situaciones:

- Un rasonware cifra los datos, paraliza la red y nadie sabe a quién avisar ni cómo recuperar los datos.
- Un empleado descontento filtra datos sensibles a la competencia.
- Se pierde un disco duro externo con informes financieros sin cifrar.
- La web de comercio electrónico sufre un ataque de denegación de servicio y queda fuera de línea en plena campaña.
- Un servidor de correo deja de funcionar durante un día por falta de mantenimiento.

En todos estos casos aparecen preguntas inquietantes: ¿hay copias de seguridad fiables?
¿se habían identificado los riesgos? ¿contamos con personal preparado para reaccionar?
Si las respuestas son dudosas, es el momento de diseñar un Plan Director de Seguridad.

### 2. Concepto y objetivos del Plan Director de Seguridad

Un PDS consiste en definir y priorizar un conjunto de proyectos de seguridad de la
información con el fin de reducir los riesgos a niveles aceptables. Para que sea eficaz:

1. Debe **alinearse con la estrategia** general y tecnológica de la empresa.
2. Requiere un **alcance claro** (qué procesos, departamentos o sistemas están incluidos).
3. Tiene que **asignar responsabilidades** tanto a personal interno como a proveedores.
4. Necesita la **aprobación explícita de la dirección** para asegurar recursos y legitimidad.
5. Debe **contemplar obligaciones legales** (RGPD, ENS, PCI-DSS...) y buenas prácticas.

El PDS no es un documento estático. Tras completar un ciclo, se revisa y vuelve a empezar
para incorporar cambios en la organización, nuevas amenazas o lecciones aprendidas.

### 3. Visión general del ciclo del PDS

El ciclo propuesto por INCIBE comprende seis fases, que abordaremos en detalle:

1. Conocer la situación actual de la organización.
2. Entender la estrategia de la organización.
3. Definir proyectos e iniciativas.
4. Clasificar y priorizar los proyectos.
5. Obtener la aprobación de la dirección.
6. Poner en marcha el plan y establecer la mejora continua.

Cada fase se apoya en la anterior. Si la fotografía inicial es deficiente, las decisiones
posteriores quedarán desalineadas y el plan perderá credibilidad.

<figure markdown>
  ![](assets/IS-U1.2.1.-PlanDirectorDeSeguridad-ejemplo-1698075761312.png)
  <figcaption>Fases de PDS</figcaption>
</figure>

Una cosa a tener en cuenta al terminar el ciclo es que el PDS es un proceso iterativo. La
última fase consiste en volver a la primera para iniciar un nuevo ciclo, aprovechando
la experiencia adquirida y adaptándose a los cambios en el entorno.


### 4. Fase 1. Conocer la situación actual de la organización

En estas primeras etapas se recopila información para entender cómo se gestiona la seguridad
actualmente. 

<figure markdown>
  ![](assets/IS-U121-PlanDirectorDeSeguridad18.png)
  <figcaption>Fase 1</figcaption>
</figure>


Esta fase recoge la mayor parte del trabajo. Se trata de obtener una visión honesta y
documentada del **estado de la seguridad en aspectos organizativos, técnicos, físicos y
legales**. La dirección debe respaldarla para garantizar que los departamentos colaboren.

#### 4.1. Actividades previas

Las primeras tareas se centran en preparar el terreno:

##### 4.1.1. Definir el alcance

Antes de empezar es necesario acotar el terreno de juego. Podemos centrarnos en toda
la empresa o iniciar el plan en un área crítica (por ejemplo, el proceso de facturación,
el departamento de TI o la plataforma de comercio electrónico). Determinar el alcance
condiciona el esfuerzo, los recursos y los tiempos.

Lo recomendable es determinar aquellos activos y procesos de negocio críticos, aquellos sin los que la empresa no puede
subsistir, y utilizar éstos como alcance del PDS. De esta manera, la ejecución del PDS tendrá un impacto más positivo sobre la seguridad de la información de la organización

**Ejemplo práctico**: una pyme industrial decide iniciar el PDS con los procesos de compras,
almacén y facturación porque dependen de un ERP cuyos fallos afectan a la continuidad del negocio.


Si el proceso más crítico de nuestra empresa está relacionado con el proceso de facturación, podemos limitar
el alcance a éste: sistemas y equipos implicados, personal, aplicaciones necesarias, riesgos específicos, etc.
Aunque las mejoras serán específicas dentro de este proceso, nos permitirá profundizar en el resultado y
partir de un punto para extenderlo a otros departamentos o procesos.

##### 4.1.2. Identificar responsables de los activos

Los activos de información incluyen personas, procesos, datos, aplicaciones, equipos,
instalaciones y servicios. Para gestionarlos conviene asignar responsabilidades:

- Responsable de Seguridad: coordina el plan y hace seguimiento de las medidas.
- Responsables de información: velan por datos concretos (clientes, nóminas, diseño).
- Responsables de ámbito: supervisan controles lógicos, físicos, legales y organizativos. (ej ámbito: TI, RR. HH., Jurídico, Compras).

En empresas pequeñas una misma persona puede asumir varios roles, pero deben quedar
documentados para saber quién toma decisiones y quién valida los controles.

##### 4.1.3. Realizar una valoración inicial

> **controles**: medidas de todo tipo (técnico, legal u organizativo) que se implementan para contrarrestar los riesgos de seguridad.

Consiste en identificar qué controles existen y cómo se aplican. La guía propone apoyarse
en la norma ISO/IEC 27002:2017 para seleccionar controles relevantes. No se trata de
aplicar toda la norma sino de elegir los apartados que realmente afecten al alcance. 

<figure markdown>
  ![](assets/IS-U121-PlanDirectorDeSeguridad9.png)
  <figcaption>iso 27002</figcaption>
</figure>

Por ejemplo:

- Si nuestra empresa no desarrolla aplicaciones, no tendremos que valorar aquellos controles de esta norma que hagan referencia al desarrollo seguro de aplicaciones.
- Si nuestra empresa no proporciona un servicio de comercio electrónico, no será necesario que apliquemos los controles relacionados con la transacción de datos personales en la compra-venta online.
- Por el contrario, sí será necesario aplicar medidas o controles relacionados con las copias de seguridad o el proceso de altas y bajas de personal, ya que éstos serán de aplicación en cualquier organización.

El resultado se refleja en un “Documento de Selección de Controles” o *Declaración de
Aplicabilidad (SoA)*, donde se indica si cada control está implantado, en curso o pendiente.

Para medir el grado de implantación se recomienda usar un modelo de madurez inspirado
en CMM, en el se parte de una escala de seis niveles:

- Nivel 0 – Inexistente: no hay evidencia del control (ej. no se hacen copias de seguridad).
- Nivel 1 – Inicial: se realiza ocasionalmente sin procedimientos ni responsables claros (ej. copias de seguridad manuales sin proceimiento, planificación).
- Nivel 2 – Repetible: se sigue un método informal dependiente de la experiencia personal (ej. copias de seguridad regulares pero sin verificación ni pruebas de restauración).
- Nivel 3 – Definido: el control está documentado, aunque no siempre aprobado formalmente (ej. procedimiento documentado de copias de seguridad con roles definidos, pero no ha sido aprobado por la dirección).
- Nivel 4 – Administrado: hay procedimientos aprobados y seguimiento regular.
- Nivel 5 – Optimizado: el control se mide con indicadores y se mejora continuamente.


<figure markdown>
  ![](assets/IS-U121-PlanDirectorDeSeguridad11.png)
  <figcaption>Niveles de madurez</figcaption>
</figure>


##### 4.1.4. Analizar el cumplimiento

Una vez seleccionados los controles, se evalúa su implantación real y su valoración de madurez mediante una auditoría de cumplimiento.

Esta actividad combina entrevistas, revisión documental y visitas a instalaciones:

1. Preparad cuestionarios y checklists basados en los controles seleccionados.
2. Reuníos con responsables de todas las áreas implicadas (TI, RR. HH., Jurídico, Administración,
   Servicios Generales, Calidad) para evaluar cómo aplican los controles.
3. Revisad la seguridad física: accesos a CPD, sistemas antiincendios, condicionantes ambientales.
4. Recoged pruebas y evidencias (fotografías, registros, informes) y registrad incidencias/problemas detectadas.
5. Analizar resultados y asignad puntuaciones de 0 a 5 en cada control para poder representar los resultados en gráficos radar.
6. Solicitad a la dirección un comunicado que refuerce la importancia del proyecto para asegurar la colaboración.


##### 4.1.5. Establecer objetivos de mejora

Con los resultados del análisis de madurez se definen objetivos realistas de mejora. La
guía propone agrupar los controles en dominios temáticos (políticas, organización, RR. HH.,
seguridad física, comunicaciones, operaciones, control de acceso, adquisición de sistemas,
desarrollo, gestión de incidentes, continuidad, cumplimiento legal) y representar los
resultados en un gráfico radar.

Entonces, se fijan objetivos realistas. Es útil dibujar un gráfico con tres curvas:

- Línea roja: grado de cumplimiento actual.
- Línea amarilla: objetivo de cumplimiento a medio plazo (por ejemplo, 12 meses).
- Línea verde: nivel óptimo de cumplimiento a largo plazo.

Así se visualiza qué dominios requieren más esfuerzo: seguridad física, control de acceso,
gestión de incidentes, copias de seguridad, criptografía, etc.


<figure markdown>
  ![](assets/IS-U121-PlanDirectorDeSeguridad14.png)
  <figcaption>Objetivos de mejora</figcaption>
</figure>


#### 4.2. Análisis técnico de seguridad

Las tareas anteriores se centran en aspectos organizativos y de gestión, y son esenciales
para entender el contexto. Sin embargo, es necesario complementar esa visión con un
análisis técnico que identifique vulnerabilidades en sistemas, redes y aplicaciones.

Por tanto, paralelamente a las tareas anteriores se deben realizar auditorías técnicas:

- Verificar la segmentación de la red y la correcta ubicación de los sistemas expuestos a Internet.
- Comprobar la existencia y actualización de cortafuegos, IDS/IPS, antivirus y soluciones antimalware.
- Revisar la política de contraseñas, la gestión de parches y las configuraciones de servidores.
- Evaluar la seguridad del sitio web y de las aplicaciones críticas.
- Planificar pruebas de restauración para minimizar impactos en producción.

Debido a que se trata de un trabajo especializado, es habitual que la organización opte
por externalizar el análisis técnico de la seguridad. En estos casos debemos prestar especial atención a la coordinación del
equipo externo con el personal propio de nuestra organización, para establecer el tipo
de pruebas a realizar y el método de trabajo que se utilizará.

Se recomienda realizar auditorías tanto externas como internas. Así evaluamos el punto
de vista de un atacante externo y la posible amenaza interna. Todos los hallazgos deben
documentarse con su evidencia y se clasifican según criticidad para integrarlos más tarde
en el catálogo de iniciativas.

#### 4.3. Análisis de riesgos en el contexto del PDS

El análisis de riesgos es el puente entre la situación actual y las acciones futuras. INCIBE
lo describe en varias etapas que conectan con el proceso visto anteriormente.

<figure markdown>
  ![](assets/IS-U121-PlanDirectorDeSeguridad17.png)
  <figcaption>Análisis de riesgos</figcaption>
</figure>



1. **Identificación de activos**: ¿qué servicios, aplicaciones, datos y recursos resultan críticos?
2. **Identificación de amenazas y vulnerabilidades**: ataques externos, errores internos, desastres físicos, fallos eléctricos, etc. Y vulnerabilidades técnicas u organizativas como falta de parches, configuraciones débiles, ausencia de formación o procedimientos inadecuados.
3. **Valoración de consecuencias y probabilidad**: se estima el impacto (económico, reputacional, legal)
   y la probabilidad de que la amenaza se materialice.
4. **Evaluación de controles existentes**: qué salvaguardas hay ya implantadas y con qué eficacia.
5. **Cálculo del riesgo residual**: nivel de riesgo que permanece tras aplicar los controles actuales.

El proceso se puede representar como un flujo:

> Activos expuestos a amenazas → Amenazas aprovechan vulnerabilidades → Se produce un impacto
> → Los controles reducen probabilidad/impacto → Queda un riesgo residual que debemos decidir
> si aceptar, mitigar, transferir o eliminar.

<figure markdown>
  ![](assets/IS-U121-PlanDirectorDeSeguridad20.png)
  <figcaption>Evolución de los riesgos</figcaption>
</figure>



##### 4.3.1. Estrategias de tratamiento

Tras calcular el riesgo residual, se decide cómo tratar cada riesgo que supera el umbral
aceptable:

- **Transferir**: contratar un seguro o firmar acuerdos con proveedores para compartir el riesgo.
- **Eliminar**: suprimir la actividad que genera el riesgo (por ejemplo, cerrar un servicio que apenas aporta valor).
- **Asumir**: aceptar el riesgo de forma justificada cuando el coste del control es desproporcionado.
- **Mitigar**: implantar controles técnicos, organizativos o procedimentales que reduzcan la probabilidad
  o el impacto (copias de seguridad con pruebas periódicas, planes de continuidad, redundancia de servidores).

Es fundamental documentar quién adopta cada decisión y con qué argumentos, porque esa
información se revisará en las fases posteriores.

### 5. Fase 2. Conocer la estrategia de la organización

<figure markdown>
  ![](assets/IS-U121-PlanDirectorDeSeguridad28.png)
  <figcaption>Fase 2</figcaption>
</figure>


El PDS solo tendrá sentido si está alineado con la dirección estratégica. En esta fase:

- Se revisan planes corporativos: expansión geográfica, fusiones, nuevas líneas de negocio,
  proyectos de transformación digital o cambios organizativos.
- Se identifican requisitos legales emergentes (por ejemplo, una empresa que comienza a trabajar
  con administraciones públicas deberá cumplir el ENS).
- Se analiza el modelo de servicios TIC (centralización, externalización, uso de cloud).
- Se organiza una reunión con los responsables de los departamentos implicados y con la dirección
  para validar los supuestos y obtener una visión global.

Este análisis permite **anticipar inversiones y evitar proyectos** que quedarán obsoletos en poco tiempo.

Una buena práctica será analizar la estrategica de la organización con los responsables de los departamentos implicados y con la dirección, para hacer partícipes a todas las áreas y obtener una visión objetiva y global de la organización.

### 6. Fase 3. Definir proyectos e iniciativas

<figure markdown>
  ![](assets/IS-U121-PlanDirectorDeSeguridad29.png)
  <figcaption>Fase 3</figcaption>
</figure>

Con la información recopilada se definen las acciones necesarias para alcanzar los objetivos
de seguridad. INCIBE sugiere agruparlas en tres bloques:

1. Iniciativas para mejorar **métodos de trabajo y cumplimiento normativo**.
2. Iniciativas **técnicas y físicas que corrigen deficiencias** detectadas en auditorías.
3. Iniciativas orientadas a **tratar riesgos que superan el nivel aceptable**.

Cada iniciativa debe describirse con los siguientes elementos: objetivo, alcance, responsables,
recursos internos/externos, coste estimado, duración y dependencias.

Ejemplo de formato:    

| ID  | Nombre del proyecto                  | Objetivo                                      | Alcance                | Responsable        | Recursos necesarios         | Coste estimado | Duración estimada | Dependencias               |
|-----|-------------------------------------|-----------------------------------------------|------------------------|--------------------|-----------------------------|----------------|-------------------|----------------------------|
| 01  | Política de seguridad de la información | Definir marco normativo y compromisos de la dirección | Toda la organización    | Responsable de Seguridad | Consultoría externa, tiempo del Responsable de Seguridad | 3.000 €        | 2 meses          | Aprobación de la dirección | |
| 02  | Plan de concienciación                 | Mejorar cultura de seguridad entre empleados   | Toda la organización    | Responsable de RR.HH. | Empresa de formación, materiales de campaña | 5.000 €        | 4 meses          | Coordinación con RR.HH.    |
| ... | ...                                 | ...                                           | ...                    | ...                | ...                         | ...            | ...               |  

Ejemplos de proyectos definidos en esta fase se muestran a continuación:

#### 6.1. Iniciativas tipo

A modo de ejemplo, la guía propone un catálogo inicial con diez proyectos comunes en muchas organizaciones:

| ID  | Proyecto                               | Descripción ampliada                                                                                                                                                                                  |
|-----|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 01  | Política de seguridad de la información | Documento marco que define principios, compromisos de la dirección, uso aceptable de recursos, tratamiento de datos personales y régimen sancionador interno. Debe comunicarse y revisarse anualmente. |
| 02  | Plan de concienciación                 | Programa formativo que combine sesiones presenciales, campañas de correo, cartelería y simulacros de phishing, contando con indicadores de seguimiento.                                               |
| 03  | Gestión de incidentes                  | Procedimientos claros para identificar, registrar, analizar y cerrar incidentes, con un canal de notificación 24/7 y métricas de tiempo de respuesta.                                                 |
| 04  | Adecuación al RGPD                     | Inventario de tratamientos, análisis de legitimación, contratos con encargados, formación específica y revisión de medidas técnicas y organizativas.                                                  |
| 05  | Coordinación RR. HH. – TIC             | Circuitos ágiles para altas y bajas de personal, control de accesos físicos y lógicos, retirada de credenciales y devolución de dispositivos.                                                         |
| 06  | Plan de continuidad TIC                | Análisis de impacto en el negocio (BIA), estrategias de recuperación, procedimientos, pruebas regulares y revisión post-ejercicio.                                                                    |
| 07  | Seguridad en la red corporativa        | Segmentación, VLAN, firewalls internos, IDS/IPS, monitorización de tráfico y gestión de parches, especialmente en servicios expuestos.                                                                |
| 08  | Política de copias de seguridad        | Clasificación de la información, periodicidad de copias, almacenamiento fuera de línea, pruebas de restauración y registros de resultados.                                                            |
| 09  | Clasificación de la información        | Esquema de etiquetado (pública, interna, confidencial) con procedimientos de acceso, cifrado, destrucción y tratamiento por proveedores.                                                              |
| 10  | Gestión de proveedores TIC             | Revisión de contratos, establecimiento de acuerdos de nivel de servicio (SLA) y cláusulas de seguridad, auditorías a proveedores críticos.                                                            |

Estos proyectos son orientativos; cada organización los adaptará a sus necesidades y recursos.

### 7. Fase 4. Clasificar y priorizar los proyectos

<figure markdown>
  ![](assets/IS-U121-PlanDirectorDeSeguridad36.png)
  <figcaption>Fase 4</figcaption>
</figure>

Una vez definido el catálogo de iniciativas, es necesario priorizarlo. Algunas recomendaciones:

- **Agrupar proyectos** por origen (cumplimiento, auditoría técnica, riesgos) o por tipo (organizativo,
  técnico, legal) para tener una visión equilibrada.
- Utilizar una matriz esfuerzo/impacto que permita **clasificar proyectos** a corto, medio y largo plazo.
- **Identificar “quick wins”**: acciones de bajo esfuerzo con alto beneficio que generen resultados visibles.
- **Analizar dependencias** (por ejemplo, no tiene sentido desplegar un EDR sin tener actualizado el inventario
  de equipos).
- **Ajustar la carga de trabajo** al tamaño del equipo disponible para evitar la saturación.

### 8. Fase 5. Aprobar el Plan Director de Seguridad

La aprobación del PDS por parte de la dirección es crucial para asegurar recursos, legitimidad y compromiso. La aprobación formaliza el plan y permite iniciar su ejecución.

<figure markdown>
  ![](assets/IS-U121-PlanDirectorDeSeguridad37.png)
  <figcaption>Fase 5</figcaption>
</figure>


Con el catálogo priorizado se prepara un dossier ejecutivo para la dirección. Debe incluir:

- Resumen del análisis de situación (fortalezas, debilidades, riesgos críticos).
- Lista priorizada de iniciativas con su coste estimado y calendario.
- Beneficios esperados (reducción del riesgo, cumplimiento legal, mejora operativa).
- Consecuencias de no ejecutar el plan (escenarios de riesgo sin tratar).

La aprobación puede requerir ajustes de alcance o de plazos. Es habitual repetir el ciclo de revisión
hasta lograr un consenso. Una vez aprobado, la dirección debe comunicarlo a todas las personas para
reforzar el compromiso colectivo.

### 9. Fase 6. Puesta en marcha y mejora continua

<figure markdown>
  ![](assets/IS-U121-PlanDirectorDeSeguridad38.png)
  <figcaption>Fase 6</figcaption>
</figure>


El éxito del PDS depende de su ejecución. INCIBE recomienda:

- Organizar una **presentación inicial** con todas las personas involucradas para explicar objetivos y responsabilidades.
- **Nombrar responsables o coordinadores** de cada proyecto y dotarlos de recursos (humanos, económicos, técnicos).
- **Crear un comité de gestión** que se reúna periódicamente para revisar el avance, resolver bloqueos y actualizar riesgos.
- **Definir indicadores** (KPIs) como porcentaje de controles implantados, tiempos de respuesta a incidentes
  o grado de cumplimiento de SLAs con proveedores.
- **Revisar periódicamente** que cada acción completada corrige la brecha detectada.
- **Revaluar el plan** cuando cambien las condiciones del negocio o aparezcan nuevas amenazas relevantes.

Al finalizar el ciclo se inicia de nuevo la fase 1, aprovechando los datos del seguimiento para mejorar
la siguiente iteración.

### 10. Caso práctico ilustrativo

Imaginemos una editorial que combina tienda en línea y logística de libros físicos:

<figure markdown>
  ![](assets/IS-U1.2.1.-PlanDirectorDeSeguridad-ejemplo-1698075503913.png)
  <figcaption>Ejemplo de PDS</figcaption>
</figure>

el flujo del PDS podría ser así:

1. **Situación inicial**: la empresa detecta incidentes recurrentes (correo caído, pedidos perdidos),
   no dispone de inventario actualizado de activos y solo realiza copias de seguridad semanales.
2. **Análisis**: se revisan controles según ISO/IEC 27002. La mayoría están en niveles 0-1.
   El análisis técnico identifica falta de segmentación, ausencia de IDS y políticas de contraseñas débiles.
3. **Estrategia**: la dirección planea crecer ofreciendo servicios de impresión bajo demanda,
   lo que requiere más volumen de datos personales.
4. **Riesgos**: se identifican amenazas como ransomware, ataque DDoS y fugas de datos.
   El riesgo residual supera el umbral aceptable en la web y en el ERP de logística.
5. **Proyectos**: se definen veinte iniciativas, entre ellas políticas de seguridad, plan de concienciación, despliegue de MFA, segmentación de red y plan de continuidad.
6. **Priorización**: se eligen tres quick wins para el primer trimestre (probar restauraciones, formalizar proceso de incidentes y segmentar la red perimetral) y se planifican proyectos estructurales a un año.
7. **Aprobación**: la dirección aprueba el plan tras ver el impacto de no actuar (posible sanción por RGPD y pérdidas de ventas por caídas de la web).
8. **Ejecución**: se nombra un comité, se establecen indicadores mensuales y se documentan lecciones aprendidas.
   Al finalizar el primer ciclo, los riesgos críticos bajan a niveles aceptables y se inicia un nuevo ciclo para ampliar el alcance a otras áreas.

### 11. Entregables esenciales del PDS

Tras completar el ciclo, los principales entregables son:

- Inventario de activos con responsables y clasificación de la información.
- Informe de valoración inicial y Declaración de Aplicabilidad.
- Matriz de madurez por dominios con objetivos a corto y largo plazo.
- Informes de auditoría técnica y listas de comprobación de cumplimiento.
- Registro de riesgos con decisiones de tratamiento y riesgo residual.
- Catálogo de iniciativas con costes, recursos, dependencias y métricas de éxito.
- Cronograma consolidado, acta de aprobación y plan de seguimiento.
- Informes periódicos al comité de dirección y actas del comité de gestión.

### 12. Buenas prácticas y errores frecuentes

Algunas recomendaciones para maximizar el éxito del PDS:

- **Apoyo de la dirección**: sin patrocinio real, el plan se queda sin recursos y pierde legitimidad.
- **Comunicación**: informar periódicamente a toda la plantilla refuerza la cultura de seguridad.
- **Coordinación entre áreas**: la seguridad es transversal; RR. HH., Jurídico, Compras, TI y Dirección
  deben colaborar desde el inicio.
- **Documentación y evidencias**: toda decisión y resultado debe quedar documentado para auditorías futuras.
- **Capacidad realista**: es mejor avanzar con menos proyectos bien gestionados que iniciar muchos y no terminarlos.
- **Lecciones aprendidas**: al final de cada ciclo extraed conclusiones para mejorar la siguiente iteración.

### 13. Referencias recomendadas

* [INCIBE. *Plan director de seguridad*. Documento guía](OtrosRecursos/metad_plan-director-seguridad.pdf "Guia para la elaboración de un PDS").
* [¿Qué es el Plan Director de Seguridad?](https://ayudaleyprotecciondatos.es/2020/10/30/plan-director-de-seguridad/#Que_es_el_Plan_Director_de_Seguridad "¿Qué es el Plan Director de Seguridad?")
* [Objetivos generales de un Plan Director de Seguridad](https://ayudaleyprotecciondatos.es/2020/10/30/plan-director-de-seguridad/#Objetivos_generales_de_un_Plan_Director_de_Seguridad "Objetivos generales de un Plan Director de Seguridad")
* [Cómo implantar un Plan Director de Seguridad en una empresa. Pasos a seguir](https://ayudaleyprotecciondatos.es/2020/10/30/plan-director-de-seguridad/#Como_implantar_un_Plan_Director_de_Seguridad_en_una_empresa_Pasos_a_seguir "Cómo implantar un Plan Director de Seguridad en una empresa. Pasos a seguir")
    * [Definición de la política de seguridad de la empresa](https://ayudaleyprotecciondatos.es/2020/10/30/plan-director-de-seguridad/#Definicion_de_la_politica_de_seguridad_de_la_empresa "Definición de la política de seguridad de la empresa")
    * [Conocimiento de la estrategia de la empresa](https://ayudaleyprotecciondatos.es/2020/10/30/plan-director-de-seguridad/#Conocimiento_de_la_estrategia_de_la_empresa "Conocimiento de la estrategia de la empresa")
    * [Definir los proyectos e iniciativas](https://ayudaleyprotecciondatos.es/2020/10/30/plan-director-de-seguridad/#Definir_los_proyectos_e_iniciativas "Definir los proyectos e iniciativas")
    * [Clasificar y priorizar los proyectos a realizar](https://ayudaleyprotecciondatos.es/2020/10/30/plan-director-de-seguridad/#Clasificar_y_priorizar_los_proyectos_a_realizar "Clasificar y priorizar los proyectos a realizar")
    * [Aprobación](https://ayudaleyprotecciondatos.es/2020/10/30/plan-director-de-seguridad/#Aprobacion "Aprobación")
    * [Puesta en marcha del plan](https://ayudaleyprotecciondatos.es/2020/10/30/plan-director-de-seguridad/#Puesta_en_marcha_del_plan "Puesta en marcha del plan")
* [Ejemplos](https://ayudaleyprotecciondatos.es/2020/10/30/plan-director-de-seguridad/#Ejemplos "Ejemplos")
