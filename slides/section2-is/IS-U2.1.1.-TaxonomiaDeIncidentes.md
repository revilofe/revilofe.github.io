# U2.1.1 - Taxonomía de Incidentes

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## 1. Introducción a la taxonomía


### 1.1. ¿Por qué necesitamos una taxonomía?

* Diversidad de empresas, sectores y tamaños.
* Gran variedad de ciberincidentes posibles.
* Cada organización puede tener su propia forma de describir incidentes.
* Sin estándar común: confusión y respuesta ineficaz.

Note: Como alumnos y alumnas, debéis entender que la taxonomía es como aprender un idioma común para hablar de ciberseguridad. Sin ella, sería como si cada organización hablara un idioma diferente.


### 1.2. La taxonomía como idioma común

* Permite categorizar y describir incidentes de forma estandarizada.
* Facilita la colaboración entre organizaciones.
* Mejora el intercambio de información.
* Permite respuesta rápida y efectiva.

Note: La taxonomía actúa como un mapa en terreno desconocido, proporcionando orientación necesaria para abordar amenazas efectivamente.


### 1.3. Beneficios de una taxonomía común

Ventajas prácticas:

1. **Identificación rápida** del tipo de ciberataque
2. **Mejor comunicación** entre departamentos y organizaciones
3. **Respuesta efectiva** con estrategias específicas
4. **Aprendizaje continuo** de incidentes anteriores

Note: Una taxonomía bien definida no es solo teoría, tiene aplicaciones prácticas inmediatas que salvan a las organizaciones de pérdidas significativas.

---

## 2. Factores de clasificación


### 2.1. Tipo de amenaza o método

* Determina la técnica usada por atacantes.
* Ejemplos: código dañino, intrusiones, fraude.
* Permite identificar el tipo de incidente.
* Facilita aplicar medidas de respuesta adecuadas.

Note: Conocer el método del ataque es como conocer el modus operandi de un criminal; nos ayuda a anticipar sus próximos movimientos.


### 2.2. Origen de la amenaza

* **Interna**: empleado descontento, error humano.
* **Externa**: hacker, grupo organizado, competencia.

Identificar el origen ayuda a:
* Ajustar la respuesta
* Prevenir futuros incidentes
* Aplicar medidas específicas

Note: No es lo mismo responder a un ataque externo sofisticado que a un error interno. La estrategia de respuesta cambia completamente.


### 2.3. Categoría de sistemas afectados

* Sistemas críticos vs no críticos.
* Según ENS - Esquema Nacional de Seguridad.
* Categorías: BAJO, MEDIO, ALTO.
* Prioridad de respuesta según criticidad.

Note: Un incidente en sistema crítico puede paralizar toda la organización. Los alumnos y alumnas deben entender la importancia de priorizar.


### 2.4. Perfil de usuarios afectados

* Posición en la estructura organizativa.
* Nivel de privilegios de acceso.
* Acceso a información sensible o confidencial.
* Impacto potencial del compromiso.

Note: El compromiso de una cuenta administrativa es mucho más grave que el de un usuario estándar. Los privilegios determinan el alcance del daño.


### 2.5. Número y tipología de sistemas

* **Número**: ¿Un sistema o toda la red?
* **Tipología**: servidores, estaciones, móviles.
* Impacto escalado según alcance.
* Recursos necesarios para la respuesta.

Note: Un ransomware que afecta a un servidor de bases de datos crítico requiere respuesta muy diferente a uno en una estación de trabajo aislada.


### 2.6. Impacto organizacional

Dimensiones del impacto:

* **Protección de información**: confidencialidad comprometida.
* **Prestación de servicios**: disponibilidad afectada.
* **Conformidad legal**: incumplimientos normativos.
* **Imagen pública**: reputación dañada.

Note: El impacto no es solo técnico. Los aspectos legales y reputacionales pueden ser incluso más costosos para la organización.


### 2.7. Requerimientos legales

* Notificación a autoridades competentes.
* Notificación a afectados (GDPR).
* Plazos legales de notificación (72 horas).
* Documentación y evidencias necesarias.

Note: El GDPR impone multas de hasta 20 millones de euros o 4% de facturación global. El cumplimiento legal no es opcional.

---

## 3. Taxonomía de referencia INCIBE


### 3.1. Basada en estándares

Fundamentos:

* Guía Nacional de Notificación y Gestión de Ciberincidentes (INCIBE).
* CCN-STIC 817 (CCN-CERT).
* Taxonomía ENISA (Agencia Europea).
* Coordinada internacionalmente.

Note: Esta taxonomía no es invención española, es el resultado de coordinación internacional entre equipos de respuesta a incidentes.


### 3.2. Estructura de la taxonomía

Dos niveles de clasificación:

* **Primer nivel**: Categoría general del incidente.
* **Segundo nivel**: Tipos específicos dentro de cada categoría.

Permite precisión y flexibilidad simultáneamente.

Note: Es como un árbol: el tronco es la categoría, las ramas son los tipos específicos. Esto permite ser específico sin perder claridad.

---

## 4. Categorías principales (1/3)


### 4.1. Contenido abusivo

Incidentes con spam, comentarios ofensivos, contenido ilegal.

**Tipos:**

* **SPAM**: Correo masivo no solicitado.
* **Delito de odio**: Contenido difamatorio o discriminatorio.
* **Pornografía infantil**: Material ilegal.

Note: Aunque parezca menos técnico, el contenido abusivo tiene serias implicaciones legales y puede ser el inicio de ataques más sofisticados.


### 4.2. Código dañino

Software malicioso que compromete sistemas.

**Tipos:**

* **Malware**: Virus, troyanos, gusanos.
* **Ransomware**: Cifrado de datos con rescate.
* **Spyware**: Recopilación no autorizada de información.
* **Rootkit**: Ocultación de presencia maliciosa.

Note: El código dañino es una de las amenazas más comunes. Los alumnos y alumnas deben conocer la diferencia entre cada tipo para responder adecuadamente.


### 4.3. Recopilación de información

Actividades para obtener información de la organización.

**Tipos:**

* **Escaneo**: Búsqueda de vulnerabilidades.
* **Sniffing**: Interceptación de comunicaciones.
* **Social Engineering**: Ingeniería social.

Note: La recopilación de información es la fase previa al ataque real. Detectarla a tiempo puede prevenir el incidente mayor.


### 4.4. Intento de intrusión

Intentos de acceder sin autorización.

**Tipos:**

* **Explotación de vulnerabilidades**: Uso de fallos conocidos.
* **Login attempts**: Intentos de acceso por fuerza bruta.
* **New attack signature**: Nuevas técnicas de ataque.

Note: Un intento no es un éxito, pero indica que alguien está intentando entrar. Es la alarma que debe activar la vigilancia.

---

## 5. Categorías principales (2/3)


### 5.1. Intrusión

Acceso no autorizado exitoso.

**Tipos:**

* **Compromiso de cuenta**: Credenciales robadas.
* **Compromiso de aplicación**: Vulnerabilidad explotada.
* **Compromiso de sistema**: Control total del sistema.

Note: Cuando se confirma una intrusión, el incidente ya es grave. La respuesta debe ser inmediata y contundente.


### 5.2. Disponibilidad

Ataques que afectan la disponibilidad de servicios.

**Tipos:**

* **DDoS**: Denegación de servicio distribuida.
* **Sabotaje**: Destrucción intencionada.
* **Interrupción**: Fallo en servicios críticos.

Note: Sin disponibilidad, no hay negocio. Los ataques de disponibilidad pueden ser tan dañinos como el robo de datos.


### 5.3. Seguridad de la información

Compromiso de confidencialidad o integridad.

**Tipos:**

* **Acceso no autorizado**: Lectura de información sensible.
* **Modificación no autorizada**: Alteración de datos.
* **Pérdida de datos**: Información perdida o destruida.

Note: La tríada CIA (Confidencialidad, Integridad, Disponibilidad) se ve afectada. Cada tipo requiere respuesta específica.


### 5.4. Fraude

Uso de recursos informáticos con intención fraudulenta.

**Tipos:**

* **Phishing**: Suplantación de identidad.
* **Copyright**: Uso ilegal de software.
* **Masquerade**: Falsificación de identidad.

Note: El fraude combina ingeniería social con técnicas técnicas. Es uno de los vectores de ataque más exitosos actualmente.

---

## 6. Categorías principales (3/3)


### 6.1. Vulnerabilidad

Debilidad que puede ser explotada.

**Tipos:**

* **Criptografía débil**: Algoritmos obsoletos.
* **Amplificación**: Vulnerabilidad en protocolos.
* **Configuración incorrecta**: Errores de configuración.

Note: Las vulnerabilidades por sí mismas no son incidentes, pero son la puerta de entrada. Gestionarlas es prevenir futuros incidentes.


### 6.2. Otras categorías

Categorías adicionales según necesidades:

* **Pruebas de seguridad**: Auditorías y pentesting.
* **Otros**: Incidentes que no encajan en categorías anteriores.

Note: La taxonomía debe ser flexible para adaptarse a nuevos tipos de incidentes que emergen constantemente.

---

## 7. Aplicación práctica


### 7.1. Ejemplo 1: Phishing exitoso

**Escenario**: Empleado recibe email suplantando a director financiero, hace clic y descarga malware.

**Clasificación**:
* Categoría: **Fraude** (phishing)
* También: **Código dañino** (malware descargado)
* Origen: **Externo**
* Usuario: **Alto privilegio** (área financiera)

Note: Un mismo incidente puede caer en múltiples categorías. Lo importante es identificar todas para responder completamente.


### 7.2. Ejemplo 2: Ransomware

**Escenario**: Ransomware cifra servidores de producción, exige pago en Bitcoin.

**Clasificación**:
* Categoría: **Código dañino** (ransomware)
* También: **Disponibilidad** (servicios caídos)
* Sistemas: **ALTO** (servidores críticos)
* Impacto: **Prestación de servicios + legal**

Note: El ransomware es uno de los incidentes más costosos. Requiere respuesta coordinada entre técnicos, legales y dirección.


### 7.3. Ejemplo 3: Fuga de datos

**Escenario**: Base de datos de clientes expuesta en internet por error de configuración.

**Clasificación**:
* Categoría: **Seguridad de la información**
* Tipo: **Acceso no autorizado**
* Origen: **Interno** (error humano)
* Legal: **Notificación GDPR obligatoria**

Note: Las fugas de datos tienen implicaciones legales inmediatas. El tiempo de respuesta es crítico (72 horas para notificar bajo GDPR).

---

## 8. Proceso de clasificación


### 8.1. Pasos para clasificar

1. **Detectar y confirmar** el incidente.
2. **Recopilar información** inicial.
3. **Identificar factores** relevantes.
4. **Asignar categoría** principal.
5. **Determinar tipos** específicos.
6. **Evaluar impacto** y prioridad.
7. **Documentar** la clasificación.

Note: La clasificación no es aleatoria, sigue un proceso estructurado. Como investigadores, debéis documentar cada paso.


### 8.2. Herramientas de apoyo

* **Matrices de decisión**: Flujos para determinar categoría.
* **Checklist de factores**: Verificación sistemática.
* **Base de datos de incidentes**: Casos similares previos.
* **Sistemas SIEM**: Correlación automática de eventos.

Note: Las herramientas ayudan, pero la experiencia y criterio del analista son insustituibles para una clasificación precisa.


### 8.3. Documentación obligatoria

Para cada incidente clasificado:

* Fecha y hora de detección.
* Categoría y tipo asignado.
* Factores considerados en la decisión.
* Sistemas y usuarios afectados.
* Impacto preliminar.
* Analista responsable.

Note: La documentación no es burocracia, es evidencia. En caso de auditoria o legal, será vuestra mejor defensa.

---

## 9. Revisión y actualización


### 9.1. Taxonomía viva

* Las amenazas evolucionan constantemente.
* Nuevos tipos de ataques emergen.
* La taxonomía debe actualizarse.
* Revisión periódica necesaria.

Note: La ciberseguridad no es estática. La taxonomía de hace 5 años no contemplaba muchos de los ataques actuales como el ransomware as a service.


### 9.2. Fuentes de actualización

* Boletines de CCN-CERT.
* Alertas de INCIBE.
* Informes de ENISA.
* Comunidad internacional de respuesta a incidentes.
* Lecciones aprendidas de incidentes propios.

Note: Mantenerse actualizado es responsabilidad profesional. Suscribiros a estas fuentes es indispensable para vuestra carrera.

---

## 10. Conclusión


### 10.1. Resumen de conceptos clave

* La taxonomía es un **idioma común** en ciberseguridad.
* Permite **identificación rápida** y **respuesta efectiva**.
* Basada en **estándares internacionales** (INCIBE, CCN-CERT, ENISA).
* Considera **múltiples factores** para clasificación precisa.
* Incluye **categorías principales** reconocidas.

Note: La taxonomía no es solo memorizar categorías, es entender cómo y por qué clasificamos incidentes de cierta manera.


### 10.2. Importancia para profesionales

Para alumnos y alumnas:

* Habilidad fundamental en equipos SOC/CSIRT.
* Comunicación efectiva con stakeholders.
* Base para procedimientos de respuesta.
* Requisito en certificaciones profesionales.

Note: Dominar la taxonomía os diferenciará como profesionales. Es una habilidad que utilizaréis diariamente en vuestra carrera.


### 10.3. Próximos pasos

1. Estudiar la taxonomía de referencia completa.
2. Practicar con casos reales.
3. Familiarizarse con herramientas de clasificación.
4. Participar en ejercicios de respuesta a incidentes.
5. Mantenerse actualizado con nuevas amenazas.

Note: La práctica es esencial. Buscad CTFs, laboratorios virtuales, y casos de estudio para aplicar lo aprendido.

---

## Bibliografía

* [Guía Nacional INCIBE](https://www.incibe.es/sites/default/files/contenidos/guias/doc/guia_nacional_notificacion_gestion_ciberincidentes.pdf)
* [CCN-STIC 817](https://www.ccn-cert.cni.es/)
* [ENISA Taxonomy](https://www.enisa.europa.eu/publications/reference-incident-classification-taxonomy)
* [Repositorio GitHub](https://github.com/flosada/RSITaxonomy_ES/blob/master/humanv1.md)

Note: Estas son las fuentes oficiales y autorizadas. Consultadlas regularmente y estad atentos a actualizaciones.
