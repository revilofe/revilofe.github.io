# U2.3.1 - Fuentes Abiertas (OSINT)

Note: Presentacion de la unidad 2.3.1. Se explica que veremos OSINT, footprinting, proceso, tecnicas, herramientas y limites legales.


---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

Note: Portada de la unidad. Recordar que el objetivo es aprender a investigar con fuentes abiertas de forma legal y ordenada.


---

## Indice

* 1. Introduccion y contexto
* 2. Uso de OSINT en ciberseguridad
* 3. Proceso OSINT
* 4. Tecnicas OSINT
* 5. Herramientas OSINT
* 6. Casos practicos y actividades
* 7. Retos eticos y legales
* 8. Recursos y lecturas

Note: Repaso del indice para situar a la clase y anticipar la estructura.


---

## 1. Introduccion a OSINT (Inteligencia de Fuentes Abiertas)

Note: Iniciamos con el contexto del analisis de incidentes y la idea de OSINT.


### 1. Introduccion a OSINT I

* Analisis del incidente: causa, alcance e impacto
* Recogida y analisis del entorno digital
* Tecnicas: monitorizacion, registros y entrevistas
* Footprinting: huella digital y datos tecnicos
* Modalidades: activo y pasivo
* OSINT: fuentes publicas y enfoque amplio

Note: Explica que antes de investigar hay que entender el incidente y el entorno. Introduce el footprinting como recopilacion tecnica, con enfoque activo y pasivo. Conecta esto con OSINT, que usa fuentes publicas y amplias.


### 1. Introduccion a OSINT II

* OSINT = recopilacion y analisis de fuentes abiertas
* Fuentes abiertas: publicas y de acceso legitimo
* Ambitos: ciberseguridad, periodismo, crimen, empresas
* Ejemplo: buscar documentos expuestos en Google
* Objetivo: inteligencia util sin intrusiones

Note: Define OSINT de forma clara. Aclara que las fuentes pueden ser publicas o legitimamente accesibles. Usa el ejemplo de documentos expuestos para reforzar el enfoque legal y etico.


### 1.1. Importancia y aplicaciones de OSINT

* Anticipa amenazas y evalua riesgos
* Apoya investigaciones forenses
* Mejora el pentesting con reconocimiento previo
* Protege la identidad digital
* Vigila datos filtrados en foros

Note: Subraya la importancia de OSINT en seguridad. No se trata solo de buscar informacion, sino de transformar datos en medidas de defensa.


### 1.1.1. Principales usos en ciberseguridad

* Amenazas en foros y redes sociales
* Evidencias en investigaciones forenses
* Reconocimiento previo a un pentest
* Mitigacion de exposicion personal
* Monitorizacion de mercados ilegales

Note: Aterriza los usos con ejemplos reales. Enfatiza que cada uso tiene un objetivo defensivo y preventivo.


### 1.2. Diferencias con otras metodologias I

* OSINT: fuentes publicas y legales
* HUMINT: informacion obtenida con personas
* SIGINT: interceptacion de comunicaciones
* ELINT: captura de datos electronicos
* SOCMINT: redes sociales

Note: Explica las metodologias de inteligencia y sus diferencias. Resalta que OSINT se basa en informacion de acceso publico.


### 1.2. Diferencias con otras metodologias II

* OSINT es legal si respeta acceso publico
* SIGINT sin permiso es ilegal
* Ejemplo: Wi-Fi publica vs PDFs indexados
* Etica y normativa siempre presentes

Note: Usa el ejemplo de Wi-Fi publica frente a PDFs indexados para mostrar el limite entre legal e ilegal. Recalca el marco etico y legal.


### 1.3. Proceso OSINT en una vista rapida

* Planificacion y direccion
* Identificacion de fuentes
* Adquisicion de informacion
* Procesamiento y organizacion
* Analisis e interpretacion
* Difusion y aplicacion

Note: Explica que el proceso OSINT es un ciclo y puede ser iterativo. Presenta las fases como una ruta practica.


### 1.4. Actividades

* Buscar huella digital propia en Internet
* Clasificar casos por metodologia
* Proponer una estrategia OSINT etica

Note: Actividades iniciales para conectar con el alumnado y fomentar criterio etico y metodologico.


---

## 2. Uso de OSINT en Ciberseguridad

Note: Bloque centrado en aplicaciones concretas dentro de la ciberseguridad.


### 2.1. Auditoria e investigacion forense

* Detectar informacion expuesta
* Analizar vulnerabilidades sin interaccion
* Obtener evidencias tras incidentes
* Ejemplo: credenciales en filtraciones
* Apoyo con Have I Been Pwned

Note: Explica que OSINT permite auditar sin tocar sistemas. El ejemplo de credenciales filtradas muestra el valor preventivo.


### 2.2. Pentesting y hacking etico

* Reconocimiento previo al pentest
* Google Dorking y redes sociales
* Metadatos en documentos publicos
* Ejemplo: `site:empresa.com filetype:pdf`

Note: El pentest empieza antes del escaneo activo. OSINT reduce riesgos y da contexto para pruebas mas efectivas.


### 2.3. Prevencion y Threat Intelligence

* Detectar filtraciones en Dark Web
* Analizar grupos de ciberdelincuentes
* Monitorizar menciones a la empresa
* Ejemplo: venta de acceso detectada

Note: OSINT es clave para anticipar ataques. El seguimiento de foros permite actuar antes de que exploten una vulnerabilidad.


### 2.4. Riesgos y limites legales

* No acceder a informacion privada
* No acoso ni suplantacion
* Respetar GDPR y normativa local
* Ejemplo: LinkedIn si, correo no

Note: La legalidad es un limite claro. OSINT no es hacking. Reforzar el respeto por privacidad y leyes.


### 2.5. Actividades

* Auditoria OSINT de empresa ficticia
* Deteccion de amenazas con OSINT
* Evaluar legalidad de escenarios

Note: Actividades para aplicar OSINT con criterio profesional y etico.


---

## 3. Proceso de OSINT

Note: Se detalla el ciclo completo de OSINT y sus fases.


### 3.1. Ciclo OSINT: fases y estructura

* Modelo de seis fases
* No siempre es lineal
* Puede requerir retrocesos
* Objetivo: inteligencia util

Note: Explica que el ciclo es flexible y se ajusta a la investigacion.


### 3.2. Planificacion y direccion

* Definir objetivos claros
* Establecer alcance y limites
* Fijar necesidades de informacion
* Ejemplo: credenciales filtradas

Note: Sin objetivos claros, la investigacion se dispersa. Esta fase marca la ruta y evita perdida de tiempo.


### 3.2.1. Errores comunes en esta fase

* Objetivos vagos o confusos
* Alcance mal definido
* No considerar la legalidad
* Falta de criterios de exito

Note: Resalta errores tipicos para evitar investigaciones sin rumbo.


### 3.3. Identificacion de fuentes

* Motores de busqueda
* Registros publicos
* Redes sociales
* Bases de datos filtradas
* Foros y Dark Web
* Archivos historicos

Note: Explica cada tipo de fuente y su utilidad. Incluye ejemplos como BOE y registros mercantiles, DeHashed, Pastebin, BreachForums, Tor y Wayback Machine. Destaca la verificacion de fiabilidad.


### 3.4. Adquisicion de informacion

* Recopilar datos de las fuentes
* Almacenar con orden y trazabilidad
* Fase mas larga del proceso
* Acotar para no saturar

Note: La adquisicion debe ser controlada. Se insiste en guardar contexto y fuentes.


### 3.4.1. Tecnicas de adquisicion

* Google Dorking
* Consultas WHOIS
* Herramientas: Shodan, Maltego, SpiderFoot
* Analisis de redes sociales

Note: Cada tecnica aporta un tipo de dato distinto. Combinar varias mejora la calidad del resultado.


### 3.5. Procesamiento y organizacion

* Clasificar por relevancia
* Eliminar duplicados
* Organizar para el analisis
* Verificar autenticidad

Note: El objetivo es transformar datos en informacion manejable. La calidad supera a la cantidad.


### 3.5.1. Errores comunes en esta fase

* No validar la informacion
* No documentar las fuentes
* Exceso de datos sin criterio
* Falta de registro de pasos

Note: Mantener un registro mejora la trazabilidad y el valor del informe.


### 3.6. Analisis e interpretacion

* Identificar patrones y tendencias
* Correlacionar fuentes distintas
* Detectar amenazas potenciales
* Extraer conclusiones accionables

Note: Es el paso donde los datos se convierten en inteligencia util.


### 3.6.1. Metodos de analisis OSINT

* Analisis de correlacion
* Identificacion de tendencias
* Visualizacion con Maltego

Note: La visualizacion ayuda a entender relaciones complejas y detectar puntos criticos.


### 3.7. Difusion y aplicacion

* Presentar resultados claros
* Elegir el formato adecuado
* Facilitar decisiones de seguridad
* Ejemplo: informe pericial

Note: Sin una buena presentacion, la inteligencia pierde valor. El informe debe ser claro y util.


### 3.7.1. Formatos comunes

* Informes escritos
* Graficos y diagramas
* Alertas de amenazas

Note: Cada formato se adapta al destinatario: tecnico, directivo o judicial.


### 3.8. Actividades

* Simulacion del ciclo OSINT
* Procesar credenciales ficticias
* Crear un informe completo

Note: Estas actividades refuerzan el trabajo en equipo y la documentacion.


---

## 4. Tecnicas de OSINT

Note: Bloque centrado en tecnicas concretas de busqueda y analisis.


### 4.1. Footprinting y Fingerprinting

* Footprinting: recopilacion general
* Fingerprinting: detalles tecnicos
* Complementarios en investigacion
* Ejemplo: dorks, WHOIS y LinkedIn

Note: Diferencia ambos conceptos y muestra como se usan en un pentest.


### 4.2. Google Dorking

* Operadores: site:, filetype:, intitle:
* Operadores: inurl: y "palabras"
* Busca informacion oculta en sitios
* Uso responsable y autorizado
* Ejemplo: `intitle:"index of"`

Note: Explica el valor del dorking y la necesidad de no acceder a contenido restringido.


### 4.2.1. Recursos para Google Dorking

* Google Hacking Database
* Repositorios de dorks
* Guias y cursos de apoyo

Note: Recursos para ampliar conocimiento sin improvisar. Recordar el uso etico.


### 4.3. Metadatos en documentos

* Documentos con datos ocultos
* Revelan autores y fechas
* Pueden exponer sistemas internos

Note: Los metadatos son una fuente de inteligencia. Explica riesgos de no limpiarlos.


### 4.3.1. Herramientas para metadatos

* ExifTool
* FOCA
* Metagoofil
* Ejemplo: `exiftool documento.pdf`

Note: Muestra herramientas habituales y su uso basico.


### 4.4. Busqueda en redes sociales

* Fuente clave de informacion
* Riesgo de exposicion personal
* Respetar privacidad y normas

Note: Resalta el valor y el riesgo. Se insiste en trabajar solo con perfiles publicos.


### 4.4.1. Herramientas en redes sociales

* Sherlock
* OSINTgram
* Twint

Note: Cada herramienta facilita la busqueda de usuarios y patrones.


### 4.5. Infraestructuras con WHOIS y DNS

* Identificar propietarios de dominios
* Consultar registros DNS
* Apoyar analisis de exposicion

Note: Explica el uso de WHOIS, NSLookup y Shodan para mapear activos.


### 4.5.1. Metodos comunes

* WHOIS para datos de registro
* NSLookup o Dig para DNS
* Shodan para dispositivos

Note: Reforzar que no se deben hacer escaneos sin autorizacion.


### 4.6. Monitorizacion Deep y Dark Web

* No indexado en buscadores
* Util para detectar filtraciones
* Acceso con precaucion

Note: Explica diferencias y riesgos. Limitarse a la observacion autorizada.


### 4.6.1. Herramientas Dark Web

* TOR Browser
* OnionScan
* DarkSearch

Note: Presenta herramientas y advierte de riesgos legales y tecnicos.


### 4.7. Analisis de imagenes y videos

* Verificar autenticidad
* Buscar origen y manipulación
* Extraer metadatos

Note: La analitica forense ayuda a detectar bulos y montajes.


### 4.7.1. Tecnicas forenses en imagenes

* Busqueda inversa (Google, TinEye)
* Metadatos con ExifTool
* FotoForensics para manipulacion

Note: Explica cada tecnica y cuando usarla. Refuerza el respeto a derechos.


### 4.8. Actividades

* Dorking en dominio ficticio
* Extraer metadatos de documentos
* Analisis de perfiles publicos
* Infraestructura con WHOIS y DNS
* Verificacion de imagenes

Note: Actividades practicas para consolidar tecnicas OSINT.


---

## 5. Herramientas OSINT

Note: Bloque dedicado a herramientas y buscadores especializados.


### 5.1. Motores de busqueda especializados

* Complementan a Google
* Acceso a otras fuentes
* Utiles para web profunda

Note: No todo esta en Google. Otros motores aportan perspectiva distinta.


### 5.1.1. Herramientas destacadas

* Google Dorking
* DuckDuckGo
* Bing y Yandex
* Wayback Machine

Note: Compara resultados y destaca el valor de historicos web.


### 5.2. Shodan

* Buscador de dispositivos conectados
* Detecta exposicion de servicios
* Util en auditorias

Note: Shodan muestra activos expuestos en Internet. Su uso debe ser responsable.


### 5.2.1. Caracteristicas principales

* Filtros por puertos y protocolos
* Busqueda por CVE
* Identificacion de activos propios
* Ejemplo: `port:3389`

Note: Explica como Shodan ayuda a descubrir superficies de ataque.


### 5.2.2. Recursos utiles de Shodan

* Consultas y filtros populares
* Ejemplos de busqueda
* Guias oficiales

Note: Recursos para practicar con consultas seguras y controladas.


### 5.3. Wayback Machine

* Versiones antiguas de sitios
* Recuperar informacion eliminada
* Detectar filtraciones pasadas

Note: Muestra el valor de la historia web para investigaciones.


### 5.4. Maltego

* Visualiza relaciones
* Mapea infraestructura y actores
* Apoya analisis de amenazas

Note: Herramienta clave para relacionar entidades en una investigacion.


### 5.4.1. Usos de Maltego en OSINT

* Relacionar correos, dominios y redes
* Identificar conexiones entre infraestructuras
* Analizar redes de amenazas y actores
* Visualizar relaciones complejas

Note: Este uso ayuda a entender dependencias y posibles vectores de ataque.


### 5.5. SpiderFoot

* Automatiza OSINT
* Mas de 200 fuentes
* IPs, dominios, correos, CVE

Note: Permite hacer barridos amplios con un enfoque sistematico.


### 5.6. OSINT Framework

* Directorio de herramientas
* Organizado por categorias
* Util para investigar por tema
* Acceso: https://osintframework.com

Note: Repositorio esencial para elegir herramientas segun necesidad.


### 5.7. Buscadores en redes sociales

* Twint para Twitter/X
* OSINTgram para Instagram
* CrossLinked para LinkedIn
* Telegram OSINT para canales

Note: Cada red social requiere herramientas especificas y respeto a normas.


### 5.8. Tecnicas de busqueda en redes

* Dorks en LinkedIn
* Busqueda avanzada en plataformas
* Ejemplo: `site:linkedin.com "trabaja en empresa"`
* Solo perfiles publicos

Note: Refuerza que el objetivo es informacion publica y uso etico.


### 5.9. Actividades

* Buscar dispositivos con Shodan
* Rastrear usuarios con Sherlock
* Dorking en dominio ficticio
* Extraer metadatos con ExifTool

Note: Actividades para practicar herramientas reales con datos controlados.


---

## 6. Casos Practicos y Actividades de OSINT

Note: Casos completos para aplicar las tecnicas aprendidas.


### 6.1. Google Dorking para info oculta

* Objetivo: aprender dorks basicos
* `site:empresa.com filetype:pdf`
* `intext:"password" site:pastebin.com`
* `intitle:"admin login" site:empresa.com`
* Documentar hallazgos

Note: Se trabaja el criterio de busqueda avanzada con dominio ficticio.


### 6.2. Analisis de dominios con WHOIS y DNS

* Obtener datos de registro
* `whois google.com`
* Consultar registros DNS
* `nslookup google.com`
* `dig google.com MX`
* Analizar infraestructura

Note: Los alumnos deben identificar propietario y servidores del dominio.


### 6.3. Dispositivos IoT con Shodan

* Buscar dispositivos expuestos
* Filtrar por pais y puerto
* `country:ES port:3389`
* `product:"Webcam"`
* Evaluar riesgos

Note: Se enfatiza la seguridad en dispositivos conectados.


### 6.4. Usuarios en redes con Sherlock

* Instalar y ejecutar Sherlock
* `python3 sherlock.py usuario`
* Rastrear presencia en plataformas
* Analizar exposicion

Note: Practica de rastreo con usuarios ficticios y reflexion sobre privacidad.


### 6.5. Analisis de imagenes

* Buscar origen con busqueda inversa
* Detectar manipulaciones
* Identificar fuentes fiables

Note: Actividad contra desinformacion y fake news.


### 6.6. Proyecto final OSINT

* Empresa ficticia como objetivo
* Recolectar datos publicos
* Analizar riesgos y recomendar

Note: Se integra todo el proceso OSINT en un informe final.


---

## 7. Retos Eticos y Legales de OSINT

Note: Se abordan limites legales, privacidad y buenas practicas.


### 7.1. Privacidad y derechos

* Respeto a datos personales
* Riesgo de doxxing
* Uso responsable de metadatos
* Cuidado con Dark Web

Note: Aunque la info sea publica, su uso puede ser delicado. Reforzar limites.


### 7.1.1. Principales preocupaciones

* Publicar datos con intencion de dano
* Perfiles usados sin consentimiento
* Metadatos como exposicion oculta

Note: Explica por que la privacidad sigue siendo un derecho.


### 7.2. Regulaciones legales

* GDPR en Europa
* Codigo Penal en España
* CCPA en California
* Leyes locales en LATAM

Note: Recordar que OSINT debe cumplir la normativa vigente del pais.


### 7.2.1. Principales regulaciones sobre privacidad

* GDPR (Union Europea)
* Codigo Penal en España (Art. 197)
* CCPA en California
* Leyes locales en LATAM

Note: Cada normativa define limites y obligaciones en el tratamiento de datos.


### 7.3. Buenas practicas y uso responsable

* Respetar la privacidad
* Cumplir la ley
* Proposito legitimo
* Verificar fuentes
* Minimizar datos

Note: Buenas practicas para un trabajo profesional y etico.


### 7.3. Buenas practicas y uso responsable II

* No divulgar datos sensibles
* Informar a afectados cuando proceda
* Documentar y justificar acciones

Note: Enfatiza la responsabilidad y la trazabilidad de la investigacion.


### 7.4. Actividades

* Evaluar casos eticos
* Analizar leyes de privacidad
* Caso practico con reglas claras

Note: Actividades para entrenar criterio legal y etico.


---

## 8. Recursos y lecturas recomendadas

Note: Cierre con recursos para ampliar conocimientos y buenas practicas.


### 8.1. Recursos recomendados

* OSINT desde cero
* OSINT Scraping
* Sock puppets en OSINT
* Tecnicas y herramientas OSINT
* Introduccion a Dark Web

Note: Indicar que son lecturas de referencia y deben citarse en trabajos.


### 8.2. Lectura recomendada

* Metodologia OSINT para investigar en Internet
* Autor: Julian Gutierrez
* Ediciones Ciberpatrulla (2021)

Note: Recordar derechos de autor y uso responsable de materiales.
