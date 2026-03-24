# U3.1.1 - Recopilación de Evidencias

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## 1. Introducción a las evidencias


### 1.1. ¿Qué son las evidencias?

**Evidencias**: Datos recopilados durante la investigación de un incidente de seguridad.

**Características:**
* Pueden ser de distintos tipos y procedencias.
* Logs, registros, capturas de red, imágenes de disco.
* Se utilizan para probar algo.
* Pueden combinarse con otra información.

Note: Las evidencias son la materia prima de la investigación forense. Sin evidencias sólidas, no hay caso que investigar ni defender en un juicio.


### 1.2. ¿Qué es la recopilación de evidencias?

**Proceso crítico** en gestión de incidentes:

* Garantizar **integridad** de la evidencia.
* Asegurar **autenticidad** de los datos.
* Mantener **admisibilidad** legal.
* Permitir **reproducibilidad** del proceso.

Note: La forma en que se recopilan las evidencias puede ser tan importante como las evidencias mismas. Un error en el proceso puede invalidar toda la investigación.


### 1.3. Los tres pilares

Para gestión eficaz de evidencias:

1. **Personas**: Personal especializado en equipo de respuesta.
2. **Procedimientos**: Procesos claros y documentados.
3. **Tecnología**: Herramientas adecuadas para recopilación.

Note: Como alumnos y alumnas, debéis entender que la tecnología sin procedimientos y personas capacitadas es inútil.

---

## 2. Metodología de recopilación


### 2.1. Fases principales

Proceso forense digital:

1. **Preservación**: Mantener integridad.
2. **Adquisición**: Recoger evidencia admisible.
3. **Documentación**: Registro preciso y detallado.
4. **Análisis**: Extracción imparcial de información.
5. **Presentación**: Comunicación clara y comprensible.

Note: Estas fases son secuenciales pero pueden solaparse. La documentación, por ejemplo, ocurre durante todo el proceso.


### 2.2. Preservación

**Objetivo**: Mantener la integridad de la evidencia.

**Acciones clave:**
* No alterar la evidencia original.
* Aislar sistemas comprometidos.
* Proteger de modificaciones.
* Documentar estado inicial.

Note: La preservación es como sellar una escena del crimen. Cualquier contaminación posterior invalida las evidencias.


### 2.3. Adquisición

**Objetivo**: Recoger evidencia de forma que sea admitida en juicio.

**Métodos:**
* Imágenes forenses bit-a-bit.
* Copia de logs y registros.
* Capturas de memoria RAM.
* Fotografías y videos de pantallas.

Note: La adquisición debe ser forensically sound - lo que significa que puede defenderse en un tribunal de justicia.


### 2.4. Documentación

**Objetivo**: Documentar el proceso de recogida.

**Requisitos:**
* Preciso y detallado.
* Fecha y hora de cada acción.
* Persona responsable de cada paso.
* Herramientas y comandos utilizados.
* Observaciones y anomalías.

Note: Si no está documentado, no ocurrió. En un juicio, vuestra documentación será vuestra mejor defensa contra cuestionamientos.


### 2.5. Análisis

**Objetivo**: Analizar evidencia de forma imparcial.

**Proceso:**
* Examinar sin prejuicios.
* Buscar patrones y correlaciones.
* Extraer información relevante.
* Contrastar hipótesis.

Note: El análisis forense requiere imparcialidad absoluta. Vuestro trabajo es descubrir la verdad, no confirmar vuestras sospechas.


### 2.6. Presentación

**Objetivo**: Presentar evidencia de forma clara.

**Elementos:**
* Informe ejecutivo para dirección.
* Informe técnico detallado.
* Timeline de eventos.
* Evidencias y su interpretación.
* Conclusiones y recomendaciones.

Note: La mejor evidencia es inútil si no podéis explicarla de forma que no-técnicos la entiendan. Practicad vuestras habilidades de comunicación.

---

## 3. RFC 3227 I


### 3.1. ¿Qué es RFC 3227?

**Documento estándar** para recopilación de evidencias:

* Directrices para recopilación.
* Estándar de almacenamiento.
* Estándar de facto en la industria.
* Reconocido internacionalmente.

Note: RFC 3227 es lectura obligatoria para cualquier profesional forense. Es el manual básico de vuestra profesión.


### 3.2. Principios fundamentales I

Principios clave durante la recolección:

1. Capturar imagen del sistema **tan precisa** como sea posible.
2. Realizar **anotaciones detalladas** con fechas y horas.
3. Indicar si se usa **horario local o UTC**.
4. **Minimizar cambios** en la información recopilada.

Note: La precisión es fundamental. Un error de timestamp puede hacer que toda la línea temporal del incidente sea incorrecta.


### 3.3. Principios fundamentales II

Más principios esenciales:

5. Eliminar **agentes externos** que puedan modificar evidencias.
6. Ante dilema: **primero recopilación, después análisis**.
7. Recoger según **orden de volatilidad**.
8. Cada dispositivo puede requerir **método diferente**.

Note: El principio de "primero recopilación, después análisis" es crítico. No dejéis que la curiosidad comprometa las evidencias.

---

## 4. RFC 3227 II


### 4.1. Orden de volatilidad

Recopilar de **mayor a menor** volatilidad:

1. **Registros y caché** (muy volátil)
2. **Memoria RAM**, tabla de procesos, estadísticas kernel
3. **Información temporal** del sistema
4. **Disco duro** (menos volátil)
5. **Logs del sistema**
6. **Configuración física** y topología de red
7. **Documentos**

Note: La volatilidad determina cuánto tiempo está disponible la información. La RAM se pierde al apagar, pero el disco persiste.


### 4.2. ¿Por qué el orden de volatilidad?

**Justificación:**

* Información volátil se pierde fácilmente.
* Apagar un sistema destruye memoria RAM.
* Datos persistentes pueden recuperarse después.
* Priorizar lo que puede perderse primero.

Note: En un incidente real, tendréis que tomar decisiones rápidas. Conocer el orden de volatilidad os guiará bajo presión.


### 4.3. Acciones a evitar

**Errores que invalidan evidencias:**

* ❌ **No apagar** el ordenador hasta recopilar información volátil.
* ❌ **No ejecutar** programas que modifiquen timestamps.
* ❌ **No confiar** en programas del sistema comprometido.
* ❌ **No usar** herramientas del sistema comprometido.

Note: Estos errores son más comunes de lo que pensáis. En la presión del momento, es fácil cometer un error que invalide toda la evidencia.


### 4.4. Medio protegido

**Uso de herramientas confiables:**

* Recopilar desde **medio protegido** (USB forensically clean).
* No usar herramientas del sistema comprometido.
* Llevar toolkit forense preparado.
* Herramientas verificadas con hashes.

Note: Un atacante sofisticado puede haber modificado las herramientas del sistema. Confiad solo en vuestras herramientas verificadas.


### 4.5. Consideraciones de privacidad

**Aspectos legales:**

* Solicitar **autorización escrita** para recopilación.
* Considerar información **confidencial** de la empresa.
* Evaluar **impacto en disponibilidad** de servicios.
* No entrometerse en **privacidad** sin justificación.

Note: La privacidad es un derecho fundamental. Necesitáis autorización legal antes de acceder a información personal, incluso en una investigación.


### 4.6. Balance privacidad-investigación

**Principio de proporcionalidad:**

* Solo recopilar datos **relevantes**.
* No acceder a archivos **personales** sin indicios.
* Documentar **justificación** de cada acción.
* Respetar **normativa** GDPR y LOPDGDD.

Note: El GDPR impone restricciones estrictas. Un mal manejo de datos personales puede resultar en multas millonarias para la organización.

---

## 5. Procedimiento de recopilación


### 5.1. Características del procedimiento

Debe ser:

* **Detallado**: Sin ambigüedades.
* **Transparente**: Explicar cada paso.
* **Reproducible**: Otros deben poder repetirlo.
* **Verificable**: Testeable por expertos independientes.

Note: Un procedimiento que no puede reproducirse no es válido en un tribunal. Vuestra metodología debe poder ser auditada.


### 5.2. Preparación - Paso 1

**¿Dónde está la evidencia?**

* Listar **sistemas involucrados** en el incidente.
* Identificar **de cuáles tomar evidencias**.
* Priorizar según criticidad.
* Evaluar riesgos de cada sistema.

Note: No siempre podréis recopilar evidencias de todos los sistemas. Priorizad los más críticos y con información más relevante.


### 5.3. Relevancia - Paso 2

**Establecer qué es relevante:**

* Definir alcance de la investigación.
* En caso de duda, **mejor recopilar de más que de menos**.
* Considerar evidencias indirectas.
* Evaluar cadena de eventos.

Note: Es mejor tener evidencias de más que luego podéis descartar, que quedarse cortos y perder información crítica.


### 5.4. Orden de volatilidad - Paso 3

**Fijar orden para cada sistema:**

* Aplicar principio de volatilidad.
* Adaptar a características del sistema.
* Documentar decisiones de priorización.
* Preparar herramientas necesarias.

Note: El orden puede variar según el sistema operativo y la configuración. Adaptad el proceso a cada situación.


### 5.5. Obtención - Paso 4

**Obtener información según orden establecido:**

* Seguir procedimiento documentado.
* Usar herramientas verificadas.
* Calcular hashes de evidencias.
* No interrumpir el proceso.

Note: La obtención es el momento crítico. Cualquier error aquí puede comprometer toda la evidencia. Concentración máxima.


### 5.6. Sincronización de relojes - Paso 5

**Comprobar sincronización:**

* Verificar **hora del sistema**.
* Documentar **diferencia con NTP**.
* Registrar **zona horaria**.
* Impacto en timeline de eventos.

Note: Un reloj desincronizado puede hacer que parezca que eventos ocurrieron en orden diferente al real. Esto puede cambiar completamente la interpretación del incidente.


### 5.7. Iteración - Paso 6

**Preguntarse continuamente:**

* ¿Qué más puede ser evidencia?
* ¿Hay fuentes adicionales de información?
* ¿Qué podríamos estar pasando por alto?

Note: La recopilación es un proceso iterativo. A medida que analizáis, descubriréis nuevas fuentes de evidencia.


### 5.8. Documentar todo - Paso 7

**Documentar cada paso:**

* Qué se encontró.
* Qué **NO** se encontró (también es evidencia).
* Anomalías observadas.
* Decisiones tomadas y por qué.

Note: La ausencia de evidencia también es evidencia. Documentad lo que esperabais encontrar pero no encontrasteis.


### 5.9. Factor humano - Paso 8

**No olvidar a las personas:**

* Qué **gente** estaba presente.
* Qué estaban **haciendo**.
* Qué **observaron**.
* Cómo **reaccionaron**.

Note: Los testimonios de testigos pueden ser tan valiosos como las evidencias técnicas. Recopilad declaraciones lo antes posible.

---

## 6. Almacenamiento de evidencias


### 6.1. Cadena de custodia

**Documentación obligatoria:**

* ¿Dónde?, ¿cuándo? y ¿quién? **descubrió** la evidencia.
* ¿Dónde?, ¿cuándo? y ¿quién? **recolectó** la evidencia.
* ¿Quién ha **manejado** la evidencia.
* ¿Quién ha **custodiado** la evidencia y cómo.

Note: La cadena de custodia es como un registro de propiedad. Cualquier eslabón roto invalida toda la cadena.


### 6.2. Cambios de custodia

**Al transferir evidencia:**

* Documentar **cuándo** ocurrió el intercambio.
* Documentar **cómo** se realizó.
* Número de **albarán** o recibo.
* **Firmas** de quien entrega y recibe.
* Estado de **precintos** de seguridad.

Note: Cada transferencia es un punto de riesgo. La documentación exhaustiva protege contra cuestionamientos futuros.


### 6.3. Requisitos de almacenamiento

**Dónde y cómo almacenar:**

* Dispositivos de **seguridad demostrada**.
* Acceso **solo a personal autorizado**.
* **Detección** de intentos de acceso no autorizados.
* **Ambiente controlado** (temperatura, humedad).
* **Protección física** (caja fuerte, sala segura).

Note: Las evidencias digitales son frágiles. Condiciones ambientales inadecuadas pueden destruirlas.


### 6.4. Protección de evidencias

**Medidas de seguridad:**

* **Cifrado** de copias de evidencias.
* **Hashes** para verificar integridad.
* **Copias** múltiples en ubicaciones separadas.
* **Logs** de acceso a evidencias.
* **Auditoría** periódica del almacenamiento.

Note: Tratad las evidencias como el oro que son. Su pérdida o alteración puede costar millones a la organización.

---

## 7. Otras metodologías


### 7.1. Alternativas a RFC 3227

Otros estándares reconocidos:

* **ENFSI** - European Network of Forensic Science Institutes
* **NIJ** - National Institute of Justice (USA)
* **UNE 71506** - Metodología forense española
* **ACPO** - UK Good Practice Guide

Note: RFC 3227 es el más común, pero estos otros estándares son igualmente válidos y en algunos contextos preferidos.


### 7.2. Selección de metodología

**Factores a considerar:**

* Requisitos **legales** del país.
* **Complejidad** del incidente.
* **Recursos** disponibles.
* **Urgencia** de la situación.
* **Normativa** sectorial aplicable.

Note: No hay una metodología única para todos los casos. Debéis adaptar vuestro enfoque a cada situación específica.

---

## 8. Herramientas forenses


### 8.1. Herramientas de adquisición

Software esencial:

* **FTK Imager**: Creación de imágenes forenses.
* **dd / dc3dd**: Herramientas Unix/Linux.
* **EnCase**: Suite forense completa.
* **Autopsy**: Plataforma open source.
* **Volatility**: Análisis de memoria RAM.

Note: Familiarizaos con múltiples herramientas. Cada una tiene fortalezas y debilidades según el tipo de evidencia.


### 8.2. Herramientas de análisis

Para examen de evidencias:

* **Wireshark**: Análisis de tráfico de red.
* **Log2timeline**: Construcción de timelines.
* **Sleuth Kit**: Análisis de sistemas de archivos.
* **Strings**: Extracción de cadenas de texto.
* **binwalk**: Análisis de archivos binarios.

Note: El análisis requiere múltiples herramientas trabajando en conjunto. Montad un laboratorio virtual para practicar.


### 8.3. Validación de herramientas

**Antes de usar en producción:**

* Verificar **hashes** de la herramienta.
* Probar en **entorno controlado**.
* Documentar **versión** utilizada.
* Mantener **registro de validación**.
* Actualizar con **precaución**.

Note: Una herramienta comprometida o defectuosa puede contaminar todas vuestras evidencias. La validación es obligatoria.

---

## 9. Casos prácticos


### 9.1. Caso 1: Malware en estación de trabajo

**Escenario**: Usuario reporta comportamiento extraño.

**Recopilación:**
1. Memoria RAM (procesos, conexiones).
2. Captura de red.
3. Imagen del disco.
4. Logs del sistema.
5. Entrevista con usuario.

Note: Este es un caso típico. La memoria RAM puede revelar el malware en ejecución antes de que se oculte en el disco.


### 9.2. Caso 2: Fuga de datos

**Escenario**: Información confidencial aparece en internet.

**Recopilación:**
1. Logs de acceso a archivos sensibles.
2. Logs de transferencias de red.
3. Correos electrónicos sospechosos.
4. Accesos USB.
5. Timeline de actividad del usuario.

Note: Las fugas internas requieren investigación cuidadosa. Debéis equilibrar la investigación con los derechos de privacidad.


### 9.3. Caso 3: Compromiso de servidor web

**Escenario**: Defacement o inyección de código.

**Recopilación:**
1. Logs del servidor web.
2. Base de datos del sitio.
3. Archivos modificados (con timestamps).
4. Logs de firewall/IPS.
5. Backups previos al incidente.

Note: En servidores en producción, debéis balancear la recopilación con la disponibilidad del servicio. Documentad todas las decisiones.

---

## 10. Conclusión


### 10.1. Resumen de conceptos clave

* **Evidencias**: Datos que prueban hechos en investigación.
* **Metodología**: RFC 3227 como estándar principal.
* **Fases**: Preservación, adquisición, documentación, análisis, presentación.
* **Orden de volatilidad**: Priorizar lo más volátil.
* **Cadena de custodia**: Documentar cada manipulación.

Note: Estos conceptos son la base de la investigación forense digital. Dominarlos os distinguirá como profesionales.


### 10.2. Errores comunes a evitar

**Top 5 errores:**

1. Apagar el sistema sin recopilar memoria RAM.
2. Usar herramientas del sistema comprometido.
3. Documentación insuficiente.
4. Romper cadena de custodia.
5. Trabajar sobre evidencia original.

Note: Aprended de los errores de otros. Cada uno de estos errores ha invalidado investigaciones reales y costado millones.


### 10.3. Habilidades a desarrollar

Para alumnos y alumnas:

* **Técnicas**: Uso de herramientas forenses.
* **Legales**: Conocer normativa aplicable.
* **Documentación**: Escritura clara y precisa.
* **Análisis**: Pensamiento crítico.
* **Comunicación**: Explicar hallazgos técnicos.

Note: La parte técnica es solo el 50% del trabajo. La documentación y comunicación son igual de importantes.


### 10.4. Próximos pasos

Práctica recomendada:

1. Montar laboratorio forense virtual.
2. Practicar con herramientas (FTK Imager, Autopsy).
3. Participar en CTFs forenses.
4. Estudiar casos reales documentados.
5. Leer estándares completos (RFC 3227, UNE 71506).

Note: La teoría sin práctica es inútil. Dedicad tiempo cada semana a practicar recopilación de evidencias.

---

## Bibliografía

* [RFC 3227](https://www.ietf.org/rfc/rfc3227.txt) - Guidelines for Evidence Collection
* [UNE 71506](http://www.aenor.es) - Metodología forense española
* NIST SP 800-86 - Guide to Integrating Forensic Techniques
* ENFSI Guidelines - Forensic Examination of Digital Technology
* NIJ - Electronic Crime Scene Investigation

Note: RFC 3227 debe ser vuestra lectura prioritaria. Es corto pero fundamental para todo lo que haréis en investigación forense.
