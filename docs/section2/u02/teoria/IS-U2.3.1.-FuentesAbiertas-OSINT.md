---
title: "UD 2 - 2.3.1 Fuentes Abiertas. OSINT."
description: Fuentes Abiertas. OSINT
summary: Fuentes Abiertas. OSINT
authors:
    - Eduardo Fdez
date: 2025-02-11
icon: "material/file-document-outline"
permalink: /is/unidad2/2.3.1
categories:
    - IS
tags:
    - OSINT
---

# 2.3.1.- Fuentes Abiertas. OSINT

Al detectar un incidente se debe llevar a cabo un análisis mas detallado, comprender la causa, el alcance, etc. El objetivo es identificar la vulnerabilidad, evluar amenajas potenciales y detectar brechas de seguirad o indicios sobre porque se ha producido el incidente.

El análisis incluye:

- Recogida de la información
- AnálIsis de datos relacionados con el entorno digital de la organización: red de comunicaciones, sistemas, aplicaciones, empleados, usuarios, etc.

La recopilación de la información se realiza a través de diferentes técnicas y herramientas:

- Herramientas de monitorización de red: direcciones ip, dominios, protocolos. Por ejemplo *wireshark*
- Recopilación de datos de registro, que nos proporcionan información sobre las actividades o detectar anomalías producidas en los sistemas. Por ejmplo SIEM de elastic para recolectar datos de registros
- Entrevistas con miembros de personal, que nos dan información de los sistemas con los que trabajan, y nos pueden proporcionar detalles sobre posibles riesgos que no serán fáciles de detectar a través de herramientas. Por ejemplo: Software instalado q no se utiliza, contraseñas débiles o compartidas

El FOOTPRINTING hace referencia a la huella digital, técnica de recopilación de información que se usa en el hacking ético, y que consiste en recopilar datos del entorno digital de una org. para identificar vulnerabilidades y posibles puntos de entrada para la penetración. La información se obtiene de los sistemas informáticos y de la red, para recopilar datos de la org., de los empleados y socios externos. Se recopilan: SO, Config. de los cortafuegos, direcciones IP, Mapas de Red, Config. de seguridad, emails, password, Confg. de servidores, URLs, VPN, infor. de empleados, Nombres de dominios,etc

Este trabajo puede ser:

- Activo: Se interactúa con el SO para recopilar la info. a través de herramientas y técnicas como escaneos de red y comandos tipo traceroute o tracert
- Pasivo: No se interactúa, solo se consulta motores de búsqueda y redes sociales u otras fuentes publicas.

Cuando se hace a través de fuentes publicas, hablamos de OSINT. La diferencia entre fooprinting y OSINT, es que en el primero esta mas centrado en recopilar info técnica en un sistema concreto, mientras que en el segundo es un concepto más amplio que incluye varios métodos de recopilación de fuentes abiertas.

## 1. Introducción a OSINT (Inteligencia de Fuentes Abiertas)

OSINT (Open Source Intelligence) se refiere a la recopilación y análisis de información proveniente de fuentes públicas o accesibles libremente, con el objetivo de extraer inteligencia útil. Se emplea en diversos campos, como la ciberseguridad, el periodismo, la investigación criminal, el análisis de amenazas y la inteligencia empresarial.

**Ejemplo:**

Imagina que un investigador de ciberseguridad quiere analizar la posible filtración de datos de una empresa. En lugar de acceder ilegalmente a sus servidores, realiza búsquedas avanzadas en Google para encontrar documentos públicos que contengan credenciales expuestas.

### 1.1. Importancia y Aplicaciones de OSINT en Ciberseguridad

OSINT es una herramienta clave en el mundo de la seguridad informática, ya que permite anticiparse a posibles amenazas y evaluar riesgos sin la necesidad de acceder a información privada.

#### 1.1.1. Principales usos de OSINT en ciberseguridad:

1. **Detección de amenazas**: Identificación de posibles ataques dirigidos a una organización a partir de información pública en foros o redes sociales.
2. **Investigaciones forenses**: Análisis de incidentes de ciberseguridad mediante la recopilación de evidencias de fuentes abiertas.
3. **Pentesting y hacking ético**: Recopilación de datos de un objetivo antes de realizar pruebas de seguridad (footprinting y fingerprinting).
4. **Protección de la identidad digital**: Identificación de información personal expuesta en internet para mitigar posibles ataques de ingeniería social.
5. **Vigilancia de la dark web**: Monitoreo de mercados ilegales y foros donde se comercializan datos robados.

**Ejemplo:**

Un auditor de seguridad usa OSINT para descubrir que en un foro de hacking se están vendiendo credenciales de acceso a una empresa, permitiendo a la organización tomar medidas preventivas antes de sufrir un ataque.

### 1.2. Diferencias entre OSINT y otras metodologías de recopilación de información

OSINT se diferencia de otros métodos de inteligencia en que **toda la información obtenida es legalmente accesible**. No se trata de hacking ilegal ni de violar la privacidad de los usuarios.


| **Método**                            | **Descripción**                                               | **Ejemplo**                                                                            |
| -------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **OSINT**(Open Source Intelligence)    | Recopilación de información pública y accesible legalmente. | Búsqueda de información en redes sociales y bases de datos públicas.                |
| **HUMINT**(Human Intelligence)         | Obtención de información mediante interacción con personas. | Entrevistas a empleados o infiltración en eventos.                                    |
| **SIGINT**(Signals Intelligence)       | Intercepción de señales de comunicación.                    | Escucha de comunicaciones en redes inalámbricas.                                      |
| **ELINT**(Electronic Intelligence)     | Captura de datos electrónicos.                                | Análisis de tráfico de red con herramientas como Wireshark.                          |
| **SOCMINT**(Social Media Intelligence) | Recopilación de información en redes sociales.               | Análisis de perfiles de LinkedIn y Twitter para identificar empleados de una empresa. |

**Ejemplo:**

Un atacante malintencionado usa **SIGINT** para interceptar el tráfico de red y capturar contraseñas en una WiFi pública (actividad ilegal). En cambio, un auditor de seguridad usa **OSINT** para analizar si la empresa ha expuesto contraseñas en documentos PDF indexados en Google (actividad legal).

OSINT es una metodología poderosa que permite recopilar información sin infringir leyes ni normas éticas. Su correcta aplicación en ciberseguridad permite detectar vulnerabilidades, prevenir ataques y mejorar la protección de datos personales y corporativos.

### 1.4. Actividades

1. **Ejercicio 1: ¿Qué información hay sobre ti en Internet?**       
   Pide a los alumnos que busquen su propio nombre en Google y redes sociales para analizar qué información pública existe sobre ellos.    
   Discusión: ¿Es peligroso? ¿Cómo podrían mejorar su privacidad?      
2. **Ejercicio 2: Comparación de metodologías de inteligencia**    
   Presenta a los alumnos varios casos ficticios y pídeles que clasifiquen si el método utilizado es OSINT, HUMINT, SIGINT, etc.    
3. **Ejercicio 3: OSINT en la vida real**    
   Divide a los alumnos en grupos y entrégales diferentes escenarios (ej. "Una empresa quiere saber qué información sensible está expuesta en internet").    
   Deberán proponer estrategias de OSINT para recopilar información útil de forma ética y legal.   

## 2. Uso de OSINT en Ciberseguridad

El uso de OSINT (Inteligencia de Fuentes Abiertas) en ciberseguridad es fundamental para identificar amenazas, evaluar vulnerabilidades y proteger la información de una organización. Esta metodología permite recopilar información de fuentes públicas para anticiparse a posibles ataques y fortalecer la seguridad digital.

### 2.1. OSINT en Auditoría de Seguridad e Investigación Forense

La recopilación de información de fuentes abiertas es una herramienta clave en las auditorías de seguridad y en la investigación de incidentes. OSINT permite:

* Identificar información expuesta que podría ser utilizada por atacantes.
* Analizar vulnerabilidades en infraestructuras y sistemas sin interacción directa.
* Obtener evidencias en investigaciones forenses tras un ataque.

**Ejemplo:**

Un equipo de ciberseguridad quiere evaluar si una empresa tiene credenciales filtradas en internet. Utilizan OSINT para buscar en bases de datos de filtraciones como **"Have I Been Pwned?"** y descubren que varias cuentas de correo de empleados han sido comprometidas.

### 2.2. OSINT en Pentesting y Hacking Ético

Antes de realizar una prueba de penetración (pentesting), los expertos en seguridad usan OSINT para recolectar información del objetivo sin necesidad de lanzar escaneos activos que puedan ser detectados.

Las técnicas OSINT aplicadas en pentesting incluyen:

* **Google Dorking** para encontrar documentos sensibles expuestos.
* **Búsqueda en redes sociales** para obtener información sobre empleados.
* **Análisis de metadatos** en documentos públicos para descubrir información interna.

**Ejemplo:**

Un pentester usa Google para buscar información sobre una empresa antes de un ataque:

```txt
site:empresa.com filetype:pdf
```

Encuentra un documento con metadatos que contienen nombres de usuario internos, lo que podría facilitar ataques de fuerza bruta.

### 2.3. OSINT en Prevención de Ataques y Detección de Amenazas (Threat Intelligence)

El análisis OSINT es una parte esencial de la **inteligencia sobre amenazas (Threat Intelligence)**, ya que permite monitorear posibles ataques antes de que ocurran.

Los expertos en ciberseguridad pueden:

* **Detectar filtraciones** de datos en la dark web.
* **Analizar grupos de ciberdelincuentes** que planean ataques.
* **Monitorear menciones** a la empresa en foros de hacking.

**Ejemplo:**

Una empresa de ciberseguridad detecta en un foro clandestino que se vende acceso a su red corporativa. Gracias a OSINT, identifica las credenciales filtradas y obliga a los empleados a cambiarlas antes de que sean explotadas.

### 2.4. Riesgos y Límites Legales de OSINT

Aunque OSINT se basa en la recopilación de información pública, es fundamental respetar la **legalidad y la ética** en su aplicación.

Algunos **límites legales** incluyen:

* No acceder a información privada sin permiso (ej. correos electrónicos protegidos).
* No usar OSINT con fines de acoso, espionaje o suplantación de identidad.
* Respetar normativas de privacidad como el **GDPR** en Europa.

**Ejemplo:**

Un investigador de OSINT quiere obtener datos sobre una persona. Es legal buscar su perfil de LinkedIn, pero no lo es entrar a su correo privado sin permiso.

> OSINT es una herramienta poderosa en ciberseguridad, pero su uso debe estar guiado por principios éticos y legales. Aplicado correctamente, permite anticiparse a ataques, fortalecer la seguridad y mejorar la protección de la información.

### 2.5. Actividades

1. **Ejercicio 1: OSINT en auditoría de seguridad**
   Los alumnos deben buscar información pública sobre una empresa ficticia utilizando OSINT (Google Dorking, redes sociales, WHOIS).
   Reflexión: ¿Qué información expuesta podría ser peligrosa?
2. **Ejercicio 2: Identificación de amenazas con OSINT**
   Se da a los alumnos un caso de posible ataque a una empresa.
   Deben investigar en fuentes OSINT para detectar si hay información filtrada en foros o la dark web.
3. **Ejercicio 3: Legalidad y ética en OSINT**
   Se presentan varios escenarios y los alumnos deben decidir si la actividad es legal o ilegal.

## 3. Proceso de OSINT

El proceso de OSINT sigue un ciclo estructurado para garantizar la recolección, análisis y utilización efectiva de la información obtenida de fuentes abiertas. Aunque existen varias metodologías, el modelo más común consta de **seis fases**.

### 3.1. Ciclo OSINT: Fases y Estructura

El ciclo OSINT es un modelo teórico que guía la recopilación, procesamiento y análisis de información. Sus fases no siempre son secuenciales, ya que a veces es necesario volver a etapas previas para mejorar la precisión de los datos obtenidos.

Las **seis fases del ciclo OSINT** son:

1. **Planificación y dirección**
2. **Identificación de fuentes**
3. **Adquisición de información**
4. **Procesamiento y organización**
5. **Análisis e interpretación**
6. **Difusión y aplicación de la inteligencia**

### 3.2. Planificación y Dirección

La fase inicial consiste en definir **qué información se necesita** y establecer los objetivos de la investigación OSINT.

**Ejemplo:**

Una empresa quiere saber si existen filtraciones de datos de sus empleados. Se establecen los siguientes objetivos:

* Buscar credenciales filtradas en bases de datos públicas.
* Analizar redes sociales en busca de información sensible.
* Identificar vulnerabilidades en su infraestructura digital.

#### 3.2.1. Errores comunes en esta fase

Durante la planificación, es importante evitar errores como:

* No definir claramente el alcance de la investigación.
* Buscar información sin un objetivo específico.
* No considerar aspectos legales y éticos antes de iniciar.

### 3.3. Identificación de Fuentes de Información

Una vez definidos los objetivos, se deben identificar las **fuentes** de donde se obtendrá la información.  Los requisitos nos guiarán a la hora de identificar las fuentes potenciales desde las que recopilar la información

Algunas fuentes OSINT incluyen:

* **Motores de búsqueda:** Google, Bing, DuckDuckGo.
* **Registros públicos:** BOE, registros mercantiles, patentes.
* **Redes sociales:** Twitter, Facebook, LinkedIn, Telegram.
* **Bases de datos filtradas:** Have I Been Pwned?, DeHashed.
* **Foros y Dark Web:** Pastebin, BreachForums, Tor.
* **Archivos históricos:** Wayback Machine.

**Ejemplo:**

Un investigador busca información sobre una empresa en **Wayback Machine** para ver cómo ha cambiado su página web a lo largo del tiempo y descubrir si en el pasado expuso información sensible.

### 3.4. Adquisición de Información

En esta fase se recopila activamente la información de las fuentes identificadas. Se trabaja en la recopilación a partir de las fuentes. La información se almacena y se tratará posteriormente. Suele ser la fase más larga. Hay que acotar las fuentes adecuadamente para no alargar mucho.

#### 3.4.1. Técnicas de adquisición OSINT:

1. **Google Dorking:** Uso de operadores avanzados en Google para encontrar información oculta.
2. **Búsqueda en registros WHOIS:** Identificación de propietarios de dominios web.
3. **Uso de herramientas especializadas:** Shodan (dispositivos conectados), Maltego (visualización de relaciones), SpiderFoot (automatización de OSINT).
4. **Análisis de redes sociales:** Herramientas como Sherlock permiten rastrear nombres de usuario en múltiples plataformas.

**Ejemplo:**

Un investigador usa Google Dorking para encontrar los paneles phpMyAdmin en el sitio web de la empresa target:

```txt
site:target.com inurl:"/phpmyadmin/"
```

Encuentra paneles que tienen que estar ocultos al acceso externo.

### 3.5. Procesamiento y Organización de Datos

Después de recopilar la información, es necesario:

* Clasificarla según su relevancia y fiabilidad.
* Eliminar datos redundantes o irrelevantes.
* Organizarla de manera que facilite su análisis.

Si durante el procesamiento surgen nuevos requisitos, se vuelve a la fase de identificación de fuentes.

**Ejemplo:**

Un equipo de seguridad ha encontrado **100 posibles credenciales filtradas**. Ahora deben:

* Eliminar registros duplicados.
* Verificar si las contraseñas aún son válidas.
* Evaluar si las cuentas comprometidas pertenecen a usuarios activos.

#### 3.5.1. Errores comunes en esta fase

Al procesar los datos, es importante evitar errores como:

* No verificar la autenticidad de la información.
* No documentar adecuadamente las fuentes de los datos obtenidos.
* Recopilar información en exceso sin un criterio claro.

### 3.6. Análisis e Interpretación de Datos

Aquí es donde la información se convierte en **inteligencia útil**. El análisis debe identificar patrones, correlaciones y amenazas potenciales.

**Ejemplo:**

Un analista de seguridad detecta que varias cuentas de empleados han sido filtradas junto con sus contraseñas. Analiza los patrones y descubre que la mayoría de las contraseñas son débiles y repetitivas.

#### 3.6.1. Métodos de análisis OSINT

Los métodos de análisis incluyen:

* **Análisis de correlación:** Relacionar datos de diferentes fuentes para obtener conclusiones.
* **Identificación de tendencias:** Detectar patrones recurrentes en filtraciones de datos.
* **Visualización de datos:** Uso de herramientas como **Maltego** para representar conexiones entre información.

### 3.7. Difusión y Aplicación de la Inteligencia

Finalmente, la información obtenida se presenta de forma clara para que los responsables de seguridad puedan tomar decisiones. Presentar los resultados, a través de medio adecuado para que sea útil y comprensible. Si es un peritaje informático para una investigación, sería a través de un informe pericial informáticos que se remite al tribunal competente.

#### 3.7.1. Formatos comunes de presentación

Para difundir la inteligencia OSINT, se utilizan:

* Informes escritos detallados.
* Visualización de datos en gráficos o diagramas de relaciones.
* Alertas sobre amenazas emergentes.

**Ejemplo:**

Un analista OSINT elabora un informe sobre una filtración de datos de empleados de una empresa, recomendando:

1. Obligar a los empleados a cambiar sus contraseñas.
2. Implementar autenticación en dos factores (2FA).
3. Monitorear foros de hacking en busca de futuras filtraciones.

El proceso OSINT es un ciclo estructurado que permite convertir datos dispersos en **inteligencia útil** para la ciberseguridad. Una correcta planificación y análisis permiten anticiparse a amenazas y mejorar la protección de la información.

### 3.8. Actividades

1. **Ejercicio 1: Simulación de un Ciclo OSINT**
   Dividir a los alumnos en grupos.
   Cada grupo investiga un objetivo ficticio siguiendo las fases del ciclo OSINT.
   Al final, presentan un informe con sus hallazgos y recomendaciones.
2. **Ejercicio 2: Adquisición y Procesamiento de Datos**
   Se les da a los alumnos un conjunto de datos de credenciales filtradas (ficticias).
   Deben procesar y organizar la información para identificar patrones y riesgos.
3. **Ejercicio 3: Creación de un Informe OSINT**
   Cada alumno selecciona un tema de investigación OSINT (por ejemplo, análisis de redes sociales de una marca).
   Deben realizar el proceso completo y elaborar un informe detallado con sus hallazgos.

## 4. Técnicas de OSINT

Para que la recopilación de información OSINT sea efectiva, se utilizan diversas **técnicas y estrategias** que permiten encontrar, extraer y analizar datos relevantes de fuentes públicas. Estas técnicas pueden aplicarse en ciberseguridad, investigación forense, análisis de amenazas y otros campos.

### 4.1. Footprinting y Fingerprinting

**Footprinting**: Es el proceso de recopilar información sobre un objetivo (persona, empresa, sistema) sin interactuar directamente con él. Permite entender la infraestructura, tecnologías y servicios utilizados.

**Fingerprinting**: Se refiere a la identificación de características específicas de sistemas, dispositivos o usuarios, como versiones de software, sistemas operativos o configuraciones de red.

La diferencia entre ambos radica en que el footprinting es más amplio y se enfoca en la recopilación de información general, mientras que el fingerprinting es más específico y se centra en identificar características técnicas.

**Ejemplo:**

Un pentester usa OSINT para recopilar información sobre una empresa antes de realizar un ataque de prueba. Utiliza:

* **Google Dorking** para encontrar documentos internos.
* **WHOIS y Shodan** para identificar servidores y direcciones IP públicas.
* **LinkedIn** para conocer a los empleados y sus roles dentro de la empresa.

### 4.2. Google Dorking: Búsquedas Avanzadas en Google

Google Dorking (también conocido como Google Hacking) permite encontrar información oculta usando operadores avanzados en Google.


| **Operador**   | **Función**                               | **Ejemplo**                     |
| -------------- | ------------------------------------------ | ------------------------------- |
| **site:**      | Busca dentro de un dominio específico     | `site:empresa.com`              |
| **filetype:**  | Filtra por tipo de archivo (PDF, XLS, DOC) | `filetype:pdf site:empresa.com` |
| **intitle:**   | Busca en el título de una página web     | `intitle:"Acceso restringido"`  |
| **inurl:**     | Busca en las URL de los sitios web         | `inurl:admin login`             |
| **"palabras"** | Búsqueda exacta                           | `"documento confidencial"`      |

**Ejemplo:**

Un investigador usa el siguiente comando para buscar carpetas de administración de WordPress en un sitio web:

```
site:target.com intitle:"index of" "wp-admin"
```

Encuentra archivos con información interna que nunca debieron ser públicos.

#### 4.2.1. Recursos para Google Dorking

Algunos recursos útiles para Google Dorking son:    

* https://achirou.com/dorks-de-google-hacking-para-osint/    

* https://www.exploit-db.com/google-hacking-database    

* https://github.com/chr3st5an/Google-Dorking    

* https://github.com/Tobee1406/Awesome-Google-Dorks    

* https://www.udemy.com/course/osint-de-principiante-a-experto-en-investigacion-digital/    




### 4.3. Recopilación de Metadatos en Documentos

Los documentos digitales (PDF, DOC, JPG, etc.) contienen **metadatos ocultos** que pueden revelar información sobre sus autores, fechas de creación y herramientas utilizadas.

#### 4.3.1. Herramientas OSINT para extraer metadatos:

* **ExifTool**: Extrae metadatos de imágenes, documentos y archivos multimedia.
* **FOCA**: Analiza documentos para extraer metadatos y descubrir servidores internos.
* **Metagoofil**: Automatiza la búsqueda de documentos en un dominio y extrae sus metadatos.

**Ejemplo:**

Un auditor de seguridad descarga un documento de una empresa y usa **ExifTool**:

```bash
exiftool documento.pdf
```

Descubre que el archivo contiene nombres de usuarios internos y la versión de software utilizada para crearlo.

### 4.4. Búsqueda de Información en Redes Sociales

Las redes sociales son una fuente clave de información OSINT. Muchos empleados y directivos publican datos sensibles sin darse cuenta. La búsqueda en redes sociales permite identificar posibles vulnerabilidades y filtraciones de datos. Es importante respetar la privacidad de los usuarios y no infringir las normas de las plataformas.

#### 4.4.1. Herramientas para OSINT en redes sociales

Algunas herramientas especializadas en OSINT en redes sociales son:

* **Sherlock**: Busca nombres de usuario en múltiples plataformas.
* **OSINTgram**: Extrae información de perfiles de Instagram.
* **Twint**: Recopila datos de Twitter sin necesidad de una cuenta.

**Ejemplo:**

Un investigador quiere saber si un hacker está activo en redes sociales. Usa **Sherlock**:

```Bash
python3 sherlock.py usuario
```

Obtiene una lista de redes sociales donde el usuario tiene cuentas.

### 4.5. Identificación de Infraestructuras con WHOIS, DNS y Direcciones IP

La información sobre dominios y servidores puede obtenerse con herramientas OSINT. WHOIS, NSLookup y Shodan son útiles para identificar propietarios de dominios, registros DNS y dispositivos conectados a internet. Estas técnicas son fundamentales para el análisis de infraestructuras y la detección de vulnerabilidades. Es importante respetar las normativas de privacidad y no realizar escaneos sin autorización.

#### 4.5.1. Métodos comunes

Algunos métodos comunes para identificar infraestructuras son:

* **WHOIS**: Identifica el propietario de un dominio y sus datos de registro.
* **NSLookup/Dig**: Consulta registros DNS de un dominio.
* **Shodan**: Encuentra dispositivos y servidores conectados a internet.

**Ejemplo:**

Un investigador quiere saber quién registró un dominio. Usa **WHOIS**:

```bash
whois empresa.com
```

Obtiene el nombre, correo y dirección del registrante.

### 4.6. Monitorización de la Deep y Dark Web

La Deep Web y la Dark Web contienen información que no aparece en buscadores convencionales. La monitorización de estos espacios es esencial para detectar amenazas y filtraciones de datos. Es importante tener en cuenta que acceder a la Dark Web puede ser peligroso y debe hacerse con precaución. Se recomienda utilizar herramientas especializadas y respetar la legalidad.

#### 4.6.1. Herramientas para exploración en la Dark Web

Algunas herramientas para explorar la Dark Web son:

* **TOR Browser**: Permite acceder a sitios .onion.
* **OnionScan**: Identifica vulnerabilidades en servicios ocultos.
* **DarkSearch**: Un buscador especializado en la Dark Web.

**Ejemplo:**

Un analista de seguridad usa TOR para buscar filtraciones de datos de una empresa en foros de hacking.

### 4.7. Análisis de Imágenes y Videos con Técnicas Forenses

Las imágenes y videos contienen datos ocultos que pueden ser analizados con OSINT. La búsqueda inversa de imágenes, el análisis de metadatos y la detección de manipulaciones son técnicas útiles para verificar la autenticidad de los archivos y descubrir información oculta. Es importante respetar los derechos de autor y la privacidad de las personas.

#### 4.7.1. Técnicas forenses en imágenes

Algunas técnicas forenses en imágenes son:

* **Búsqueda inversa de imágenes** (Google Images, TinEye).
* **Análisis de metadatos con ExifTool**.
* **Comparación de imágenes para detectar manipulaciones (FotoForensics).

**Ejemplo:**

Un investigador encuentra una imagen sospechosa en internet. Usa Google Imágenes para verificar su autenticidad y descubre que ha sido modificada para desinformar.

Las técnicas OSINT permiten extraer información valiosa de fuentes abiertas de manera ética y legal. Su correcto uso en ciberseguridad ayuda a prevenir ataques, detectar amenazas y fortalecer la defensa de organizaciones y personas.

### 4.8. Actividades

1. **Ejercicio 1: Google Dorking**
   Los alumnos deben usar operadores avanzados de Google para encontrar información pública de un sitio web (ficticio).
   Reflexión: ¿Qué riesgos implica que una empresa exponga archivos en internet?
2. **Ejercicio 2: Extracción de Metadatos**
   Se proporciona un conjunto de documentos (ficticios).
   Los alumnos deben analizar los metadatos con **ExifTool** o **FOCA**.
3. **Ejercicio 3: Análisis OSINT en Redes Sociales**
   Cada alumno investiga un perfil público de una celebridad o empresa (sin invadir la privacidad).
   Discusión: ¿Qué información personal puede obtenerse legalmente de redes sociales?
4. **Ejercicio 4: Identificación de Infraestructura**
   Los alumnos usan **WHOIS** y **NSLookup** para analizar dominios.
   Reflexión: ¿Cómo podrían los ciberdelincuentes utilizar esta información?
5. **Ejercicio 5: Búsqueda Inversa de Imágenes**
   Se presentan imágenes falsas y los alumnos deben verificar su autenticidad con Google Imágenes o TinEye.

## 5. Herramientas OSINT

Las herramientas OSINT permiten automatizar la recopilación y análisis de información de fuentes abiertas. Se dividen en varias categorías según el tipo de datos que procesan, desde buscadores especializados hasta herramientas de análisis de redes sociales y metadatos. Es importante elegir las herramientas adecuadas para cada objetivo y respetar las normativas de privacidad y legalidad.

El uso de herramientas OSINT especializadas permite automatizar la recopilación de información y el análisis de datos de fuentes abiertas. Estas herramientas son fundamentales en ciberseguridad, investigación forense y análisis de amenazas para identificar vulnerabilidades, prevenir ataques y proteger la información.

### 5.1. Motores de Búsqueda Especializados

Aunque Google es el buscador más conocido, existen herramientas específicas que permiten acceder a información más detallada. Estos motores de búsqueda especializados facilitan la búsqueda de datos en la web profunda, la dark web y otros espacios no indexados por Google.

#### 5.1.1. Herramientas destacadas

Algunos motores de búsqueda especializados son:

* **Google Dorking**: Usa operadores avanzados para encontrar información oculta en internet.
* **DuckDuckGo**: No rastrea las búsquedas y permite encontrar información que Google filtra.
* **Bing y Yandex**: Alternativas para obtener resultados distintos a los de Google.
* **Wayback Machine**: Permite ver versiones antiguas de sitios web y detectar cambios en su contenido.

**Ejemplo:**

Un investigador usa **Wayback Machine** para revisar cómo lucía un sitio web antes de una supuesta filtración de datos.

### 5.2. Shodan: Búsqueda de Dispositivos Conectados a Internet

**Shodan** es un motor de búsqueda que permite encontrar dispositivos conectados a internet como servidores, cámaras de seguridad, routers, sistemas industriales, etc. Es útil para identificar vulnerabilidades en infraestructuras y evaluar la exposición de activos a posibles ataques. Los resultados de Shodan pueden ser utilizados en auditorías de seguridad, pentesting y análisis de amenazas.

#### 5.2.1. Características principales de Shodan

Algunas características de Shodan son:

* Permite filtrar por **puertos abiertos, protocolos y versiones de software**.
* Se pueden buscar **dispositivos vulnerables** según CVEs (vulnerabilidades conocidas).
* Ayuda a las empresas a identificar **sus propios activos expuestos**.

**Ejemplo:**

Un pentester busca dispositivos con acceso remoto expuesto mediante el puerto **3389** (Remote Desktop Protocol):

`port:3389`

Encuentra varios servidores accesibles sin autenticación segura.

#### 5.2.2. Recursos utiles para Shodan

Algunos recursos útiles para Google Dorking son:

- https://github.com/jakejarvis/awesome-shodan-queries    

- https://hayageek.com/shodan-search-queries/    

- https://help.shodan.io/the-basics/search-query-fundamentals    

- https://www.shodan.io/search/examples    

- https://github.com/JavierOlmedo/shodan-filters    



### 5.3. Wayback Machine: Análisis de Versiones Antiguas de Sitios Web

**Wayback Machine** permite acceder a versiones archivadas de sitios web, lo que ayuda a:

* **Analizar cambios en una web a lo largo del tiempo**.
* **Recuperar información eliminada** por administradores.
* **Detectar filtraciones accidentales** de datos en versiones anteriores de un sitio.

**Ejemplo:**

Un investigador encuentra que un sitio web eliminó un archivo con nombres de empleados. Usa **Wayback Machine** para ver versiones anteriores del sitio y recuperar la información.

### 5.4. Maltego: Visualización y Análisis de Relaciones

**Maltego** es una herramienta de inteligencia que permite visualizar conexiones entre personas, organizaciones y servidores. Es útil para mapear infraestructuras digitales, identificar relaciones entre entidades y analizar redes de amenazas. Maltego se utiliza en ciberseguridad, investigación forense y análisis de inteligencia.

#### 5.4.1. Usos de Maltego en OSINT

Algunos usos de Maltego en OSINT son:

* Relacionar direcciones de correo, nombres de dominio y redes sociales.
* Identificar conexiones entre infraestructuras digitales.
* Analizar redes de amenazas y actores malintencionados.

**Ejemplo:**

Un investigador introduce un dominio en **Maltego** y descubre conexiones con otras webs de la misma empresa, lo que ayuda a mapear su infraestructura digital.

### 5.5. SpiderFoot: Automatización de la Recopilación OSINT

**SpiderFoot** permite realizar búsquedas automatizadas en más de **200 fuentes** para recopilar información sobre:

* **Direcciones IP y dominios**.
* **Correos electrónicos filtrados**.
* **Vulnerabilidades conocidas** en sistemas.
* **Perfiles en redes sociales**.

**Ejemplo:**

Un investigador ejecuta **SpiderFoot** sobre un dominio y descubre que está relacionado con varias direcciones IP en otros países, lo que sugiere la existencia de servidores adicionales no documentados.

### 5.6. OSINT Framework: Repositorio de Herramientas OSINT

**OSINT Framework** es un directorio online con herramientas de código abierto organizadas por categorías:

* **Búsqueda de usuarios y correos electrónicos**.
* **Análisis de redes sociales**.
* **Investigación de dominios y direcciones IP**.

🌍 **Acceso:**[https://osintframework.com](https://osintframework.com)

**Ejemplo:**

Un investigador usa OSINT Framework para encontrar herramientas gratuitas para analizar redes sociales sin necesidad de registrarse.

### 5.7. Buscadores de Información en Redes Sociales

Las redes sociales son una fuente clave de información OSINT. Existen herramientas especializadas en cada plataforma:


| **Red Social** | **Herramienta OSINT** | **Descripción**                               |
| -------------- | --------------------- | ---------------------------------------------- |
| **Twitter/X**  | **Twint**             | Extrae tuits sin necesidad de cuenta.          |
| **Instagram**  | **Osintgram**         | Permite analizar perfiles sin iniciar sesión. |
| **LinkedIn**   | **CrossLinked**       | Extrae datos de empleados de una empresa.      |
| **Telegram**   | **Telegram OSINT**    | Rastrea usuarios y grupos públicos.           |

**Ejemplo:**

Un investigador usa **Twint** para analizar la actividad de un usuario de Twitter sin necesidad de iniciar sesión. Descubre que ha publicado información sensible sobre su empresa.

### 5.8. Técnicas de Búsqueda en Telegram, LinkedIn, Twitter, Facebook

Cada red social tiene técnicas de búsqueda avanzadas para obtener información pública. Estas técnicas permiten encontrar perfiles, grupos y publicaciones relevantes sin necesidad de una cuenta. Es importante respetar la privacidad de los usuarios y no infringir las normas de las plataformas.

**Ejemplo:**

Para buscar empleados de una empresa en LinkedIn sin iniciar sesión:

```bash
site:linkedin.com "trabaja en empresa"
```

Esto muestra perfiles públicos de personas que mencionan trabajar en la empresa.

Las herramientas OSINT permiten recopilar información de forma rápida y organizada. Su uso responsable y ético es clave para evitar violaciones de privacidad y legalidad.

### 5.9. Actividades

1. **Ejercicio 1: Uso de Shodan**
   Los alumnos buscan dispositivos conectados a internet con Shodan y analizan su exposición.
2. **Ejercicio 2: Análisis de redes sociales con Sherlock**
   Se les asigna un nombre de usuario y deben rastrear en qué redes sociales está presente.
3. **Ejercicio 3: Búsqueda de datos con Google Dorking**
   Se les da un dominio y deben encontrar información oculta usando operadores de Google.
4. **Ejercicio 4: Extracción de metadatos con ExifTool**
   Se proporciona un conjunto de imágenes y documentos para que extraigan sus metadatos.


## 6. Casos Prácticos y Actividades de OSINT

Para que los alumnos comprendan y apliquen el conocimiento sobre **OSINT**, es fundamental trabajar con **casos prácticos y ejercicios** que simulen situaciones reales. En este apartado, se presentan seis ejercicios prácticos que permitirán a los estudiantes desarrollar sus habilidades en inteligencia de fuentes abiertas. Estos ejercicios pueden adaptarse a diferentes niveles de conocimiento y ser utilizados en cursos de ciberseguridad, análisis forense y prevención de amenazas.

### 6.1. Ejercicio: Uso de Google Dorking para encontrar información oculta

**Objetivo:**

Enseñar a los alumnos a utilizar **búsquedas avanzadas en Google** para encontrar información que no está fácilmente accesible.

**Instrucciones:**

* Explicar el concepto de **Google Dorking** y sus operadores.
* Presentar una serie de búsquedas específicas con operadores avanzados:

   Encontrar archivos PDF en un dominio:

   `site:empresa.com filetype:pdf`

   Buscar páginas con credenciales filtradas:

   `intext:"password" site:pastebin.com`

   Ver páginas de administración de un sitio:

   `intitle:"admin login" site:empresa.com`    

* Pedir a los alumnos que realicen búsquedas sobre un dominio ficticio y **documenten sus hallazgos**.

**Resultados esperados:**

* Comprensión del uso de **Google Dorking**.
* Identificación de **información expuesta accidentalmente**.

### 6.2. Ejercicio: Análisis de dominios con WHOIS y DNS

**Objetivo:**

Enseñar cómo obtener información de un **dominio** mediante herramientas OSINT.

**Instrucciones:**

* Explicar cómo funcionan **WHOIS** y las consultas **DNS**.
* Pedir a los alumnos que usen **WHOIS** para investigar un dominio:

   `whois google.com`   

* Usar **nslookup** o **dig** para obtener registros DNS:

   ```
   nslookup google.com
   dig google.com MX
   ```   

* Analizar los resultados y responder:

   ¿Quién registró el dominio?
   ¿Dónde están sus servidores?
   ¿Hay correos electrónicos filtrados?

**Resultados esperados:**

* Identificación de **propietarios de dominios**.
* Análisis de **infraestructura digital**.

### 6.3. Ejercicio: Identificación de dispositivos IoT con Shodan

**Objetivo**

Mostrar cómo se pueden encontrar **cámaras, routers y servidores** expuestos en internet con Shodan.

**Instrucciones:**

* Explicar qué es **Shodan** y cómo funciona.
* Pedir a los alumnos que busquen dispositivos en España con ciertos puertos abiertos:

   `country:ES port:3389`
   `product:"Webcam"`   

* Analizar los resultados y responder:

   ¿Cuántos dispositivos hay expuestos?
   ¿Qué riesgos de seguridad tienen?

**Resultados esperados:**

* Comprender la importancia de **seguridad en dispositivos conectados**.
* Identificar **errores comunes en configuraciones de red**.

### 6.4. Ejercicio: Búsqueda de usuarios en redes sociales con Sherlock

**Objetivo:**

Aprender a rastrear **nombres de usuario** en múltiples plataformas.

**Instrucciones:**

* Explicar cómo **los ciberdelincuentes usan OSINT** en redes sociales.
* Instalar y ejecutar **Sherlock**:

   ```bash
   python3 sherlock.py usuario
   ```   

* Elegir un usuario ficticio y analizar:
   ¿En qué plataformas está presente?
   ¿Se puede obtener más información sobre él?

**Resultados esperados:**

* Concienciación sobre **riesgos de exposición en redes sociales**.
* Desarrollo de habilidades de **recolección de datos en plataformas públicas**.

### 6.5. Ejercicio: Análisis de imágenes con búsqueda inversa

**Objetivo:**

Mostrar cómo verificar la **autenticidad de imágenes** mediante herramientas OSINT.

**Instrucciones:**

* Explicar qué es la **búsqueda inversa de imágenes**.    
* Proporcionar a los alumnos imágenes sospechosas.   
* Usar **Google Images** o **TinEye** para rastrear su origen.   

**Resultados esperados:**

* Identificar **fuentes originales de imágenes**.
* Detectar **fake news y manipulación de imágenes**.

### 6.6. Proyecto Final: Investigación OSINT sobre una empresa ficticia

**Objetivo:**

Aplicar todas las técnicas aprendidas en un caso completo de investigación.

**Instrucciones:**

* Dividir a los alumnos en grupos y asignarles una empresa ficticia.    
* Cada grupo deberá:    

    - Encontrar información pública sobre la empresa (Google Dorking, WHOIS, Shodan).    
    - Analizar perfiles de empleados en redes sociales.    
    - Buscar posibles vulnerabilidades de seguridad.    

* Presentar un **informe final** con:    

    - **Hallazgos clave**.   
    - **Riesgos detectados**.
    - **Recomendaciones de seguridad**.    

**Resultados esperados:**

* Capacidad para realizar **investigaciones OSINT completas**.
* Desarrollo de habilidades en **ciberseguridad y análisis forense**.

Las actividades prácticas son esenciales para que los alumnos entiendan **cómo funciona OSINT en el mundo real**. Estos ejercicios les permiten desarrollar una **mentalidad analítica**, fortalecer sus habilidades en **ciberseguridad** y comprender la **importancia de la privacidad en línea**.

Las actividades prácticas son esenciales para entender **cómo funciona OSINT en el mundo real**. Estos ejercicios les permiten desarrollar una **mentalidad analítica**, fortalecer sus habilidades en **ciberseguridad** y comprender la **importancia de la privacidad en línea**. Un resumen de las actividades propuestas:


| **Ejercicio**                        | **Objetivo**                                        | **Herramientas utilizadas**  |
| ------------------------------------ | --------------------------------------------------- | ---------------------------- |
| **Google Dorking**                   | Encontrar información oculta en Google             | Google, operadores avanzados |
| **Análisis de dominios**            | Identificar propietarios y servidores de un dominio | WHOIS, nslookup, dig         |
| **Uso de Shodan**                    | Detectar dispositivos expuestos en internet         | Shodan                       |
| **Investigación en redes sociales** | Rastrear nombres de usuario en varias plataformas   | Sherlock, LinkedIn, Twitter  |
| **Búsqueda inversa de imágenes**   | Verificar autenticidad de imágenes                 | Google Images, TinEye        |
| **Proyecto Final OSINT**             | Aplicar todas las técnicas en un caso real         | Todas las herramientas       |

## 7. Retos Éticos y Legales de OSINT

El uso de **OSINT** (Open Source Intelligence) implica la recopilación y análisis de información de fuentes abiertas. Sin embargo, aunque la información sea pública, su uso indebido puede generar problemas **legales y éticos**. En este apartado se abordan las consideraciones clave para garantizar un uso responsable de OSINT.

### 7.1. Privacidad y Derechos de los Usuarios

La recopilación de información OSINT debe respetar la privacidad de las personas y las organizaciones. Aunque los datos sean accesibles públicamente, su recolección y análisis pueden representar riesgos. Es fundamental tener en cuenta las normas de privacidad y los derechos de los usuarios al utilizar OSINT.

#### 7.1.1. Principales preocupaciones sobre privacidad en OSINT

Algunas preocupaciones comunes sobre privacidad en OSINT son:

* **Doxxing:** Publicación de información personal con intención de dañar o acosar a alguien.
* **Perfiles en redes sociales:** Aunque la información sea pública, usarla sin consentimiento puede ser considerado una invasión a la privacidad.
* **Metadatos ocultos:** Extraer información oculta de documentos e imágenes puede ser problemático si se usa con fines maliciosos.
* **Dark Web:** Monitorear foros en la Dark Web puede llevar a la exposición de datos sensibles o ilegales.

**Ejemplo:**

Un analista OSINT encuentra información personal de un individuo en un foro. Aunque los datos sean públicos, compartirlos sin su consentimiento podría violar leyes de privacidad.

### 7.2. Regulaciones Legales (GDPR, Código Penal, Normativas de Privacidad)

El uso de OSINT está regulado por diversas leyes que protegen la privacidad de los datos personales. Es importante conocer las normativas legales aplicables en cada país para evitar problemas legales y sanciones. Algunas de las regulaciones más comunes son el **GDPR** (General Data Protection Regulation), el **Código Penal** y las leyes de protección de datos personales.

#### 7.2.1. Principales regulaciones sobre privacidad

| **Regulación**                                                       | **Descripción**                                                          | **Ámbito**    |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------- |
| **GDPR (General Data Protection Regulation)**                         | Regula la recopilación y uso de datos personales en la UE.               | Europa         |
| **Código Penal (España, Art. 197)**                                 | Penaliza el acceso y uso indebido de información privada.                | España        |
| **CCPA (California Consumer Privacy Act)**                            | Protege los datos personales de los ciudadanos de California.             | EE.UU.         |
| **Ley de Protección de Datos Personales (México, Argentina, etc.)** | Establece normas para la recopilación y tratamiento de datos personales. | Latinoamérica |


**Ejemplo:**

Un investigador OSINT recopila correos electrónicos expuestos en una filtración y los almacena en una base de datos. Según el **GDPR**, si estos datos incluyen información personal identificable, su uso sin consentimiento puede ser ilegal.

### 7.3. Buenas Prácticas y Uso Responsable de OSINT

Para evitar problemas éticos y legales, es fundamental seguir **buenas prácticas** en la recopilación y análisis de información de fuentes abiertas. Respetar la privacidad, cumplir con las regulaciones y utilizar OSINT de manera ética son aspectos clave para un uso responsable.

#### 7.3.1. Principios de uso ético de OSINT

Algunos principios éticos para el uso de OSINT son:

1. **Respeto a la privacidad:** No recopilar ni divulgar información personal sin consentimiento.
2. **Cumplimiento legal:** Conocer y respetar las regulaciones de protección de datos.
3. **Propósito legítimo:** Utilizar OSINT solo para fines de seguridad, investigación o análisis legítimo.
4. **Fuentes verificadas:** Asegurar que la información recopilada proviene de fuentes confiables y legítimas.
5. **Minimización de datos:** Recopilar solo la información necesaria para la investigación.

**Ejemplo:**

Una empresa de ciberseguridad usa OSINT para identificar filtraciones de datos. En lugar de divulgar la información públicamente, contacta a la empresa afectada para advertirle sobre la vulnerabilidad.

El uso de OSINT implica un equilibrio entre la obtención de información y el respeto por la privacidad y la legalidad. Aplicar **buenas prácticas** y conocer las normativas legales es esencial para evitar problemas éticos y jurídicos.

### 7.4. Actividades

1. **Ejercicio 1: Evaluación de casos éticos en OSINT**
   Se presentan diferentes escenarios y los alumnos deben determinar si la actividad es legal y ética.
   **Ejemplo:** ¿Es correcto recolectar información de empleados en LinkedIn para un análisis de seguridad?
2. **Ejercicio 2: Análisis de regulaciones sobre privacidad**
   Cada grupo investiga una ley de privacidad (GDPR, CCPA, etc.).
   Explican cómo afecta el uso de OSINT y presentan ejemplos de casos legales.
3. **Ejercicio 3: Uso ético de OSINT en un caso práctico**
   Se asigna un caso ficticio donde los alumnos deben recopilar información con OSINT, asegurando que cumplen las normas legales y éticas.

Como resumen, se presentan las **consideraciones éticas y legales** más importantes en el uso de OSINT:

| **Aspecto**         | **Consideraciones Éticas y Legales**                              |
| ------------------- | -------------------------------------------------------------------- |
|
| **Privacidad**      | No exponer información personal sin consentimiento.               |
| **Regulaciones**    | Cumplir con normativas como GDPR, CCPA y leyes nacionales.         |
| **Uso Responsable** | OSINT solo debe utilizarse con fines legítimos y éticos.         |
| **Riesgos**         | Uso indebido puede llevar a sanciones legales o problemas éticos. |
