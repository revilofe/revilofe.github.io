![](assets/IS-U211-TaxonomiaDeIncidentes0.png)

__Taxonomía de incidentes de ciberseguridad__

#### RA1
a) Se ha clasificado y definido la taxonomía de incidentes de ciberseguridad que pueden afectar a la organización.

#### ÍNDICE

Motivación

Taxonomía

Taxonomía de Referencia para la Clasificación de Incidentes de Seguridad

Actividad

#### Motivación

__Diversidad\, variedad__

__Organización\, clasificación__

<span style="color:#FFFFFF"> __Ayuda para abordar la solución__ </span>

__No todos los ciberincidentes poseen las mismas características ni tienen las mismas implicaciones\.__

__Se considera necesario disponer de una taxonomía común de los posibles incidentes que se  registren__

<span style="color:#FFFFFF">Ayudará posteriormente a su análisis\, contención y erradicación\. </span>

#### Taxonomía

Clasificación u ordenación en grupos de cosas que tienen unas características comunes\.

![](assets/IS-U211-TaxonomiaDeIncidentes1.png)

#### Taxonomía de incidentes

La taxonomía definida en la  __Guía Nacional de Notificación y Gestión de Ciberincidentes__ \, se basa en la  _Taxonomía de Referencia para la Clasificación de Incidentes de Seguridad_ \, desarrollada coordinadamente por un grupo internacional de equipos de respuesta a incidentes \(textos sacados de INCIBE\):

_[https://github\.com/flosada/RSITaxonomy\_ES/blob/master/humanv1\.md](https://github.com/flosada/RSITaxonomy_ES/blob/master/humanv1.md)_

#### Taxonomía de Referencia para la Clasificación de Incidentes de Seguridad

#### Contenido abusivo

* __Contenido abusivo__
  * __SPAM__  __: correo electrónico masivo no solicitado\. El receptor del contenido no ha otorgado autorización válida para recibir un mensaje colectivo\.__
  * __Delito de odio__  __: contenido difamatorio o discriminatorio\. __  _Ejemplos: ciberacoso\, racismo\, amenazas a una persona o dirigidas contra colectivos_  __\.__
  * __Pornografía infantil\, contenido sexual o violento inadecuado__  __: material que represente de manera visual contenido relacionado con pornografía infantil\, apología de la violencia\, etc\.__

#### Contenido dañino

* __Contenido dañino__
  * __Sistema infectado__  __: sistema infectado con malware\. __  _Ejemplo: sistema\, computadora o teléfono móvil infectado con un rootkit_  __\.__
  * __Servidor C&C \(Mando y Control\)__  __: conexión con servidor de Mando y Control \(C&C\) mediante malware o sistemas infectados\.__
  * __Distribución de malware__  __: recurso usado para distribución de malware\. __  _Ejemplo: recurso de una organización empleado para distribuir malware_  __\.__
  * __Configuración de malware__  __: recurso que aloje ficheros de configuración de malware\. __  _Ejemplo: ataque de webinjects para troyano_  __\.__
  * __Malware dominio DGA__  __: nombre de dominio generado mediante DGA \(Algoritmo de Generación de Dominio\)\, empleado por malware para contactar con un servidor de Mando y Control \(C&C\)\.__

#### Obtención de información

* __Obtención de información__
  * __Escaneo de redes \(scanning\)__  __: envío de peticiones a un sistema para descubrir posibles debilidades\. Se incluyen también procesos de comprobación o testeo para recopilar información de alojamientos\, servicios y cuentas\. __  _Ejemplos: peticiones DNS\, ICMP\, SMTP\, escaneo de puertos_  __\.__
  * __Análisis de paquetes \(sniffing\)__  __: observación y grabación del tráfico de redes\.__
  * __Ingeniería social__  __: recopilación de información personal sin el uso de la tecnología\. __  _Ejemplos: mentiras\, trucos\, sobornos\, amenazas_  __\.__

#### Intento de intrusión

* __Intento de intrusión__
  * __Explotación de vulnerabilidades conocidas__  __: intento de compromiso de un sistema o de interrupción de un servicio mediante la explotación de vulnerabilidades con un identificador estandarizado \(véase CVE\)\. __  _Ejemplos: desbordamiento de buffer\, puertas traseras\, cross site scripting \(XSS\)_  __\.__
  * __Intento de acceso con vulneración de credenciales__  __: múltiples intentos de vulnerar credenciales\. __  _Ejemplos: intentos de ruptura de contraseñas\, ataque por fuerza bruta_  __\.__
  * __Ataque desconocido__  __: ataque empleando exploit desconocido\.__

#### Intrusión

* __Intrusión__
  * __Compromiso de cuenta con privilegios__  __: compromiso de un sistema en el que el atacante ha adquirido privilegios\.__
  * __Compromiso de cuenta sin privilegios__  __: compromiso de un sistema empleando cuentas sin privilegios\.__
  * __Compromiso de aplicaciones__  __: compromiso de una aplicación mediante la explotación de vulnerabilidades de software\. __  _Ejemplo: inyección SQL_  __\.__
  * __Robo__  __: intrusión física\. __  _Ejemplo: acceso no autorizado a Centro de Proceso de Datos y sustracción de equipo_  __\.__

#### Disponibilidad

* __Disponibilidad__
  * __DoS \(Denegación de Servicio\)__  __: ataque de Denegación de Servicio\. __  _Ejemplo: envío de peticiones a una aplicación web que provoca la interrupción o ralentización en la prestación del servicio_  __\.__
  * __DDoS \(Denegación Distribuida de Servicio\)__  __: ataque de Denegación Distribuida de Servicio\. __  _Ejemplos: inundación de paquetes SYN\, ataques de reflexión y amplificación utilizando servicios basados en UDP_  __\.__
  * __Sabotaje__  __: sabotaje físico\. __  _Ejemplos: cortes de cableados de equipos o incendios provocados_  __\.__
  * __Interrupciones__  __: interrupciones por causas externas\. __  _Ejemplo: desastre natural_  __\.__

#### Compromiso de la información

__Compromiso de la información__

__Acceso no autorizado a información__  __: acceso no autorizado a información\. __  _Ejemplos: robo de credenciales de acceso mediante interceptación de tráfico o mediante el acceso a documentos físicos_  __\.__

__Modificación no autorizada de información__  __: modificación no autorizada de información\. __  _Ejemplos: modificación por un atacante empleando credenciales sustraídas de un sistema o aplicación o encriptado de datos mediante ransomware_  __\.__

__Pérdida de datos__  __: pérdida de información\. __  _Ejemplos: pérdida por fallo de disco duro o robo físico_

#### Fraude

* __Fraude__
  * __Uso no autorizado de recursos__  __: uso de recursos para propósitos inadecuados\, incluyendo acciones con ánimo de lucro\. __  _Ejemplo: uso de correo electrónico para participar en estafas piramidales_  __\.__
  * __Derechos de autor__  __: ofrecimiento o instalación de software carente de licencia u otro material protegido por derechos de autor\. __  _Ejemplos: Warez_  __\.__
  * __Suplantación__  __: tipo de ataque en el que una entidad suplanta a otra para obtener beneficios ilegítimos\.__
  * __Phishing__  __: suplantación de otra entidad con la finalidad de convencer al usuario para que revele sus credenciales privadas\.__

#### 

* __Vulnerable__
  * __Criptografía débil__  __: servicios accesibles públicamente que pueden presentar criptografía débil\. __  _Ejemplo: servidores web susceptibles de ataques POODLE/FREAK_  __\.__
  * __Amplificador DDoS__  __: servicios accesibles públicamente que puedan ser empleados para la reflexión o amplificación de ataques DDoS\. __  _Ejemplos: DNS open\-resolvers o Servidores NTP con monitorización monlist_  __\.__
  * __Servicios con acceso potencial no deseado__  __: servicios accesibles públicamente potencialmente no deseados\. __  _Ejemplos: Telnet\, RDP o VNC_  __\.__
  * __Revelación de información__  __: acceso público a servicios en los que potencialmente pueda revelarse información sensible\. __  _Ejemplos: SNMP o Redis_  __\.__
  * __Sistema vulnerable__  __: sistema vulnerable\. __  _Ejemplos: mala configuración de proxy en cliente \(WPAD\)\, versiones desfasadas de sistema_  __\.__

#### Otros

* __Otros__
  * __Otros__  __: todo aquel incidente que no tenga cabida en ninguna categoría anterior\.__
  * __APT__  __: ataques dirigidos contra organizaciones concretas\, sustentados en mecanismos muy sofisticados de ocultación\, anonimato y persistencia\. Esta amenaza habitualmente emplea técnicas de ingeniería social para conseguir sus objetivos junto con el uso de procedimientos de ataque conocidos o genuinos\.__
  * __Ciberterrorismo__  __: uso de redes o sistemas de información con fines de carácter terrorista\.__
  * __Daños informáticos PIC__  __: borrado\, dañado\, alteración\, supresión o inaccesibilidad de datos\, programas informáticos o documentos electrónicos de una infraestructura crítica\. Conductas graves relacionadas con los términos anteriores que afecten a la prestación de un servicio esencial\.__

#### Actividad

_[2\.a\.01 \- Taxonomía de incidentes \(grupo\)Tarea](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/assign/view.php?id=411507)_

![](assets/IS-U211-TaxonomiaDeIncidentes2.png)

