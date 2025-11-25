![](assets/IS-U241-DocumentacionDeIncidentes0.png)

**Documentación de incidentes**

**RA2**

> e) Se ha realizado una clasificación, valoración, documentación y seguimiento de los incidentes detectados dentro de la organización.

### 1. Introduccón
El criterio de evaluación e) del Resultado de Aprendizaje 2 se centra en la capacidad para clasificar, valorar, documentar y hacer seguimiento de incidentes de ciberseguridad, asegurando una respuesta eficaz y una mejora continua en las prácticas de seguridad de la organización.

Es fundamental considerar ciertos aspectos clave:

* Clasificación de Incidentes: Los incidentes de ciberseguridad deben ser clasificados según su tipo, basandonos en una taxonomía pre establecida y que ha hemos visto. Esta taxonomía incluye categorías como malware, phishing, ataques de denegación de servicio, entre otros. La clasificación ayuda a priorizar los esfuerzos de respuesta y a aplicar los protocolos de manejo adecuados.  

* Valoración de Incidentes: La valoración implica determinar el impacto potencial de un incidente de ciberseguridad en la organización, asi como la peligrosidad de este. Esto incluye consideraciones sobre la sensibilidad de los datos afectados, el potencial de daño a la reputación de la empresa, y las posibles pérdidas económicas.  

* Documentación de Incidentes: La documentación es crucial para registrar detalladamente cada incidente, incluyendo cómo fue detectado, cuáles fueron las acciones inmediatas tomadas, y cualquier otra información relevante. Esta documentación debe ser precisa y debe almacenarse de forma segura para futuras consultas.  

* Seguimiento de Incidentes: Durante el proceso de resolución, como una vez resuelto un incidente, es importante realizar un seguimiento del incidente, para tener información sobre el estado de este, asi como para asegurar que las medidas tomadas fueron efectivas y prevenir incidentes similares en el futuro. Esto puede incluir la revisión y actualización de los planes de respuesta, políticas de seguridad, así como la realización de capacitaciones adicionales para el personal.


NDICE

Gestión de incidentes

Documentación

Clasificación

Valoración

#### Gestión de incidentes

* Incidente
 * Cualquier _suceso_ que afecte a la **confidencialidad**, **integridad** o **disponibilidad** de los activos de información de la empresa,
 * por ejemplo: acceso o intento de acceso a los sistemas, uso, divulgación, modificación o destrucción no autorizada de información.
* La gestión de incidentes consiste:
 * _plan de acción_ para **atender a los incidentes** que se den.
 * Además de resolverlos debe incorporar _medidas de desempeño_ que permitan:
  * conocer la **calidad del sistema** de protección
  * detectar **tendencias** antes de que se conviertan en grandes problemas.

![](assets/IS-U241-DocumentacionDeIncidentes1.png)

#### Documentación

* La documentación de los incidentes es necesaria para
 * La **notificación** a las entidades que centralizan esta información de forma que se puedan obtener conseguir los indicadores de compromiso y **generar la inteligencia** necesaria que permita detectar estos incidentes.
 * En la gestión de incidentes de seguridad resulta de gran importancia documentar todo lo aprendido en incidentes anteriores a modo de _lecciones aprendidas_, estas pueden resultar vitales para **evitar futuros incidentes de seguridad o solucionar nuevos** incidentes con similares características.

![](assets/IS-U241-DocumentacionDeIncidentes2.png)

* La documentación de los incidentes es necesaria para
 * Conocer con exactitud la **naturaleza** y **tipo** de incidente, las **características** del mismo y los **vectores** de infección con malware o intrusión para parametrizar los sistemas de seguridad de manera adecuada.
 * Para iniciar **campañas de sensibilización** adaptadas a la organización, conocer sus puntos más débiles y saber cómo protegerlos.

![](assets/IS-U241-DocumentacionDeIncidentes3.png)

* La documentación de los incidentes es necesaria para
 * Es importante que esta documentación resulte muy _detallada_, permitiendo conocer:
  * **qué herramientas ** se utilizaron y **cómo**,
  * las **investigaciones** realizadas y sus **resultados**,
  * las **colaboraciones** que se necesitaron,
  * la **documentación utilizada** para resolver el incidente,
  * la **línea temporal** de las acciones seguidas, etc.

![](assets/IS-U241-DocumentacionDeIncidentes4.png)

* La documentación de los incidentes es necesaria para
 * También permite conocer a
  * los **atacantes**,
  * sus **estrategias y sus patrones** en las denegaciones de servicio.
  * Las **nuevas vulnerabilidades** que afectan los sistemas más críticos de la organización también ayudarán en gran medida a **prevenir y solucionar** los posibles incidentes de seguridad.

![](assets/IS-U241-DocumentacionDeIncidentes5.png)

* La documentación de los incidentes es necesaria para
 * Todas estas _acciones técnicas y procedimentales de la organización deben tener siempre en cuenta_ durante el proceso de resolución de un incidente, en especial en la toma y adquisición de evidencias que se deriven en un caso de análisis forense.
  * las **consideraciones legales** que apliquen a la organización por su sector o ámbito,
  * los **principios del secreto de las comunicaciones y privacidad de las personas**, **el código penal**, etc.

![](assets/IS-U241-DocumentacionDeIncidentes6.png)

#### Documentación: notificar

**Qué notificar Descripción**

_Asunto_: Frase que describa de forma general el incidente. Este campo lo heredarán todas las notificaciones asociadas al incidente.

_OSE/PSD_: Denominación del operador de servicios esenciales o proveedor de servicios digitales que notifica.

_Sector estratégico_: Energía, transporte, financiero, etc.

_Fecha y hora del incidente_: Indicar con la mayor precisión posible cuándo ha ocurrido el ciberincidente.

_Fecha y hora de detección del incidente_: Indicar con la mayor precisión posible cuándo se ha detectado el ciberincidente.

_Descripción_: Describir con detalle lo sucedido.

![](assets/IS-U241-DocumentacionDeIncidentes7.png)

**Qué notificar: Descripción**

_Recursos tecnológicos afectados_: Indicar la información técnica sobre el número y tipo de activos afectados por el ciberincidente, incluyendo direcciones IP, sistemas operativos, aplicaciones, versiones…

_Origen del incidente_: Indicar la causa del incidente si se conoce. Apertura de un fichero sospechoso, conexión de un dispositivo USB, acceso a una página web maliciosa, etc.

_Taxonomía (clasificación)_: Posible clasificación y tipo de ciberincidente en función de la taxonomía descrita.

_Nivel de Peligrosidad_: Especificar el nivel de peligrosidad asignado a la amenaza. Consultar Tabla 4. Criterios de determinación del nivel de peligrosidad de un ciberincidente. (Más adelante se indica donde está la tabla 4)

![](assets/IS-U241-DocumentacionDeIncidentes8.png)

**Qué notificar: Descripción**

_Nivel de Impacto_: Especificar el nivel de impacto asignado al incidente. Consultar Tabla 5. Criterios de determinación del nivel de impacto de un ciberincidente. (Más adelante se indica donde está la tabla 5)

_Impacto transfronterizo_: Indicar si el incidente tiene impacto transfronterizo en algún Estado miembro de la Unión Europea. Especificar.

_Plan de acción y contramedidas_: Actuaciones realizadas hasta el momento en relación al ciberincidente. Indicar el Plan de acción seguido junto con las contramedidas implantadas.

_Afectación_: Indicar si el afectado es una empresa o un particular y las afectaciones de acuerdo a los criterios indicados en la Tabla 5. Criterios de determinación del nivel de impacto de un ciberincidente

![](assets/IS-U241-DocumentacionDeIncidentes9.png)

**Qué notificar: Descripción**

_Medios necesarios para la resolución (JP)_: Capacidad empleada en la resolución del incidente en Jornadas\-Persona.

_Impacto económico estimado (Si se conoce)_: Costes asociados al incidente, tanto de carácter directo como indirecto.

_Extensión geográfica (Si se conoce)_: Local, autonómico, nacional, supranacional, etc.

_Daños reputacionales (Si se conocen)_: Afectación a la imagen corporativa del operador.

![](assets/IS-U241-DocumentacionDeIncidentes10.png)

**Qué notificar: Descripción**

_Adjuntos_: Indicar la relación de documentos adjuntos que se aportan para ayudar a conocer la causa del problema o a su resolución (capturas de pantalla, ficheros de registro de información, correos electrónicos, etc.)

_Regulación afectada_: ENS / RGPD /NIS / PIC / Otros

_Se requiere actuación de FFCCSE_: Si / No

![](assets/IS-U241-DocumentacionDeIncidentes11.png)

#### Documentación:

**Para documentar, ** sigue esta guía:

_[https://docs.google.com/document/d/e/2PACX\-1vTDsl2bB5vCiNKj\-cAqj8aitMmxQneXlS1UxC4Wv7KyMwu8ja2qKdMUeBMx4F\-lF9VYH8A66ldw4gxl/pub](https://docs.google.com/document/d/e/2PACX-1vTDsl2bB5vCiNKj-cAqj8aitMmxQneXlS1UxC4Wv7KyMwu8ja2qKdMUeBMx4F-lF9VYH8A66ldw4gxl/pub)_

![](assets/IS-U241-DocumentacionDeIncidentes12.png)

#### Clasificación

* Clasificación según la Taxonomía:
 * Vista _[aquí](https://docs.google.com/presentation/d/e/2PACX-1vRf_Wm-uJCcioeso59vwC-YKqKFWU2AlORCGeeLF5ZwXQ5EEttAjDTWUC3jnWfQWJk1e7p7O74XHbCa/pub?start=false&loop=false&delayms=3000)_
 * También se puede consultar en la _[guía nacional de notificación y gestión de ciberincidentes (pag. 14)](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/resource/view.php?id=508441)_ .

![](assets/IS-U241-DocumentacionDeIncidentes13.png)

#### Valoración

A la hora de valorar la importancia de un incidente, usaremos:

El nivel de peligrosidad: criterio de referencia.

El nivel de impacto.

Si un incidente puede asociarse a más de un tipo de incidente, éste quedará asociado a aquel incidente que tenga un nivel de peligrosidad superior.

![](assets/IS-U241-DocumentacionDeIncidentes14.png)

Peligrosidad ( _[guía nacional de notificación y gestión de ciberincidentes (pag. 19)](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/resource/view.php?id=508441)_ .

La **potencial amenaza que supondría la materialización de un incidente** en los sistemas de información o comunicación del ente afectado, así como para los servicios prestados o la continuidad de negocio en caso de haberla.

Este indicador se fundamenta en las **características intrínsecas a la tipología de amenaza y su comportamiento** .

![](assets/IS-U241-DocumentacionDeIncidentes15.png)

Impacto ( _[guía nacional de notificación y gestión de ciberincidentes (pag. 21)](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/resource/view.php?id=508441)_ .

Se determinará evaluando las **consecuencias que tal ciberincidente ha tenido en las funciones y actividades de la organización afectada**, en sus activos o en los individuos afectados.

De acuerdo a ello,se tienen en cuenta aspectos como las **consecuencias potenciales o materializadas que provoca una determinada amenaza en un sistema de información y/o comunicación, así como en la propia entidad afectada** (organismos públicos o privados, y particulares)

![](assets/IS-U241-DocumentacionDeIncidentes16.png)

Relacionado con el Impacto,

adicionalmente a lo visto en la slide anterior, en la siguiente guía _[https://www.incibe\-cert.es/sites/default/files/contenidos/guias/doc/incibe\-cert\_gestion\_ciberincidentes\_sector\_privado.pdf](https://www.incibe-cert.es/sites/default/files/contenidos/guias/doc/incibe-cert_gestion_ciberincidentes_sector_privado.pdf)_ (pag,. 23)

Se muestra una tabla que expone a modo orientativo un apoyo para las labores de cálculo de impacto de un incidente de seguridad.

#### Bibliografía

_[https://www.incibe\-cert.es/guias\-y\-estudios/guias/guia\-nacional\-notificacion\-y\-gestion\-ciberincidentes](https://www.incibe-cert.es/guias-y-estudios/guias/guia-nacional-notificacion-y-gestion-ciberincidentes)_

_[https://www.incibe\-cert.es/sites/default/files/contenidos/guias/doc/incibe\-cert\_gestion\_ciberincidentes\_sector\_privado.pdf](https://www.incibe-cert.es/sites/default/files/contenidos/guias/doc/incibe-cert_gestion_ciberincidentes_sector_privado.pdf)_

#### Actividad

Documenta un incidente:

de la _[actividad](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/assign/view.php?id=368724)_

descrito en una noticia, por ejemplo los vistos en la _[actividad](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/url/view.php?id=422815)_

Evaluación:

Documentación según guía (80%)

Clasificación según taxonomía (10%)

Valoración (10%)

6 caras máximo en pdf.

![](assets/IS-U241-DocumentacionDeIncidentes17.png)

