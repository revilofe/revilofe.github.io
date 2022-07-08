![](assets/IS-U311-RecopilacionDeEvidencias0.png)

__Recopilación y almacenamiento de evidencias__

#### RA3
a) Se han recopilado y almacenado de forma segura evidencias de incidentes de ciberseguridad que afectan a la organización.

#### ÍNDICE

#### Recopilación de evidencias

#### Evidencias

Las evidencias son información que\, por sí misma\, o en combinación con otra información\, se utiliza para  _probar algo_ \.

Se trata de una  _fase inicia_ l en la que toda entidad debe estar preparada para cualquier suceso que pudiera ocurrir\.

Una buena  __anticipación__  y  __entrenamiento previo__  es clave para realizar una gestión eficaz de un incidente\, para lo que hace falta tener en cuenta tres pilares fundamentales: las personas\, los procedimientos y la tecnología\.

#### Metodologías de recolección y almacenamiento

Existen gran diversidad de incidentes\, y de muchos tipos… como hemos visto hasta ahora\. No obstante\, los pasos a seguir durante el proceso de recopilación y análisis de evidencias e investigación del incidente\, equivalentes al análisis forense de un incidente\, son los siguientes:

De las distintas guías que existen\, la  __RFC 3227__  es unestándar ampliamente usado\.

_[https://www\.ietf\.org/rfc/rfc3227\.txt](https://www.ietf.org/rfc/rfc3227.txt)_

![](assets/IS-U311-RecopilacionDeEvidencias1.png)

Otras propuestas:

<span style="color:#DF1A21"> _[Guidelines for the best practices in the forensic examination of digital technology](https://enfsi.eu/wp-content/uploads/2016/09/1._forensic_examination_of_digital_technology_0.pdf)_ </span>

<span style="color:#DF1A21"> _[Electronic Crime Scene Investigation: A Guide for First Responders](https://www.ncjrs.gov/pdffiles1/nij/187736.pdf)_ </span>

<span style="color:#DF1A21"> _[Forensic Examination of Digital Evidence: A Guide for Law Enforcement](https://www.ncjrs.gov/pdffiles1/nij/199408.pdf)_ </span>

<span style="color:#DF1A21"> _[UNE 71506 \- Metodología para el análisis forense de las evidencias electrónicas](http://www.aenor.es/aenor/normas/normas/fichanorma.asp?tipo=N&codigo=N0051414&PDF=Si#.UmTshXC8B5H)_ </span>

<span style="color:#DF1A21"> _[Good Practice Guide for Computer\-Based Electronic Evidence ](https://www.7safe.com/docs/default-source/default-document-library/acpo_guidelines_computer_evidence_v4_web.pdf)_ </span>

<span style="color:#DF1A21"> _[RFC 3227 «Guidelines for Evidence Collection and Archiving» o Directrices para la recopilación de evidencias y su almacenamiento](http://www.ietf.org/rfc/rfc3227.txt)_ </span>

#### Metodologías de recolección y almacenamiento
RFC 3227

El RFC 3227 es un  __documento__  que recoge las directrices para:

la  __recopilación__  de evidencias y su  __almacenamiento__ \.

puede llegar a servir como  __estándar de facto__  para la recopilación de información en incidentes de seguridad\.

#### Principios

#### RFC 3227 - Principios I

Principios durante la recolección de evidencias

Capturar una  __imagen del sistema tan precisa__  como sea posible\.

Realizar  __notas detalladas\, incluyendo fechas y horas__  indicando si se utiliza horario local o UTC\.

__Minimizar los cambios en la información__  que se está recolectando y eliminar los agentes externos que puedan hacerlo\.

Principios durante la recolección de evidencias

En el caso de enfrentarse a un dilema entre recolección y análisis elegir  __primero recolección y después análisis__ \.

Recoger la información  __según el orden de volatilidad __ \(de mayor a menor\)\.

Tener en cuenta que por cada dispositivo __ la recogida de información puede realizarse de distinta manera__ \.

#### 1. Orden de volatilidad

Período de  __tiempo en el que está accesible cierta información__ \. Recolectar la de mayor volatilidad\, según este orden:

Registros y contenido de la caché\.

Tabla de enrutamiento\, caché ARP\, tabla de procesos\, estadísticas del kernel\, memoria\.

Información temporal del sistema\.

Disco

Logs del sistema\.

Configuración física y topología de la red\.

Documentos\.

#### 2. Acciones a evitarse

Las que invaliden el proceso de recolección de información\, los resultados deben poder ser utilizados en un juicio si fuera necesario:

__No apagar el ordenado__ r hasta que se haya recopilado toda la información\.

__No ejecutar programas__  que modifiquen la fecha y hora de acceso de todos los ficheros del sistema\.

__No confiar en la información proporcionada por los programas del sistema__  ya que pueden haberse visto comprometidos\.

Recopilar la información mediante  __programas desde un medio protegido__ \.

#### 3. Consideraciones sobre la privacidad

* Es muy importante  __tener en consideración las pautas de la empresa__  en lo que a privacidad se refiere:
  * Es habitual  __solicitar una autorización__  por escrito de quien corresponda para poder llevar a cabo la recolección de evidencias\.
  * Este es un aspecto fundamental ya que puede darse el caso de que se  _trabaje con información confidencial_  o de vital importancia para la empresa\, o que  _la disponibilidad de los servicios se vea afectada\._
* __No hay que entrometerse en la privacidad__  de las personas sin una justificación\.
  * No se deben recopilar datos de lugares a los que normalmente no hay razón para acceder\, como ficheros personales\, a menos que haya suficientes indicios\.

#### Procedimiento de recolección

#### Recolección

Debe de ser lo más detallado posible\, procurando que no sea ambiguo y reduciendo al mínimo la toma de decisiones\.

Transparencia

Los métodos utilizados para recolectar evidencias deben de ser  __transparentes y reproducibles__ \.

Se debe estar preparado para reproducir con precisión los métodos usados\, y que dichos métodos hayan sido  __testados por expertos independientes__ \.

Pasos I

¿Dónde está la evidencia? Listar  __qué sistemas están involucrados__  en el incidente y  __de cuáles de ellos se deben tomar evidencias__ \.

Establecer  __qué es relevante__ \. En caso de duda es mejor recopilar mucha información que poca\.

Fijar el  __orden de volatilidad__  para cada sistema\.

__Obtener la información__  de acuerdo al orden establecido

Pasos II

Comprobar el  __grado de sincronización del reloj del sistema__ \.

Según se vayan realizando los pasos de recolección preguntarse  __qué más puede ser una evidencia__ \.

__Documentar cada paso\.__

No olvidar a la gente involucrada\. Tomar notas sobre  __qué gente estaba allí\, qué estaban haciendo\, qué observaron y cómo reaccionaron__ \.

#### Procedimiento de almacenado

#### Almacenamiento

__Cadena de custodia__

Debe estar claramente documentada y se deben detallar los siguientes puntos:

¿Dónde?\, ¿cuándo? y ¿quién?  __descubrió y recolectó la evidencia__ \.

¿Dónde?\, ¿cuándo? y ¿quién?  __manejó la evidencia__ \.

¿Quién ha custodiado la evidencia?\, ¿cuánto tiempo? y ¿cómo la ha almacenado?

En el caso de que la evidencia cambie de custodia  __indicar cuándo y cómo se realizó el intercambio__ \, incluyendo número de albarán\, etc\.

__Dónde y cómo almacenarlo__

Se debe almacenar la información en dispositivos:

cuya  __seguridad__  haya sido  __demostrada__

que  __permitan detectar intentos de acceso no autorizados__ \.

#### Herramientas

* Pautas para selección de herramientas\, para la recolección:
* herramientas externas al sistema\, para evitar que hayan podido ser comprometidas\.
* herramientas que alteren lo mínimo posible el escenario \(no GUI\, uso excesivo de memoria\)
* deben estar ubicados en un dispositivo de solo lectura\. \(CDROM\, USB\)
* tener un kit básico de herramientas según S\.O\, que incluyan:
  * listar y examinar procesos
  * examinar el estado del sistema
  * realizar copias bit a bit\.

#### Bibliografía

_[https://www\.incibe\-cert\.es/blog/rfc3227](https://www.incibe-cert.es/blog/rfc3227)_

_[https://www\.ietf\.org/rfc/rfc3227\.txt](https://www.ietf.org/rfc/rfc3227.txt)_

#### Actividad

#### Actividad I

Ya conocemos la RFC 3227\. Y sobre la UNE 71506?

Enumera las diferencias más significativas entre ambas\.

Cuales incorporarías a tu normativa para completar la 3227\. Justifica las respuesta tanto para decisiones positivas como negativas\.

Resumen de forma esquemática cómo quedaría metodología para el análisis forense de las evidencias electrónicas

Evaluación:

Identificar procedimiento de recopilación y almacenamiento de evide\.

Justifica haber trabajado UNE 71506\, justificando o no la decisión\.

6 caras máximo en pdf\.

Recopilación de evidencias sobre un incidente:

de la  _[actividad](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/assign/view.php?id=368724)_

descrito en una noticia\, por ejemplo los vistos en la  _[actividad](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/url/view.php?id=422815)_

Evidencias\, y memoria del proceso seguido…\.

Evaluación:

Se ha seguido los pasos de la toma según la memoria\.

Se ha seguido los pasos del almacenamiento según la memoria\.

6 caras máximo en pdf\.

![](assets/IS-U311-RecopilacionDeEvidencias2.png)

