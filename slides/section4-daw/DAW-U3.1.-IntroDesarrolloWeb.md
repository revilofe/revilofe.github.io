# DAW-U3.1 - Introducción al Desarrollo Web

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

1. El desarrollo web actual
2. Modelos de ejecución: cliente y servidor  
3. Componentes web: Frontend y Backend
4. Página Web vs Aplicación Web
5. Clics en la web: ¿Qué sucede?
6. Resumen

Note: Esta presentación cubre los fundamentos del desarrollo web moderno, desde los conceptos básicos hasta el flujo completo de una petición HTTP. Aprenderemos la diferencia entre frontend y backend, cómo colaboran cliente y servidor, y qué diferencia una página web de una aplicación web. También entenderemos todo el proceso que ocurre cuando hacemos clic en un enlace web.

---

## 1. El desarrollo web actual

Note: El desarrollo web moderno va mucho más allá de crear páginas HTML estáticas. Hoy en día implica crear aplicaciones completas que funcionan a través de Internet, y un aspecto crucial es el **despliegue**: cómo ponemos estas aplicaciones a disposición de los usuarios finales. El despliegue es el proceso de llevar nuestra aplicación del entorno de desarrollo al entorno de producción, donde estará accesible 24/7 para usuarios de todo el mundo.


### 1.1. Objetivos del despliegue

- **Accesibilidad**: disponible 24/7 desde cualquier lugar
- **Estabilidad**: funciona sin errores ni caídas
- **Escalabilidad**: crece según la demanda
- **Seguridad**: protege datos y usuarios

Note: Los cuatro pilares del despliegue son fundamentales. **Accesibilidad** significa que los usuarios pueden acceder desde cualquier dispositivo y ubicación, con tiempos de carga óptimos. **Estabilidad** implica minimizar tiempos de inactividad y garantizar que las actualizaciones no rompan funcionalidades. **Escalabilidad** es la capacidad de soportar picos de tráfico y añadir recursos según demanda. **Seguridad** incluye cifrado HTTPS, autenticación robusta y protección contra ataques comunes como SQL injection o XSS.


### 1.2. Ventajas del despliegue eficiente I

- **Rapidez Time-to-Market**: lanzar productos rápidamente
- **Iteración rápida**: entregas frecuentes de mejoras
- **Automatización**: reducir errores humanos

Note: Un despliegue eficiente transforma la velocidad de entrega. **Time-to-Market** rápido permite responder a necesidades del mercado y obtener ventaja competitiva. **Iteración rápida** significa despliegues frecuentes con cambios pequeños, obteniendo feedback rápido de usuarios y corrigiendo errores ágilmente. **Automatización** mediante scripts, pipelines y pruebas automáticas reduce drásticamente los errores humanos y permite rollback automático si algo falla.


### 1.2. Ventajas del despliegue eficiente II

- **Competitividad**: servicio fiable y de calidad
- **Documentación**: procesos bien documentados

Note: La **competitividad** mejora porque ofrecemos mejor experiencia de usuario, generamos mayor confianza y reducimos costes operativos. Una buena **documentación** de los procesos de despliegue es indispensable: facilita la replicación de entornos, ayuda en resolución de problemas, es esencial para formar nuevos miembros del equipo y cumple con requisitos de auditorías. Recordad que estos conceptos están directamente relacionados con DevOps y CI/CD que ya estudiamos en la Unidad 1.

---

## 2. Modelos de ejecución: cliente y servidor

Note: La lógica de una aplicación web se divide en dos entornos: el lado del cliente (frontend) y el lado del servidor (backend). Esta separación no es arbitraria, sino que responde a responsabilidades específicas y complementarias. Entender esta división es fundamental para comprender cómo funcionan las aplicaciones web modernas y tomar decisiones correctas sobre dónde ejecutar cada parte de nuestra lógica.


### 2.1. Código en el lado del cliente (Frontend) I

**Tecnologías principales:**

- **HTML**: estructura y contenido
- **CSS**: presentación y estilos
- **JavaScript**: interactividad y lógica dinámica

Note: El frontend es todo lo que se ejecuta en el navegador del usuario. **HTML** define la estructura semántica del contenido (títulos, párrafos, listas, formularios). **CSS** controla toda la presentación visual: colores, tipografías, disposición de elementos, animaciones. **JavaScript** añade la interactividad: responde a clics, valida formularios, hace peticiones al servidor sin recargar la página (AJAX/Fetch), manipula dinámicamente el contenido. Estas tres tecnologías son la base de cualquier experiencia web.


### 2.1. Código en el lado del cliente (Frontend) II

**Responsabilidades:**

- Renderizar interfaz de usuario
- Responder a acciones del usuario
- Validación preliminar de datos
- Manipular DOM dinámicamente
- Comunicación asíncrona con servidor

Note: El frontend tiene responsabilidades claras. **Renderiza** lo que el usuario ve en pantalla. **Responde** a interacciones: clics, scroll, tecleo. Hace **validación preliminar** de formularios (¿el email tiene formato correcto?), pero nunca debemos confiar solo en esto. **Manipula el DOM** para actualizar contenido sin recargar la página completa, mejorando la experiencia. Realiza **comunicación asíncrona** mediante AJAX o Fetch API para enviar y recibir datos del servidor en segundo plano.


### 2.1. Código en el lado del cliente (Frontend) III

**Ventajas y limitaciones:**

✅ Respuesta inmediata
✅ Reduce carga del servidor  
✅ Mejor experiencia de usuario

⚠️ Código visible y manipulable
⚠️ Recursos limitados del dispositivo
⚠️ Problemas de compatibilidad entre navegadores

Note: Las **ventajas** del frontend son claras: respuesta instantánea sin esperar al servidor, el navegador hace parte del trabajo reduciendo carga del servidor, las interacciones son fluidas y algunas funcionalidades pueden trabajar offline. Pero tiene **limitaciones importantes**: el código es completamente visible y puede ser manipulado por usuarios malintencionados, depende de la capacidad del dispositivo del usuario (móvil antiguo vs PC potente), y debe funcionar en diferentes navegadores y versiones. **Regla de oro: nunca confiar completamente en validaciones del cliente**.


### 2.2. Código en el lado del servidor (Backend) I

**Lenguajes más utilizados:**

- PHP (WordPress, Laravel)
- Python (Django, Flask)
- Java (Spring Boot)
- JavaScript/Node.js
- Ruby (Rails), C# (ASP.NET), Go

Note: El backend se ejecuta en el servidor y puede escribirse en muchos lenguajes. **PHP** es el más usado en la web, especialmente en CMS como WordPress y frameworks como Laravel. **Python** con Django o Flask es popular por su claridad y potencia. **Java** con Spring Boot domina en grandes empresas. **Node.js** permite usar JavaScript tanto en frontend como backend. Cada lenguaje tiene sus fortalezas: PHP para web tradicional, Python para datos e IA, Java para sistemas empresariales, Node.js para aplicaciones en tiempo real.


### 2.2. Código en el lado del servidor (Backend) II

**Responsabilidades:**

- Lógica de negocio y reglas del sistema
- Acceso y gestión de bases de datos
- Autenticación y autorización
- Procesamiento y transformación de datos
- Integración con servicios externos
- Seguridad y validación definitiva

Note: El backend es el **cerebro** de la aplicación. Implementa la **lógica de negocio**: reglas complejas, cálculos, procesos del sistema. Gestiona el **acceso a datos**: lee y escribe en bases de datos de forma segura. Controla **autenticación** (¿quién eres?) y **autorización** (¿qué puedes hacer?). Realiza **procesamiento pesado**: cálculos complejos, análisis de datos, generación de reportes. Se integra con **APIs externas**: pagos, envío de emails, servicios de terceros. Y lo más importante: garantiza la **seguridad** haciendo todas las validaciones críticas que no podemos confiar al cliente.


### 2.2. Código en el lado del servidor (Backend) III

**Ventajas:**

- Código seguro e invisible para usuarios
- Control total del entorno de ejecución
- Recursos potentes disponibles
- Centralización: fácil actualización
- Acceso directo a bases de datos

Note: Las ventajas del backend son críticas para la seguridad y fiabilidad. El **código es invisible**: los usuarios no pueden ver ni manipular tu lógica de negocio. Tienes **control total**: sabes exactamente qué hardware, sistema operativo y versiones estás usando. Dispones de **recursos potentes**: RAM, CPU, almacenamiento sin límites del dispositivo del usuario. La **centralización** facilita actualizaciones: cambias una vez en el servidor y todos los usuarios se benefician inmediatamente. Tienes **acceso directo y optimizado** a bases de datos con consultas complejas y transacciones seguras.


### 2.3. Colaboración cliente-servidor

1. Cliente realiza petición (ej: clic en "Enviar")
2. Servidor procesa: valida, ejecuta lógica, accede a BD
3. Servidor envía respuesta (datos o HTML)
4. Cliente procesa respuesta y actualiza interfaz

Note: La magia de las aplicaciones web está en la colaboración. El **cliente inicia**: usuario hace clic, envía formulario o simplemente carga una página. El **servidor trabaja**: recibe la petición, valida todos los datos (¡nunca confiar en el cliente!), ejecuta la lógica de negocio necesaria, accede a la base de datos si hace falta, y prepara la respuesta apropiada. El servidor **responde**: envía datos (JSON), HTML completo, o mensajes de error. El **cliente reacciona**: recibe la respuesta, actualiza la interfaz mostrando nuevos datos, mensajes de confirmación o errores, y puede hacer nuevas peticiones según sea necesario. Este ciclo se repite constantemente en una aplicación web activa.

---

## 3. Componentes web: Frontend y Backend

Note: Ya entendemos dónde se ejecuta el código. Ahora profundicemos en los dos grandes componentes de una aplicación web moderna y cómo se organizan las responsabilidades entre ellos. Esta división no es solo técnica, sino que responde a principios de arquitectura que hacen las aplicaciones más mantenibles, escalables y seguras.


### 3.1. Frontend: la cara visible

**Interfaz de usuario (UI):**

- Formularios, botones, menús
- Navegación entre vistas
- Visualización de datos
- Feedback visual al usuario

Note: El frontend es todo lo que el usuario ve y con lo que interactúa. Incluye **formularios** para entrada de datos con validaciones visuales inmediatas, **botones** que responden con efectos visuales, **menús** de navegación intuitivos. Gestiona la **navegación** entre diferentes vistas o páginas de la aplicación, a menudo sin recargar toda la página (SPA). **Visualiza datos** recibidos del backend: tablas, gráficos, listas, tarjetas. Proporciona **feedback visual**: spinners mientras carga, mensajes de éxito o error, animaciones de transición. Todo orientado a crear una experiencia de usuario fluida e intuitiva.


### 3.2. Backend: el cerebro de la aplicación I

**Responsabilidades principales:**

- API REST/GraphQL para comunicación
- Autenticación y gestión de sesiones
- Lógica de negocio compleja
- Validación definitiva de datos

Note: El backend organiza su funcionalidad en **APIs**: REST es el estándar con endpoints como /users, /products, usando métodos HTTP (GET, POST, PUT, DELETE); GraphQL es más flexible permitiendo al cliente pedir exactamente lo que necesita. Gestiona **autenticación**: login/logout, tokens JWT, sesiones, cookies seguras. Implementa toda la **lógica de negocio**: reglas complejas que definen cómo funciona tu aplicación (cálculo de precios, aplicación de descuentos, procesamiento de pedidos). Hace **validación definitiva**: nunca confía en lo que viene del cliente, valida tipos, rangos, permisos, consistencia de datos.


### 3.2. Backend: el cerebro de la aplicación II

**Más responsabilidades:**

- Acceso y gestión de bases de datos
- Procesamiento de archivos
- Integración con servicios externos
- Generación de contenido dinámico

Note: El backend **gestiona bases de datos**: consultas SQL complejas, transacciones ACID, optimización de queries, migraciones de esquema. **Procesa archivos**: subida de imágenes con redimensionado, generación de PDFs, procesamiento de CSV, compresión de archivos. Se **integra con servicios externos**: pasarelas de pago (Stripe, PayPal), envío de emails (SendGrid), SMS, servicios de almacenamiento en nube (S3), APIs de terceros (mapas, clima, redes sociales). **Genera contenido dinámico**: emails personalizados, reportes en PDF, plantillas HTML con datos del usuario. Todo esto de forma segura y eficiente.


### 3.3. Backend universal

**Un Backend → Múltiples clientes:**

- Aplicación web (navegador)
- App móvil (iOS, Android)
- App de escritorio
- IoT y dispositivos inteligentes

Note: Una de las grandes ventajas de separar frontend y backend es que puedes tener **un solo backend** sirviendo a **múltiples tipos de clientes**. Tu backend con API REST puede servir simultáneamente a: una **web** desarrollada en React, una **app móvil nativa** en Swift/Kotlin, una **app de escritorio** en Electron, incluso **dispositivos IoT** como smartwatches o asistentes de voz. Todos consumen la misma API, aplican las mismas reglas de negocio, acceden a los mismos datos. Esto es mucho más eficiente que duplicar lógica: desarrollas una vez, sirves a todos. Facilita mantenimiento, actualizaciones y garantiza consistencia entre plataformas.

---

## 4. Página Web vs Aplicación Web

Note: Aunque usamos los términos indistintamente, hay diferencias importantes entre una página web y una aplicación web. No es solo semántica: implica diferentes arquitecturas, tecnologías y experiencias de usuario. Entender estas diferencias nos ayuda a elegir el enfoque correcto para cada proyecto.


### 4.1. Página Web tradicional I

**Características:**

- Contenido mayormente estático
- Enfoque informativo
- Navegación entre páginas completas
- Recarga completa en cada cambio

Note: Las **páginas web tradicionales** son principalmente **informativas**: blogs, sitios corporativos, portfolios, documentación. El contenido es **mayormente estático**: aunque puede generarse dinámicamente en el servidor, no cambia constantemente. La **navegación** funciona así: cada clic en un enlace solicita una página HTML completa al servidor, el navegador descarga todo de nuevo y **recarga la página entera**, aunque solo cambie un pequeño detalle. Esto era el estándar hace años: sitios como periódicos, wikis, páginas de productos. Son más simples de desarrollar y perfectas cuando la interactividad no es crítica.


### 4.1. Página Web tradicional II

**Tecnologías comunes:**

- HTML + CSS básico
- JavaScript mínimo (si acaso)
- CMS: WordPress, Joomla
- Generadores estáticos: Hugo, Jekyll

Note: Las tecnologías son más simples. **HTML y CSS** puros o con frameworks básicos como Bootstrap. **JavaScript** solo para funcionalidades puntuales: menús desplegables, sliders de imágenes. **CMS tradicionales** como WordPress dominan: plantillas, plugins, editor visual. O **generadores estáticos** como Hugo, Jekyll, Gatsby que crean HTML puro en tiempo de construcción, super rápidos y seguros porque no hay backend dinámico. Son perfectos para sitios donde el contenido no cambia frecuentemente y no necesitas funcionalidad compleja.


### 4.2. Aplicación Web (Web App) I

**Características:**

- Alta interactividad y funcionalidad compleja
- Comportamiento similar a app nativa
- Actualizaciones parciales de contenido
- Estado y datos dinámicos

Note: Las **aplicaciones web** son sistemas complejos con **alta interactividad**: Gmail, Google Docs, Trello, Spotify Web. Proporcionan **funcionalidad rica**: edición en tiempo real, colaboración, notificaciones, sincronización. Se comportan como **apps nativas**: fluidas, responsivas, sin recargas molestas. Usan **actualizaciones parciales**: cambias de vista sin recargar toda la página (SPA), solo se actualiza la parte que cambia. Mantienen **estado**: recuerdan dónde estabas, qué estabas haciendo, qué datos has cargado. Gestionan **datos dinámicos** constantemente: sincronización con servidor, caché local, manejo de conflictos.


### 4.2. Aplicación Web (Web App) II

**Tecnologías comunes:**

- Frameworks JS: React, Vue, Angular
- State management: Redux, Vuex
- APIs REST o GraphQL
- Backend: Node.js, Django, Spring

Note: Las tecnologías son más sofisticadas. **Frameworks JavaScript modernos**: React de Facebook (más popular), Vue (más sencillo), Angular de Google (más completo). Estos organizan tu app en **componentes reutilizables**, gestionan el **estado** de forma predecible, optimizan el **rendering** para máximo rendimiento. **State management**: Redux, Vuex, MobX para gestionar estado complejo en aplicaciones grandes. **APIs bien diseñadas**: REST con buenas prácticas o GraphQL para queries flexibles. **Backends potentes**: Node.js para JavaScript full-stack, Django para apps con mucha lógica, Spring Boot para empresas grandes. Stack tecnológico más complejo pero también más potente.


### 4.3. Progressive Web Apps (PWA)

**Lo mejor de ambos mundos:**

- Funcionan offline con Service Workers
- Instalables como app nativa
- Push notifications
- Acceso a hardware del dispositivo

Note: Las **PWA** son el futuro de las aplicaciones web. Combinan lo mejor de web y apps nativas. Usan **Service Workers** para funcionar offline: cachean recursos, interceptan peticiones de red, sincronizan cuando vuelve conexión. Son **instalables**: el usuario las añade a su pantalla de inicio sin pasar por una App Store. Envían **push notifications** igual que apps nativas. Acceden al **hardware**: cámara, GPS, sensores, con permisos del usuario. Ejemplos exitosos: Twitter Lite, Starbucks, Pinterest. Las PWA son especialmente valiosas en mercados con conexión limitada y para empresas que quieren evitar los procesos y comisiones de las App Stores.


### 4.4. Comparación clave

| Aspecto           | Página Web      | Aplicación Web  |
|-------------------|-----------------|-----------------|
| **Objetivo**      | Informar        | Funcionalidad   |
| **Interacción**   | Baja            | Alta            |
| **Actualización** | Página completa | Parcial (SPA)   |
| **Complejidad**   | Baja-Media      | Media-Alta      |
<!-- .element.table: style="font-size:75%;" -->

Note: La diferencia fundamental está en el **objetivo**: si quieres **informar** (blog, portfolio, documentación), una página web tradicional es perfecta, más simple, más barata, más fácil de mantener. Si necesitas **funcionalidad compleja** (edición, colaboración, transacciones), necesitas una aplicación web. La **interacción** marca la diferencia: páginas web tienen interacción básica (leer, navegar), aplicaciones web tienen interacción continua (editar, arrastrar, notificaciones en tiempo real). Las **actualizaciones** también: páginas web recargan completamente en cada navegación, aplicaciones web actualizan solo lo necesario creando experiencia fluida. Y la **complejidad de desarrollo** es proporcional: páginas web son más rápidas y baratas de desarrollar, aplicaciones web requieren más inversión inicial pero ofrecen mucho más valor.

---

## 5. Clics en la web: ¿Qué sucede? I

Note: Vamos a desgranar todo lo que ocurre cuando escribes una URL o haces clic en un enlace. Lo que parece instantáneo en realidad involucra docenas de pasos, desde resolución DNS hasta renderizado final en pantalla. Entender este flujo es crucial para optimizar rendimiento y diagnosticar problemas.


### 5.1. Escribes la URL

**Usuario escribe:** `https://ejemplo.com`

1. Navegador verifica caché local
2. Si no está cacheado, inicia proceso DNS
3. DNS traduce dominio → dirección IP

Note: Todo comienza cuando escribes una URL. Primero, el **navegador revisa su caché**: ¿ya visitó este sitio recientemente? Si sí, puede tener la IP guardada y algunos recursos cacheados. Si no está en caché, necesita hacer **resolución DNS**: tu equipo pregunta al servidor DNS configurado "¿cuál es la IP de ejemplo.com?". El DNS es como la guía telefónica de Internet: traduce nombres legibles (ejemplo.com) a direcciones IP numéricas (93.184.216.34). Este proceso puede tener varios niveles: caché local → router → ISP → servidores raíz → servidores autoritativos del dominio. Una vez tiene la IP, puede conectar.


### 5.2. Conexión TCP y TLS

**Establecimiento de conexión:**

- Three-way handshake TCP (SYN, SYN-ACK, ACK)
- Si HTTPS: negociación TLS/SSL
- Intercambio de certificados
- Establecimiento de canal cifrado

Note: Con la IP, establece **conexión TCP**: protocolo que garantiza entrega fiable de datos. Es el famoso **three-way handshake**: cliente envía SYN ("¿podemos conectar?"), servidor responde SYN-ACK ("sí, conectemos"), cliente confirma con ACK ("ok, conectados"). Si es **HTTPS** (prácticamente todo hoy), añade **negociación TLS**: intercambio de certificados para verificar identidad del servidor, acuerdo de algoritmos de cifrado, generación de claves de sesión. Todo esto **antes** de enviar la primera petición HTTP. Por eso la primera conexión es más lenta que las siguientes (que reutilizan la conexión). Este cifrado es crucial: protege tus datos de escuchas en la red.


### 5.3. Petición HTTP

```http
GET /index.html HTTP/1.1
Host: ejemplo.com
User-Agent: Chrome/120.0
Accept: text/html
Cookie: session=abc123
```

Note: Ahora sí, el navegador envía la **petición HTTP**. Incluye el **método** (GET para obtener, POST para enviar datos), la **ruta** (/index.html o /), la **versión HTTP** (HTTP/1.1, HTTP/2, HTTP/3). Los **headers** son metadatos: Host indica el dominio, User-Agent identifica el navegador, Accept especifica qué tipos de contenido acepta, Cookie envía cookies de sesión si las hay. Pueden haber docenas de headers: idioma preferido, codificación aceptada, si acepta compresión gzip, información de caché. Todo esto viaja por el canal cifrado si es HTTPS. El servidor recibe y procesa esta petición.


### 5.4. Servidor procesa

**Servidor web (Apache, Nginx):**

1. Recibe petición y parsea
2. Enruta a código apropiado (PHP, Node, etc.)
3. Código ejecuta lógica
4. Consulta base de datos si necesita
5. Genera respuesta HTML

Note: En el servidor ocurre mucho. El **servidor web** (Apache, Nginx) recibe la conexión TCP, parsea la petición HTTP, decide qué hacer: ¿es un archivo estático (imagen, CSS) o código dinámico? Si es **estático**, lo lee del disco y lo sirve. Si es **dinámico**, lo pasa al **intérprete apropiado**: PHP, Python, Node.js, Java. Ese código **ejecuta lógica de negocio**: valida permisos, calcula datos, aplica reglas. Si necesita datos, **consulta la base de datos**: SELECT, JOIN, WHERE... procesa los resultados. Finalmente **genera la respuesta**: HTML con los datos incrustados, o JSON si es una API. Todo esto puede tomar milisegundos o segundos según complejidad.


### 5.5. Respuesta HTTP

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234
Set-Cookie: session=xyz789

<!DOCTYPE html>
<html>...</html>
```

Note: El servidor devuelve la **respuesta HTTP**. Comienza con el **código de estado**: 200 OK significa éxito, 404 Not Found si no existe, 500 si hubo error del servidor, 301/302 para redirecciones. Los **headers de respuesta** indican: Content-Type qué tipo de contenido es (text/html, application/json, image/png), Content-Length cuántos bytes mide, Set-Cookie establece cookies en el navegador, Cache-Control indica si/cómo cachear. Luego viene el **cuerpo**: el HTML completo, o JSON, o imagen binaria. Códigos se agrupan: 1xx información, 2xx éxito, 3xx redirecciones, 4xx errores del cliente, 5xx errores del servidor.


### 5.6. Navegador procesa HTML

**Parsing y construcción:**

- HTML → DOM Tree (estructura de nodos)
- CSS → CSSOM Tree (reglas de estilos)
- JavaScript se carga y ejecuta
- JS puede modificar DOM y CSSOM

Note: El navegador recibe el HTML y empieza el trabajo pesado. **Parsea HTML**: lo analiza línea por línea creando el **DOM Tree**, árbol de objetos representando cada elemento (&lt;html&gt;, &lt;body&gt;, &lt;div&gt;, &lt;p&gt;). **Parsea CSS**: procesa hojas de estilos creando el **CSSOM Tree** con todas las reglas (colores, tamaños, posiciones). **JavaScript** se descarga y ejecuta: puede manipular el DOM (añadir/quitar elementos), cambiar estilos, hacer peticiones AJAX para más datos. Por eso JS puede bloquear el renderizado: si está en el &lt;head&gt; sin async/defer, el navegador espera a descargarlo y ejecutarlo antes de continuar. Los frameworks modernos hacen mucho DOM manipulation.


### 5.7. Render Tree y pintado

**Proceso final:**

1. Combina DOM + CSSOM → Render Tree
2. Layout: calcula posiciones y tamaños
3. Painting: dibuja píxeles en pantalla
4. Compositing: ensambla capas

Note: El navegador combina DOM y CSSOM en el **Render Tree**: qué elementos pintar y con qué estilos. Excluye elementos invisibles (&lt;head&gt;, elementos con display:none). Hace **Layout** (reflow): calcula **posiciones exactas** y **tamaños** de cada elemento según CSS (flexbox, grid, floats, márgenes, paddings). Es costoso computacionalmente. Luego **Painting**: rasteriza cada elemento dibujando píxeles: fondos, bordes, sombras, texto, imágenes. Finalmente **Compositing**: ensambla diferentes capas (elementos con position:absolute, fixed, transforms) en la imagen final. Todo esto lo hace el **Render Engine** del navegador (Blink en Chrome, Gecko en Firefox, WebKit en Safari).


### 5.8. Página cargada

**Resultado:**

- Página visible y funcional
- JavaScript puede seguir actualizando
- Conexión TCP puede reutilizarse
- Assets adicionales se descargan en paralelo

Note: Finalmente ves la **página completa** en pantalla. Pero el proceso no termina: **JavaScript sigue ejecutándose**, puede hacer peticiones AJAX para cargar más datos, actualizar partes de la página sin recargar, responder a interacciones del usuario. La **conexión TCP permanece abierta** un tiempo (HTTP keep-alive) para reutilizarla en nuevas peticiones: si haces clic en otro enlace del mismo sitio, no necesita hacer todo el handshake de nuevo. El navegador descarga **assets adicionales en paralelo**: imágenes, fuentes, más JS/CSS referenciados en el HTML. Navegadores modernos optimizan esto con HTTP/2 multiplexing. Lo que parece simple ("entro a una web") involucra cientos de operaciones en milisegundos.

---

## 6. Resumen

Note: Hemos cubierto los fundamentos del desarrollo web moderno. Repasemos los conceptos clave que debéis retener de esta introducción.


### 6.1. Conceptos clave I

- Desarrollo web = funcionalidad + despliegue
- Código se ejecuta en cliente Y servidor
- Frontend: interfaz e interacción
- Backend: lógica, datos y seguridad

Note: El **desarrollo web moderno** va más allá de escribir código, incluye todo el ciclo hasta poner la aplicación en producción de forma eficiente y segura. El **código se ejecuta en dos lugares**: en el navegador (frontend) con HTML, CSS y JavaScript para la interfaz e interacción, y en el servidor (backend) con PHP, Python, Java, Node.js para lógica de negocio, acceso a datos y seguridad. Cada entorno tiene sus responsabilidades y limitaciones específicas.


### 6.2. Conceptos clave II

- Backend universal sirve múltiples clientes
- Páginas web: informativas
- Aplicaciones web: funcionalidad rica
- Cada clic es un proceso complejo

Note: Un mismo **backend puede servir a múltiples tipos de clientes**: web, móvil, escritorio, IoT, todos consumiendo la misma API con las mismas reglas de negocio. Las **páginas web tradicionales** son principalmente informativas con navegación entre páginas completas. Las **aplicaciones web modernas** son sistemas complejos con alta interactividad, actualizaciones parciales y comportamiento similar a apps nativas. Lo que parece simple (hacer clic en un enlace) desencadena un **flujo complejo**: DNS, TCP, TLS, HTTP, procesamiento servidor, parsing, renderizado. Entender este flujo es esencial para optimizar y depurar aplicaciones.


### 6.3. Lo que viene

- Arquitecturas web (MVC, microservicios)
- Protocolos HTTP en detalle
- Servicios Web y APIs REST
- Lenguajes y frameworks de backend
- Despliegue en servidores reales

Note: Esta introducción sienta las bases para todo lo que estudiaremos en las siguientes unidades. Veremos **arquitecturas web**: patrones MVC, arquitecturas en capas, microservicios. Profundizaremos en el **protocolo HTTP**: métodos, headers, códigos de estado, HTTP/2 y HTTP/3. Estudiaremos **servicios web y APIs**: diseño RESTful, GraphQL, autenticación con JWT, documentación con OpenAPI. Exploraremos **lenguajes y frameworks** de backend específicos con ejercicios prácticos. Y lo más importante: haremos **despliegue real** de aplicaciones en servidores, con todo lo que implica: configuración, seguridad, monitorización, escalabilidad. Estos fundamentos son esenciales para todo ello.
