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

Note: Como alumnos y alumnas, debéis entender que **la taxonomía es como aprender un idioma común** para hablar de ciberseguridad. **Sin ella, sería como si cada organización hablara un idioma diferente**.


### 1.2. La taxonomía como idioma común

* Permite categorizar y describir incidentes de forma estandarizada.
* Facilita la colaboración entre organizaciones.
* Mejora el intercambio de información.
* Permite respuesta rápida y efectiva.

Note: **La taxonomía actúa como un mapa en terreno desconocido**, proporcionando **orientación necesaria para abordar amenazas efectivamente**.


### 1.3. Beneficios de una taxonomía común

Ventajas prácticas:

1. **Identificación rápida** del tipo de ciberataque
2. **Mejor comunicación** entre departamentos y organizaciones
3. **Respuesta efectiva** con estrategias específicas
4. **Aprendizaje continuo** de incidentes anteriores

Note: Una taxonomía bien definida **no es solo teoría, tiene aplicaciones prácticas inmediatas** que salvan a las organizaciones de pérdidas significativas.


### 1.4. Incidente de seguridad I

¿Qué es un incidente de ciberseguridad?

* Evento no planificado o no deseado.
* Compromete la seguridad de la información.
* Afecta integridad, confidencialidad o disponibilidad.
* Puede tomar muchas formas: malware, brechas, accesos no autorizados.

Note: Un incidente de ciberseguridad es cualquier evento que comprometa la seguridad de la información. Estos incidentes pueden afectar **a la tríada CIA: Confidencialidad** (acceso no autorizado a información), **Integridad** (modificación no autorizada de datos) y **Disponibilidad** (interrupción de servicios). Los incidentes van desde ataques de malware hasta brechas de seguridad y accesos no autorizados a sistemas críticos.


### 1.4. Incidente de seguridad II

Ciclo de vida de un incidente:

1. **Preparación:** medidas preventivas antes del incidente.
2. **Identificación:** detección y alerta del incidente.
3. **Contención:** aislar para evitar propagación.
4. **Erradicación:** eliminar causa raíz.
5. **Recuperación:** restaurar sistemas a estado operativo.
6. **Lecciones aprendidas:** analizar y mejorar.

Note: El ciclo de vida de gestión de incidentes es un **proceso estructurado** que comienza con la **preparación** (formación de empleados, controles de seguridad, pruebas). **La identificación es donde entra la taxonomía**, permitiendo clasificar rápidamente el tipo de incidente. La **contención evita que se propague** (por ejemplo, aislar un sistema infectado). La **erradicación elimina el malware o la vulnerabilidad**. La **recuperación restaura servicios y datos**. Las **lecciones aprendidas son cruciales** para mejorar la respuesta futura.


### 1.5. Importancia de la clasificación

¿Por qué clasificar correctamente?

* Comprender naturaleza y alcance del ataque.
* Aplicar respuesta específica al tipo de incidente.
* Un phishing requiere respuesta diferente a un DDoS.
* Identificar fuentes: internas vs externas.

Note: **La clasificación correcta es el primer paso crítico** en la respuesta a incidentes. Un ataque de **phishing** que busca robar credenciales requiere medidas como **resetear contraseñas, alertar a usuarios y revisar accesos**. Un ataque **DDoS** requiere **mitigación de tráfico, contactar con proveedores de servicios y habilitar protecciones anti-DDoS**. Las fuentes también importan: un **ataque interno** (empleado descontento) requiere **medidas de recursos humanos y forenses** diferentes a un **ataque externo** (grupo de hackers).

---

## 2. ¿Qué significa Taxonomía?


### 2.1. Definición general

**Taxonomía:**

* Clasificación u ordenación en grupos.
* Elementos con características comunes.
* Sistema estructurado de categorización.
* Facilita comprensión y comunicación.

Note: La taxonomía es un concepto que viene de la **biología, donde se clasifican seres vivos** en reinos, familias, especies. En ciberseguridad, **aplicamos el mismo principio: agrupar incidentes que comparten características similares**. Por ejemplo, todos los ataques de malware comparten características comunes (software malicioso que compromete sistemas), pero **dentro de esta categoría hay subcategorías**: virus, gusanos, troyanos, ransomware, cada uno con características específicas.


### 2.2. Taxonomía en ciberseguridad

Sistema de clasificación estructurado para incidentes:

* Categoriza incidentes con características comunes.
* Ejemplo: malware por tipo (virus, gusanos, troyanos).
* Ejemplo: ataques DDoS por volumen de tráfico.
* Permite identificación y respuesta rápida.

Note: En ciberseguridad, **la taxonomía es nuestro sistema de organización**. Imagina una **biblioteca sin sistema de clasificación: imposible encontrar un libro específico**. **La taxonomía nos da ese sistema**. Los ataques de malware se clasifican por el tipo de software malicioso. Los ataques DDoS se pueden categorizar **por el vector de ataque** (volumétrico, de aplicación, de protocolo) o por el objetivo (servidor web, DNS, infraestructura de red).


### 2.3. Beneficios de la taxonomía

Ventajas prácticas de una taxonomía común:

* **Identificación rápida** del tipo de ataque.
* **Comunicación efectiva** entre equipos y organizaciones.
* **Respuesta coordinada** con procedimientos específicos.
* **Aprendizaje continuo** de incidentes similares.

Note: **Los beneficios son tangibles y medibles**. **La identificación rápida reduce el tiempo de respuesta de horas a minutos**. La comunicación efectiva evita malentendidos costosos: cuando un analista dice **"tenemos un ataque de ransomware tipo CryptoLocker", todo el equipo entiende inmediatamente la gravedad** y el procedimiento a seguir. La respuesta coordinada aprovecha las mejores prácticas documentadas para ese tipo específico de ataque. **El aprendizaje continuo permite mejorar las defensas** basándose en patrones identificados.

---

## 3. Factores de clasificación


### 3.1. Tipo de amenaza o método

* Determina la técnica usada por atacantes.
* Ejemplos: código dañino, intrusiones, fraude.
* Permite identificar el tipo de incidente.
* Facilita aplicar medidas de respuesta adecuadas.

Note: **El tipo de amenaza o método es el primer factor crítico** de clasificación. Nos indica la técnica empleada por los atacantes: ¿es código malicioso como un virus o ransomware? ¿Es una intrusión mediante explotación de vulnerabilidades? ¿Es fraude mediante phishing? **Cada método requiere contramedidas específicas**. Por ejemplo, un ataque de código dañino requiere **análisis forense del malware**, actualización de antivirus y búsqueda de sistemas infectados. Una intrusión requiere **análisis de logs**, revisión de accesos y parcheo de vulnerabilidades. El fraude requiere **formación de usuarios** y mejora de controles de autenticación.


### 3.2. Origen de la amenaza

* **Interna**: empleado descontento, error humano.
* **Externa**: hacker, grupo organizado, competencia.

Identificar el origen ayuda a:
* Ajustar la respuesta
* Prevenir futuros incidentes
* Aplicar medidas específicas

Note: **El origen determina completamente la estrategia de respuesta**. Una **amenaza interna** (empleado descontento que filtra información) requiere: investigación de recursos humanos, revisión de controles de acceso, posible acción legal interna y análisis de motivaciones. Una **amenaza externa** (grupo APT que realiza espionaje) requiere: análisis de indicadores de compromiso, coordinación con fuerzas de seguridad, mejora de perímetro de seguridad y posible colaboración con organismos nacionales de ciberseguridad. **Los errores humanos internos requieren formación y mejora de procesos, no sanciones**.


### 3.3. Categoría de sistemas afectados

* Sistemas críticos vs no críticos.
* Según ENS - Esquema Nacional de Seguridad.
* Categorías: BAJO, MEDIO, ALTO.
* Prioridad de respuesta según criticidad.

Note: **El Esquema Nacional de Seguridad (ENS) establece tres categorías** de sistemas según su criticidad. **Categoría BAJA**: sistemas cuyo compromiso tiene impacto limitado (ej: web informativa pública). **Categoría MEDIA**: sistemas importantes pero no críticos (ej: intranet corporativa). **Categoría ALTA**: sistemas críticos cuyo compromiso afecta gravemente a la organización (ej: sistemas de control industrial, bases de datos con información personal sensible, sistemas financieros). Un incidente en un sistema categoría ALTA requiere **respuesta inmediata 24/7**, mientras que uno en categoría BAJA puede esperar al horario laboral. La criticidad determina también los recursos asignados a la respuesta.


### 3.4. Perfil de usuarios afectados

* Posición en la estructura organizativa.
* Nivel de privilegios de acceso.
* Acceso a información sensible o confidencial.
* Impacto potencial del compromiso.

Note: **El perfil del usuario afectado es crucial para determinar la gravedad**. Un usuario estándar típicamente tiene acceso limitado: su correo, documentos de trabajo, aplicaciones básicas. El compromiso es limitado. Un usuario con privilegios medios (jefe de departamento) puede acceder a información sensible de su área: datos de empleados, presupuestos, contratos. Un administrador de sistemas tiene acceso completo: puede modificar configuraciones, acceder a todos los datos, crear cuentas, instalar software. **El compromiso de una cuenta administrativa es crítico** porque el atacante obtiene **"llaves del reino"**. Por eso, un phishing exitoso contra el CEO es mucho más grave que contra un becario.


### 3.5. Número y tipología de sistemas

* **Número**: ¿Un sistema o toda la red?
* **Tipología**: servidores, estaciones, móviles.
* Impacto escalado según alcance.
* Recursos necesarios para la respuesta.

Note: **El alcance del incidente determina los recursos necesarios**. Un **ransomware en una estación de trabajo aislada**: 1-2 horas de respuesta, un técnico, impacto limitado al usuario. Un **ransomware que afecta 100 servidores de producción**: equipo completo de respuesta, días de trabajo, impacto en toda la organización, posible parada de negocio. La tipología también importa: un servidor comprometido puede afectar a cientos de usuarios, un dispositivo móvil comprometido generalmente afecta solo a un usuario pero puede exponer datos corporativos si tiene acceso a correo empresarial. Los servidores críticos (bases de datos, controladores de dominio) requieren respuesta inmediata aunque sea solo uno.


### 3.6. Impacto organizacional

Dimensiones del impacto:

* **Protección de información**: confidencialidad comprometida.
* **Prestación de servicios**: disponibilidad afectada.
* **Conformidad legal**: incumplimientos normativos.
* **Imagen pública**: reputación dañada.

Note: **El impacto organizacional va más allá de lo técnico**. La protección de información se refiere a confidencialidad e integridad: ¿se han filtrado datos personales? ¿se han modificado registros financieros? La prestación de servicios es la disponibilidad: ¿pueden los usuarios acceder a sistemas críticos? ¿está caída la web de ventas? La conformidad legal es crítica: una fuga de datos personales puede violar el RGPD con **multas de hasta 20 millones de euros** o 4% de facturación global. **La imagen pública es difícil de cuantificar pero puede ser devastadora**: clientes perdidos, desconfianza del mercado, caída en bolsa. Un incidente puede tener impacto en una o varias dimensiones simultáneamente.


### 3.7. Requerimientos legales

* Notificación a autoridades competentes.
* Notificación a afectados (GDPR).
* Plazos legales de notificación (72 horas).
* Documentación y evidencias necesarias.

Note: **Los requerimientos legales no son opcionales**. El **RGPD (Reglamento General de Protección de Datos) exige notificar** a la autoridad de protección de datos en máximo **72 horas** desde que se tiene conocimiento de una brecha de datos personales. Si el incidente supone alto riesgo para los afectados, también hay que notificarles a ellos directamente. Las multas por incumplimiento son severas: hasta 20 millones de euros o 4% de facturación global anual, lo que sea mayor. Además, hay que conservar toda la documentación y evidencias del incidente: logs, forenses, decisiones tomadas, comunicaciones. Esta documentación puede ser requerida en auditorías o procesos judiciales. Otras normativas como NIS2 o PCI-DSS también imponen obligaciones específicas de notificación.

---

## 4. Taxonomía de referencia INCIBE


### 4.1. Basada en estándares

Fundamentos:

* Guía Nacional de Notificación y Gestión de Ciberincidentes (INCIBE).
* CCN-STIC 817 (CCN-CERT).
* Taxonomía ENISA (Agencia Europea).
* Coordinada internacionalmente.

Note: **La taxonomía española no es una invención aislada**, es el resultado de coordinación internacional entre equipos de respuesta a incidentes. **INCIBE (Instituto Nacional de Ciberseguridad)** publica la Guía Nacional que usan todas las organizaciones públicas y muchas privadas en España. **CCN-CERT (Centro Criptológico Nacional** - Capacidad de Respuesta a Incidentes) desarrolla las guías CCN-STIC que son de **obligado cumplimiento para administraciones públicas** según el Esquema Nacional de Seguridad. **ENISA (Agencia Europea de Ciberseguridad)** coordina a nivel europeo y publica taxonomías de referencia adoptadas por múltiples países. Esta coordinación asegura que podamos compartir información de amenazas con otros países usando un lenguaje común.


### 4.2. Estructura de la taxonomía

Dos niveles de clasificación:

* **Primer nivel**: Categoría general del incidente.
* **Segundo nivel**: Tipos específicos dentro de cada categoría.

Permite precisión y flexibilidad simultáneamente.

Note: **La estructura de dos niveles es como un árbol**: el **tronco representa la categoría general** (por ejemplo "Código dañino"), y las **ramas son los tipos específicos** dentro de esa categoría (malware, ransomware, spyware, rootkit). Este diseño permite ser específico sin perder claridad. Por ejemplo, puedes decir "tenemos un incidente de código dañino" si aún no sabes exactamente qué tipo, o ser más preciso: "tenemos un incidente de código dañino tipo ransomware CryptoLocker". **La flexibilidad es importante** porque en las fases iniciales de detección puede que no tengamos todos los detalles, pero aún así podemos empezar a clasificar y responder basándonos en la categoría general.

---

## 5. Categorías principales (1/3)


### 5.1. Contenido abusivo

Incidentes con spam, comentarios ofensivos, contenido ilegal.

**Tipos:**

* **SPAM**: Correo masivo no solicitado.
* **Delito de odio**: Contenido difamatorio o discriminatorio.
* **Pornografía infantil**: Material ilegal.

Note: **El contenido abusivo puede parecer menos técnico** que otros incidentes, pero **tiene serias implicaciones legales** y puede ser el preludio de ataques más sofisticados. El SPAM no es solo molesto: puede contener malware, enlaces de phishing o ser parte de campañas de fraude. El delito de odio incluye ciberacoso, amenazas contra personas o colectivos, publicación de comentarios racistas o discriminatorios en redes sociales o sistemas corporativos. **La pornografía infantil es un delito gravísimo** con **obligación legal inmediata** de notificación a fuerzas de seguridad. El contenido abusivo puede originarse desde sistemas comprometidos de la organización, lo que la convierte en parte del problema aunque sea víctima.


### 5.2. Código dañino

Software malicioso que compromete sistemas.

**Tipos:**

* **Malware**: Virus, troyanos, gusanos.
* **Ransomware**: Cifrado de datos con rescate.
* **Spyware**: Recopilación no autorizada de información.
* **Rootkit**: Ocultación de presencia maliciosa.

Note: **El código dañino es una de las amenazas más comunes y diversas**. El malware genérico incluye virus (se replica modificando archivos), troyanos (se disfrazan de software legítimo) y gusanos (se propagan automáticamente por la red sin intervención del usuario). El **ransomware cifra los archivos** de la víctima y **exige pago** (generalmente en criptomonedas) para recuperarlos; es uno de **los incidentes más costosos actualmente**. El spyware captura información sin consentimiento: pulsaciones de teclado, capturas de pantalla, credenciales, historial de navegación. Los **rootkits son especialmente peligrosos** porque se ocultan en el sistema operativo a nivel profundo, haciendo muy difícil su detección y eliminación. Cada tipo requiere herramientas y técnicas de respuesta específicas.


### 5.3. Recopilación de información

Actividades para obtener información de la organización.

**Tipos:**

* **Escaneo**: Búsqueda de vulnerabilidades.
* **Sniffing**: Interceptación de comunicaciones.
* **Social Engineering**: Ingeniería social.

Note: **La recopilación de información es la fase de reconocimiento previa al ataque real**. El escaneo incluye técnicas como escaneo de puertos (¿qué servicios están abiertos?), escaneo de vulnerabilidades (¿qué versiones de software tienen fallos conocidos?), peticiones DNS, ICMP o SMTP para mapear la red. El sniffing intercepta tráfico de red para capturar información: credenciales enviadas sin cifrar, sesiones web, correos electrónicos. Los ataques man-in-the-middle son un ejemplo clásico. La ingeniería social recopila información sin tecnología: llamadas telefónicas haciéndose pasar por soporte técnico, correos solicitando información, incluso búsqueda en redes sociales o basura física (dumpster diving). **Detectar esta fase es crítico** porque prevenir aquí **evita el ataque posterior**.


### 5.4. Intento de intrusión

Intentos de acceder sin autorización.

**Tipos:**

* **Explotación de vulnerabilidades**: Uso de fallos conocidos.
* **Login attempts**: Intentos de acceso por fuerza bruta.
* **New attack signature**: Nuevas técnicas de ataque.

Note: **Un intento de intrusión no es todavía un compromiso exitoso**, pero indica que alguien está intentando activamente entrar en nuestros sistemas. La explotación de vulnerabilidades usa fallos conocidos con identificador CVE: desbordamientos de buffer, inyecciones SQL, cross-site scripting (XSS), puertas traseras en software. Los intentos de acceso por fuerza bruta prueban múltiples combinaciones de usuario/contraseña: ataques de diccionario (palabras comunes), fuerza bruta completa (todas las combinaciones), o uso de credenciales filtradas en otras brechas (credential stuffing). Las **nuevas técnicas de ataque (zero-day exploits) son especialmente peligrosas** porque explotan vulnerabilidades desconocidas para el fabricante. **Monitorizar intentos fallidos es crucial**: muchos intentos desde la misma IP indican ataque automatizado.

---

## 6. Categorías principales (2/3)


### 6.1. Intrusión

Acceso no autorizado exitoso.

**Tipos:**

* **Compromiso de cuenta**: Credenciales robadas.
* **Compromiso de aplicación**: Vulnerabilidad explotada.
* **Compromiso de sistema**: Control total del sistema.

Note: **Cuando confirmamos una intrusión, el incidente ya es grave** y requiere **respuesta inmediata** y contundente. El compromiso de cuenta significa que el atacante ha obtenido credenciales válidas: mediante phishing, keyloggers, brechas de datos de terceros, o fuerza bruta exitosa. Puede ser cuenta sin privilegios (acceso limitado pero puede escalar) o con privilegios (acceso administrativo inmediato). El compromiso de aplicación explota vulnerabilidades en el software: inyección SQL accediendo a la base de datos, XSS ejecutando código malicioso en navegadores de usuarios, deserialización insegura ejecutando código arbitrario. El **compromiso de sistema da control completo**: el atacante puede instalar software, modificar configuraciones, crear cuentas, acceder a todos los archivos. La respuesta incluye: **aislar sistemas**, cambiar credenciales, análisis forense, búsqueda de persistencia.


### 6.2. Disponibilidad

Ataques que afectan la disponibilidad de servicios.

**Tipos:**

* **DDoS**: Denegación de servicio distribuida.
* **Sabotaje**: Destrucción intencionada.
* **Interrupción**: Fallo en servicios críticos.

Note: **Sin disponibilidad, no hay negocio**. Los ataques de disponibilidad pueden ser tan dañinos económicamente como el robo de datos. **DDoS (Denegación de Servicio Distribuida)** usa múltiples sistemas (botnets) para inundar el objetivo con tráfico: ataques volumétricos (saturan ancho de banda), ataques de protocolo (agotan recursos de servidores/firewalls), ataques de aplicación (peticiones complejas que consumen CPU/memoria). El **sabotaje es destrucción deliberada**: corte de cables de red, incendios provocados en CPD, destrucción física de equipos, borrado intencionado de datos. Las interrupciones incluyen fallos por mala configuración (firewall mal configurado bloquea tráfico legítimo, cuota de disco llena impide operaciones) o causas externas (desastres naturales, cortes eléctricos). La respuesta varía: DDoS requiere mitigación de tráfico, sabotaje requiere investigación criminal, interrupciones requieren recuperación de servicios.


### 6.3. Seguridad de la información

Compromiso de confidencialidad o integridad.

**Tipos:**

* **Acceso no autorizado**: Lectura de información sensible.
* **Modificación no autorizada**: Alteración de datos.
* **Pérdida de datos**: Información perdida o destruida.

Note: **La tríada CIA (Confidencialidad, Integridad, Disponibilidad) se ve afectada directamente**. El **acceso no autorizado compromete la confidencialidad**: alguien lee información para la que no tiene autorización, puede ser deliberado (explotando vulnerabilidades, usando credenciales robadas) o accidental (mala configuración expone directorios web con documentos sensibles, permisos incorrectos permiten acceso a archivos). La **modificación no autorizada compromete la integridad**: alteración de páginas web (defacement), modificación de bases de datos (cambiar precios, borrar registros), encriptado mediante ransomware. La pérdida de datos puede ser por ataque (ransomware sin recuperación, borrado malicioso) o accidente (fallo de hardware sin backups, borrado accidental). Cada tipo requiere respuesta específica: acceso no autorizado requiere análisis de qué se accedió y notificación si procede, modificación requiere recuperación desde backups, pérdida requiere activación de plan de continuidad.


### 6.4. Fraude

Uso de recursos informáticos con intención fraudulenta.

**Tipos:**

* **Phishing**: Suplantación de identidad.
* **Copyright**: Uso ilegal de software.
* **Masquerade**: Falsificación de identidad.

Note: **El fraude combina técnicas técnicas con ingeniería social**, siendo uno de **los vectores más exitosos actualmente**. El phishing suplanta entidades legítimas (bancos, proveedores, compañeros de trabajo) para robar credenciales o información financiera: correos que parecen del banco solicitando contraseñas, páginas web falsas que imitan sitios legítimos, mensajes SMS (smishing) o llamadas (vishing) suplantando identidad. El **spear phishing es dirigido a personas específicas** con información personalizada, aumentando su efectividad. El copyright incluye uso de software sin licencia, distribución de material protegido, lo que puede tener consecuencias legales para la organización. El masquerade falsifica identidad en sistemas: usar cuenta de otro usuario, falsificar direcciones IP o MAC, suplantar sistemas en la red. La respuesta al fraude incluye **formación de usuarios (principal defensa contra phishing)**, controles técnicos (filtros de correo, verificación de dominios) y auditorías de licencias.

---

## 7. Categorías principales (3/3)


### 7.1. Vulnerabilidad

Debilidad que puede ser explotada.

**Tipos:**

* **Criptografía débil**: Algoritmos obsoletos.
* **Amplificación**: Vulnerabilidad en protocolos.
* **Configuración incorrecta**: Errores de configuración.

Note: **Las vulnerabilidades por sí mismas no son incidentes consumados, pero son la puerta de entrada** que los atacantes buscan explotar. **Gestionarlas proactivamente previene futuros incidentes**. La criptografía débil incluye algoritmos obsoletos como MD5 (hashes rotos), DES (cifrado débil), SSL/TLS antiguo susceptible a ataques POODLE o FREAK, WEP para WiFi (completamente roto). Las vulnerabilidades de amplificación permiten ataques DDoS de reflexión: servidores DNS abiertos, servidores NTP sin restricciones, que responden a peticiones falsificadas amplificando el tráfico hacia la víctima. **La configuración incorrecta es muy común**: servicios expuestos que deberían ser internos (bases de datos, paneles de administración, RDP, VNC), permisos excesivos, contraseñas por defecto sin cambiar, software sin parchear. La gestión de vulnerabilidades incluye escaneos regulares, priorización según criticidad y exposición, y parcheo sistemático.


### 7.2. Otras categorías

Categorías adicionales según necesidades:

* **Pruebas de seguridad**: Auditorías y pentesting.
* **Otros**: Incidentes que no encajan en categorías anteriores.

Note: **La taxonomía debe ser flexible** para adaptarse a nuevos tipos de incidentes que emergen constantemente en el panorama de ciberseguridad. Las pruebas de seguridad son actividades legítimas pero que pueden parecer ataques: auditorías de seguridad contratadas, ejercicios de pentesting, red team exercises, bug bounty programs. Es crítico que estas actividades estén autorizadas y documentadas para evitar falsas alarmas y respuestas innecesarias. La categoría "Otros" captura incidentes que no encajan en las categorías anteriores: **APT (Advanced Persistent Threats)** con técnicas muy sofisticadas y objetivos específicos, ciberterrorismo contra infraestructuras críticas, incidentes relacionados con sistemas de control industrial (SCADA), nuevos vectores de ataque que aún no tienen categoría específica. Esta flexibilidad permite que la taxonomía evolucione con las amenazas sin requerir rediseño completo.

---

## 8. Peligrosidad e Impacto


### 8.1. Grado de peligrosidad I

¿Qué es la peligrosidad?

* Potencial amenaza si el incidente se materializa.
* Características intrínsecas del tipo de amenaza.
* Comportamiento típico del ataque.
* Capacidad de causar daños significativos.

Note: **El grado de peligrosidad evalúa la amenaza potencial** que representa un tipo de incidente, independientemente de si se ha materializado completamente. Se basa en **las características inherentes del ataque**: un ransomware es intrínsecamente más peligroso que un escaneo de puertos porque puede cifrar datos críticos y paralizar operaciones. **La peligrosidad considera el peor escenario posible**: ¿qué pasaría si este ataque tuviera éxito completo? Un ataque DDoS masivo tiene alta peligrosidad porque puede dejar todos los servicios inaccesibles. Un intento fallido de phishing tiene baja peligrosidad si fue detectado y bloqueado antes de causar daño.


### 8.1. Grado de peligrosidad II

Niveles de peligrosidad:

* **Nivel 1 - Bajo**: Amenaza limitada, sin riesgo inmediato.
* **Nivel 2 - Medio**: Puede causar daños moderados.
* **Nivel 3 - Alto**: Puede causar daños significativos.
* **Nivel 4 - Muy Alto**: Amenaza grave con daños severos.
* **Nivel 5 - Crítico**: Amenaza existencial para la organización.

Note: Los niveles se asignan según el tipo de incidente y su potencial destructivo. **Nivel 1 (Bajo)**: escaneo de puertos aislado, spam sin malware. **Nivel 2 (Medio)**: phishing genérico, vulnerabilidad menor. **Nivel 3 (Alto)**: malware conocido, intrusión en sistema no crítico. **Nivel 4 (Muy Alto)**: ransomware, compromiso de cuenta administrativa. **Nivel 5 (Crítico)**: APT dirigido, ataque a infraestructura crítica, compromiso completo de red. La Guía Nacional de INCIBE proporciona tablas detalladas relacionando cada tipo de incidente con su nivel de peligrosidad típico, aunque el contexto específico puede modificar esta asignación.


### 8.2. Impacto del incidente I

¿Qué es el impacto?

* Consecuencias reales o potenciales del incidente.
* Efectos en funciones y actividades de la organización.
* Afectación a activos e individuos.
* Puede ser técnico, operativo, legal, reputacional.

Note: **Mientras la peligrosidad evalúa la amenaza potencial, el impacto evalúa las consecuencias reales** o esperadas en la organización específica. Un ransomware tiene la misma peligrosidad alta en cualquier organización, **pero su impacto varía**: en un hospital con pacientes en riesgo es crítico, en una oficina administrativa puede ser alto pero no crítico. El impacto considera múltiples dimensiones: técnica (sistemas afectados), operativa (servicios interrumpidos), financiera (pérdidas económicas), legal (multas, incumplimientos), reputacional (pérdida de confianza). Un mismo incidente puede tener bajo impacto técnico pero alto impacto reputacional.


### 8.2. Impacto del incidente II

Niveles de impacto:

* **L1 - Bajo**: Afectación mínima, recuperación rápida.
* **L2 - Medio**: Afectación moderada, requiere recursos.
* **L3 - Alto**: Afectación significativa, servicios comprometidos.
* **L4 - Muy Alto**: Afectación grave, operaciones críticas afectadas.
* **L5 - Crítico**: Afectación existencial, supervivencia en riesgo.

Note: Los niveles de impacto se evalúan considerando varios parámetros según la Guía Nacional de INCIBE. **L1 (Bajo)**: un usuario sin acceso a correo durante una hora. **L2 (Medio)**: departamento sin acceso a aplicación no crítica durante horas. **L3 (Alto)**: servicio público interrumpido, datos sensibles expuestos. **L4 (Muy Alto)**: servicios críticos caídos, pérdida de datos importantes, incumplimientos legales. **L5 (Crítico)**: paralización completa de operaciones, pérdida masiva de datos, compromiso de infraestructura crítica, riesgo para vidas humanas. El impacto se evalúa en cuatro dimensiones: protección de información, prestación de servicios, conformidad legal e imagen pública.


### 8.3. Diferencia: Peligrosidad vs Impacto

Conceptos complementarios:

* **Peligrosidad**: Potencial del tipo de ataque (genérico).
* **Impacto**: Consecuencias en esta organización (específico).
* Mismo ataque, diferente impacto según contexto.
* Ambos necesarios para priorizar respuesta.

Note: **Es fundamental entender la diferencia**. Un ataque de ransomware tiene **peligrosidad "Muy Alta" siempre**, porque su naturaleza es muy destructiva. Pero **el impacto depende del contexto**: si cifra un servidor de backup que no se usa activamente, el impacto puede ser "Medio". Si cifra la base de datos principal de producción de un hospital, el impacto es "Crítico". Otro ejemplo: un escaneo de puertos tiene peligrosidad "Baja" (solo busca vulnerabilidades), pero si se detecta un escaneo exhaustivo desde una IP conocida de grupo APT dirigido a nuestra organización específica, el impacto potencial sube porque indica que seremos objetivo de un ataque mayor. **La combinación de ambos factores determina la prioridad de respuesta**.

---

## 9. Prioridades de respuesta


### 9.1. Matriz de priorización

Peligrosidad + Impacto = Prioridad

* Cruza niveles de peligrosidad (1-5) con impacto (L1-L5).
* Determina urgencia de respuesta.
* Asigna recursos según prioridad.
* Matriz definida en Guía Nacional INCIBE.

Note: **La matriz de priorización combina peligrosidad e impacto** para determinar cómo de urgente es responder al incidente. **No es una simple suma**: utiliza una matriz que pondera ambos factores. Por ejemplo, peligrosidad "Crítica" (5) con impacto "Crítico" (L5) resulta en prioridad "Emergencia". Pero peligrosidad "Baja" (1) con impacto "Alto" (L3) resulta en prioridad "Media", porque aunque afecte a sistemas importantes, el tipo de amenaza no requiere respuesta inmediata. **La matriz ayuda a tomar decisiones objetivas** sobre asignación de recursos limitados cuando hay múltiples incidentes simultáneos.


### 9.2. Niveles de prioridad I

**Emergencia:**

* Resolución no admite demora alguna.
* Procesamiento en paralelo si hay varios.
* Todos los recursos disponibles dedicados.
* Ejemplos: peligro para vidas humanas, seguridad nacional.

Note: **La prioridad "Emergencia" es el nivel máximo** y se reserva para situaciones críticas que **no pueden esperar ni un minuto**. Incluye incidentes que ponen en peligro vidas humanas (ataque a sistemas hospitalarios durante cirugías, sabotaje de sistemas de control de tráfico aéreo), amenazas a la seguridad nacional (ciberterrorismo, espionaje de infraestructuras críticas), o ataques de propagación masiva y rápida (ransomware tipo WannaCry expandiéndose exponencialmente). En emergencias, se **movilizan todos los recursos disponibles**: todo el equipo de respuesta **trabaja 24/7**, se cancela cualquier otra actividad, se escala a dirección inmediatamente, se contacta con autoridades y proveedores externos si es necesario. Si hay múltiples emergencias, se procesan en paralelo con equipos separados.


### 9.2. Niveles de prioridad II

**Alta:**

* Requiere atención prioritaria.
* Cola independiente de alta prioridad.
* Se atienden antes que los de menor prioridad.
* Procesamiento en serie por orden de detección.

Note: **La prioridad "Alta" indica incidentes graves** que deben atenderse antes que otros pero permiten un mínimo de organización secuencial. Ejemplos típicos: compromiso confirmado de servidor crítico, fuga de datos sensibles en curso, ataque DDoS afectando servicios importantes. Se mantiene una cola separada de incidentes de alta prioridad y no se procesan incidentes de prioridad normal mientras haya incidentes altos pendientes. Sin embargo, a diferencia de emergencias, se procesan en serie: primero el detectado primero, luego el siguiente, permitiendo mejor asignación de recursos. **Requieren respuesta en horas, no en días**. El equipo debe estar disponible fuera de horario si es necesario.


### 9.3. Niveles de prioridad III

**Normal y Baja:**

* **Normal**: Atención por orden de llegada.
* **Baja**: Última prioridad, pueden cerrarse si no se atienden.
* Mientras haya prioridades superiores, estos esperan.
* Pueden escalar de prioridad si no reciben atención.

Note: **La prioridad "Normal" es la asignada por defecto** a incidentes que no clasifican como emergencia o alta. Incluye escaneos de red insistentes, intentos de intrusión donde el atacante no ha ganado acceso, malware contenido por antivirus. Se atienden en **horario laboral normal**, por orden de llegada, siempre que no haya incidentes de mayor prioridad. Un incidente normal **puede escalar a alta prioridad** si no recibe atención prolongada o si aparece nueva información que aumenta su gravedad. **La prioridad "Baja" es para incidentes menores**: intentos aislados en fase de tentativa sin éxito, spam sin contenido malicioso, escaneos esporádicos. Estos se documentan pero pueden cerrarse automáticamente sin acción si permanecen sin atención mucho tiempo, liberando recursos para incidentes más importantes.

---

## 10. Aplicación práctica


### 10.1. Ejemplo 1: Phishing exitoso

**Escenario**: Empleado recibe email suplantando a director financiero, hace clic y descarga malware.

**Clasificación**:
* Categoría: **Fraude** (phishing)
* También: **Código dañino** (malware descargado)
* Origen: **Externo**
* Usuario: **Alto privilegio** (área financiera)

Note: Este ejemplo demuestra que **un mismo incidente puede caer en múltiples categorías**, lo cual es importante para una respuesta completa. El ataque comienza como Fraude (phishing mediante suplantación del director financiero), pero cuando el empleado hace clic, se descarga malware convirtiéndolo también en incidente de Código Dañino. El origen es externo (atacante fuera de la organización). **El factor crítico** es que afecta a un usuario del área financiera con alto privilegio, que potencialmente tiene acceso a cuentas bancarias, autorizaciones de pagos, información financiera sensible. La peligrosidad es Alta (combina ingeniería social efectiva con malware). El impacto depende de qué logró hacer el malware: si solo infectó el equipo, impacto Medio; si robó credenciales bancarias, impacto Muy Alto. La respuesta incluye: **aislar equipo infectado**, cambiar credenciales del usuario y cuentas relacionadas, análisis forense del malware, revisar transacciones financieras recientes, formar al personal sobre phishing dirigido.


### 10.2. Ejemplo 2: Ransomware

**Escenario**: Ransomware cifra servidores de producción, exige pago en Bitcoin.

**Clasificación**:
* Categoría: **Código dañino** (ransomware)
* También: **Disponibilidad** (servicios caídos)
* Sistemas: **ALTO** (servidores críticos)
* Impacto: **Prestación de servicios + legal**

Note: **El ransomware representa uno de los incidentes más costosos y complejos** actualmente. La clasificación principal es Código Dañino tipo ransomware, pero también afecta a la Disponibilidad porque los servicios quedan inoperativos mientras los datos están cifrados. Los sistemas afectados son categoría ALTO según ENS (servidores de producción críticos para el negocio). **El impacto es múltiple**: prestación de servicios interrumpida (clientes no pueden acceder), legal (si hay datos personales cifrados, obligación de notificación RGPD), financiero (pérdida de ventas, posible rescate, coste de recuperación), reputacional (pérdida de confianza). La peligrosidad es Muy Alta o Crítica. La prioridad es **Emergencia**. La respuesta requiere coordinación entre equipos técnicos (contención, análisis forense, recuperación desde backups), legales (notificaciones obligatorias, decisión sobre pagar o no rescate), dirección (gestión de crisis, comunicación con stakeholders) y posiblemente fuerzas de seguridad. **Nunca se recomienda pagar el rescate** porque financia el crimen organizado y no garantiza recuperación.


### 10.3. Ejemplo 3: Fuga de datos

**Escenario**: Base de datos de clientes expuesta en internet por error de configuración.

**Clasificación**:
* Categoría: **Seguridad de la información**
* Tipo: **Acceso no autorizado**
* Origen: **Interno** (error humano)
* Legal: **Notificación RGPD obligatoria**

Note: Este ejemplo ilustra un incidente **muy común pero con graves consecuencias legales**. La base de datos quedó expuesta por error de configuración (permisos incorrectos en servidor web, base de datos sin autenticación, bucket S3 público). La categoría es Seguridad de la Información tipo Acceso no autorizado, porque aunque no hubo intrusión activa, la información estuvo disponible para cualquiera. El origen es interno (error humano del administrador al configurar), no fue un ataque externo. La peligrosidad puede ser Media (fue un error, no un ataque), pero el impacto es Alto o Muy Alto dependiendo de cuántos datos y durante cuánto tiempo estuvieron expuestos. **El aspecto legal es crítico**: si contiene datos personales, hay **obligación de notificar** a la autoridad de protección de datos en máximo **72 horas**. Las **multas RGPD pueden alcanzar 20 millones de euros**. La respuesta incluye: corrección inmediata de configuración, análisis de logs para determinar si alguien accedió, notificación a autoridades, notificación a afectados si hay alto riesgo, implementación de controles para prevenir futuros errores similares.

---

## 11. Proceso de clasificación


### 11.1. Pasos para clasificar

1. **Detectar y confirmar** el incidente.
2. **Recopilar información** inicial.
3. **Identificar factores** relevantes.
4. **Asignar categoría** principal.
5. **Determinar tipos** específicos.
6. **Evaluar impacto** y prioridad.
7. **Documentar** la clasificación.

Note: **La clasificación sigue un proceso estructurado y sistemático**, no es aleatoria. Primer paso: **detectar y confirmar que realmente es un incidente** (¿es una alarma falsa? ¿es una actividad legítima?). Segundo: recopilar información inicial mediante logs, alertas de sistemas de seguridad, informes de usuarios. Tercero: identificar factores relevantes (origen, sistemas afectados, usuarios implicados, momento del día). Cuarto: asignar la categoría principal según taxonomía (¿es código dañino, intrusión, fraude?). Quinto: determinar el tipo específico dentro de esa categoría (si es código dañino, ¿es ransomware, spyware, virus?). Sexto: evaluar peligrosidad e impacto para determinar prioridad. Séptimo: documentar todo el proceso y la decisión tomada. Como futuros profesionales, **debéis documentar meticulosamente cada paso** para auditorías futuras y aprendizaje organizacional.


### 11.2. Herramientas de apoyo

* **Matrices de decisión**: Flujos para determinar categoría.
* **Checklist de factores**: Verificación sistemática.
* **Base de datos de incidentes**: Casos similares previos.
* **Sistemas SIEM**: Correlación automática de eventos.

Note: **Las herramientas son facilitadoras pero no sustituyen el criterio experto** del analista. Las matrices de decisión son árboles de decisión que guían: "¿Es software malicioso? → Sí → ¿Cifra archivos? → Sí → Ransomware". Los checklists aseguran que no olvidamos evaluar ningún factor importante. Las bases de datos de incidentes previos son valiosas: "ya tuvimos un incidente similar hace seis meses, la clasificación fue X, la respuesta fue Y, funcionó". Los sistemas **SIEM (Security Information and Event Management)** correlacionan automáticamente eventos de múltiples fuentes y pueden sugerir clasificaciones basadas en patrones, pero requieren validación humana. **La experiencia del analista es crucial** para detectar sutilezas: un escaneo de puertos puede ser preparación de ataque APT o una auditoría legítima contratada, el contexto lo determina el analista.


### 11.3. Documentación obligatoria

Para cada incidente clasificado:

* Fecha y hora de detección.
* Categoría y tipo asignado.
* Factores considerados en la decisión.
* Sistemas y usuarios afectados.
* Impacto preliminar.
* Analista responsable.

Note: **La documentación no es burocracia innecesaria, es evidencia fundamental**. En caso de **auditoría externa, investigación legal, o proceso judicial**, esta documentación será **vuestra mejor defensa** para demostrar que actuasteis diligentemente. Debe incluir: timestamp exacto de cuándo se detectó el incidente (crítico para cumplir **plazos legales de 72 horas RGPD**), categoría y tipo asignado según taxonomía (para reporting y estadísticas), justificación de la clasificación explicando qué factores se consideraron (para auditorías), lista completa de sistemas y usuarios afectados (para análisis de alcance), evaluación preliminar del impacto en las cuatro dimensiones (información, servicios, legal, reputación), y nombre del analista responsable (para accountability). Esta documentación se archiva en el sistema de gestión de incidentes y debe ser inmutable (no se puede modificar retroactivamente sin dejar traza).

---

## 12. Respuesta a incidentes


### 12.1. Estrategias de respuesta

Acciones según tipo de incidente:

* **Malware**: Aislamiento, análisis forense, limpieza, búsqueda.
* **Intrusión**: Cambio de credenciales, análisis de accesos, parcheo.
* **DDoS**: Mitigación de tráfico, contacto con ISP, defensa perimetral.
* **Fuga de datos**: Corrección, notificación, auditoría de accesos.

Note: **Cada tipo de incidente requiere estrategias de respuesta específicas**. Para **malware**: aislar sistemas infectados de la red (contención), análisis forense del código malicioso para entender su comportamiento, limpieza mediante herramientas especializadas o reinstalación, búsqueda de otros sistemas comprometidos (el malware suele propagarse). Para **intrusión**: cambio inmediato de todas las credenciales potencialmente comprometidas, análisis exhaustivo de logs para determinar qué hizo el atacante mientras tuvo acceso, parcheo de la vulnerabilidad explotada, revisión de cuentas creadas y modificaciones realizadas. Para **DDoS**: activar servicios de mitigación (Cloudflare, Akamai), contactar con ISP para filtrado upstream, implementar rate limiting y geo-blocking. Para **fuga de datos**: corrección inmediata del error, análisis forense de quién accedió, notificaciones legales obligatorias, comunicación con afectados, mejora de controles.


### 12.2. Mitigación y prevención

Medidas para minimizar impacto futuro:

* **Copias de seguridad** regulares y probadas.
* **Formación de empleados** en detección de amenazas.
* **Actualización de sistemas** y parcheo de vulnerabilidades.
* **Implementación de controles** técnicos adicionales.

Note: **La respuesta a incidentes no termina con la recuperación**, debe incluir medidas para prevenir recurrencia. **Las copias de seguridad son la última línea de defensa** contra ransomware y pérdida de datos: deben ser regulares (diarias para datos críticos), almacenadas offline o inmutables (para que el ransomware no las cifre), y probadas periódicamente (una backup no probada es **una esperanza, no una certeza**). **La formación de empleados es crítica** porque el factor humano es el eslabón más débil: entrenarlos para detectar phishing, reportar actividades sospechosas, usar contraseñas fuertes, no instalar software no autorizado. La actualización de sistemas y parcheo elimina vulnerabilidades conocidas antes de que los atacantes las exploten. Los controles técnicos incluyen: autenticación multifactor, segmentación de red, monitorización mejorada, políticas de mínimo privilegio.


### 12.3. Planificación de respuesta

Elementos del plan de respuesta a incidentes:

* Procedimientos documentados por tipo de incidente.
* Roles y responsabilidades del equipo CSIRT/SOC.
* Protocolos de comunicación y escalado.
* Contactos de autoridades y proveedores externos.

Note: **Un plan de respuesta a incidentes bien diseñado marca la diferencia** entre caos y respuesta organizada. Debe incluir procedimientos específicos documentados: "Si detectas ransomware: paso 1, paso 2, paso 3...". **Definir claramente roles y responsabilidades**: quién lidera la respuesta (incident manager), quién hace análisis forense (analistas técnicos), quién gestiona comunicación (relaciones públicas), quién coordina con legal (DPO/compliance). Establecer protocolos de comunicación: ¿a quién se notifica? ¿cuándo se escala a dirección? ¿cómo se comunica con clientes? Mantener actualizada una lista de contactos críticos: CCN-CERT, INCIBE, policía especializada en cibercrimen, proveedores de servicios de seguridad, abogados especializados, aseguradoras. **El plan debe practicarse mediante simulacros regulares** para identificar gaps antes de un incidente real.

---

## 13. Revisión y actualización


### 13.1. Taxonomía viva

* Las amenazas evolucionan constantemente.
* Nuevos tipos de ataques emergen.
* La taxonomía debe actualizarse.
* Revisión periódica necesaria.

Note: **La ciberseguridad no es estática, es un campo en constante evolución**. **La taxonomía debe ser un documento vivo** que evoluciona con las amenazas. **Hace 5 años, la taxonomía no contemplaba muchos ataques actuales**: **ransomware-as-a-service (RaaS)** donde grupos criminales alquilan infraestructura de ransomware, ataques a la cadena de suministro (supply chain) como SolarWinds, cryptojacking (uso no autorizado de recursos para minar criptomonedas), deepfakes utilizados en ingeniería social avanzada. Los organismos como INCIBE, CCN-CERT y ENISA publican actualizaciones periódicas de la taxonomía incorporando nuevos tipos de amenazas. Las organizaciones deben **revisar su taxonomía interna al menos anualmente**, o inmediatamente cuando aparezca un tipo de ataque nuevo que no encaje en las categorías existentes.


### 13.2. Fuentes de actualización

* Boletines de CCN-CERT.
* Alertas de INCIBE.
* Informes de ENISA.
* Comunidad internacional de respuesta a incidentes.
* Lecciones aprendidas de incidentes propios.

Note: **Mantenerse actualizado es una responsabilidad profesional crítica**. **CCN-CERT publica boletines semanales** con alertas de seguridad, vulnerabilidades críticas, y campañas activas de malware; es **obligatorio seguirlos si trabajáis en administraciones públicas**. INCIBE ofrece alertas temprana de amenazas dirigidas al sector privado español. ENISA publica informes trimestrales sobre el panorama de amenazas europeo (ENISA Threat Landscape - ETL). La comunidad internacional incluye organizaciones como **FIRST (Forum of Incident Response and Security Teams)**, **MITRE ATT&CK framework** (taxonomía de técnicas de atacantes), y equipos CERT/CSIRT de otros países. Internamente, las lecciones aprendidas de vuestros propios incidentes son invaluables: "detectamos un nuevo tipo de ataque contra nuestra organización, debemos añadirlo a nuestra taxonomía". Como profesionales, **debéis suscribiros a estas fuentes** y dedicar tiempo semanal a manteneros actualizados.

---

## 14. Conclusión


### 14.1. Resumen de conceptos clave

* La taxonomía es un **idioma común** en ciberseguridad.
* Permite **identificación rápida** y **respuesta efectiva**.
* Basada en **estándares internacionales** (INCIBE, CCN-CERT, ENISA).
* Considera **múltiples factores** para clasificación precisa.
* Incluye **categorías principales** reconocidas.

Note: **Recapitulemos los conceptos fundamentales** que habéis aprendido. **La taxonomía no es una lista arbitraria de categorías** para memorizar, es **un idioma común** que permite a todas las organizaciones comunicarse eficazmente sobre incidentes de ciberseguridad. **Sin este lenguaje común**, cada organización describiría incidentes de manera diferente, dificultando la colaboración y el intercambio de información sobre amenazas. La taxonomía permite identificación rápida del tipo de incidente, lo que acelera la respuesta: en lugar de perder tiempo debatiendo "¿qué tipo de ataque es esto?", usamos categorías estándar y pasamos directamente a la respuesta. Está basada en **estándares internacionales coordinados**, no inventados arbitrariamente. La clasificación considera múltiples factores (origen, método, impacto, sistemas afectados) para ser precisa. Las categorías principales están reconocidas y aceptadas globalmente.


### 14.2. Importancia para profesionales

Para alumnos y alumnas:

* Habilidad fundamental en equipos SOC/CSIRT.
* Comunicación efectiva con stakeholders.
* Base para procedimientos de respuesta.
* Requisito en certificaciones profesionales.

Note: **¿Por qué es importante para vosotros como futuros profesionales?** Primero, es una **habilidad fundamental absolutamente necesaria** si trabajáis en un **SOC (Security Operations Center)** o **CSIRT (Computer Security Incident Response Team)**; literalmente **no podéis hacer el trabajo sin dominar la taxonomía**. Segundo, facilita la comunicación efectiva con stakeholders: podéis explicar a dirección "tenemos un incidente categoría X con impacto Y" y ellos entienden inmediatamente la gravedad sin necesidad de explicaciones técnicas largas. Tercero, es la base para todos los procedimientos de respuesta: cada categoría tiene procedimientos específicos asociados. Cuarto, es **requisito en certificaciones profesionales reconocidas**: GIAC (GCIH), CISM, CISSP, todas evalúan conocimiento de taxonomías de incidentes. **Dominar la taxonomía os diferenciará como profesionales competentes** y os permitirá contribuir efectivamente desde el primer día en cualquier equipo de ciberseguridad.


### 14.3. Próximos pasos

1. Estudiar la taxonomía de referencia completa.
2. Practicar con casos reales.
3. Familiarizarse con herramientas de clasificación.
4. Participar en ejercicios de respuesta a incidentes.
5. Mantenerse actualizado con nuevas amenazas.

Note: **¿Qué debéis hacer ahora para consolidar este conocimiento?** Primero, **estudiad en profundidad la Guía Nacional de INCIBE** y la CCN-STIC 817, **no solo las slides**; entended cada categoría con ejemplos reales. Segundo, **practicad con casos reales**: analizad noticias de incidentes recientes (brechas de datos publicadas, ataques ransomware a empresas conocidas) e intentad clasificarlos según la taxonomía. Tercero, familiarizaos con herramientas reales de clasificación: probad SIEMs en entornos de laboratorio, explorad plataformas de threat intelligence. Cuarto, participad en ejercicios prácticos: CTFs (Capture The Flag) de seguridad defensiva, simulacros de respuesta a incidentes, competiciones como CyberLeague. Quinto y más importante, manteneos actualizados: suscribiros a boletines de CCN-CERT e INCIBE, seguid cuentas de Twitter/X de investigadores de seguridad, leed informes de empresas como Mandiant, CrowdStrike, Kaspersky. **La ciberseguridad evoluciona rápidamente**; lo que aprendéis hoy es la base, pero **debéis aprender continuamente toda vuestra carrera profesional**.

---

## Bibliografía

* [Guía Nacional INCIBE](https://www.incibe.es/sites/default/files/contenidos/guias/doc/guia_nacional_notificacion_gestion_ciberincidentes.pdf)
* [CCN-STIC 817](https://www.ccn-cert.cni.es/)
* [ENISA Taxonomy](https://www.enisa.europa.eu/publications/reference-incident-classification-taxonomy)
* [Repositorio GitHub](https://github.com/flosada/RSITaxonomy_ES/blob/master/humanv1.md)

Note: **Estas son las fuentes oficiales y autorizadas que debéis consultar** para profundizar. **La Guía Nacional de INCIBE es el documento fundamental en España**, contiene la taxonomía completa, ejemplos de clasificación, niveles de peligrosidad e impacto, y procedimientos de notificación obligatorios. **Es lectura obligatoria** para cualquier profesional de ciberseguridad en España. **La CCN-STIC 817** es la guía del Centro Criptológico Nacional para gestión de ciberincidentes en el marco del Esquema Nacional de Seguridad; es **vinculante para administraciones públicas**. **La taxonomía de ENISA es la referencia europea**, proporciona contexto internacional y permite comparar con taxonomías de otros países. El repositorio GitHub de RSITaxonomy_ES es un proyecto colaborativo que traduce y adapta la taxonomía de FIRST al contexto español, muy útil para ver la evolución de la taxonomía. **Consultad estas fuentes regularmente** porque se actualizan periódicamente con nuevas categorías y tipos de incidentes a medida que emergen nuevas amenazas.
