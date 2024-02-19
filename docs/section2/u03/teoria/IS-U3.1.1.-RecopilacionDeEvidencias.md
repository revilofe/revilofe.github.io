---
title: "UD 3 - 1.1 Recopilación y almacenamiento de evidencias"
description: Recopilación y almacenamiento de evidencias
summary: Recopilación y almacenamiento de evidencias
authors:
    - Eduardo Fdez
date: 2024-02-13
icon: 
permalink: /is/unidad3/3.1
categories:
    - IS
tags:
    - IS
    - Seguridad
    - Evidencias
    - Recopilación
    - Almacenamiento
---
![](assets/IS-U311-RecopilacionDeEvidencias0.png)

## Recopilación y almacenamiento de evidencias

> **RA3**
> a) Se han recopilado y almacenado de forma segura evidencias de incidentes de ciberseguridad que afectan a la organización.

### 1. Recopilación de evidencias

__Evidencias__: Las evidencias son información que, por sí misma, o en combinación con otra información, se utiliza para _probar algo_.

__La recopilación de evidencias__: es una _fase inicial_ dentro de una gestión eficaz de un incidente que toda entidad debe tener lista y preparada para ejecutarla ante cualquier suceso que pudiera ocurrir.

Una buena __anticipación__ y __entrenamiento previo__ es clave para realizar una gestión eficaz de un incidente, para lo que hace falta tener en cuenta tres pilares fundamentales: las personas, los procedimientos y la tecnología.

### 2. Metodologías de Recopilación y Almacenamiento

En el día a día se dan gran diversidad de incidentes, y de muchos tipos… como hemos visto hasta ahora. No obstante, los pasos a seguir durante el proceso de recopilación y análisis de evidencias e investigación del incidente, equivalentes al análisis forense de un incidente, son los siguientes:

De las distintas guías que existen, la __RFC 3227__ es un estándar ampliamente usado.

- _[RFC 3227](https://www.ietf.org/rfc/rfc3227.txt)_

![](assets/IS-U311-RecopilacionDeEvidencias1.png)

- Preservación: __mantener la integridad__ de la evidencia. 
- Adquisición: __recoger la evidencia__ de forma que sea __admitida en un juicio__.
- Documentación: __documentar__ el proceso de recogida de evidencias.
- Análisis: __analizar__ la evidencia de forma __imparcial__. an
- Presentación: __presentar__ la evidencia de forma __clara y comprensible__.   
 
Otras propuestas:

- _[Guidelines for the best practices in the forensic examination of digital technology](https://enfsi.eu/wp-content/uploads/2016/09/1._forensic_examination_of_digital_technology_0.pdf)_
- _[Electronic Crime Scene Investigation: A Guide for First Responders](https://www.ncjrs.gov/pdffiles1/nij/187736.pdf)_
- _[Forensic Examination of Digital Evidence: A Guide for Law Enforcement](https://www.ncjrs.gov/pdffiles1/nij/199408.pdf)_
- _[UNE 71506 - Metodología para el análisis forense de las evidencias electrónicas](http://www.aenor.es/aenor/normas/normas/fichanorma.asp?tipo=N&codigo=N0051414&PDF=Si#.UmTshXC8B5H)_
- _[Good Practice Guide for Computer-Based Electronic Evidence ](https://www.7safe.com/docs/default-source/default-document-library/acpo_guidelines_computer_evidence_v4_web.pdf)_
- _[RFC 3227 «Guidelines for Evidence Collection and Archiving» o Directrices para la recopilación de evidencias y su almacenamiento](http://www.ietf.org/rfc/rfc3227.txt)_

### 3 RFC 3227

El RFC 3227 es un __documento__ que recoge las directrices para la __recopilación__ de evidencias y su __almacenamiento__.  Puede llegar a servir como __estándar de facto__ para la recopilación de información en incidentes de seguridad.



#### 3.1. Principios

Principios durante la recolección de evidencias:

- Capturar una __imagen del sistema tan precisa__ como sea posible.
- Realizar __notas detalladas, incluyendo fechas y horas__ indicando si se utiliza horario local o UTC (tiempo universal coordinado).
- __Minimizar los cambios en la información__ que se está recolectando y eliminar los agentes externos que puedan hacerlo.
- En el caso de enfrentarse a un dilema entre recolección y análisis elegir __primero recolección y después análisis__.
- Recoger la información __según el orden de volatilidad__ (de mayor a menor).
- Tener en cuenta que por cada dispositivo __la recogida de información puede realizarse de distinta manera__.

##### 3.1.1. Orden de volatilidad

Período de __tiempo en el que está accesible cierta información__. Recolectar la de mayor volatilidad, según este orden:

- Registros y contenido de la caché.
- Tabla de enrutamiento, caché ARP, tabla de procesos, estadísticas del kernel, memoria.
- Información temporal del sistema.
- Disco
- Logs del sistema.
- Configuración física y topología de la red.
- Documentos.

##### 3.1.2. Acciones a evitarse

Deben evitarse las acciones que invaliden el proceso de recolección de información, los resultados deben poder ser utilizados en un juicio si fuera necesario:

- __No apagar el ordenador__ hasta que se haya recopilado toda la información.
- __No ejecutar programas__ que modifiquen la fecha y hora de acceso de todos los ficheros del sistema.
- __No confiar en la información proporcionada por los programas del sistema__ ya que pueden haberse visto comprometidos.
- Recopilar la información mediante __programas desde un medio protegido__.

##### 3.1.3. Consideraciones sobre la privacidad

- Es muy importante __tener en consideración las pautas de la empresa__ en lo que a privacidad se refiere:
  * Es habitual __solicitar una autorización__ por escrito de quien corresponda para poder llevar a cabo la recolección de evidencias.
  * Este es un aspecto fundamental ya que puede darse el caso de que se _trabaje con información confidencial_ o de vital importancia para la empresa, o que _la disponibilidad de los servicios se vea afectada_.

* __No hay que entrometerse en la privacidad__ de las personas sin una justificación.
  * No se deben recopilar datos de lugares a los que normalmente no hay razón para acceder, como ficheros personales, a menos que haya suficientes indicios.

#### 3.2. Procedimiento de recolección

Debe de ser lo más detallado posible, procurando que no sea ambiguo y reduciendo al mínimo la toma de decisiones. Y tener en cuenta que la información recopilada debe ser __relevante__ y __suficiente__.

Trasnsparencia: Los métodos utilizados para recolectar evidencias deben de ser __transparentes__ y __reproducibles__ .Se debe estar preparado para reproducir con precisión los métodos usados, y que dichos métodos hayan sido __testados por expertos independientes__ .

Pasos para una recolección de evidencias efectiva:

- ¿Dónde está la evidencia? Listar __qué sistemas están involucrados__ en el incidente y __de cuáles de ellos se deben tomar evidencias__ .
- Establecer __qué es relevante__ . En caso de duda es mejor recopilar mucha información que poca.
- Fijar el __orden de volatilidad__ para cada sistema.
- __Obtener la información__ de acuerdo al orden establecido
- Comprobar el __grado de sincronización del reloj del sistema__ .
- Según se vayan realizando los pasos de recolección preguntarse __qué más puede ser una evidencia__ .
- __Documentar cada paso__, el no encontrar una evidencia puede ser una evidencia en sí misma. Por tanto, hay que __documentar también lo que no se ha encontrado__.
- No olvidar a la gente involucrada. Tomar notas sobre __qué gente estaba allí, qué estaban haciendo, qué observaron y cómo reaccionaron__ .

#### 3.3. Procedimiento de almacenado

##### 3.3.1. Cadena de custodia

Debe estar claramente documentada y se deben detallar los siguientes puntos:

* ¿Dónde?, ¿cuándo? y ¿quién? __descubrió y recolectó la evidencia__ .
* ¿Dónde?, ¿cuándo? y ¿quién? __manejó la evidencia__ .
* ¿Quién ha custodiado la evidencia?, ¿cuánto tiempo? y ¿cómo la ha almacenado?
* En el caso de que la evidencia cambie de custodia __indicar cuándo y cómo se realizó el intercambio__, incluyendo número de albarán, etc.

##### 3.3.2. Dónde y cómo almacenarlo

Se debe almacenar la información en dispositivos:

* cuya __seguridad__ haya sido __demostrada__
* que __permitan detectar intentos de acceso no autorizados__ .

#### 3.4. Herramientas

Más que una lista de herramientas, la RFC 3227 proporciona una serie de __pautas__ para la selección de herramientas, para la recolección:

* herramientas externas al sistema, para evitar que hayan podido ser comprometidas.
* herramientas que alteren lo mínimo posible el escenario (no GUI, evitar uso excesivo de memoria)
* deben estar ubicados en un dispositivo de solo lectura. (CDROM, USB)
* tener un kit básico de herramientas según S.O, que incluyan:
  * listar y examinar procesos
  * examinar el estado del sistema
  * realizar copias bit a bit.


### 4. Ejemplo de recopilación de evidencias
A continuación se muestra un ejemplo muy básico de recopilación de evidencias. Supongamos que se ha detectado un ataque a un servidor web, relacionado con un ataque de denegación de servicio (DoS). Se ha detectado que el servidor web ha dejado de responder y se ha detectado un tráfico anómalo en la red.

Tras detectar el ataque, se ha procedido a la __recopilación de evidencias__, para ello se ha utilizado:
- La herramienta `volatility` para la recopilación de evidencias que se encuentran en la memoria.
- También se ha utilizado `wireshark` para la recopilación de tráfico de red.
- Por último, para la recopilación de evidencias del disco duro se ha utilizado `dd`, creando una imagen del disco duro.

En cuanto al __almacenamiento de evidencias__, se ha almacenado la evidencia de la memoria en un fichero llamado `memoria.img`, la evidencia del tráfico de red en un fichero llamado `trafico.pcap` y la evidencia del disco duro en un fichero llamado `disco.img`. Estos ficheros se han almacenado en un dispositivo de almacenamiento seguro, con un sistema de detección de intentos de acceso no autorizados.

Se ha __documentado la cadena de custodia__, indicando quién ha descubierto y recolectado la evidencia, quién ha manejado la evidencia y quién ha custodiado la evidencia.

De esta forma se ha recopilado evidencia de la memoria, del tráfico de red y del disco duro junto con la documentación de los pasos seguidos y la cadena de custodia, se ha recopilado evidencia de forma efectiva.

### 5. Conclusiones
Como hemos visto, la recopilación de evidencias es un proceso fundamental en la gestión de incidentes de seguridad. La RFC 3227 proporciona una serie de pautas para la recopilación de evidencias, que deben ser seguidas para garantizar que la recopilación de evidencias se realiza de forma efectiva. El almacenamiento de evidencias también es un proceso fundamental, y la RFC 3227 proporciona una serie de pautas para el almacenamiento de evidencias, que deben ser seguidas para garantizar que las evidencias se almacenan de forma segura. 
La cadena de custodia es un aspecto fundamental en la recopilación y almacenamiento de evidencias, y debe ser documentada de forma detallada.
Por último, es importante tener en cuenta que la recopilación y almacenamiento de evidencias debe ser realizada por personal cualificado, que siga las pautas proporcionadas por la RFC 3227. 


#### Bibliografía

_[https://www.incibe-cert.es/blog/rfc3227](https://www.incibe-cert.es/blog/rfc3227)_
_[https://www.ietf.org/rfc/rfc3227.txt](https://www.ietf.org/rfc/rfc3227.txt)_

![](assets/IS-U311-RecopilacionDeEvidencias2.png)
