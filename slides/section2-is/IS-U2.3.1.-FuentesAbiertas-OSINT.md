# U2.3.1 - Fuentes Abiertas (OSINT)

Note: Presentacion de la unidad 2.3.1. El objetivo es entender **OSINT** como metodo de investigacion con **fuentes abiertas**, diferenciarlo de **footprinting**, y aplicar un **proceso** ordenado (de principio a fin) sin salirnos de la **legalidad** y la **etica**.

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

Note: Portada de la unidad. Recalcar desde el inicio que OSINT no es "hackear": es **buscar, verificar y analizar** informacion accesible de forma **legitima**, documentando siempre el **origen** de los datos.

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

Note: Repaso del indice para situar a la clase. Adelanta que el bloque mas importante sera el **proceso OSINT** (como trabajar paso a paso) porque es lo que se aplica en los **casos practicos** y en el mundo profesional.

---

## 1. Introduccion a OSINT (Inteligencia de Fuentes Abiertas)

Note: Iniciamos con el contexto del analisis de incidentes: primero necesitamos **informacion** para entender causa, alcance e impacto. OSINT aporta contexto rapido sin tocar sistemas, pero exige **metodo**, **criterio** y **documentacion**.


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

Note: Define OSINT de forma clara y corta: **recopilar + analizar**. Aclara que "fuentes abiertas" significa **acceso legitimo** (no credenciales robadas ni acceso indebido). Usa el ejemplo de documentos expuestos para hablar de **busqueda avanzada** y de por que esto es util en incidentes.


### 1.1. Importancia y aplicaciones de OSINT

* Anticipa amenazas y evalua riesgos
* Apoya investigaciones forenses
* Mejora el pentesting con reconocimiento previo
* Protege la identidad digital
* Vigila datos filtrados en foros

Note: Subraya que OSINT no es "coleccionar enlaces": el valor esta en convertir datos en **decisiones** (por ejemplo, cambiar contraseñas, cerrar exposiciones, priorizar un riesgo). Repite la idea: **calidad** y **contexto** por encima de cantidad.


### 1.1.1. Principales usos en ciberseguridad

* Amenazas en foros y redes sociales
* Evidencias en investigaciones forenses
* Reconocimiento previo a un pentest
* Mitigacion de exposicion personal
* Monitorizacion de mercados ilegales

Note: Aterriza los usos con ejemplos reales y remarca el enfoque **defensivo**: anticiparse, confirmar hipotesis y reducir incertidumbre. Puedes preguntar: "¿Que tipo de dato buscarias primero si sospechas phishing o fuga de credenciales?"


### 1.2. Diferencias con otras metodologias I

* OSINT: fuentes publicas y legales
* HUMINT: informacion obtenida con personas
* SIGINT: interceptacion de comunicaciones
* ELINT: captura de datos electronicos
* SOCMINT: redes sociales

Note: Explica las metodologias de inteligencia y sus diferencias. Destaca que OSINT es **publico/legitimo**; HUMINT implica **personas**; SIGINT/ELINT implican **interceptacion** (normalmente con fuertes limites legales); SOCMINT se centra en **redes sociales**.


### 1.2. Diferencias con otras metodologias II

* OSINT es legal si respeta acceso publico
* SIGINT sin permiso es ilegal
* Ejemplo: Wi-Fi publica vs PDFs indexados
* Etica y normativa siempre presentes

Note: Usa el ejemplo de Wi-Fi publica frente a PDFs indexados para marcar el limite: OSINT es **observar** y **analizar** fuentes legitimas, no **interceptar**. Recalca que la **etica** y la **normativa** no son un "extra": son parte del trabajo.


### 1.3. Proceso OSINT en una vista rapida

* Planificacion y direccion
* Identificacion de fuentes
* Adquisicion de informacion
* Procesamiento y organizacion
* Analisis e interpretacion
* Difusion y aplicacion

Note: Presenta el proceso como un **ciclo**: definimos objetivo, buscamos, recogemos, limpiamos, analizamos y comunicamos. Insiste en que puede ser **iterativo**: si aparece una pista nueva, volvemos a fases anteriores de forma controlada.


### 1.4. Actividades

* Buscar huella digital propia en Internet
* Clasificar casos por metodologia
* Proponer una estrategia OSINT etica

Note: Actividades iniciales para conectar con el alumnado: (1) ver su propia huella digital, (2) diferenciar metodologias, (3) proponer una estrategia OSINT. Aprovecha para hablar de **privacidad** y de que no todo lo "publico" es apropiado de usar.

---

## 2. Uso de OSINT en Ciberseguridad

Note: Bloque centrado en aplicaciones concretas. Idea clave: OSINT aporta **evidencia contextual** y reduce el "ruido" antes de pasar a tecnicas mas invasivas (forense, escaneos, pruebas activas).


### 2.1. Auditoria e investigacion forense

* Detectar informacion expuesta
* Analizar vulnerabilidades sin interaccion
* Obtener evidencias tras incidentes
* Ejemplo: credenciales en filtraciones
* Apoyo con Have I Been Pwned

Note: Explica que OSINT permite auditar sin tocar sistemas: buscamos **exposicion** y **señales**. Con el ejemplo de credenciales, enfatiza medidas accionables: **reset**, **2FA**, y revisar si hay **reutilizacion** de contraseñas.


### 2.2. Pentesting y hacking etico

* Reconocimiento previo al pentest
* Google Dorking y redes sociales
* Metadatos en documentos publicos
* Ejemplo: `site:empresa.com filetype:pdf`

Note: El pentest empieza antes del escaneo activo: OSINT ayuda a entender "que hay" y "que podria doler". Remarca que el objetivo es preparar un **reconocimiento** mas preciso, sin generar ruido ni salirse del **alcance** acordado.


### 2.3. Prevencion y Threat Intelligence

* Detectar filtraciones en Dark Web
* Analizar grupos de ciberdelincuentes
* Monitorizar menciones a la empresa
* Ejemplo: venta de acceso detectada

Note: OSINT es clave para anticipar ataques: vigilar menciones, filtraciones y venta de accesos. Destaca la idea de **ventana de reaccion**: cuanto antes lo detectas, mas facil es cortar el impacto (reset, bloqueo, rotacion de claves).


### 2.4. Riesgos y limites legales

* No acceder a informacion privada
* No acoso ni suplantacion
* Respetar GDPR y normativa local
* Ejemplo: LinkedIn si, correo no

Note: La legalidad es un limite claro. OSINT no es hacking: es trabajar con informacion **publica/legitima** sin **acceso no autorizado**, **suplantacion** ni **acoso**. Repite el principio: si dudas, **paras** y validas el marco legal o el permiso.


### 2.5. Actividades

* Auditoria OSINT de empresa ficticia
* Deteccion de amenazas con OSINT
* Evaluar legalidad de escenarios

Note: Actividades para aplicar OSINT con criterio profesional: que documenten **fuentes**, **fecha/hora**, **busquedas** y **conclusiones**. El entregable ideal es un mini-informe, no una lista de enlaces.

---
## 3. Proceso de OSINT

Note: Se detalla el ciclo completo de OSINT. Mensaje para el profesor: aqui queremos que el alumnado vea OSINT como **proceso reproducible** (pasos claros, evidencias, y decisiones), no como "buscar cosas en Internet".


### 3.1. Ciclo OSINT: fases y estructura

* Modelo de seis fases
* No siempre es lineal
* Puede requerir retrocesos
* Objetivo: inteligencia util

Note: Explica el modelo de **seis fases** y recalca que no es estrictamente lineal: es normal volver atras si una fuente no cuadra o aparece una pista nueva. Idea clave: cada fase produce un **resultado** que alimenta a la siguiente (y todo queda documentado).


### 3.2. Planificacion y direccion I

* Definir objetivos claros
* Establecer alcance y limites
* Fijar necesidades de informacion
* Ejemplo: credenciales filtradas

Note: Sin **objetivos** claros, la investigacion se dispersa. Enfatiza que aqui se decide el **alcance** (que buscamos y que no), y los **limites** (tiempo, legalidad, permisos). Pide que formulen 2-3 **preguntas** concretas que guiaran toda la busqueda.


### 3.2. Planificacion y direccion II

* Definir preguntas: que, quien, cuando, donde y por que
* Preparar palabras clave y variaciones
* Elegir entregables: informe, alerta o lista de IOCs
* Definir criterios de exito y cierre
* Registrar supuestos y riesgos (sesgos, fuentes dudosas)

Note: Convierte la planificacion en algo operativo: **preguntas**, **keywords**, **entregables** y **criterios de exito**. Remarca que documentar supuestos evita sesgos y facilita justificar por que se investigo una cosa y no otra.


### 3.2.1. Errores comunes en esta fase

* Objetivos vagos o confusos
* Alcance mal definido
* No considerar la legalidad
* Falta de criterios de exito

Note: Resalta errores tipicos para evitar investigaciones sin rumbo. Puedes usar un ejemplo: objetivo vago ("ver que hay") frente a objetivo concreto ("confirmar si hay correos del dominio X en filtraciones publicas").


### 3.3. Identificacion de fuentes I

* Motores de busqueda
* Registros publicos
* Redes sociales
* Bases de datos filtradas
* Foros y Dark Web
* Archivos historicos

Note: Explica cada tipo de fuente y su utilidad. Destaca que una "fuente" no es solo una web: tambien son **registros**, **historicos** (Wayback) y **bases de datos**. Repite la regla: siempre evaluar **fiabilidad** (autor, fecha, evidencia) y anotar el **contexto**.


### 3.3. Identificacion de fuentes II

* Crear una matriz: pregunta -> fuentes -> evidencia esperada
* Priorizar por valor vs esfuerzo (primero lo rapido y fiable)
* Triangular: no quedarse con una sola fuente
* Registrar URLs, capturas y fecha/hora de consulta

Note: Propone una forma practica de trabajar: **matriz de fuentes** y **priorizacion**. Recalca la **triangulacion** (confirmar con 2 fuentes) y la necesidad de guardar evidencias con fecha para poder repetir la investigacion.


### 3.4. Adquisicion de informacion I

* Recopilar datos de las fuentes
* Almacenar con orden y trazabilidad
* Fase mas larga del proceso
* Acotar para no saturar

Note: La adquisicion debe ser controlada: recoger lo necesario y con orden. Enfatiza **trazabilidad**: que busqueda hiciste, cuando, donde y que encontraste. Sin trazabilidad, los resultados no se pueden defender ni repetir.


### 3.4. Adquisicion de informacion II

* Guardar evidencias: capturas, exportaciones y notas de busqueda
* Mantener cadena de consulta: query -> resultado -> conclusion
* Separar datos brutos de datos procesados
* Automatizar solo lo que puedas explicar y reproducir

Note: Aqui el objetivo es que el alumnado trabaje como analista: evidencias y pasos claros. Diferencia **datos brutos** (lo que sale de la fuente) de **datos trabajados** (limpios/enriquecidos) para evitar confusiones.


### 3.4.1. Tecnicas de adquisicion

* Google Dorking
* Consultas WHOIS
* Herramientas: Shodan, Maltego, SpiderFoot
* Analisis de redes sociales

Note: Cada tecnica aporta un tipo de dato distinto. Recomienda combinar tecnicas (por ejemplo, dorks + WHOIS + redes) pero sin perder el foco del objetivo. Remarca que todo debe quedar documentado y dentro del **permiso**.


### 3.5. Procesamiento y organizacion I

* Clasificar por relevancia
* Eliminar duplicados
* Organizar para el analisis
* Verificar autenticidad

Note: El objetivo es transformar datos en informacion manejable: limpiar, ordenar y validar. Mensaje clave: **calidad > cantidad**. Si el alumnado se pierde en cientos de registros, probablemente falto criterio en fases anteriores.


### 3.5. Procesamiento y organizacion II

* Normalizar formatos (nombres, fechas, dominios, IPs)
* Deduplicar y agrupar por entidad (persona, dominio, activo)
* Etiquetar fiabilidad: confirmado, probable, dudoso
* Enriquecer con cuidado (sin inventar datos)

Note: Explica el "como": normalizar, deduplicar y etiquetar fiabilidad. Recalca que el **enriquecimiento** debe ser prudente: si una fuente no confirma, se marca como **dudoso** y no se presenta como hecho.


### 3.5.1. Errores comunes en esta fase

* No validar la informacion
* No documentar las fuentes
* Exceso de datos sin criterio
* Falta de registro de pasos

Note: Mantener un **registro** mejora la trazabilidad y el valor del informe. Puedes sugerir una plantilla minima: fuente, fecha, query, evidencia, fiabilidad, y nota de por que es relevante.


### 3.6. Analisis e interpretacion I

* Identificar patrones y tendencias
* Correlacionar fuentes distintas
* Detectar amenazas potenciales
* Extraer conclusiones accionables

Note: Es el paso donde los datos se convierten en **inteligencia util**: responder preguntas, confirmar o descartar hipotesis y priorizar riesgos. Recalca que el analisis debe acabar en algo accionable (no solo "he encontrado X").


### 3.6. Analisis e interpretacion II

* Formular hipotesis y buscar evidencias a favor y en contra
* Correlacionar entidades: dominio, correo, IP, usuario, fecha
* Controlar sesgos: confirmacion, autoridad, disponibilidad
* Separar hechos, inferencias y suposiciones

Note: Guia al profesor para insistir en pensamiento critico: hipotesis, evidencias y control de **sesgos**. Pide al alumnado que distinga entre **hechos** (verificables) e **inferencias** (conclusion razonada).


### 3.6.1. Metodos de analisis OSINT

* Analisis de correlacion
* Identificacion de tendencias
* Visualizacion con Maltego

Note: La visualizacion ayuda a entender relaciones complejas (por ejemplo, un mismo correo apareciendo en varias filtraciones). Recalca que un grafo bonito no vale si no explica una conclusion clara y comprobable.


### 3.7. Difusion y aplicacion I

* Presentar resultados claros
* Elegir el formato adecuado
* Facilitar decisiones de seguridad
* Ejemplo: informe pericial

Note: Sin una buena presentacion, la inteligencia pierde valor. Insiste en adaptar el mensaje a la audiencia (tecnica vs directiva) y en incluir **evidencias** y **recomendaciones** claras: que hacer, quien lo hace y con que prioridad.


### 3.7. Difusion y aplicacion II

* Estructura: resumen, hallazgos, evidencias, impacto, acciones
* Incluir limites: que no se pudo verificar o quedo fuera
* Usar lenguaje claro y sin tecnicismos innecesarios
* Añadir anexos con capturas, enlaces y queries

Note: Explica como "empaquetar" el trabajo: un informe con **resumen ejecutivo**, hallazgos y acciones. Recalca que declarar **limites** aumenta la credibilidad y evita conclusiones exageradas.


### 3.7.1. Formatos comunes

* Informes escritos
* Graficos y diagramas
* Alertas de amenazas

Note: Cada formato se adapta al destinatario: tecnico, directivo o judicial. Aprovecha para recordar que, si el contexto es pericial, la documentacion debe ser especialmente cuidadosa (fuentes, fechas, evidencias y trazabilidad).


### 3.8. Actividades

* Simulacion del ciclo OSINT
* Procesar credenciales ficticias
* Crear un informe completo

Note: Estas actividades refuerzan el trabajo en equipo y la documentacion. Pide que entreguen: objetivo, fuentes usadas, evidencias, conclusiones y 3 recomendaciones priorizadas.

---

## 4. Tecnicas de OSINT

Note: Bloque centrado en tecnicas concretas. Recalca que una **tecnica** es el "como" (dorks, metadatos, WHOIS), mientras que una **herramienta** es el "con que". La eleccion depende del **objetivo** y de la fase del **proceso OSINT**.


### 4.1. Footprinting y Fingerprinting

* Footprinting: recopilacion general
* Fingerprinting: detalles tecnicos
* Complementarios en investigacion
* Ejemplo: dorks, WHOIS y LinkedIn

Note: Aclara la diferencia: **footprinting** da vision general (organizacion, activos, huella), y **fingerprinting** baja al detalle (versiones, tecnologias, configuraciones). Conecta con el proceso: primero contexto, luego precision, y siempre respetando el **alcance**.


### 4.2. Google Dorking

* Operadores: site:, filetype:, intitle:
* Operadores: inurl: y "palabras"
* Busca informacion oculta en sitios
* Uso responsable y autorizado
* Ejemplo: `intitle:"index of"`

Note: Explica el valor del dorking: encontrar exposiciones accidentales (docs, backups, listados) con operadores. Repite el limite: localizar no es lo mismo que **acceder**; si aparece un panel o carpeta sensible, se documenta y se reporta sin interactuar.


### 4.2.1. Recursos para Google Dorking

* Google Hacking Database
* Repositorios de dorks
* Guias y cursos de apoyo

Note: Recursos para ampliar conocimiento sin improvisar. Recomienda crear una "chuleta" de dorks por objetivo (docs, paneles, indices) y recordar siempre el uso **etico** y dentro de **autorizacion**.


### 4.3. Metadatos en documentos

* Documentos con datos ocultos
* Revelan autores y fechas
* Pueden exponer sistemas internos

Note: Los metadatos son una fuente de inteligencia porque revelan **quien** creo un documento, **cuando** y con que herramienta. Insiste en el riesgo: pueden exponer usuarios internos, rutas, impresoras o ubicaciones; por eso se deben **limpiar** antes de publicar.


### 4.3.1. Herramientas para metadatos

* ExifTool
* FOCA
* Metagoofil
* Ejemplo: `exiftool documento.pdf`

Note: Muestra herramientas habituales y su uso basico. Recalca que el resultado debe guardarse como **evidencia** (salida, captura, fecha) y que no se deben subir documentos sensibles a servicios online para analizarlos.


### 4.4. Busqueda en redes sociales

* Fuente clave de informacion
* Riesgo de exposicion personal
* Respetar privacidad y normas

Note: Resalta el valor (roles, tecnologias, ubicaciones, relaciones) y el riesgo (ingenieria social y doxxing). Repite reglas: solo **perfiles publicos**, sin suplantacion, sin contacto ni acoso, y minimizando datos personales en el informe.


### 4.4.1. Herramientas en redes sociales

* Sherlock
* OSINTgram
* Twint

Note: Cada herramienta facilita la busqueda de usuarios y patrones, pero no sustituye el criterio humano. Pide al alumnado validar resultados (falsos positivos) y respetar **ToS** y **privacidad**.


### 4.5. Infraestructuras con WHOIS y DNS

* Identificar propietarios de dominios
* Consultar registros DNS
* Apoyar analisis de exposicion

Note: Explica el uso de WHOIS, NSLookup y Shodan para mapear activos.


### 4.5.1. Metodos comunes

* WHOIS para datos de registro
* NSLookup o Dig para DNS
* Shodan para dispositivos

Note: Reforzar que no se deben hacer escaneos sin autorizacion. Aqui hablamos de **consulta** y **observacion** (registros y exposicion), no de intentar acceder a servicios.


### 4.6. Monitorizacion Deep y Dark Web

* No indexado en buscadores
* Util para detectar filtraciones
* Acceso con precaucion

Note: Explica diferencias y riesgos. Limitarse a la observacion autorizada.


### 4.6.1. Herramientas Dark Web

* TOR Browser
* OnionScan
* DarkSearch

Note: Presenta herramientas y advierte de riesgos legales y tecnicos. Enfatiza seguridad operativa: separar entorno de clase, no descargar contenidos dudosos y no interactuar con servicios ilegales.


### 4.7. Analisis de imagenes y videos

* Verificar autenticidad
* Buscar origen y manipulación
* Extraer metadatos

Note: La analitica forense ayuda a detectar bulos y montajes. Insiste en separar **lo que se ve** (hechos) de **lo que se deduce** (inferencias) y en buscar confirmacion con varias fuentes.


### 4.7.1. Tecnicas forenses en imagenes

* Busqueda inversa (Google, TinEye)
* Metadatos con ExifTool
* FotoForensics para manipulacion

Note: Explica cada tecnica y cuando usarla: busqueda inversa para origen, metadatos para contexto, y analisis forense para manipulacion. Refuerza el respeto a derechos y que una imagen "viral" no es evidencia si no se valida su **origen**.


### 4.8. Actividades

* Dorking en dominio ficticio
* Extraer metadatos de documentos
* Analisis de perfiles publicos
* Infraestructura con WHOIS y DNS
* Verificacion de imagenes

Note: Actividades practicas para consolidar tecnicas OSINT. Pide que documenten: tecnica usada, query, fuente, evidencia y conclusion, para entrenar **trazabilidad**.

---

## 5. Herramientas OSINT

Note: Bloque dedicado a herramientas. Idea clave: usar herramientas para **acelerar**, no para "delegar" el analisis. Todo resultado debe verificarse y citarse como **fuente**.


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

Note: Compara resultados y destaca el valor de historicos web: cambios en una web pueden explicar filtraciones antiguas o endpoints expuestos en el pasado. Buen momento para hablar de **contexto temporal**.


### 5.2. Shodan

* Buscador de dispositivos conectados
* Detecta exposicion de servicios
* Util en auditorias

Note: Shodan muestra activos expuestos en Internet. Remarca que es un buscador: se consulta informacion ya indexada. No implica conectarse al servicio; el uso debe ser **responsable** y preferiblemente sobre activos propios o autorizados.


### 5.2.1. Caracteristicas principales

* Filtros por puertos y protocolos
* Busqueda por CVE
* Identificacion de activos propios
* Ejemplo: `port:3389`

Note: Explica como Shodan ayuda a descubrir **superficie de ataque** (puertos/servicios expuestos). Repite que encontrar un servicio no autoriza a interactuar con el: se reporta y se prioriza su cierre.


### 5.2.2. Recursos utiles de Shodan

* Consultas y filtros populares
* Ejemplos de busqueda
* Guias oficiales

Note: Recursos para practicar con consultas seguras y controladas.


### 5.3. Wayback Machine

* Versiones antiguas de sitios
* Recuperar informacion eliminada
* Detectar filtraciones pasadas

Note: Muestra el valor de la historia web para investigaciones: comparar versiones, recuperar paginas borradas y encontrar referencias antiguas. Recalca que hay que anotar la **fecha** de la captura.


### 5.4. Maltego

* Visualiza relaciones
* Mapea infraestructura y actores
* Apoya análisis de amenazas

Note: Herramienta clave para relacionar entidades en una investigacion. Explica el concepto de "transforms" y advierte: los grafos son utiles, pero hay que evitar conclusiones sin evidencia.


### 5.4.1. Usos de Maltego en OSINT

* Relacionar correos, dominios y redes
* Identificar conexiones entre infraestructuras
* Analizar redes de amenazas y actores
* Visualizar relaciones complejas

Note: Este uso ayuda a entender dependencias y posibles vectores de ataque. Pide confirmar relaciones importantes con mas de una fuente para reducir falsos positivos.


### 5.5. SpiderFoot

* Automatiza OSINT
* Mas de 200 fuentes
* IPs, dominios, correos, CVE

Note: Permite hacer barridos amplios con un enfoque sistematico. Recalca que la automatizacion genera **ruido**: hay que filtrar, validar y documentar, y nunca ejecutar contra objetivos sin permiso.


### 5.6. OSINT Framework

* Directorio de herramientas
* Organizado por categorias
* Util para investigar por tema
* Acceso: https://osintframework.com

Note: Repositorio esencial para elegir herramientas segun necesidad. Úsalo como "mapa" para decidir que herramienta encaja con tu objetivo y tu fase del proceso.


### 5.7. Buscadores en redes sociales

* Twint para Twitter/X
* OSINTgram para Instagram
* CrossLinked para LinkedIn
* Telegram OSINT para canales

Note: Cada red social requiere herramientas especificas y respeto a normas. Recuerda: trabajar con **perfiles publicos**, no recolectar mas de lo necesario y no contactar ni acosar a nadie durante la investigacion.


### 5.8. Tecnicas de busqueda en redes

* Dorks en LinkedIn
* Busqueda avanzada en plataformas
* Ejemplo: `site:linkedin.com "trabaja en empresa"`
* Solo perfiles publicos

Note: Refuerza que el objetivo es informacion publica y uso etico. Importante: dorking en redes puede descubrir datos sensibles; el rol profesional es **reportar** y **proteger**, no explotar.


### 5.9. Actividades

* Buscar dispositivos con Shodan
* Rastrear usuarios con Sherlock
* Dorking en dominio ficticio
* Extraer metadatos con ExifTool

Note: Actividades para practicar herramientas reales con datos controlados. Pide que entreguen capturas o exportaciones, y un mini-informe con hallazgos y recomendaciones.

---

## 6. Casos Practicos y Actividades de OSINT

Note: Casos completos para aplicar lo aprendido. Repite el guion: **objetivo -> fuentes -> adquisicion -> procesamiento -> analisis -> informe**. Aqui se evalua sobre todo el **metodo** y la **justificacion**.


### 6.1. Google Dorking para info oculta

* Objetivo: aprender dorks basicos
* `site:empresa.com filetype:pdf`
* `intext:"password" site:pastebin.com`
* `intitle:"admin login" site:empresa.com`
* Documentar hallazgos

Note: Se trabaja el criterio de busqueda avanzada con dominio ficticio. Pide que expliquen por que cada dork es relevante y que anoten la query exacta para reproducirla.


### 6.2. Analisis de dominios con WHOIS y DNS

* Obtener datos de registro
* `whois google.com`
* Consultar registros DNS
* `nslookup google.com`
* `dig google.com MX`
* Analizar infraestructura

Note: Los alumnos deben identificar propietario y servidores del dominio. Aprovecha para explicar que DNS/WHOIS ayudan a construir un "mapa" de activos y a entender dependencias.


### 6.3. Dispositivos IoT con Shodan

* Buscar dispositivos expuestos
* Filtrar por pais y puerto
* `country:ES port:3389`
* `product:"Webcam"`
* Evaluar riesgos

Note: Se enfatiza la seguridad en dispositivos conectados. Repite que se trata de **identificar exposicion**, no de acceder al dispositivo. Que propongan mitigaciones (cambio de puerto, VPN, MFA, hardening).


### 6.4. Usuarios en redes con Sherlock

* Instalar y ejecutar Sherlock
* `python3 sherlock.py usuario`
* Rastrear presencia en plataformas
* Analizar exposicion

Note: Practica de rastreo con usuarios ficticios y reflexion sobre privacidad. Pregunta guia: "¿Que dato encontrado podria facilitar un ataque de ingenieria social?"


### 6.5. Analisis de imagenes

* Buscar origen con busqueda inversa
* Detectar manipulaciones
* Identificar fuentes fiables

Note: Actividad contra desinformacion y fake news. Recalca pasos: busqueda inversa, contrastar con fuentes fiables y explicar el razonamiento (no basta con decir "parece falso").


### 6.6. Proyecto final OSINT

* Empresa ficticia como objetivo
* Recolectar datos publicos
* Analizar riesgos y recomendar

Note: Se integra todo el proceso OSINT en un informe final. Pide estructura minima: resumen, hallazgos con evidencia, impacto, recomendaciones priorizadas y anexos con queries/capturas.

---

## 7. Retos Eticos y Legales de OSINT

Note: Se abordan limites legales, privacidad y buenas practicas. Mensaje clave: que algo sea accesible no significa que sea correcto usarlo. OSINT profesional exige **minimizacion**, **proposito legitimo** y **proteccion** de datos.


### 7.1. Privacidad y derechos

* Respeto a datos personales
* Riesgo de doxxing
* Uso responsable de metadatos
* Cuidado con Dark Web

Note: Aunque la info sea publica, su uso puede ser delicado. Explica el concepto de **doxxing** y por que hay que evitar exponer datos personales. Enfatiza: recopilar lo minimo necesario y anonimizando cuando proceda.


### 7.1.1. Principales preocupaciones

* Publicar datos con intencion de dano
* Perfiles usados sin consentimiento
* Metadatos como exposicion oculta

Note: Explica por que la privacidad sigue siendo un derecho: contexto, intencion y acumulacion de datos cambian el riesgo. Habla de **consentimiento** y de impacto real (acoso, fraude, suplantacion).


### 7.2. Regulaciones legales

* GDPR en Europa
* Codigo Penal en España
* CCPA en California
* Leyes locales en LATAM

Note: Recordar que OSINT debe cumplir la normativa vigente del pais y las politicas internas. Aclara que en España/UE el **RGPD** marca obligaciones (base legal, minimizacion, seguridad, derechos).


### 7.2.1. Principales regulaciones sobre privacidad

* GDPR (Union Europea)
* Codigo Penal en España (Art. 197)
* CCPA en California
* Leyes locales en LATAM

Note: Cada normativa define limites y obligaciones en el tratamiento de datos. Enfatiza que en el aula buscamos criterio: identificar cuando un dato personal requiere especial cuidado y cuando hay que pedir asesoramiento.


### 7.3. Buenas practicas y uso responsable

* Respetar la privacidad
* Cumplir la ley
* Proposito legitimo
* Verificar fuentes
* Minimizar datos

Note: Buenas practicas para un trabajo profesional y etico: **verificar**, **minimizar**, **documentar**, y mantener un proposito legitimo. Introduce la idea de "necesidad de saber" aplicada a OSINT.


### 7.3. Buenas practicas y uso responsable II

* No divulgar datos sensibles
* Informar a afectados cuando proceda
* Documentar y justificar acciones

Note: Enfatiza la responsabilidad y la trazabilidad de la investigacion. Añade que, si se detecta un dato sensible, la accion correcta es **reportar** por canal adecuado y limitar su difusion.


### 7.4. Actividades

* Evaluar casos eticos
* Analizar leyes de privacidad
* Caso practico con reglas claras

Note: Actividades para entrenar criterio legal y etico. Pide que justifiquen sus decisiones: por que es legal/ilegal, que riesgo hay, y que alternativa OSINT valida existiria.

---

## 8. Recursos y lecturas recomendadas

Note: Cierre con recursos para ampliar conocimientos. Recalca que OSINT se aprende practicando con **casos controlados**, citando fuentes y mejorando el metodo, no memorizando herramientas.


### 8.1. Recursos recomendados

* Webs con recursos OSINT

Note: Indicar que son lecturas de referencia y deben citarse en trabajos. Recomienda crear una pequena "biblioteca" de fuentes fiables y una lista de dorks/plantillas reutilizables.


### 8.2. Lectura recomendada

* Metodologia OSINT para investigar en Internet
* Autor: Julian Gutierrez
* Ediciones Ciberpatrulla (2021)

Note: Recordar derechos de autor y uso responsable de materiales. Aprovecha para enlazar con el cierre: buen analista = **metodo**, **evidencia**, **etica** y **comunicacion clara**.
