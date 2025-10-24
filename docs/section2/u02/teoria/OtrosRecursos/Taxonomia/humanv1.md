# REFERENCE TAXONOMY INCIDENT  Taxonomy Spanish version (human readable version)


This is the Spanish version of Reference Security Incident Classification Taxonomy (https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force)

Reference:
https://www.incibe-cert.es/sites/default/files/contenidos/guias/doc/guia_nacional_notificacion_gestion_ciberincidentes.pdf

Version: 1002


| CLASIFICACIÓN (1ª COLUMNA)                                   | EJEMPLOS DE INCIDENTES (2ª COLUMNA)        | Descripción / Ejemplos |
|---------------------------------------------------------      |------------------------------------   |------------------------|
| Contenido abusivo | Spam | O "correo masivo no solicitado", significa que el destinatario no ha concedido un permiso verificable para el envío del mensaje y que éste se envía como parte de una colección más amplia de mensajes, todos ellos con un contenido funcionalmente comparable. Este IoC se refiere a los recursos que conforman la infraestructura de spam, por ejemplo, los recolectores como los verificadores de direcciones, las URL en los correos electrónicos de spam, etc. |
| Contenido abusivo | Delito de odio | Bullying, contenido difamatorio o discriminatorio. Ej:  ciberacoso,  racismo,  amenazas  a  una  persona o dirigidas contra colectivos. |
| Contenido abusivo | Explotación sexual (infantil), contenido sexual o violento | Material que represente de manera visual contenido relacionado con pornografía infantil, apología de la violencia, etc. |
| Contenido malicioso | Sistema infectado | Sistema infectado con malware. Ej: Sistema, computadora o teléfono móvil infectado con un rootkit. |
| Contenido malicioso | Servidor C&C | Conexión con servidor de Mando y Control (C&C) mediante malware o sistemas infectados. |
| Contenido malicioso | Distribución de malware | Recurso usado para distribución de malware. Ej: recurso de una organización empleado para distribuir malware. |
| Contenido malicioso | Configuración de malware | Recurso que aloje ficheros de configuración de malware Ej: ataque de webinjects para troyano. |
| Obtención de información | Escaneo de redes | Envío de peticiones a un sistema para descubrir posibles debilidades. Se incluyen también procesos de comprobación o testeo para recopilar información de alojamientos, servicios y cuentas. Ej: peticiones DNS, ICMP, SMTP, escaneo de puertos. |
| Obtención de información | Análisis de paquetes | Observación y grabación del tráfico de redes. |
| Obtención de información | Ingeniería social | Recopilación de información personal sin el uso de la tecnología. Ej: mentiras, trucos, sobornos, amenazas. |
| Intento de intrusión | Exploitación de vulnerabilidades conocidas | Intento de compromiso de un sistema o de interrupción de un servicio mediante la explotación de vulnerabilidades con un identificador estandarizado (véase CVE). Ej: desbordamiento de buffer, puertas traseras, cross site scripting (XSS). |
| Intento de intrusión | Intento de acceso con vulneración de credenciales | Múltiples intentos de vulnerar credenciales. Ej: intentos de ruptura de contraseñas, ataque por fuerza bruta. |
| Intento de intrusión | Ataque desconocido | Ataque empleando exploit desconocido. |
| Intrusión | Compromiso de cuenta con privilegios | Compromiso de un sistema en el que el atacante ha adquirido privilegios. |
| Intrusión | Compromiso de cuenta sin privilegios | Compromiso de un sistema empleando cuentas sin privilegios. |
| Intrusión | Compromiso de aplicación | Compromiso de una aplicación mediante la explotación de vulnerabilidades de software. Ej: inyección SQL. |
| Intrusión | Robo | Intrusión física. Ej: acceso no autorizado a Centro de Proceso de Datos. |
| Disponibilidad | Denegación de servicio | Ataque de denegación de servicio. Ej: envío de peticiones a una aplicación web que provoca la interrupción o ralentización en la prestación del servicio. |
| Disponibilidad | Denegación de servicio distribuida | Ataque de denegación distribuida de servicio. Ej: inundación de paquetes SYN, ataques de reflexión y amplificación utilizando servicios basados en UDP. |
| Disponibilidad | Mala configuración | Mala configuración de aplicación que provoca problemas de disponibilidad de un servicio p.e. Servidor DNS con zona KSK raíz DNSSEC caducada. |
| Disponibilidad | Sabotaje | Sabotaje físico. Ej: cortes de cableados de equipos o incendios provocados. |
| Disponibilidad | Interrupción | Interrupciones por causas ajenas. Ej: desastre natural. |
| Compromiso de la información | Acceso no autorizado a información | Acceso no autorizado a información. Ej: robo de credenciales de acceso mediante interceptación de tráfico o mediante el acceso a documentos físicos. |
| Compromiso de la información | Modificación no autorizada de información | Modificación no autorizada de información. Ej: modificación por un atacante empleando credenciales sustraídas de un sistema o aplicación o encriptado de datos mediante ransomware. |
| Compromiso de la información | Pérdida de datos | Pérdida de información Ej: pérdida por fallo de disco duro o robo físico. |
| Fraude | Uso no autorizado de recursos | Uso de recursos para propósitos inadecuados, incluyendo acciones con ánimo de lucro. Ej: uso de correo electrónico para participar en estafas piramidales. |
| Fraude | Derechos de autor | Ofrecimiento o instalación de software carente de licencia u otro material protegido por derechos de autor. Ej: Warez |
| Fraude | Suplantación | Tipo de ataque en el que una entidad suplanta a otra para obtener beneficios ilegítimos. |
| Fraude | Phishing | Suplantación de otra entidad con la finalidad de convencer al usuario para que revele sus credenciales privadas. |
| Vulnerable | Criptografía débil | Servicios accesibles públicamente que puedan presentar criptografía débil. Ej: servidores web susceptibles de ataques POODLE/FREAK. |
| Vulnerable | Amplificador DDoS | Servicios accesibles públicamente que puedan ser empleados para la reflexión o amplificación de ataques DDoS. Ej: DNS open-resolvers o Servidores NTP con monitorización monlist. |
| Vulnerable | Servicios con acceso potencialmente no deseado | Servicios con acceso potencialmente no deseado. Ej: Telnet, RDP o VNC. |
| Vulnerable | Revelación de información | Acceso público a servicios en los que potencialmente pueda relevarse información sensible. Ej: SNMP o Redis. |
| Vulnerable | Sistema vulnerable | Sistema vulnerable. Ej: mala configuración de proxy en cliente (WPAD), versiones desfasadas de sistema. |
| Otro | No clasificado | Todos aquellos incidentes que no encajen en ninguna de las anteriores categorías. |
| Otro | Indeterminado | La clasificación del incidente es desconocida o indeterminada. |
| Test | Test | Pruebas. |

