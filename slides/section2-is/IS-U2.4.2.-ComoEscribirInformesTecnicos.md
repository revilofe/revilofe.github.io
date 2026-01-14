# U2.4.2 - Cómo escribir informes técnicos

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

Note: Presentamos la unidad **U2.4.2 Cómo escribir informes técnicos**. Explicaremos qué es un informe técnico, los consejos estratégicos, de estructura, de redacción y **espirituales** para mejorar tu capacidad de comunicar hallazgos y análisis de forma clara y efectiva. Esta unidad es fundamental para tu desarrollo profesional como técnico de seguridad.

---

## Índice

* 1. Introducción
* 2. Consejos estratégicos
* 3. Consejos de estructura
* 4. Consejos de redacción
* 5. Consejos espirituales
* 6. Informes de incidentes de seguridad
* 7. Conclusiones

Note: Explica el recorrido de la unidad. Empezaremos viendo por qué es importante escribir bien, pasaremos a consejos prácticos de estrategia y estructura, veremos cómo redactar profesionalmente, mejorar con técnicas de revisión, y finalizaremos con recomendaciones específicas para informes de incidentes de seguridad.

---

## 1. Introducción

Note: Introduce la realidad profesional: aunque los técnicos prefieren cacharrear y desarrollar, en el mundo laboral la capacidad de **comunicar eficazmente** es tan importante como la capacidad técnica. Un informe mal escrito o confuso puede restar credibilidad a tu trabajo técnico, por muy bueno que sea.

### 1.1. La importancia de saber escribir informes

* Tu trabajo técnico se mide por dos factores:
  * Tu capacidad técnica REAL
  * Tu capacidad técnica PERCIBIDA
* Un informe es una **extensión de tus capacidades**
* Sin buena comunicación, tu trabajo no se valora adecuadamente

Note: Enfatiza que aunque parezca injusto, la realidad es que el trabajo técnico se juzga también por cómo se presenta. Una presentación, documentación o informe pueden ser la diferencia entre que tu idea sea aprobada o rechazada, entre que consigas ascenso o no.

### 1.2. Temas que cubriremos

* Consejos estratégicos: cómo planificar tu informe
* Consejos de estructura: cómo organizarlo
* Consejos de redacción: cómo escribir profesionalmente
* Consejos espirituales: técnicas de mejora continua
* Casos específicos: informes de incidentes

Note: Adelanta brevemente qué hay en cada sección. La idea clave es que verás que escribir bien es un **conjunto de técnicas** que se pueden aprender y mejorar con práctica.

---

## 2. Consejos estratégicos

Note: Abrimos con los consejos estratégicos. Estos son los fundamentos sobre los que construirás tu informe. Son decisiones de alto nivel que marcan el tono y dirección del documento.

### 2.1. Determina los objetivos del informe

* Antes de escribir: **¿Cuál es el objetivo?**
* Condensa el objetivo en **una línea de texto**
* Úsala como regla para decidir qué incluir

Ejemplos:
* Definir la respuesta llevada a cabo respecto al incidente PI-0023
* Establecer los requisitos de seguridad de la arquitectura XXX
* Decidir si emplear la tecnología X o Y en el proyecto Z

Note: Explica que sin un objetivo claro, el informe se convierte en una lista sin dirección. El objetivo es como una **brújula**: te dice qué información es necesaria y qué es relleno. Si lo que escribes no contribuye al objetivo, probablemente deba eliminarse.

### 2.2. Identifica a tu audiencia

* Diferentes perfiles tienen necesidades distintas
* **Técnicos**: quieren detalles técnicos y solidez de decisiones
* **Directivos**: buscan costes, plazos y ventajas competitivas
* **Legal**: necesitan normativas, leyes y consecuencias

Consejo: **Redacta pensando en tu audiencia específica**

Note: Recalca que adaptar el mensaje a la audiencia es clave. No es lo mismo escribir para un CTO que para un CEO, que para un abogado. Conocer tu audiencia permite elegir qué destacar, qué minimizar y qué nivel de detalle usar.

### 2.3. KISS: Keep It Simple, Stupid

* Algunos valoran los informes por número de páginas
* La realidad: jefes quieren informes **concisos y claros**
* Mejor: 20 páginas bien escritas que 200 de relleno

Ejemplo: informe incidente (versión larga)
* *Los atacantes hicieron uso de una vulnerabilidad 0-day para realizar un DDoS para agotar los recursos de CPU en 16 frontales web, obligando a técnicos a entrar por VPN SSL y reiniciar servidores...*

Ejemplo: informe incidente (versión clara)
* *Los atacantes emplearon un 0-day para realizar un DDoS contra los frontales web del clúster PEPITO. Los técnicos tuvieron que reiniciar los servidores 2, 3 y 5.*

Note: Muestra la diferencia tangible: pasamos de 8 líneas a 2, sin perder información esencial. La brevedad no significa perder detalle; significa **eliminar lo innecesario**. Los anexos son para eso: guardar lo detallado si alguien lo necesita.

### 2.4. Ofrece valor

* Todo informe debe responder: **¿Qué valor aporto?**
* Identifica y resalta el valor en lugares estratégicos
* Ejemplo: optimización de reglas YARA eliminó 100 reglas, reduciendo un 20% la tasa de falsos positivos

Note: Subraya que el valor no es obvio por sí solo. Si has hecho un trabajo de optimización importante, di explícitamente cuál es el beneficio. Resáltalo en el resumen ejecutivo o conclusiones, no esperes que el lector lo descubra solo.

---

## 3. Consejos de estructura

Note: Una buena estructura hace que tu informe sea más fácil de escribir y, sobre todo, de leer. Es como un mapa que guía tanto a ti como al lector.

### 3.1. Define una estructura base

Estructura básica recomendada:
* **Resumen ejecutivo**: lo más importante (1 página)
* **Objeto y alcance**: qué cubre el documento
* **Antecedentes**: contexto necesario previo
* **Análisis**: el trabajo realizado
* **Conclusiones**: a qué llegamos
* **Anexos**: información adicional

Note: Explica que esta estructura funciona para casi cualquier informe técnico. El **resumen ejecutivo es crítico** porque en muchos casos es lo único que se lee. Los anexos son el lugar para evidencias extensas que demuestran tu trabajo pero no caben en el cuerpo principal.

### 3.2. Define el índice antes de escribir

* Antes de redactar: **crea el índice completo**
* Identifica puntos principales y subapartados
* Esto te ayuda a:
  * Estructurar lógicamente tu contenido
  * Saber dónde va cada cosa
  * Escribir "rellenando" los huecos

Note: Cuenta que crear un índice es como hacer un **mapa mental** antes de conducir. Te muestra adónde vas y qué pasos dar. Además, un buen índice es una excelente herramienta de navegación para el lector: con solo leerlo, sabe si el documento le interesa.

### 3.3. El resumen ejecutivo es tu mejor amigo

* **Máximo**: una página A4 a letra normal
* **Lectura**: menos de 2 minutos
* **Lenguaje**: claro, sin terminología técnica (regla del niño de 6 años)
* **Contenido esencial**:
  1. Problema objeto del informe
  2. Solución propuesta
  3. Acciones tomadas

Note: Destaca que el resumen ejecutivo es posiblemente la **parte más importante** del documento. En algunos casos es lo único que los directivos leerán. Tiene que ser un **ejercicio de minimalismo**: máxima información con mínimas palabras. Si crees que tu resumen puede ser más breve, hazlo.

### 3.4. Los anexos son el trastero de tu informe

* Problema común: saturación de información
* Solución: **anexos**
* Usa técnica de recorte:
  * En lugar de 5 páginas de salida de herramienta, muestra 4 líneas clave
  * El resto va como anexo completo (para verificabilidad)

Note: Explica la **fatiga cognitiva**: 600 páginas de informe es una pesadilla de navegación. Los anexos te permiten incluir evidencias (logs completos, herramientas, screenshots) sin sobrecargar el texto principal. El lector interesado puede profundizar; el que solo quiere lo esencial, lo encuentra.

### 3.5. Convierte tu informe en plantilla

* Antes de hacer un nuevo informe: **¿existe ya una plantilla?**
* Si no existe: crea una (deja bonito el primero)
* Ventajas:
  * Reutilizas estructura y formato
  * Ahorras mucho tiempo
  * Garantizas consistencia

Note: Como los programadores reusan código, tú puedes reusar documentos. El primer informe cuesta más trabajo porque lo haces desde cero. Pero si lo dejas como plantilla, los siguientes son cuestión de "rellenar" la estructura existente.

### 3.6. Huye de múltiples niveles anidados

* Evita estructuras complicadas como: 1.3.1.2.2.1.1
* **Regla del tres**: máximo 3 niveles de anidado
  * Nivel 1: títulos principales (##)
  * Nivel 2: subtítulos (###)
  * Nivel 3: subsubtítulos (####)

Note: Cuenta que un documento muy anidado se parece a un laberinto: pierdes al lector. Tres niveles es un **compromiso entre funcionalidad y legibilidad**. Si necesitas más niveles, probablemente debas reorganizar el contenido.

### 3.7. [Advanced] Haz tu informe fácilmente divisible

* Si varias personas usan tu informe (sistemas, redes, seguridad):
  * Estructura como "mini informes" independientes
  * Permite recortar y distribuir solo la parte relevante
* Ejemplo: auditoria de seguridad
  * Parte 1: resultados del servidor A
  * Parte 2: resultados del servidor B
  * Cada parte puede entregarse por separado

Note: Señala que esto es útil en proyectos grandes. Si bien es complicado, cuando lo consigues, el informe se vuelve **reutilizable y modular**.

---

## 4. Consejos de redacción

Note: Pasamos a cómo **escribir** el contenido. Estos consejos son tácticos: pequeños cambios que mejoran significativamente la legibilidad.

### 4.1. El corrector ortográfico es OBLIGATORIO

* Pasar corrector: **no cuesta dinero**
* Faltas como "vamos *haber*" o "*llendo*" destruyen el informe
* Consejo adicional:
  * Añade terminología técnica al diccionario personal
  * Así las faltas de ortografía destacan más

Note: Suena obvio, pero no lo es. He visto informes con faltas graves que menguan la credibilidad del autor. El corrector es tu aliado. Y no, no te hace menos hacker o menos técnico; al contrario, te hace más profesional.

### 4.2. Cuidado con las frases largas

Problema: frases de 8+ líneas son indigestas
* *Los atacantes emplearon spear-phishing contra cargos con documento malicioso que solicitaba activación de macros y lanzaba Powershell que contactaba con C2 y descargaba malware que robaba credenciales, se instalaba como servicio e intentaba escalar privilegios con CVE-2019-001.*

Solución: **divide la frase en varias**
* *Los atacantes emplearon spear-phishing contra varios cargos con documento malicioso.*
* *El documento solicitaba activación de macros. Al aceptarse, lanzaba un Powershell que contactaba con el C2.*
* *Se descargó la siguiente fase del malware.*

Regla: **si no puedes decir la frase sin respirar, divídela**

Note: La regla práctica es simple: intenta **leer en voz alta** la frase. Si necesitas respirar en medio, está demasiado larga. Frases cortas = lectura más ágil = mejor comprensión.

### 4.3. No escatimes con los párrafos

Problema: bloque de texto de 20+ líneas (ladrillito)
* Solución: **máximo 6-8 líneas por párrafo**
* Cada párrafo = una idea principal
* Ejemplo: divide un "ladrillito" en 4 párrafos temáticos

Note: El bloque de texto denso cuesta de leer, especialmente en pantalla. Los párrafos pequeños **rompen la monotonía** y hacen el texto más digerible. Además, cada párrafo centrado en una idea ayuda a la **comprensión**.

### 4.4. Elige voz pasiva o activa, pero mantén consistencia

Opción 1: primera persona (evitar)
* *Yo revisé los logs y encontré accesos inapropiados.*

Opción 2: tercera persona
* *El analista revisó los logs y encontró accesos inapropiados.*

Opción 3: voz pasiva (más profesional)
* *Se revisaron los logs y se encontraron accesos inapropiados.*

Consejo: **elige una y mantenla en todo el documento**

Note: No importa cuál elijas; lo importante es ser consistente. La voz pasiva suele quedar más profesional, pero si tercera persona te parece más natural, úsala. La inconsistencia es lo que queda mal.

### 4.5. Usa los tipos de letra con sabiduría

* Elige **un solo tipo de letra**
* Recomendados: Open Sans Light, Calibri, Liberation Sans/Serif
* Usa **negritas** para palabras clave
* Usa **cursivas** para evidencias o citas
* Ejemplo:
  * Los atacantes lanzaron un **spear-phishing** contra cargos, descargando malware en el servidor **MENGANITA**.
  * *Logs de acceso: Jan 13 15:24 Session started for user pepito1*

Note: Las negritas actúan como **anclas** que enfocan el ojo del lector. Las cursivas, en cambio, **restan importancia** (útil para evidencias técnicas que el lector interesado puede leer, pero que no es necesario para entender la idea principal).

### 4.6. Usa sangrías para mejorar legibilidad

* Las sangrías ayudan a **romper la monotonía**
* Útiles para:
  * Listas (que naturalmente llevan sangría)
  * Ejemplos o datos aislados
  * Bloques de código o logs
* Efecto: diferenciar tipos de contenido

Note: Las sangrías **crean estructura visual**. El ojo se da cuenta de que hay contenido diferente y se prepara para procesarlo distinto. Es un pequeño detalle que mejora mucho la experiencia del lector.

### 4.7. Usa terminología adecuada a la audiencia

Evitar: exceso de ATL (Acrónimos de Tres Letras) y jerga
* Mal: *Atacante usó XMAS nmap para detectar SIP, empleó RCE en Asterisk y desplegó Cobalt Strike con C2 maleable.*

Bien: *Atacante realizó port scanning con nmap y detectó el puerto 5060 (SIP). Ejecutó un exploit RCE contra Asterisk, desplegando Cobalt Strike con C2 personalizable.*

Consejo: **explica los términos en primera mención o úsalos solo si tu audiencia los entiende**

Note: El equilibrio es clave. No simplificar tanto que pierdas precisión, pero tampoco usar jerga que la audiencia no entienda. Si hablas con técnicos puros, puedes ser más técnico; si incluye directivos, simplifica.

### 4.8. Los gráficos cuestan, pero merecen la pena

* Poder de los gráficos: **transmiten información de un vistazo**
* Ejemplos útiles:
  * Matriz vulnerabilidades × sistemas (código de colores por gravedad)
  * Gráfica de barras con horas de conexión de atacantes
  * Cronología visual de incidentes
* Mensaje: **una imagen vale más que mil palabras**

Note: Los gráficos no son "cosa de diseñadores". Son una herramienta poderosa de comunicación. Especialmente en auditorias o análisis, un buen gráfico permite que cualquiera vea el estado de un vistazo.

### 4.9. [Advanced] Hazte con un libro de estilo

* Para mejorar la escritura al siguiente nivel:
  * [Libro de estilo RAE](https://www.planetadelibros.com/libro-libro-de-estilo-de-la-lengua-espanola/)
  * [Libro de estilo El País](https://www.amazon.es/)
* Consejo: aprende de un compañero/a exigente

Note: Si ya escribes bien y quieres mejorar, consigue un libro de estilo de referencia. La RAE y El País tienen excelentes manuales. También puedes pedirle a un compañero crítico que revise tu trabajo; ese feedback es oro puro.

---

## 5. Consejos espirituales

Note: Estos consejos se refieren a **técnicas de revisión y mejora continua**. Son "espirituales" porque hablan de tu actitud y proceso, no solo del contenido.

### 5.1. Segundas y terceras lecturas nunca fueron malas

* Primera lectura: redactando (enfoque en escribir)
* Segunda lectura: revisando (enfoque en leer)
* La segunda lectura encuentra:
  * Frases sin sentido
  * Puntos que necesitan reescritura
  * Aspectos no reflejados
  * Incoherencias
* **Informe importante**: incluye tercera lectura

Note: Cuando escribes estás enfocado en plasmar ideas. Cuando relees, tu cerebro está en modo "recepción" y ve cosas que no viste al escribir. Una segunda lectura SIEMPRE mejora el informe.

### 5.2. Haz que tus compañeros lean tu informe

* Pide a un compañero imparcial que lo revise
* Ellos detectarán:
  * Lagunas no obvias para ti
  * Zonas de mejora
  * Errores que pasaste por alto
* Consejo: **sé también buen compañero** y revisa el suyo

Note: Un par de ojos externos siempre ve cosas que tú no ves. Además, si alguien imparcial entiende tu informe a la primera, es que está bien redactado. Si tienen que hacerte preguntas, hay puntos que debes aclarar.

### 5.3. Lee tu informe en voz alta o cuéntalo a alguien

* Leer en voz alta activa otros caminos cognitivos
* Al vocalizar surgen ideas de mejora
* Alternativa: **cuéntaselo a alguien**
  * Si tu audiencia es similar, sabes si el mensaje llega
  * Recibes feedback directo
* Efecto: mejora el documento

Note: Parece raro, pero funciona. Tu voz activa otras partes del cerebro. Además, al contar algo a alguien te das cuenta si realmente lo entiendes bien o si te faltan conexiones lógicas.

### 5.4. Deshazte de tus coletillas

* Todos tenemos peculiaridades al escribir:
  * Amor por las comas
  * Palabras predilectas
  * Formas de empezar párrafos (ej: el autor ama los puntos suspensivos)
* **Localiza tus coletillas** y trabaja para cambiarlas
* Ventaja: tu estilo se vuelve más profesional

Note: Las coletillas no son malas per se, pero si dominan tu escritura, restan calidad. Identifícalas (tus colegas te ayudan) y poco a poco elimínalas. El resultado es un estilo más **pulido y menos predecible**.

### 5.5. Practica, practica y practica

* Escribir informes es una **habilidad que mejora con práctica**
* Tu segundo informe > primero
* Tu décimo informe > noveno
* Llegará un momento: "*Level Up: Writing reports skill acquired!*"
* No es lo rápido; es **consistencia**

Note: No te desesperes si tu primer informe no es perfecto. Lo normal es que sea "una castaña". Pero cada informe que escribas te enseña algo. Con suficiente práctica, escribir buenos informes se convierte en algo natural.

---

## 6. Informes de incidentes de seguridad

Note: Los informes de incidentes de seguridad son un **caso especial**. Tienen características propias que debes tener en cuenta. Aquí vemos consejos adicionales a los ya vistos.

### 6.1. Conoce tus tipos de informe

**Informe de detección**
* Se ha confirmado un incidente
* Dirigido a: responsables técnicos
* 2-3 párrafos: qué se sabe, sistemas afectados, impacto estimado
* Objetivo: iniciar respuesta rápida

**Informes de batalla**
* Actualizaciones durante la respuesta
* Resumen de acciones del equipo de respuesta
* Aumenta exactitud a medida que avanza

**Informes de crisis**
* Misma función que "batalla" pero audiencia no técnica
* Dirigido a: dirección, legal
* Lenguaje claro, cuidado con exactitud

**Informes de IOC**
* Comparte inteligencias con otros departamentos
* 1-2 párrafos introductorios
* Listado de IOC (Indicadores de Compromiso) para verificación

Note: Cada tipo tiene propósito y audiencia distinto. Identificar cuál necesitas es el primer paso. No redactes el mismo tipo de informe para técnicos y directivos; adapta contenido y lenguaje.

### 6.2. Estructura avanzada para incidentes

* **Resumen ejecutivo**: qué pasó, claro y conciso
* **Timeline del incidente**: ver apartado propio
* **Datos del entorno**: contexto técnico
* **Gestión del incidente**: qué se hizo para responder
* **Análisis forense**: si procede
* **Análisis de malware**: si procede
* **Peligrosidad e impacto**: qué se perdió, cuántos equipos
* **Atribución**: quién fue (si es posible)
* **Recomendaciones**: cómo evitarlo en el futuro
* **Lecciones aprendidas**: qué bien, qué mal, cómo mejorar
* **Anexos**: IOC, IAC, evidencias

Note: Esta estructura es más **detallada que la básica** porque los incidentes requieren documentación rigurosa. Cada sección tiene propósito claro: recopila información, documenta respuesta y extrae lecciones.

### 6.3. Exactitud por encima de todo

* Exactitud es **crítica** en respuesta a incidentes
* Recalca todas las afirmaciones con **evidencias**
* Ejemplo efectivo:
  * Afirmación: "primera conexión el 7 de enero a 16:32h"
  * Evidencia: extracto del log que lo demuestra
* Ventaja: **repetibilidad**
  * El lector puede ejecutar el comando y obtener el mismo resultado
  * Incrementa credibilidad

Note: En incidentes, la exactitud no es lujo; es **obligación**. Tus conclusiones pueden analizarse en un juicio o auditoria externa. Por eso cada afirmación debe estar respaldada. Muestra comandos, salidas de herramientas, logs; que cualquiera pueda reproducir tu análisis.

### 6.4. Cuenta lo que se ha hecho, no lo que deberías haber hecho

* Problema: tendencia a adornar acciones para quedar mejor
* Realidad: con experiencia, cualquiera entiende que la respuesta fue difícil
* Consejo: **sé honesto en el informe**
  * Documenta lo que hiciste
  * Incluye errores (para eso están "lecciones aprendidas")
  * Un lector experto sabrá evaluar si las decisiones fueron correctas

Note: Hay presión por parecer que todo se hizo perfecto, pero eso es contramotivador. Si hiciste algo mal o que ahora ves que no fue óptimo, docúmentalo honestamente. Los jefes competentes saben que responder incidentes en tiempo real es difícil.

### 6.5. Distingue claramente hechos de hipótesis

Hechos (demostrado):
* *En el servidor PEPITO hay 4 cuentas de administrador.*
* *La usuaria MENGANITA inició sesión el 7 de enero a 14:32h.*

Hipótesis (suposición posible):
* *Los atacantes son norcoreanos.*
* *MENGANITA tenía contraseña débil.*

Consejo: **toda hipótesis debe estar sustentada con hechos**
* Hipótesis ≠ Opinión
* Evalúa hipótesis e intenta contrastarlas
* Si no hay datos que las soporten: no las incluyas

Note: La diferencia es crítica. Los hechos son lo que **puedes demostrar** (logs, archivos, etc.). Las hipótesis son lo que **crees que pasó** basándote en hechos parciales. En un informe de incidente, presenta hechos, formula hipótesis y luego valida cuáles de tus hipótesis tienen soporte.

### 6.6. Data todas tus acciones y genera una timeline

* Documentar tiempos es **fundamental**
* Puntos clave:
  * Detección de malware en equipo X
  * Extracción de C2
  * Solicitud de bloqueo
  * Bloqueo efectivo

Timeline de ejemplo (5 líneas, mucha información):
* *15/Ene 23:45h – Correo malicioso enviado*
* *16/Ene 09:32h – Usuaria abre correo e infecta equipo*
* *16/Ene 09:33h – Malware contacta C2*
* *16/Ene 10:01h – Atacantes inician sesión en servidor PEPITO*
* *17/Ene 12:07h – Disco lleno detectado; se alerta a ciberseguridad*

Ventaja: narra el incidente de forma clara y resumida

Note: La timeline es una herramienta poderosa. Con solo verla, cualquiera entiende qué pasó, cuándo pasó y qué se hizo. Además, si algo salió mal (ejemplo: solicitaste bloqueo el lunes pero no se aplicó hasta el miércoles), la timeline lo muestra claramente.

### 6.7. Crea listados de equipos y usuarios afectados

* Mantén **dos listados separados**:
  * Usuarios afectados
  * Equipos afectados
* Información por equipo:
  * Nombre del equipo
  * Dirección IP
  * MAC (si puedes)
* Ventaja:
  * Facilita recuperación (cambio contraseñas, formateo)
  * Calcula impacto correctamente

Note: Estos listados son **operativos**: el equipo de Sistemas los usa para recuperar los equipos. Ser específico (nombre, IP, MAC) evita formatear el equipo equivocado. Es un detalle pequeño pero crítico.

---

## 7. Conclusiones

Note: Cerramos la unidad enlazando todo lo visto con tu desarrollo profesional.

### 7.1. Soft skills en la práctica

* Escribir informes es una **soft skill** crítica
* Aunque prefiertes cacharrear, es fundamental para tu carrera
* Aplicaciones prácticas:
  * Convencer para aprobar presupuestos
  * Demostrar riesgos de seguridad a otros equipos
  * Documentar tu trabajo para análisis posterior

Note: Recalca que las soft skills no son secundarias. Un técnico brillante sin capacidad de comunicación es como un chef excelente que no sabe presentar los platos. La comunicación **multiplica el valor** de tu trabajo técnico.

### 7.2. Ideas clave

* Define **objetivo** y conoce tu **audiencia**
* Usa estructura base: resumen, antecedentes, análisis, conclusiones
* Resumen ejecutivo es crítico: máximo 1 página, lenguaje claro
* Redacción: frases cortas, párrafos pequeños, terminología adecuada
* Revisión: segunda lectura, feedback de compañeros, lectura en voz alta
* Incidentes: exactitud, timeline, distinción hechos/hipótesis

Note: Repasa en voz alta cada idea, conectando con ejemplos específicos de la unidad. Enfatiza que son técnicas **que funcionan** y que se mejoran con práctica.

### 7.3. Tu rol como futuro profesional

* Podrás ser **responsable de escribir informes** críticos
* Podrás **revisar y mejorar** procesos de documentación
* Podrás **enseñar a compañeros** técnicas de redacción
* Esto es una **competencia muy valorada** en el mercado

Note: Cierra conectando con el futuro profesional. Saber escribir bien te diferencia, te hace más valioso y más "ascendible". Es una inversión en ti mismo que repercute directamente en tu carrera.
