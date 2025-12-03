---
title: "UD 3 - Desarrollo y Despliegue de Aplicaciones Web"
description: Guía completa sobre desarrollo web, protocolos HTTP/HTTPS, arquitecturas, lenguajes, frameworks, servidores, despliegue, escalabilidad, seguridad y monitorización
summary: Recorrido completo desde los fundamentos del protocolo HTTP hasta el despliegue moderno con Docker y Kubernetes, pasando por arquitecturas web, APIs, servidores y seguridad
authors:
    - Eduardo Fdez
date: 2025-11-27
icon: "material/file-document-outline"
permalink: /daw/unidad3/desarrollo-despliegue-web
categories:
    - DAW
tags:
    - HTTP
    - HTTPS
    - Arquitecturas Web
    - APIs
    - REST
    - Microservicios
    - Docker
    - Kubernetes
    - Servidores Web
    - Despliegue
    - Seguridad
---

## Desarrollo y Despliegue de Aplicaciones Web

Bienvenidos a este recorrido completo por el mundo del desarrollo y despliegue de aplicaciones web. En esta unidad integrada, vamos a construir vuestro conocimiento desde los cimientos del protocolo HTTP hasta las técnicas más avanzadas de despliegue en cloud, pasando por arquitecturas modernas, APIs, seguridad y monitorización.

¿Alguna vez os habéis preguntado qué sucede realmente cuando hacéis clic en un enlace, cuando una aplicación móvil sincroniza datos con el servidor, o cómo grandes plataformas como Netflix manejan millones de usuarios simultáneos? A lo largo de esta unidad, responderemos todas estas preguntas y muchas más, proporcionándoos las herramientas y conocimientos necesarios para convertiros en profesionales del desarrollo y despliegue de aplicaciones web.

### Hilo conductor: del protocolo a la producción

Imaginad que vamos a construir juntos una aplicación web desde cero hasta ponerla en producción para millones de usuarios. Este viaje seguirá un camino lógico y progresivo:

1. **¿Cómo se comunican las aplicaciones web?** → Protocolo HTTP/HTTPS
2. **¿Qué tipo de contenido podemos generar?** → Estático vs Dinámico
3. **¿Cómo organizar nuestro código?** → Componentes y Arquitecturas
4. **¿Con qué herramientas construir?** → Lenguajes, Frameworks, Plataformas
5. **¿Cómo exponer servicios?** → APIs, REST, GraphQL
6. **¿Dónde ejecutar nuestro código?** → Servidores Web y de Aplicaciones
7. **¿Cómo llevar a producción?** → Despliegue y Escalabilidad
8. **¿Cómo modernizar la infraestructura?** → Contenedores, Cloud, CI/CD
9. **¿Cómo proteger y supervisar?** → Seguridad, Logs, Monitorización

Cada sección construye sobre la anterior, creando un conocimiento sólido y completo. Al finalizar esta unidad, tendréis una comprensión profunda del ciclo completo de una aplicación web moderna.

!!! info "Un viaje práctico"
    A lo largo de este documento, utilizaremos ejemplos prácticos, diagramas explicativos y casos reales de empresas como Netflix, para que el conocimiento teórico se conecte siempre con la realidad profesional.


## BLOQUE 1: FUNDAMENTOS DE LA WEB

Antes de construir aplicaciones complejas, debemos entender perfectamente cómo se comunican y qué tipos de contenido pueden generar. Este primer bloque establece los cimientos sobre los que construiremos todo lo demás.

### 1. Protocolo HTTP/HTTPS y comunicación web

Mas adelante hablaremos sobre los componentes de una aplicación web y cómo se divide el código entre cliente, un navegador comúnmente, y servidor. Pero, ¿cómo se comunican realmente estos dos componentes? La respuesta está en el **protocolo HTTP**, el lenguaje universal de la web.

Cada vez que escribís una URL en el navegador, hacéis clic en un enlace o enviáis un formulario, estáis utilizando HTTP. Es el protocolo que hace posible que podáis leer esta página, ver vídeos en YouTube o comprar en Amazon. Entenderlo es fundamental para cualquier profesional del desarrollo y despliegue de aplicaciones web.

#### 1.1. Características y ventajas del protocolo HTTP

El **Protocolo HTTP (HyperText Transfer Protocol)** es la base de la comunicación en la World Wide Web. Fue creado por Tim Berners-Lee en 1989 y se ha convertido en el estándar para la transferencia de información en Internet.

##### 1.1.1. Definición y concepto

HTTP es un protocolo de **capa de aplicación** que define cómo se estructuran y envían los mensajes entre clientes y servidores web. Es un protocolo **no orientado a la conexión**, lo que significa que cada petición entre cliente y servidor es independiente y no requiere mantener una conexión continua.

**Arquitectura básica:**

- **Cliente**: Típicamente un navegador web que inicia las peticiones
- **Servidor**: Aplicación que escucha y responde a las peticiones
- **Recursos**: Documentos, imágenes, datos que se intercambian
- **Mensajes**: Peticiones (requests) y respuestas (responses)

##### 1.1.2. Características principales

HTTP posee un conjunto de características que lo han convertido en la columna vertebral de la web moderna. Estas características no son casuales; cada una fue diseñada para resolver problemas específicos de la comunicación en Internet y, juntas, crean un protocolo sorprendentemente flexible y poderoso.

**Sencillo: la elegancia de la simplicidad**

Una de las razones por las que HTTP ha tenido tanto éxito es su **simplicidad fundamental**. A diferencia de otros protocolos de red complejos y binarios, HTTP utiliza texto plano que podemos leer y escribir directamente. Imaginad poder "ver" realmente lo que vuestro navegador está enviando al servidor, no como bytes incomprensibles, sino como texto que podéis leer. Esto significa que:

- **Es legible por humanos**: Podéis abrir una conexión HTTP y ver exactamente qué se está enviando. Cada petición es simplemente texto que describe lo que queremos hacer: "Dame este recurso", "Envía estos datos", etc.
    
- **Fácil de depurar**: Cuando algo falla (y en desarrollo web, las cosas fallan constantemente), no necesitáis herramientas especializadas complejas. Con un simple navegador en modo desarrollador o con `curl` en la terminal, podéis ver exactamente qué está pasando, qué se envió y qué se recibió.
    
- **Bajo umbral de entrada**: Para aprender HTTP, no necesitáis entender complejos protocolos binarios ni documentación críptica. Podéis hacer peticiones HTTP manualmente y ver las respuestas inmediatamente, aprendiendo de forma práctica.

Por ejemplo, podéis abrir una terminal ahora mismo y hacer una petición HTTP completa con una simple línea:

```bash
# Ejemplo de petición HTTP manual con curl
# Esto os mostrará toda la conversación HTTP
curl -v http://www.ejemplo.com
```

Esta simplicidad no significa que sea limitado; al contrario, significa que es **accesible y potente al mismo tiempo**. Es como tener una herramienta que cualquiera puede entender, pero que los expertos pueden usar para construir aplicaciones increíblemente sofisticadas.

**Extensible: preparado para evolucionar**

Cuando Tim Berners-Lee diseñó HTTP en 1989, no podía imaginar las necesidades de las aplicaciones web de 2025. Sin embargo, HTTP sigue siendo relevante porque fue diseñado para **evolucionar sin romperse**. Esta extensibilidad se manifiesta de varias formas:

- **Se pueden añadir cabeceras personalizadas**: Si tu aplicación necesita enviar información adicional que no estaba prevista en el estándar original, simplemente añades una cabecera. Por ejemplo, `X-User-Session: abc123` o `X-API-Version: 2.0`. El protocolo no se rompe; simplemente transporta la información adicional.
    
- **Permite enviar metadatos más allá de los estándares**: Cada empresa, cada framework, cada aplicación puede añadir sus propias cabeceras sin necesidad de cambiar el protocolo base. Google puede añadir cabeceras para Analytics, tu aplicación puede añadir cabeceras para autenticación personalizada, y todo funciona sin conflictos.
    
- **Facilita la evolución del protocolo sin romper compatibilidad**: HTTP ha evolucionado de HTTP/1.0 a HTTP/1.1, HTTP/2, y HTTP/3, pero un servidor HTTP/3 moderno todavía puede comunicarse con un cliente HTTP/1.1 antiguo. Esta retrocompatibilidad es crucial para la web.

Esta extensibilidad es la razón por la que HTTP ha sobrevivido más de 30 años y seguirá siendo relevante en el futuro.

**Sin estado (Stateless): simplicidad que escala**

Esta es quizás la característica más contraintuitiva pero más importante de HTTP. En un protocolo **stateless** (sin estado), cada petición es como empezar de cero:

- **Cada petición es independiente de las anteriores**: Cuando hacéis una segunda petición, el servidor no "recuerda" la primera. Es como hablar con alguien que tiene amnesia total entre cada frase que le decís.
    
- **El servidor no guarda información sobre peticiones previas**: No hay memoria de sesión, no hay contexto mantenido. Cada petición debe contener toda la información necesaria para ser procesada.
    
- **Simplifica el diseño del servidor y mejora la escalabilidad**: Esto suena como una limitación, pero es en realidad una **ventaja enorme**. Si el servidor no necesita recordar el estado de cada cliente, puede manejar millones de peticiones sin quedarse sin memoria. Puede reiniciarse sin perder "contexto", y múltiples servidores pueden trabajar juntos sin necesidad de sincronizar estados complejos.

Pensad en la diferencia: un servidor con estado es como un camarero que debe recordar todo lo que cada cliente ha pedido durante toda la comida. Un servidor sin estado es como una máquina expendedora: cada interacción es independiente, simple y rápida.

!!! warning "El problema del estado"
    Que HTTP sea stateless presenta un desafío: ¿cómo mantener la sesión de un usuario (por ejemplo, en un carrito de compra)? La solución son las **cookies** y las **sesiones**, que estudiaremos en detalle más adelante.

##### 1.1.3. Ventajas del protocolo HTTP

HTTP ofrece múltiples ventajas que lo han convertido en el protocolo estándar de Internet. Estas ventajas no son accidentales; son el resultado de décadas de evolución y refinamiento del protocolo. Veamos cómo cada característica se traduce en beneficios concretos para desarrolladores y usuarios.

**Control de caché: velocidad sin sacrificar frescura**

Imaginad que cada vez que visitáis YouTube, tuvierais que descargar de nuevo todo el código JavaScript, todas las imágenes del logo, todos los estilos CSS... La web sería insoportablemente lenta. HTTP soluciona esto elegantemente con su sistema de **control de caché**:

- **Permite especificar cómo y cuándo se almacenan temporalmente los recursos**: Los servidores pueden decir "este logo no cambia nunca, guárdalo durante un año" o "estos datos son muy dinámicos, pide actualizaciones cada minuto". Esta flexibilidad es crucial.
    
- **Mejora significativamente la velocidad de carga**: La primera visita a un sitio puede tardar 3 segundos, pero las visitas posteriores toman solo 0.5 segundos porque el navegador ya tiene la mayoría de los recursos guardados localmente.
    
- **Reduce el consumo de ancho de banda**: Si un millón de usuarios visitan tu sitio, sin caché descargarían los mismos archivos estáticos un millón de veces. Con caché, solo los descargan una vez. Esto ahorra dinero en servidores y es mejor para el medio ambiente (menos consumo energético).
    
- **Las cabeceras `Cache-Control` y `Expires` controlan este comportamiento**: Los desarrolladores tienen control fino sobre qué se cachea, por cuánto tiempo y bajo qué condiciones. Por ejemplo: `Cache-Control: max-age=31536000` significa "guarda esto durante un año".

Este sistema de caché es una de las razones por las que la web puede funcionar a escala global. Sin él, simplemente no sería práctico.

**Autenticación: protegiendo lo que es privado**

No todo en Internet debe ser público. Necesitamos formas de verificar que "eres quien dices ser" antes de mostrar información sensible. HTTP integra esta capacidad desde su diseño:

- **Soporta varios mecanismos de autenticación**: Desde el simple **HTTP Basic** (usuario y contraseña en Base64) hasta sistemas más sofisticados como **Digest** (con hash de la contraseña) o **Bearer tokens** (tokens JWT modernos). Cada uno ofrece diferentes niveles de seguridad según las necesidades.
    
- **Permite verificar la identidad de los usuarios**: Antes de mostrar tu correo electrónico, tu historial médico o tus datos bancarios, el servidor puede exigir que demuestres quién eres. Esta verificación sucede en cada petición HTTP mediante cabeceras de autorización.
    
- **Protege recursos sensibles**: Combinado con HTTPS, podéis crear sistemas seguros donde solo los usuarios autorizados accedan a información privada. Esto es fundamental para cualquier aplicación que maneje datos personales o sensibles.

La autenticación HTTP es la base sobre la que se construyen todos los sistemas de login, APIs privadas y zonas protegidas de las aplicaciones web modernas.

**Uso de proxies: el poder de los intermediarios**

En la conversación HTTP entre cliente y servidor, a veces es útil tener "intermediarios" que intercepten y procesen las peticiones. Estos intermediarios se llaman **proxies**, y HTTP los soporta nativamente:

- **Facilita el uso transparente de servidores intermediarios**: El cliente puede estar hablando con un proxy sin siquiera saberlo. El proxy puede estar en la oficina, en un CDN (Content Delivery Network), o en cualquier punto intermedio de Internet.
    
- **Permite filtrado, caché compartida y balanceo de carga**: 
    - **Filtrado**: Una empresa puede bloquear acceso a ciertos sitios
    - **Caché compartida**: Miles de usuarios pueden compartir una caché común, multiplicando los beneficios
    - **Balanceo de carga**: Un proxy puede distribuir peticiones entre múltiples servidores, evitando que uno se sobrecargue
    
- **Mejora la seguridad y el rendimiento**: Los proxies pueden inspeccionar tráfico malicioso, comprimir contenido, o servir contenido desde ubicaciones geográficamente cercanas al usuario (eso es lo que hace Cloudflare, por ejemplo).

Este soporte de proxies es lo que permite a servicios como Cloudflare, Akamai o Fastly hacer la web más rápida y segura para todos.

**Mantenimiento de sesiones: recordar en un mundo sin memoria**

Recordáis que HTTP es stateless (sin estado)? Entonces, ¿cómo es posible que cuando añadís algo al carrito de Amazon, siga ahí cuando vais a otra página? La respuesta son las **cookies**:

- **Aunque HTTP es stateless, soporta cookies**: Las cookies son pequeños trozos de información que el servidor envía al cliente diciendo "guarda esto y devuélvemelo en cada petición". Es como dar al camarero amnésico una tarjeta que dice "este es el pedido de esta mesa".
    
- **Las cookies permiten mantener el estado entre peticiones**: El servidor puede generar un identificador único de sesión, enviarlo como cookie, y luego usar ese identificador para recuperar datos de sesión guardados en su base de datos. Así, aunque HTTP no tenga memoria, podemos simularla.
    
- **Esencial para aplicaciones web modernas**: Sin cookies, no existirían los carritos de compra persistentes, los sistemas de login que te mantienen autenticado, o cualquier tipo de personalización. Prácticamente toda aplicación web moderna depende de esto.

Las cookies han evolucionado mucho: de simples strings a sofisticados sistemas con flags de seguridad (`Secure`, `HttpOnly`, `SameSite`) que protegen contra diversos ataques.

**Negociación de contenido: la misma información, diferentes formatos**

¿Qué pasa cuando un navegador español visita un sitio en inglés? ¿O cuando un navegador moderno visita un sitio que también debe soportar navegadores antiguos? HTTP permite **negociar** qué formato de contenido usar:

- **El cliente puede indicar qué formatos acepta**: Mediante cabeceras como `Accept-Language: es-ES, en;q=0.9` el navegador dice "prefiero español, pero acepto inglés si no hay español". O `Accept: application/json, text/html` para decir qué tipos de contenido puede procesar.
    
- **El servidor puede responder en el formato más adecuado**: El servidor analiza estas preferencias y responde con el mejor formato disponible. Esto permite que el mismo endpoint sirva JSON a aplicaciones móviles y HTML a navegadores.
    
- **Facilita la internacionalización y la adaptación a dispositivos**: Un mismo servidor puede servir:
    - Contenido en diferentes idiomas según la preferencia del usuario
    - Imágenes en diferentes resoluciones según el dispositivo
    - Formatos de datos diferentes según las capacidades del cliente

Esta negociación hace que la web sea verdaderamente universal, adaptándose automáticamente a las necesidades de cada usuario y dispositivo.

<figure markdown="span">
  ![Protocolo HTTP](assets/http.png){ width="700" }
  <figcaption>Diagrama del protocolo HTTP mostrando el flujo de comunicación entre cliente y servidor: el cliente envía una petición (request) con método, URL y cabeceras; el servidor responde con un código de estado, cabeceras y el contenido solicitado</figcaption>
</figure>

#### 1.2. Importancia en arquitecturas modernas

HTTP es fundamental en las arquitecturas web actuales:

- **APIs REST**: Se basan completamente en HTTP y sus métodos
- **Microservicios**: Utilizan HTTP para comunicarse entre sí
- **Aplicaciones web**: Toda interacción usa HTTP/HTTPS
- **Internet de las Cosas (IoT)**: Muchos dispositivos usan HTTP para comunicarse

!!! tip "HTTP es universal"
    HTTP es tan universal que incluso aplicaciones que no son web (como aplicaciones móviles o de escritorio) suelen usar HTTP para comunicarse con sus servidores, aprovechando su simplicidad y las herramientas existentes.

#### 1.3. Formato de peticiones y respuestas HTTP

La interacción en la web se basa en un intercambio constante de **peticiones** (requests) y **respuestas** (responses) HTTP entre el navegador del cliente y el servidor. Entender su estructura es fundamental.

##### 1.3.1. Estructura de una petición HTTP

Una petición HTTP del cliente tiene la siguiente estructura:

**Línea de petición (Request Line)**

La primera línea contiene tres elementos:

```
[MÉTODO] [RUTA] [VERSIÓN]
```

Ejemplo:
```
GET /index.html HTTP/1.1
```

- **MÉTODO**: La acción que se quiere realizar (GET, POST, PUT, DELETE, etc.)
- **RUTA**: El recurso solicitado (path + query string si aplica)
- **VERSIÓN**: La versión del protocolo HTTP (HTTP/1.1, HTTP/2, HTTP/3)

**Cabeceras (Headers)**

Después de la línea de petición, vienen las cabeceras, una por línea:

```
Host: www.ejemplo.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Accept: text/html,application/json
Accept-Language: es-ES,es;q=0.9
Connection: keep-alive
```

**Línea en blanco**

Una línea vacía separa las cabeceras del cuerpo

**Cuerpo (Body) - Opcional**

Contiene los datos que se envían al servidor (en POST, PUT, PATCH):

```json
{
    "usuario": "estudiante",
    "password": "secreto123"
}
```

**Ejemplo completo de petición:**

```http
POST /api/login HTTP/1.1
Host: miapp.com
Content-Type: application/json
Content-Length: 58
User-Agent: Mozilla/5.0

{
    "usuario": "estudiante",
    "password": "secreto123"
}
```

##### 1.3.2. Estructura de una respuesta HTTP

Una respuesta HTTP del servidor tiene una estructura similar:

**Línea de estado (Status Line)**

La primera línea contiene:

```
[VERSIÓN] [CÓDIGO] [TEXTO]
```

Ejemplo:
```
HTTP/1.1 200 OK
```

- **VERSIÓN**: Versión del protocolo HTTP
- **CÓDIGO**: Código de estado numérico (200, 404, 500, etc.)
- **TEXTO**: Descripción textual del código (OK, Not Found, Internal Server Error)

**Cabeceras de respuesta (Response Headers)**

```
Content-Type: text/html; charset=utf-8
Content-Length: 1234
Server: Apache/2.4.41
Date: Wed, 19 Nov 2025 15:30:00 GMT
Cache-Control: max-age=3600
```

**Línea en blanco**

Separa las cabeceras del cuerpo

**Cuerpo (Body)**

Contiene el contenido solicitado (HTML, JSON, imagen, etc.):

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi Página</title>
</head>
<body>
    <h1>Bienvenido</h1>
</body>
</html>
```

**Ejemplo completo de respuesta:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 89
Server: nginx/1.18.0
Date: Wed, 19 Nov 2025 15:30:00 GMT

{
    "status": "success",
    "mensaje": "Login correcto",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

!!! note "Herramientas de desarrollo"
    Todos los navegadores modernos incluyen herramientas de desarrollo (F12) donde podéis ver las peticiones y respuestas HTTP en la pestaña "Red" o "Network". Es fundamental aprender a usar estas herramientas para depurar aplicaciones web.

#### 1.4. Cabeceras HTTP

Las cabeceras HTTP son líneas de metadatos que se envían tanto en las peticiones como en las respuestas. Proporcionan información crucial sobre la comunicación entre cliente y servidor.

##### 1.4.1. Cabeceras de petición comunes

Estas cabeceras son enviadas por el cliente al servidor:

**Accept**

Indica los tipos de contenido (MIME types) que el cliente puede procesar:

```
Accept: text/html,application/json,application/xml
```

El cliente puede especificar preferencias con calidad (q):
```
Accept: text/html,application/json;q=0.9,*/*;q=0.8
```

**Accept-Language**

Indica los idiomas preferidos para la respuesta:

```
Accept-Language: es-ES,es;q=0.9,en;q=0.8
```

Esto permite que los sitios web multilingües devuelvan contenido en el idioma preferido del usuario.

**Host**

Especifica el dominio al que se dirige la petición (obligatoria en HTTP/1.1):

```
Host: www.ejemplo.com
```

Es crucial para alojar múltiples sitios web (virtual hosts) en un mismo servidor con una única dirección IP.

**User-Agent**

Identifica el navegador y sistema operativo del cliente:

```
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
```

Permite al servidor adaptar la respuesta según el dispositivo o navegador.

**Content-Type**

Describe el formato de los datos enviados en el cuerpo de la petición:

```
Content-Type: application/json; charset=utf-8
Content-Type: application/x-www-form-urlencoded
Content-Type: multipart/form-data
```

**Content-Length**

Especifica el tamaño en bytes del cuerpo de la petición:

```
Content-Length: 1234
```

**Authorization**

Contiene las credenciales para autenticarse en el servidor:

```
Authorization: Basic dXN1YXJpbzpwYXNzd29yZA==
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Cookie**

Envía cookies almacenadas previamente:

```
Cookie: sessionid=abc123; preferencias=tema_oscuro
```

##### 1.4.2. Cabeceras de respuesta comunes

Estas cabeceras son enviadas por el servidor al cliente:

**Content-Type**

Indica el tipo de contenido que se está devolviendo:

```
Content-Type: text/html; charset=utf-8
Content-Type: application/json
Content-Type: image/png
```

Es **crucial** para que el navegador interprete correctamente el contenido.

**Content-Length**

Tamaño en bytes del cuerpo de la respuesta:

```
Content-Length: 5432
```

**Server**

Información sobre el software del servidor:

```
Server: Apache/2.4.41 (Ubuntu)
Server: nginx/1.18.0
```

!!! warning "Seguridad"
    Por razones de seguridad, algunos servidores ocultan o minimizan esta información para no revelar detalles que podrían ser aprovechados por atacantes.

**Date**

Fecha y hora en que se generó la respuesta:

```
Date: Wed, 19 Nov 2025 15:30:00 GMT
```

**Cache-Control**

Controla cómo se debe cachear el contenido:

```
Cache-Control: max-age=3600, public
Cache-Control: no-cache, no-store, must-revalidate
```

**Set-Cookie**

Establece cookies en el navegador del cliente:

```
Set-Cookie: sessionid=abc123; Path=/; HttpOnly; Secure
```

**Location**

Usado en redirecciones (códigos 3xx) para indicar la nueva ubicación:

```
Location: https://www.ejemplo.com/nueva-pagina
```

**Content-Language**

Indica el idioma del contenido:

```
Content-Language: es-ES
```

##### 1.4.3. Tipos MIME más comunes

Los tipos MIME (Multipurpose Internet Mail Extensions) identifican el formato del contenido:

| Tipo MIME                | Descripción            |
|:-------------------------|:-----------------------|
| `text/html`              | Documento HTML         |
| `text/css`               | Hoja de estilos CSS    |
| `text/plain`             | Texto plano            |
| `application/json`       | Datos en formato JSON  |
| `application/xml`        | Datos en formato XML   |
| `application/javascript` | Código JavaScript      |
| `image/jpeg`             | Imagen JPEG            |
| `image/png`              | Imagen PNG             |
| `image/gif`              | Imagen GIF             |
| `video/mp4`              | Vídeo MP4              |
| `audio/mpeg`             | Audio MP3              |
| `application/pdf`        | Documento PDF          |
| `application/zip`        | Archivo comprimido ZIP |

#### 1.5. Métodos HTTP (verbos HTTP)

Los métodos HTTP, también llamados **verbos HTTP**, definen la acción que un cliente desea realizar sobre un recurso en el servidor. Son fundamentales para el diseño de APIs RESTful.

<figure markdown="span">
  ![Métodos HTTP](assets/http-metodos.gif){ width="600" }
  <figcaption>Representación visual de los principales métodos HTTP y sus acciones: GET para obtener, POST para crear, PUT para actualizar, DELETE para eliminar. Cada método tiene un propósito específico en la manipulación de recursos del servidor</figcaption>
</figure>

##### 1.5.1. GET - Obtener recursos

GET es el método HTTP más utilizado en toda la web. **Cada vez que escribís una URL en el navegador y pulsáis Enter, estáis haciendo una petición GET**. Es el método por excelencia para leer información, para consultar datos, para obtener recursos sin alterarlos.

**Propósito fundamental**: Solicitar y recibir datos del servidor **sin modificar absolutamente nada**. Es como mirar el escaparate de una tienda: podéis mirar todo lo que queráis, examinar los productos, pero nada cambia por el simple hecho de mirar.

**Características que lo definen:**

- **Seguro (Safe method)**: Esta es quizás su propiedad más importante. Un GET **nunca jamás** debe modificar el estado del servidor. No debe crear recursos, no debe actualizarlos, no debe borrarlos, no debe cambiar nada. Si vuestro GET tiene efectos secundarios (side effects), estáis violando HTTP y causando problemas graves. ¿Por qué? Porque navegadores y bots de búsqueda pre-cargan páginas mediante GET, y si un GET borra datos... desastre.

- **Idempotente**: Hacer la misma petición GET una vez, diez veces, mil veces, produce exactamente el mismo resultado. `GET /usuarios/123` siempre devolverá el mismo usuario con id 123 (a menos que OTRO proceso lo haya modificado entre medias, pero el GET en sí no lo modifica). Esta propiedad permite reintentar peticiones sin miedo.

- **Cacheable por naturaleza**: Como los GET no modifican nada y son idempotentes, los navegadores, los CDNs (Content Delivery Networks) y los proxies pueden guardar la respuesta en caché y reutilizarla durante horas, días o semanas. **Esto hace la web dramáticamente más rápida**. Cuando visitáis una página por segunda vez, muchos recursos se cargan instantáneamente desde la caché local.

- **Sin cuerpo en la petición**: Los parámetros van en la URL como query parameters. Por ejemplo: `/buscar?q=kotlin&tipo=tutoriales&orden=recientes`. Esto tiene ventajas (podéis compartir la URL y cualquiera obtendrá el mismo resultado, los enlaces son "bookmarkables") pero también limitaciones (las URLs tienen un límite de ~2000 caracteres en muchos navegadores).

**Ejemplo real de petición GET:**

```http
GET /usuarios/123 HTTP/1.1
Host: api.ejemplo.com
Accept: application/json
User-Agent: Mozilla/5.0
Authorization: Bearer eyJhbGc...token...
Cache-Control: no-cache
```

Lo que le estamos diciendo al servidor es: "Dame la información del usuario con ID 123, prefiero recibirla en formato JSON, soy el navegador Mozilla/Firefox, aquí está mi token de autenticación para verificar que tengo permiso, y no uses caché, dame la versión más reciente".

**Respuesta típica exitosa:**

```http
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: max-age=3600
ETag: "33a64df551425fcc"
Content-Length: 156

{
    "id": 123,
    "nombre": "Juan Pérez",
    "email": "juan@ejemplo.com",
    "rol": "estudiante",
    "fecha_registro": "2023-09-15"
}
```

El servidor responde: "Todo bien (200 OK), aquí está la información en JSON como pediste, puedes guardarla en caché durante 1 hora (3600 segundos), este es su identificador único (ETag) que puedes usar luego para verificar si ha cambiado, y el contenido pesa 156 bytes".

**Usos típicos en aplicaciones reales:**

- **Obtener una lista de recursos**: 

    - `GET /productos` → devuelve todos los productos
    - `GET /productos?categoria=libros&precio_max=30&orden=precio` → productos filtrados y ordenados
    - `GET /usuarios?page=2&limit=20` → paginación (página 2, 20 elementos por página)

- **Obtener un recurso específico**:

    - `GET /usuarios/123` → obtiene el usuario con ID 123
    - `GET /posts/456/comentarios` → obtiene los comentarios del post 456
    - `GET /cursos/DAW/alumnos` → obtiene los alumnos del curso DAW

- **Búsquedas complejas**:

    - `GET /buscar?q=kotlin&idioma=es&dificultad=intermedio&orden=fecha`
    - `GET /productos/buscar?texto=laptop&marca[]=dell&marca[]=hp&precio_min=400`


**Ejemplos prácticos con diferentes query parameters:**

```http
# Obtener todos los usuarios
GET /usuarios HTTP/1.1
Host: api.ejemplo.com

# Obtener un usuario específico
GET /usuarios/123 HTTP/1.1
Host: api.ejemplo.com

# Búsqueda con múltiples filtros
GET /productos?categoria=electronica&precio_max=500&disponible=true HTTP/1.1
Host: api.ejemplo.com

# Con paginación y ordenamiento
GET /posts?page=3&per_page=10&sort=fecha&order=desc HTTP/1.1
Host: api.ejemplo.com
```

**Errores comunes que DEBÉIS EVITAR:**

NUNCA hagáis esto: 
```http
GET /eliminar-usuario?id=123
GET /transferir-dinero?origen=123&destino=456&cantidad=1000
GET /logout
```

Estos GET tienen efectos secundarios graves (borran, transfieren, cierran sesión). Esto viola completamente el principio de seguridad de GET. Imaginad un bot de Google siguiendo ese enlace `/eliminar-usuario?id=123` y borrando usuarios...

Correcto - usar los métodos apropiados: 
```http
DELETE /usuarios/123          (para eliminar)
POST /transferencias          (para transferir dinero)
POST /logout                  (para cerrar sesión)
```

!!! warning "GET no debe modificar NUNCA"
    Aunque técnicamente es posible programar un GET que modifique el servidor, **nunca jamás debéis hacerlo**. GET es un método **seguro** por definición. Violarlo causa problemas de seguridad, problemas con cachés, problemas con bots, y rompe las expectativas de todos los clientes HTTP. Si necesitáis modificar algo, usad POST, PUT, PATCH o DELETE.

##### 1.5.2. POST - Crear recursos

Si GET es para **leer**, POST es para **escribir**. POST es el método que usáis cada vez que enviáis un formulario web, subís una foto a Instagram, publicáis un tweet, o creáis cualquier contenido nuevo en Internet.

**Propósito fundamental**: Enviar datos al servidor para que procese, típicamente para **crear un nuevo recurso**. Es como llenar un formulario de registro y enviarlo: estáis pidiendo al servidor que cree una nueva cuenta con vuestros datos.

**Características que lo hacen único:**

- **NO idempotente**: Esta es la diferencia clave con PUT. Si hacéis la misma petición POST dos veces, crearéis DOS recursos diferentes. Si os registráis dos veces en una web con el mismo email, deberíais obtener dos cuentas o un error. Cada POST es potencialmente una acción nueva.

- **NO seguro**: Por supuesto que no es seguro, ¡su propósito es modificar el servidor! Cada POST cambia el estado: crea un usuario, añade un producto, publica un comentario...

- **NO cacheable por defecto**: Como cada POST puede hacer algo diferente, los navegadores no pueden guardar la respuesta en caché. Cada POST debe ejecutarse realmente.

- **Con cuerpo (body)**: A diferencia de GET, los datos van en el cuerpo de la petición, no en la URL. Esto permite enviar cantidades masivas de datos (archivos de imagen, documentos, JSON complejo) sin las limitaciones de longitud de URL.

- **El servidor decide el identificador**: Cuando creas un recurso con POST, típicamente el cliente no especifica el ID. El servidor genera un ID único y te lo devuelve. Por eso POST a menudo devuelve código `201 Created` con una cabecera `Location` indicando dónde quedó el nuevo recurso.

**Ejemplo real de creación de usuario:**

```http
POST /usuarios HTTP/1.1
Host: api.ejemplo.com
Content-Type: application/json
Content-Length: 145
Authorization: Bearer eyJhbGc...token...

{
    "nombre": "María García",
    "email": "maria@ejemplo.com",
    "password": "contraseña_hasheada",
    "rol": "estudiante",
    "fecha_nacimiento": "2000-05-15"
}
```

Le estamos diciendo al servidor: "Crea un nuevo usuario con estos datos. Los datos están en JSON y ocupan 145 bytes. Aquí está mi token para verificar que tengo permiso para crear usuarios".

**Respuesta típica exitosa (201 Created):**

```http
HTTP/1.1 201 Created
Location: /usuarios/456
Content-Type: application/json
Content-Length: 198

{
    "id": 456,
    "nombre": "María García",
    "email": "maria@ejemplo.com",
    "rol": "estudiante",
    "fecha_nacimiento": "2000-05-15",
    "fecha_registro": "2025-11-27T10:30:00Z",
    "verificado": false
}
```

El servidor responde: "Creado exitosamente (201), el nuevo usuario está en `/usuarios/456` (cabecera Location), aquí tienes todos los datos del usuario creado, incluido el ID que yo generé (456) y campos adicionales que yo añadí automáticamente (fecha_registro, verificado)".

**Usos típicos en el mundo real:**

- **Crear recursos nuevos**:

    - `POST /productos` → crear un nuevo producto en el catálogo
    - `POST /posts` → publicar un nuevo artículo en un blog
    - `POST /comentarios` → añadir un comentario a una discusión
    - `POST /pedidos` → crear un nuevo pedido de compra

- **Enviar formularios HTML tradicionales**:

    - `POST /contacto` → enviar mensaje de contacto
    - `POST /registro` → registrar nuevo usuario
    - `POST /login` → iniciar sesión (aunque esto no crea un recurso, es común usar POST)

- **Subir archivos**:

    - `POST /uploads` → subir imágenes, documentos, videos
    - `POST /avatar` → cambiar foto de perfil
    - Con `Content-Type: multipart/form-data` para archivos

- **Operaciones complejas que no se mapean a CRUD simple**:

    - `POST /busqueda-avanzada` → búsqueda compleja con muchos parámetros (cuando GET sería demasiado largo)
    - `POST /calcular` → ejecutar un cálculo complejo con muchos inputs
    - `POST /procesar-pago` → procesar una transacción

**Ejemplo de POST para subir un archivo:**

```http
POST /uploads/avatar HTTP/1.1
Host: api.ejemplo.com
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Length: 34532

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="archivo"; filename="perfil.jpg"
Content-Type: image/jpeg

[datos binarios de la imagen aquí]
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

**Respuestas comunes de POST:**

- **201 Created**: Recurso creado exitosamente
  ```http
  HTTP/1.1 201 Created
  Location: /usuarios/789
  ```

- **200 OK**: Operación exitosa pero no se creó un recurso específico
  ```http
  HTTP/1.1 200 OK
  Content-Type: application/json
  {"mensaje": "Email enviado correctamente"}
  ```

- **400 Bad Request**: Los datos enviados son inválidos
  ```http
  HTTP/1.1 400 Bad Request
  Content-Type: application/json
  {"error": "El email ya está registrado"}
  ```

- **409 Conflict**: El recurso ya existe
  ```http
  HTTP/1.1 409 Conflict
  {"error": "Ya existe un usuario con ese username"}
  ```

**Diferencia clave: POST vs GET**

```
GET:  Leer, seguro, idempotente, cacheable, parámetros en URL
POST: Escribir, no seguro, NO idempotente, NO cacheable, datos en body
```

**Ejemplo práctico - formulario de contacto:**

```html
<!-- HTML -->
<form action="/contacto" method="POST">
    <input name="nombre" required>
    <input name="email" type="email" required>
    <textarea name="mensaje" required></textarea>
    <button type="submit">Enviar</button>
</form>
```

Cuando el usuario envía este formulario, el navegador automáticamente hace:

```http
POST /contacto HTTP/1.1
Host: ejemplo.com
Content-Type: application/x-www-form-urlencoded

nombre=Juan+Perez&email=juan%40ejemplo.com&mensaje=Hola%2C+necesito+ayuda
```

**Importante sobre idempotencia:**

```javascript
// Problema: Si hay error de red y reintentamos...
POST /transferencia
{ "origen": 123, "destino": 456, "cantidad": 100 }

// Se ejecuta 2 veces = se transfieren 200€ en lugar de 100€
// Por eso muchas APIs usan "idempotency keys" para prevenir duplicados
```

**POST con idempotency key (patrón avanzado):**

```http
POST /transferencias HTTP/1.1
Host: api.banco.com
Idempotency-Key: 550e8400-e29b-41d4-a716-446655440000
Content-Type: application/json

{
    "origen": "ES1234567890",
    "destino": "ES0987654321",
    "cantidad": 100.00
}
```

El servidor guarda el `Idempotency-Key`, y si recibe el mismo key dos veces, solo procesa la transferencia una vez. Esto hace POST "virtualmente idempotente" para operaciones críticas.

##### 1.5.3. PUT - Actualizar recursos

PUT es el método para **actualizar o reemplazar completamente** un recurso que ya existe. A diferencia de POST (que crea), PUT **modifica** algo que ya está ahí.

**Propósito fundamental**: Reemplazar por completo un recurso existente con una nueva versión. Es como reescribir todo un documento de Word: el archivo sigue teniendo el mismo nombre, pero su contenido es completamente nuevo.

**Características que lo definen:**

- **Idempotente (¡clave!)**: Esta es la diferencia fundamental con POST. Si hacéis PUT del mismo recurso 5 veces, el resultado es **exactamente el mismo** que hacerlo una sola vez. El recurso queda en el mismo estado final. Esto permite reintentar PUT sin miedo a duplicar efectos.

    ```
    PUT /usuarios/456  (primera vez)  → usuario actualizado
    PUT /usuarios/456  (segunda vez)  → usuario igual (sin cambios)
    PUT /usuarios/456  (tercera vez)  → usuario igual (sin cambios)
    ```

- **NO seguro**: Por supuesto, PUT modifica el estado del servidor. Cambia datos existentes.

- **Reemplaza completamente el recurso**: Esto es crucial de entender. PUT **no hace actualizaciones parciales**. Cuando hacéis PUT, enviáis el recurso COMPLETO. Todo lo que no enviéis se considera que debe eliminarse o establecerse a valores por defecto.

- **El cliente especifica el ID**: A diferencia de POST donde el servidor genera el ID, con PUT vosotros decís exactamente QUÉ recurso queréis actualizar (`/usuarios/456`). Si ese recurso no existe, algunos servidores lo crean (comportamiento "upsert": update or insert), aunque esto no es estándar.

**Ejemplo real de actualización completa:**

```http
PUT /usuarios/456 HTTP/1.1
Host: api.ejemplo.com
Content-Type: application/json
Authorization: Bearer eyJhbGc...token...
Content-Length: 178

{
    "nombre": "María García López",
    "email": "maria.garcia@ejemplo.com",
    "rol": "profesor",
    "fecha_nacimiento": "1985-03-20",
    "departamento": "Informática",
    "activo": true
}
```

Le decimos al servidor: "El usuario 456 debe quedar EXACTAMENTE con estos datos. Todo el recurso se reemplaza con esta información."

**Respuesta típica:**

```http
HTTP/1.1 200 OK
Content-Type: application/json
Last-Modified: Wed, 27 Nov 2025 15:45:00 GMT

{
    "id": 456,
    "nombre": "María García López",
    "email": "maria.garcia@ejemplo.com",
    "rol": "profesor",
    "fecha_nacimiento": "1985-03-20",
    "departamento": "Informática",
    "activo": true,
    "actualizado": "2025-11-27T15:45:00Z"
}
```

**⚠️ Peligro: PUT reemplaza TODO**

Imaginad que el usuario 456 tenía estos datos:
```json
{
    "id": 456,
    "nombre": "María García",
    "email": "maria@ejemplo.com",
    "rol": "estudiante",
    "telefono": "666777888",
    "direccion": "Calle Mayor 5"
}
```

Si hacéis este PUT:
```http
PUT /usuarios/456
{
    "nombre": "María García López",
    "email": "maria.garcia@ejemplo.com"
}
```

El resultado puede ser:
```json
{
    "id": 456,
    "nombre": "María García López",
    "email": "maria.garcia@ejemplo.com",
    "rol": null,
    "telefono": null,
    "direccion": null
}
```

¡Perdisteis el teléfono y la dirección! Por eso PUT requiere enviar el recurso COMPLETO.

**Diferencias clave: POST vs PUT**

| Aspecto                 | POST                            | PUT                                          |
|-------------------------|---------------------------------|----------------------------------------------|
| **Propósito**           | Crear nuevo recurso             | Actualizar recurso existente                 |
| **Idempotencia**        | NO (cada POST crea nuevo recurso) | SÍ (mismo resultado siempre)                 |
| **URL**                 | No incluye ID (`POST /usuarios`) | Incluye ID específico (`PUT /usuarios/456`)  |
| **ID**                  | Servidor lo genera              | Cliente lo especifica                        |
| **Respuesta típica**    | 201 Created + Location          | 200 OK o 204 No Content                      |
| **Reintentos seguros**  | NO (crea duplicados)            | SÍ (mismo resultado)                         |
| **Actualización**       | N/A (crea)                      | Reemplaza completamente                      |

**Ejemplo comparativo:**

```http
# POST - Crear nuevo usuario (servidor genera ID)
POST /usuarios
{"nombre": "Ana", "email": "ana@ejemplo.com"}
→ 201 Created, Location: /usuarios/789

# POST repetido - crea OTRO usuario diferente
POST /usuarios
{"nombre": "Ana", "email": "ana@ejemplo.com"}
→ 201 Created, Location: /usuarios/790  ← ¡Otro ID!

# PUT - Actualizar usuario existente
PUT /usuarios/456
{"nombre": "María", "email": "maria@ejemplo.com", ...}
→ 200 OK

# PUT repetido - MISMO resultado
PUT /usuarios/456
{"nombre": "María", "email": "maria@ejemplo.com", ...}
→ 200 OK  ← Usuario 456 sigue igual
```

**Usos típicos de PUT:**

- **Actualizar perfil de usuario completo**:
  ```http
  PUT /usuarios/123
  ```

- **Reemplazar configuración**:
  ```http
  PUT /config/aplicacion
  ```

- **Actualizar recurso con todos sus campos**:
  ```http
  PUT /productos/SKU-12345
  ```

**Patrón "upsert" (update or insert):**

Algunos servidores implementan PUT con comportamiento "upsert": si el recurso existe lo actualiza, si no existe lo crea.

```http
# Si /usuarios/999 NO existe
PUT /usuarios/999
{"nombre": "Luis", ...}
→ 201 Created  (lo crea)

# Si /usuarios/999 ya existe
PUT /usuarios/999
{"nombre": "Luis", ...}
→ 200 OK  (lo actualiza)
```

Esto es útil cuando el cliente puede generar IDs únicos (por ejemplo UUIDs) y quiere asegurarse de que el recurso exista con esos datos exactos.

**Cuándo usar vs no usar PUT:**

- Cuando conocéis el ID del recurso a actualizar
- Cuando queréis reemplazar el recurso por completo
- Cuando necesitáis idempotencia (reintentos seguros)
- Cuando implementáis "upsert" con IDs del cliente
- NO uséis PUT cuando solo queréis cambiar un campo → usar PATCH
- NO uséis PUT para crear recursos sin ID conocido → usar POST

##### 1.5.4. PATCH - Actualización parcial

PATCH es el **hermano más inteligente de PUT**. Mientras PUT reemplaza TODO el recurso, PATCH solo modifica lo que necesita cambiar. Es como usar "corrector" en un documento en lugar de reescribirlo entero.

**Propósito fundamental**: Aplicar **modificaciones parciales** a un recurso. Solo enviáis los campos que queréis cambiar, el resto permanece intacto.

**Características importantes:**

- **Potencialmente NO idempotente**: Depende de cómo se implemente. Si el PATCH dice "incrementa el contador en 1", ejecutarlo 3 veces lo incrementa 3 veces (NO idempotente). Si dice "establece el email a X", ejecutarlo 3 veces da el mismo resultado (idempotente). La especificación HTTP dice que PATCH "debería ser" idempotente, pero no lo garantiza.

- **NO seguro**: Obviamente, modifica el estado del servidor.

- **Actualiza solo campos especificados**: Esta es su ventaja principal. Solo los campos que enviáis se modifican. Todo lo demás se mantiene como estaba.

- **Más eficiente**: Ahorra ancho de banda porque solo enviáis lo que cambia, no todo el recurso.

**Ejemplo real de actualización parcial:**

```http
PATCH /usuarios/456 HTTP/1.1
Host: api.ejemplo.com
Content-Type: application/json
Authorization: Bearer eyJhbGc...token...

{
    "email": "nuevo.email@ejemplo.com"
}
```

Le decimos al servidor: "Del usuario 456, solo cambia el email. Todo lo demás déjalo como está."

**Estado ANTES del PATCH:**
```json
{
    "id": 456,
    "nombre": "María García",
    "email": "maria@ejemplo.com",
    "rol": "estudiante",
    "telefono": "666777888",
    "direccion": "Calle Mayor 5"
}
```

**Estado DESPUÉS del PATCH:**
```json
{
    "id": 456,
    "nombre": "María García",            ← Sin cambios
    "email": "nuevo.email@ejemplo.com",  ← Cambiado!!!
    "rol": "estudiante",                 ← Sin cambios
    "telefono": "666777888",             ← Sin cambios
    "direccion": "Calle Mayor 5"         ← Sin cambios
}
```

¡El teléfono y la dirección se mantuvieron! Esa es la diferencia con PUT.

**Respuesta típica:**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 456,
    "nombre": "María García",
    "email": "nuevo.email@ejemplo.com",
    "rol": "estudiante",
    "telefono": "666777888",
    "direccion": "Calle Mayor 5",
    "actualizado": "2025-11-27T16:00:00Z"
}
```

**Comparación PUT vs PATCH:**

Supongamos que el usuario tiene:
```json
{
    "id": 456,
    "nombre": "María",
    "email": "maria@ejemplo.com",
    "telefono": "666777888",
    "direccion": "Calle Mayor 5",
    "rol": "estudiante"
}
```

**Con PUT (reemplazo completo):**
```http
PUT /usuarios/456
{
    "nombre": "María García",
    "email": "maria.garcia@ejemplo.com"
}
```
Resultado:
```json
{
    "id": 456,
    "nombre": "María García",
    "email": "maria.garcia@ejemplo.com",
    "telefono": null,    ← Perdido!!!
    "direccion": null,   ← Perdido!!!
    "rol": null          ← Perdido!!!
}
```

**Con PATCH (actualización parcial):**
```http
PATCH /usuarios/456
{
    "nombre": "María García",
    "email": "maria.garcia@ejemplo.com"
}
```
Resultado:
```json
{
    "id": 456,
    "nombre": "María García",
    "email": "maria.garcia@ejemplo.com",
    "telefono": "666777888",       ← Conservado!!!
    "direccion": "Calle Mayor 5",  ← Conservado!!!
    "rol": "estudiante"            ← Conservado!!!
}
```

**Casos de uso perfectos para PATCH:**

1. **Cambiar un solo campo**:
   ```http
   PATCH /usuarios/123
   {"activo": false}
   ```

2. **Actualizar configuración parcial**:
   ```http
   PATCH /config/aplicacion
   {"tema": "oscuro", "idioma": "es"}
   ```

3. **Modificar estado de un recurso**:
   ```http
   PATCH /pedidos/789
   {"estado": "enviado", "fecha_envio": "2025-11-27"}
   ```

4. **Incrementar contador (cuidado: NO idempotente)**:
   ```http
   PATCH /articulos/123
   {"visitas": {"$inc": 1}}  ← Sintaxis tipo MongoDB
   ```

**JSON Patch (RFC 6902):**

Existe un estándar formal para PATCH llamado "JSON Patch" que usa operaciones explícitas:

```http
PATCH /usuarios/456 HTTP/1.1
Content-Type: application/json-patch+json

[
    { "op": "replace", "path": "/email", "value": "nuevo@ejemplo.com" },
    { "op": "add", "path": "/telefono", "value": "666777888" },
    { "op": "remove", "path": "/direccion" }
]
```

Operaciones disponibles:
- `replace`: Reemplazar valor
- `add`: Añadir nuevo campo
- `remove`: Eliminar campo
- `move`: Mover valor de un campo a otro
- `copy`: Copiar valor
- `test`: Verificar que un campo tiene cierto valor (útil para concurrencia)

**JSON Merge Patch (RFC 7396) - más simple:** Este RFC define una forma más sencilla de hacer PATCH usando un objeto JSON normal:

```http
PATCH /usuarios/456 HTTP/1.1
Content-Type: application/merge-patch+json

{
    "email": "nuevo@ejemplo.com",
    "direccion": null               ← null significa "eliminar"
}
```

Operaciones disponibles:
- Si un campo está presente, se actualiza o añade.
- Si un campo está presente con valor `null`, se elimina.
- Si un campo no está presente, no se toca.


**Problema de idempotencia con PATCH:** Tiene un problema potencial de idempotencia dependiendo de la operación:

```http
# NO idempotente - cada vez suma 10
PATCH /cuentas/123
{"saldo": {"incrementar": 10}}

# Primera ejecución: saldo = 100 + 10 = 110
# Segunda ejecución: saldo = 110 + 10 = 120  ← Diferente!
# Tercera ejecución: saldo = 120 + 10 = 130  ← Diferente!
```

```http
# Idempotente - siempre establece el mismo valor
PATCH /cuentas/123
{"email": "nuevo@ejemplo.com"}

# Primera ejecución: email = "nuevo@ejemplo.com"
# Segunda ejecución: email = "nuevo@ejemplo.com"  ← Igual
# Tercera ejecución: email = "nuevo@ejemplo.com"  ← Igual
```

**Cuándo usar PATCH:**

- Cuando solo necesitáis cambiar algunos campos
- Para ahorrar ancho de banda (importantes en móviles)
- Cuando no queréis obtener primero todo el recurso con GET
- Para actualizaciones frecuentes de estado

**Cuándo usar PUT en lugar de PATCH:**

- Cuando queréis reemplazar el recurso completo
- Cuando necesitáis garantía de idempotencia estricta
- Cuando la API es más simple sin PATCH

**Ejemplo práctico - cambiar solo el avatar:**

```http
PATCH /usuarios/123/perfil HTTP/1.1
Content-Type: application/json

{
    "avatar_url": "https://cdn.ejemplo.com/avatares/nuevo-avatar.jpg"
}
```

Con PUT habríais tenido que enviar nombre, email, biografía, fecha de nacimiento, y todos los demás campos aunque no cambien. Con PATCH solo enviáis el avatar.

##### 1.5.5. DELETE - Eliminar recursos

DELETE hace exactamente lo que su nombre indica: **borra** un recurso del servidor. Es la operación de "destrucción" de CRUD.

**Propósito fundamental**: Eliminar permanentemente un recurso específico del servidor. Es como tirar un archivo a la papelera de reciclaje... pero sin opción de recuperarlo (a menos que tengáis backups).

**Características importantes:**

- **Idempotente**: Esta es una propiedad interesante de DELETE. Borrar un recurso una vez, dos veces o cien veces tiene el mismo efecto final: el recurso no existe. La primera vez lo borra, las siguientes veces el recurso ya no está (y eso es idempotente: el estado final es el mismo).

    ```
    DELETE /usuarios/456  (primera vez)  → 204 No Content (borrado)
    DELETE /usuarios/456  (segunda vez)  → 404 Not Found (ya no existe)
    DELETE /usuarios/456  (tercera vez)  → 404 Not Found (sigue sin existir)
    ```
    
    Aunque la respuesta sea diferente (204 vs 404), el **estado del servidor** es idéntico: el usuario 456 no existe. Por tanto, es idempotente.

- **NO seguro**: Obviamente, DELETE modifica (destructivamente) el estado del servidor.

- **No tiene cuerpo en la petición**: Típicamente, solo especificáis QUÉ recurso eliminar en la URL. No enviáis datos adicionales (aunque técnicamente podríais).

- **Puede devolver el recurso eliminado**: Algunos servidores devuelven información del recurso que acaban de borrar, para que tengáis constancia de qué se eliminó exactamente.

**Ejemplo simple:**

```http
DELETE /usuarios/456 HTTP/1.1
Host: api.ejemplo.com
Authorization: Bearer eyJhbGc...token...
```

Le decimos al servidor: "Elimina el usuario con ID 456. Y por cierto, aquí está mi token para verificar que tengo permiso para borrar usuarios."

**Respuesta típica - 204 No Content (preferida):**

```http
HTTP/1.1 204 No Content
Date: Wed, 27 Nov 2025 16:30:00 GMT
```

El código 204 significa: "Operación exitosa, pero no hay contenido que devolver". Es la respuesta más común para DELETE.

**Respuesta alternativa - 200 OK con confirmación:**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "mensaje": "Usuario eliminado correctamente",
    "id_eliminado": 456,
    "eliminado_en": "2025-11-27T16:30:00Z"
}
```

**Respuesta con el recurso eliminado:**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 456,
    "nombre": "María García",
    "email": "maria@ejemplo.com",
    "eliminado": true,
    "eliminado_en": "2025-11-27T16:30:00Z"
}
```

Esto es útil para que el cliente tenga registro de qué datos exactamente se borraron, por si necesita mostrarlos ("Has eliminado a María García") o implementar un "deshacer".

**Respuesta si el recurso no existe:**

```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{
    "error": "Usuario no encontrado",
    "id_solicitado": 456
}
```

**Soft Delete vs Hard Delete:**

Muchas aplicaciones no borran realmente los datos, sino que los marcan como "eliminados":

**Hard Delete (borrado físico):**
```http
DELETE /usuarios/456
```
→ El usuario desaparece de la base de datos. **Irrecuperable** (sin backups).

**Soft Delete (borrado lógico):**
```http
DELETE /usuarios/456
```
→ El usuario sigue en la base de datos, pero con `eliminado: true` y `fecha_eliminacion: "2025-11-27"`. Invisible para la API normal, pero recuperable por administradores.

Base de datos después de soft delete:
```sql
| **id**  | **nombre**  | **email**              | **eliminado**    | **fecha_eliminacion** |
|---------|-------------|------------------------|------------------|-----------------------|
|      456| María       | maria@ejemplo.com      | true             |    2025-11-27 16:30:00|

```

Ventajas del soft delete:
- Recuperable en caso de error
- Mantiene integridad referencial
- Auditoría completa
- Cumplimiento legal (GDPR permite recuperación en ciertos casos)

**Casos de uso comunes:**

1. **Eliminar un recurso específico**:
   ```http
   DELETE /productos/SKU-12345
   DELETE /comentarios/789
   DELETE /pedidos/101112
   ```

2. **Eliminar relación (unfollow, unlike)**:
   ```http
   DELETE /usuarios/123/seguidos/456  ← Dejar de seguir
   DELETE /posts/789/likes/123        ← Quitar like
   ```

3. **Cerrar sesión (logout)**:
   ```http
   DELETE /sesiones/token-actual
   ```

4. **Eliminar archivo subido**:
   ```http
   DELETE /uploads/mi-documento.pdf
   ```

**Peligros y precauciones:**

-️ **DELETE es permanente**: Una vez ejecutado (hard delete), no hay vuelta atrás sin backups.
-️ **Requiere autenticación fuerte**: Nunca permitáis DELETE sin verificar permisos. Imaginad un DELETE sin autenticación:
```http
DELETE /usuarios/1  ← ¡Borramos al admin!
DELETE /productos/  ← ¡Borramos TODO el catálogo!
```
- **Considerad confirmaciones**: Para operaciones críticas, podéis requerir confirmación explícita:
```http
DELETE /cuentas/123?confirmar=true
```

**Ejemplo práctico - eliminar comentario:**

```http
DELETE /posts/456/comentarios/789 HTTP/1.1
Host: api.ejemplo.com
Authorization: Bearer usuario-token-xyz
```

**Respuesta exitosa:**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "mensaje": "Comentario eliminado",
    "comentario": {
        "id": 789,
        "autor": "Juan",
        "texto": "Comentario eliminado",
        "post_id": 456
    }
}
```

**Idempotencia de DELETE en detalle:**

```http
# Primera petición DELETE
DELETE /usuarios/456
→ HTTP/1.1 204 No Content
Estado del servidor: Usuario 456 NO EXISTE

# Segunda petición DELETE (reintento)
DELETE /usuarios/456
→ HTTP/1.1 404 Not Found
Estado del servidor: Usuario 456 NO EXISTE (igual que antes)

# Tercera petición DELETE
DELETE /usuarios/456
→ HTTP/1.1 404 Not Found
Estado del servidor: Usuario 456 NO EXISTE (igual que antes)
```

El **estado final del servidor es idéntico**: el usuario 456 no existe. Aunque las respuestas HTTP cambien (204 la primera, 404 las siguientes), el efecto sobre el servidor es el mismo. Por eso DELETE es idempotente.

**Comparación: cuando NO usar DELETE:**

**NO usar DELETE para**:
- Cerrar sesión temporalmente → usar POST /logout
- Archivar recursos → usar PATCH {archivado: true}
- Desactivar cuenta → usar PATCH {activa: false}

**SÍ usar DELETE para**:
- Eliminar definitivamente un recurso
- Borrar datos temporales caducados
- Quitar asociaciones/relaciones
- Limpiar caché o sesiones expiradas

##### 1.5.6. HEAD - Obtener metadatos

HEAD es como un GET "light": **obtiene toda la información sobre un recurso EXCEPTO el contenido real**. Es perfecto cuando solo queréis saber SOBRE el recurso, pero no descargarlo.

**Propósito fundamental**: Solicitar las mismas cabeceras HTTP que devolvería un GET, pero sin descargar el cuerpo de la respuesta. Es como preguntar "¿qué tamaño tiene este archivo?" sin descargarlo.

**Características importantes:**

- **Idempotente**: Igual que GET, hacer HEAD múltiples veces no cambia nada.
- **Seguro**: No modifica el estado del servidor, solo consulta metadatos.
- **Sin cuerpo en la respuesta**: El servidor devuelve código de estado y todas las cabeceras, pero el cuerpo está vacío.
- **Idéntico a GET (excepto el cuerpo)**: El servidor debe procesar HEAD exactamente como un GET, incluyendo ejecutar la misma lógica, pero sin enviar el contenido.

**Ejemplo - verificar si un archivo existe:**

```http
HEAD /archivos/documento-importante.pdf HTTP/1.1
Host: cdn.ejemplo.com
```

**Respuesta:**

```http
HTTP/1.1 200 OK
Content-Type: application/pdf
Content-Length: 2485760
Last-Modified: Mon, 25 Nov 2025 14:30:00 GMT
ETag: "33a64df551425fcc"
Cache-Control: public, max-age=3600
```

¡Fijaos! El servidor nos dice:
- El archivo existe (200 OK)
- Es un PDF
- Pesa 2.485.760 bytes (~2.4 MB)
- Se modificó el 25 de noviembre
- Tiene este ETag único
- Se puede cachear durante 1 hora

**Todo esto sin descargar los 2.4 MB del PDF**. Si hubiéramos usado GET, habríamos descargado el archivo completo solo para saber su tamaño.

**Casos de uso prácticos:**

**1. Verificar si un recurso existe (sin descargarlo):**

```http
HEAD /api/usuarios/123 HTTP/1.1
Host: api.ejemplo.com
```

```http
HTTP/1.1 200 OK  ← Existe
```

```http
HTTP/1.1 404 Not Found  ← No existe
```

Útil para validar que un ID existe antes de hacer operaciones costosas.

**2. Comprobar si un archivo cambió (sin descargarlo):**

```javascript
// Cliente web usando HEAD para verificar actualizaciones
const response = await fetch('/datos.json', { method: 'HEAD' });
const lastModified = response.headers.get('Last-Modified');

if (lastModified !== localStorage.getItem('lastModified')) {
    // El archivo cambió, descargarlo con GET
    const data = await fetch('/datos.json').then(r => r.json());
    localStorage.setItem('lastModified', lastModified);
} else {
    // El archivo no cambió, usar versión local
    // AHORRAMOS una descarga completa
}
```

**3. Verificar tamaño antes de descargar:**

```http
HEAD /videos/tutorial-completo.mp4 HTTP/1.1
Host: cdn.ejemplo.com
```

```http
HTTP/1.1 200 OK
Content-Length: 524288000
Content-Type: video/mp4
```

El video pesa 524 MB. El usuario puede decidir si quiere descargarlo según su conexión.

**4. Verificar tipo de contenido:**

```http
HEAD /recurso/misterioso HTTP/1.1
Host: api.ejemplo.com
```

```http
HTTP/1.1 200 OK
Content-Type: application/json
```

Ahora sabemos que es JSON sin haberlo descargado.

**5. Validar enlaces rotos en una web:**

```python
# Script que verifica 1000 enlaces
for url in enlaces:
    response = requests.head(url)
    if response.status_code == 404:
        print(f"Enlace roto: {url}")
    # Mucho más rápido que GET porque no descarga contenido
```

**6. Comprobar si necesitamos revalidar caché:**

```http
HEAD /api/productos HTTP/1.1
Host: api.ejemplo.com
If-None-Match: "33a64df551425fcc"
```

```http
HTTP/1.1 304 Not Modified
ETag: "33a64df551425fcc"
```

El servidor dice: "No ha cambiado, usa tu caché local". Todo sin enviar la lista de productos.

**Diferencia HEAD vs GET:**

| Método | Descarga contenido | Uso típico          | Ancho de banda |
|:------:|:------------------:|:--------------------|:--------------:|
|  GET   |         SÍ         | Obtener datos       |      Alto      |
|  HEAD  |         NO         | Verificar metadatos |     Mínimo     |

**Ejemplo comparativo:**

```http
# GET - descarga 2.5 MB
GET /video.mp4
→ HTTP/1.1 200 OK
   Content-Length: 2500000
   [2.5 MB de datos de video]

# HEAD - descarga ~500 bytes (solo cabeceras)
HEAD /video.mp4
→ HTTP/1.1 200 OK
   Content-Length: 2500000
   [cuerpo vacío]
```

**Aplicación real - gestor de descargas:**

```javascript
// Antes de descargar, verificamos tamaño
async function smartDownload(url) {
    const headResponse = await fetch(url, { method: 'HEAD' });
    const fileSize = headResponse.headers.get('Content-Length');
    
    if (fileSize > 100_000_000) { // 100 MB
        const confirm = await askUser(`El archivo pesa ${fileSize} bytes. ¿Descargar?`);
        if (!confirm) return;
    }
    
    // Solo ahora descargamos realmente
    const getResponse = await fetch(url);
    return await getResponse.blob();
}
```

**Limitaciones:**

- El servidor DEBE implementar HEAD correctamente: procesarlo igual que GET pero sin cuerpo. 
- Algunos servidores mal configurados responden igual a HEAD y GET (enviando el cuerpo), perdiendo el beneficio.
- HEAD no puede decirte el contenido: solo metadatos. Si necesitas el contenido, debes usar GET.


##### 1.5.7. OPTIONS - Opciones disponibles

OPTIONS es el método "preguntón" de HTTP: **"¿Qué puedo hacer contigo?"**. Pregunta al servidor qué métodos HTTP acepta para un recurso específico.

**Propósito fundamental**: Descubrir las capacidades de comunicación de un recurso sin realizar ninguna acción. Es como llamar a un hotel y preguntar "¿qué servicios ofrecéis?" sin hacer reserva.

**Características importantes:**

- **Idempotente**: Preguntar múltiples veces no cambia nada.
- **Seguro**: No modifica el estado del servidor, solo consulta capacidades.
- **Fundamental para CORS**: Los navegadores usan OPTIONS automáticamente antes de peticiones "complejas" entre diferentes dominios.
- **Documentación en vivo**: Un servidor puede usar OPTIONS para exponer qué métodos HTTP soporta cada endpoint.

**Ejemplo básico:**

```http
OPTIONS /api/usuarios HTTP/1.1
Host: api.ejemplo.com
Origin: https://mi-app.com
```

**Respuesta típica:**

```http
HTTP/1.1 200 OK
Allow: GET, POST, PUT, DELETE, OPTIONS, HEAD
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Max-Age: 86400
```

El servidor responde: "Para `/api/usuarios`, puedes usar GET, POST, PUT, DELETE, OPTIONS y HEAD. Además, acepto peticiones CORS de cualquier origen, con estos métodos, y puedes enviar las cabeceras Content-Type y Authorization. Esta respuesta es válida durante 24 horas."

**Caso de uso principal: CORS (Cross-Origin Resource Sharing)**

Cuando vuestra aplicación web en `https://mi-app.com` intenta hacer una petición a `https://api.ejemplo.com`, el navegador **automáticamente** envía primero un OPTIONS:

**Secuencia CORS (preflight request):**

```http
# 1. Navegador envía automáticamente OPTIONS (preflight)
OPTIONS /api/usuarios HTTP/1.1
Host: api.ejemplo.com
Origin: https://mi-app.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Content-Type, Authorization
```

```http
# 2. Servidor responde con permisos CORS
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: https://mi-app.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Max-Age: 3600
```

```http
# 3. Si el OPTIONS fue exitoso, navegador envía la petición real
POST /api/usuarios HTTP/1.1
Host: api.ejemplo.com
Origin: https://mi-app.com
Content-Type: application/json
Authorization: Bearer token...

{"nombre": "Ana", "email": "ana@ejemplo.com"}
```

El navegador hace este baile OPTIONS → POST automáticamente. Vosotros solo veis el POST en vuestro código JavaScript.

**¿Cuándo el navegador envía OPTIONS preflight?**

El navegador NO envía preflight para peticiones "simples":
- GET, HEAD, POST (con Content-Type application/x-www-form-urlencoded, multipart/form-data o text/plain)
- Sin cabeceras custom

El navegador SÍ envía preflight para peticiones "complejas":
- Métodos PUT, DELETE, PATCH
- POST con Content-Type: application/json
- Cualquier petición con cabecera Authorization
- Cabeceras custom (X-Custom-Header, etc.)

**Ejemplo real - API que documenta sus capacidades:**

```http
OPTIONS /api/productos/SKU-123 HTTP/1.1
Host: api.ejemplo.com
```

```http
HTTP/1.1 200 OK
Allow: GET, PUT, PATCH, DELETE
Content-Type: application/json

{
    "endpoint": "/api/productos/SKU-123",
    "metodos_soportados": [
        {
            "metodo": "GET",
            "descripcion": "Obtener detalles del producto",
            "requiere_autenticacion": false
        },
        {
            "metodo": "PUT",
            "descripcion": "Actualizar producto completo",
            "requiere_autenticacion": true,
            "roles_requeridos": ["admin", "editor"]
        },
        {
            "metodo": "PATCH",
            "descripcion": "Actualizar campos específicos",
            "requiere_autenticacion": true,
            "roles_requeridos": ["admin", "editor"]
        },
        {
            "metodo": "DELETE",
            "descripcion": "Eliminar producto",
            "requiere_autenticacion": true,
            "roles_requeridos": ["admin"]
        }
    ]
}
```

Esto convierte OPTIONS en una forma de auto-documentación de la API.

**OPTIONS para el recurso raíz:**

```http
OPTIONS * HTTP/1.1
Host: api.ejemplo.com
```

```http
HTTP/1.1 200 OK
Allow: OPTIONS, GET
Server: nginx/1.18.0
```

El `*` pregunta por las capacidades del servidor en general, no de un recurso específico.

**Ejemplo práctico - cliente que detecta capacidades:**

```javascript
async function checkCapabilities(url) {
    const response = await fetch(url, {
        method: 'OPTIONS'
    });
    
    const allowedMethods = response.headers.get('Allow');
    console.log(`Métodos disponibles: ${allowedMethods}`);
    
    if (allowedMethods.includes('DELETE')) {
        // Mostrar botón de eliminar
        showDeleteButton();
    }
    
    if (allowedMethods.includes('PUT')) {
        // Habilitar edición
        enableEditing();
    }
}
```

**Problema común: servidor que no implementa OPTIONS**

```http
OPTIONS /api/usuarios HTTP/1.1
Host: api-mal-configurada.com
Origin: https://mi-app.com
```

```http
HTTP/1.1 405 Method Not Allowed
```

Error típico cuando el servidor no está configurado para CORS. La aplicación web falla porque el navegador bloquea la petición.

**Solución: configurar el servidor para responder OPTIONS**

**Node.js/Express:**
```javascript
app.options('/api/usuarios', (req, res) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    res.sendStatus(204);
});

// O para todas las rutas:
app.use((req, res, next) => {
    if (req.method === 'OPTIONS') {
        res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
        return res.sendStatus(204);
    }
    next();
});
```

**Nginx:**
```nginx
location /api/ {
    if ($request_method = 'OPTIONS') {
        add_header 'Access-Control-Allow-Origin' '*';
        add_header 'Access-Control-Allow-Methods' 'GET, POST, PUT, DELETE, OPTIONS';
        add_header 'Access-Control-Max-Age' 86400;
        add_header 'Content-Length' 0;
        return 204;
    }
}
```

**Apache:**
```apache
Header always set Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS"
Header always set Access-Control-Allow-Headers "Content-Type, Authorization"

<If "%{REQUEST_METHOD} == 'OPTIONS'">
    Header set Access-Control-Max-Age "86400"
</If>
```

**Cabeceras CORS importantes en respuestas OPTIONS:**

| Cabecera                           | Propósito                                    | Ejemplo                        |
|------------------------------------|----------------------------------------------|--------------------------------|
| `Access-Control-Allow-Origin`      | Qué orígenes pueden acceder                  | `*` o `https://mi-app.com`     |
| `Access-Control-Allow-Methods`     | Qué métodos HTTP están permitidos            | `GET, POST, PUT, DELETE`       |
| `Access-Control-Allow-Headers`     | Qué cabeceras puede enviar el cliente        | `Content-Type, Authorization`  |
| `Access-Control-Max-Age`           | Cuánto tiempo cachear esta respuesta OPTIONS | `86400` (24 horas en segundos) |
| `Access-Control-Allow-Credentials` | Si permite cookies/autenticación             | `true`                         |

**Optimización: cachear la respuesta OPTIONS**

Con `Access-Control-Max-Age: 86400`, le decís al navegador: "Guarda esta respuesta OPTIONS durante 24 horas. No me preguntes de nuevo durante ese tiempo."

Esto reduce drásticamente las peticiones preflight innecesarias:

```
Sin Max-Age:
OPTIONS /api/usuarios       → espera respuesta
POST /api/usuarios          → espera respuesta
OPTIONS /api/usuarios       → espera respuesta (de nuevo!)
PUT /api/usuarios           → espera respuesta
...cada petición necesita preflight

Con Max-Age 86400:
OPTIONS /api/usuarios       → espera respuesta → guarda en caché 24h
POST /api/usuarios          → usa caché, no envía OPTIONS
PUT /api/usuarios           → usa caché, no envía OPTIONS  
DELETE /api/usuarios        → usa caché, no envía OPTIONS
...mucho más rápido!
```

**Cuándo usar vs NO usar OPTIONS:**

- Automáticamente (navegador lo hace por vosotros en CORS)
- Para descubrir capacidades de una API
- Para implementar auto-documentación de APIs
- Debugging de problemas CORS
- No usar, cuando frontend y backend están en el mismo dominio (no hay CORS)
- No usar, para peticiones simples GET (el navegador no envía preflight)
- No usar, si usáis un proxy que evita CORS

##### 1.5.8. Tabla resumen de métodos HTTP

| Método      | Propósito            | Idempotente  | Seguro  | Con cuerpo  | Cacheable  |
|:------------|:---------------------|:------------:|:-------:|:-----------:|:----------:|
| **GET**     | Obtener recurso      |      ✓       |    ✓    |     No      |     ✓      |
| **POST**    | Crear recurso        |      ✗       |    ✗    |     Sí      |     ✗      |
| **PUT**     | Actualizar completo  |      ✓       |    ✗    |     Sí      |     ✗      |
| **PATCH**   | Actualizar parcial   |      ✗       |    ✗    |     Sí      |     ✗      |
| **DELETE**  | Eliminar recurso     |      ✓       |    ✗    |     No      |     ✗      |
| **HEAD**    | Obtener metadatos    |      ✓       |    ✓    |     No      |     ✓      |
| **OPTIONS** | Opciones disponibles |      ✓       |    ✓    |     No      |     ✗      |

!!! tip "Diseño de APIs RESTful"
    El uso correcto de los métodos HTTP es fundamental para diseñar APIs RESTful bien estructuradas. Cada método tiene un propósito específico y debe usarse según su semántica.

#### 1.6. Códigos de estado HTTP

Después de cada petición, el servidor envía una respuesta que incluye un **código de estado HTTP**. Este código es un número de tres dígitos que indica el resultado de la petición.

<figure markdown="span">
  ![Códigos de estado HTTP](assets/status-code.png){ width="700" }
  <figcaption>Clasificación de los códigos de estado HTTP organizados por familias: 1xx (Informativos), 2xx (Éxito), 3xx (Redirección), 4xx (Errores del cliente), 5xx (Errores del servidor). Cada familia indica un tipo diferente de resultado de la petición</figcaption>
</figure>

##### 1.6.1. Familia 1xx - Respuestas informativas

Indican que la petición ha sido recibida y el proceso continúa.

| Código  | Nombre              | Descripción                                            |
|:-------:|:--------------------|:-------------------------------------------------------|
| **100** | Continue            | El cliente puede continuar con su petición             |
| **101** | Switching Protocols | El servidor acepta cambiar de protocolo                |
| **102** | Processing          | El servidor está procesando, pero aún no hay respuesta |

**Uso poco común**: Raramente se encuentran estos códigos en aplicaciones web típicas.

##### 1.6.1. Familia 2xx - Operaciones exitosas

Indican que la acción del cliente fue recibida, entendida y aceptada correctamente.

| Código  | Nombre          | Descripción                              | Uso típico                           |
|:--------|:----------------|:-----------------------------------------|:-------------------------------------|
| **200** | OK              | Petición procesada correctamente         | GET exitoso, respuesta con contenido |
| **201** | Created         | Recurso creado exitosamente              | POST que crea un recurso             |
| **202** | Accepted        | Petición aceptada para procesamiento     | Procesamiento asíncrono              |
| **204** | No Content      | Éxito pero sin contenido en la respuesta | DELETE exitoso                       |
| **206** | Partial Content | Respuesta parcial (para rangos)          | Descarga parcial de archivos         |

**Ejemplo práctico:**

```http
// Petición
POST /api/productos HTTP/1.1
Content-Type: application/json

{"nombre": "Laptop", "precio": 899}

// Respuesta
HTTP/1.1 201 Created
Location: /api/productos/789
Content-Type: application/json

{"id": 789, "nombre": "Laptop", "precio": 899}
```

##### 1.6.1. Familia 3xx - Redirecciones

El cliente necesita realizar una acción adicional para completar la petición.

| Código  | Nombre             | Descripción                              | Uso típico                                  |
|:--------|:-------------------|:-----------------------------------------|:--------------------------------------------|
| **301** | Moved Permanently  | El recurso se movió permanentemente      | URLs que cambiaron para siempre             |
| **302** | Found              | Redirección temporal                     | Redirección temporal                        |
| **304** | Not Modified       | El recurso no ha cambiado                | Caché: el cliente puede usar su copia local |
| **307** | Temporary Redirect | Redirección temporal (mantiene método)   | Similar a 302 pero más estricto             |
| **308** | Permanent Redirect | Redirección permanente (mantiene método) | Similar a 301 pero más estricto             |

**Ejemplo con Location header:**

```http
HTTP/1.1 301 Moved Permanently
Location: https://www.ejemplo.com/nueva-url
```

El navegador automáticamente seguirá la redirección.

##### 1.6.1. Familia 4xx - Errores del cliente

La petición contiene un error o no puede ser completada debido a un problema del cliente.

| Código  | Nombre             | Descripción                         | Causa común                              |
|:--------|:-------------------|:------------------------------------|:-----------------------------------------|
| **400** | Bad Request        | Petición malformada                 | JSON inválido, parámetros incorrectos    |
| **401** | Unauthorized       | Autenticación requerida o fallida   | No está logueado o token inválido        |
| **403** | Forbidden          | Acceso prohibido                    | No tiene permisos suficientes            |
| **404** | Not Found          | Recurso no encontrado               | URL incorrecta o recurso no existe       |
| **405** | Method Not Allowed | Método HTTP no permitido            | GET en un endpoint que solo acepta POST  |
| **408** | Request Timeout    | Tiempo de espera agotado            | Petición demasiado lenta                 |
| **409** | Conflict           | Conflicto con el estado actual      | Duplicado, violación de regla de negocio |
| **410** | Gone               | El recurso ya no está disponible    | Recurso eliminado permanentemente        |
| **413** | Payload Too Large  | Cuerpo de petición demasiado grande | Archivo subido muy grande                |
| **429** | Too Many Requests  | Demasiadas peticiones               | Rate limiting                            |

**Ejemplos prácticos:**

```http
// Error 401 - No autenticado
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer realm="api"
Content-Type: application/json

{
    "error": "Token de autenticación requerido"
}
```

```http
// Error 404 - No encontrado
HTTP/1.1 404 Not Found
Content-Type: application/json

{
    "error": "Usuario con ID 999 no encontrado"
}
```

```http
// Error 403 - Sin permisos
HTTP/1.1 403 Forbidden
Content-Type: application/json

{
    "error": "No tienes permisos para eliminar este recurso"
}
```

!!! note "Diferencia entre 401 y 403"
    - **401 Unauthorized**: "No sé quién eres" - Necesitas autenticarte
    - **403 Forbidden**: "Sé quién eres, pero no puedes hacer esto" - No tienes permisos

##### 1.6.1. Familia 5xx - Errores del servidor

El servidor falló al completar una petición aparentemente válida. El problema está en el servidor, no en el cliente.

| Código  | Nombre                | Descripción                              | Causa común                              |
|:--------|:----------------------|:-----------------------------------------|:-----------------------------------------|
| **500** | Internal Server Error | Error genérico del servidor              | Excepción no capturada, bug en el código |
| **501** | Not Implemented       | Funcionalidad no implementada            | Método no soportado                      |
| **502** | Bad Gateway           | Gateway/proxy recibió respuesta inválida | Servidor backend caído                   |
| **503** | Service Unavailable   | Servicio temporalmente no disponible     | Mantenimiento, sobrecarga                |
| **504** | Gateway Timeout       | Timeout en gateway/proxy                 | Backend no responde a tiempo             |

**Ejemplos:**

```http
// Error 500 - Error interno
HTTP/1.1 500 Internal Server Error
Content-Type: application/json

{
    "error": "Error interno del servidor",
    "mensaje": "Por favor, contacte al administrador"
}
```

```http
// Error 503 - Servicio no disponible
HTTP/1.1 503 Service Unavailable
Retry-After: 3600
Content-Type: application/json

{
    "error": "Servicio en mantenimiento",
    "mensaje": "Estará disponible en 1 hora"
}
```

!!! warning "Nunca exponer detalles técnicos"
    En producción, los errores 5xx **nunca deben revelar** detalles técnicos como trazas de stack, consultas SQL o rutas de archivos. Esto es un riesgo de seguridad. Guardad esos detalles en logs del servidor.

#### 1.7. El protocolo HTTPS: seguridad en la web

**HTTPS (HyperText Transfer Protocol Secure)** es la versión segura del protocolo HTTP. En la web moderna, HTTPS no es opcional: es **esencial** para la seguridad y privacidad de los usuarios.

##### 1.7.1. ¿Por qué es necesario HTTPS?

Imaginad que enviáis una carta y que cualquier persona por la que pase esa carta (el cartero, la oficina de correos, cualquiera) pueda abrirla, leerla, modificarla y volver a cerrarla sin que os déis cuenta. **Eso es HTTP**. Todo viaja en texto plano, completamente legible.

HTTP tradicional transmite datos **sin cifrar**, lo que significa que cualquiera que intercepte la comunicación entre vuestro navegador y el servidor puede leer absolutamente todo:

- **Contraseñas**: Cuando hacéis login, vuestra contraseña viaja en texto plano. Un atacante en vuestra WiFi del café puede verla.
- **Números de tarjetas de crédito**: Al comprar online, los datos de pago son visibles para cualquier atacante intermedio.
- **Mensajes privados**: Ese email confidencial o chat privado puede ser leído por terceros.
- **Cookies de sesión**: Un atacante puede robar vuestra sesión y hacerse pasar por vosotros.
- **Cualquier dato**: Formularios, búsquedas, información personal... todo visible.

**Amenazas reales sin HTTPS:**

1. **Eavesdropping (espionaje/escucha)**: 
   
   Un atacante en la misma red WiFi (aeropuerto, café, hotel) puede usar herramientas como Wireshark para capturar TODO vuestro tráfico HTTP. Ven cada petición, cada respuesta, cada dato que enviáis.

   ```
   Petición HTTP visible:
   POST /login HTTP/1.1
   username=maria@ejemplo.com&password=MiPassword123
   
   ↑ Un atacante ve esto exactamente así
   ```

2. **Man-in-the-Middle (MITM - ataque del hombre en el medio)**: 
   
   Un atacante se interpone entre vosotros y el servidor. No solo puede leer todo, sino **modificar** los datos en tránsito. Puede cambiar "transfiere 10€" por "transfiere 1000€", puede inyectar malware en la página, puede redirigiros a un sitio falso.

   ```
   Vosotros → [ATACANTE] → Servidor Real
                 ↓
             Lee y modifica todo
   ```

3. **Suplantación de identidad**: 
   
   Sin HTTPS no hay forma de verificar que realmente estáis hablando con `banco.com` y no con `banc0.com` (nota la "o" por un cero). Un atacante puede crear un servidor falso que se hace pasar por el legítimo.

4. **Session Hijacking (secuestro de sesión)**: 
   
   Vuestro navegador envía cookies de sesión en cada petición. En HTTP, un atacante puede robar esa cookie y hacerse pasar por vosotros sin necesitar vuestra contraseña.

   ```http
   # Atacante captura esto:
   GET /perfil HTTP/1.1
   Cookie: session=abc123xyz789
   
   # Ahora el atacante puede usar esa cookie para acceder como vosotros
   ```

**Ejemplo real de ataque:**

En 2011, una herramienta llamada "Firesheep" permitía a cualquiera en una WiFi pública secuestrar sesiones de Facebook, Twitter, Amazon, etc. en cuestión de segundos. Solo funcionaba contra HTTP. Esto forzó a muchos sitios a adoptar HTTPS.

**Consecuencias de NO usar HTTPS en 2025:**

1. **Navegadores te marcan como "No seguro"**: 
   
   Chrome, Firefox, Safari muestran una advertencia grande. Los usuarios huyen.
   
   <figure markdown="span">
     ![](assets/http-no-seguro.png){ width="400" }
     <figcaption>Advertencia que ven los usuarios en sitios HTTP</figcaption>
   </figure>

2. **Google penaliza tu SEO**: 
   
   HTTPS es un factor de ranking. Sitios HTTP aparecen más abajo en resultados de búsqueda.

3. **Funcionalidades modernas bloqueadas**: 
   
   APIs del navegador como Geolocalización, Cámara, Micrófono, Service Workers (PWA), HTTP/2... **solo funcionan en HTTPS**.

   ```javascript
   // Esto falla en HTTP:
   navigator.geolocation.getCurrentPosition(...)
   // Error: geolocation only available in secure contexts (HTTPS)
   ```

4. **Pérdida de confianza**: 
   
   Los usuarios saben que sin el candado 🔒 en la barra de direcciones, el sitio no es seguro. No comprarán, no se registrarán.

5. **Regulaciones legales**: 
   
   GDPR en Europa y otras regulaciones exigen proteger datos personales. HTTP sin cifrar puede ser ilegal para ciertos datos.

!!! danger "HTTP está obsoleto"
    En 2025, **NO hay excusa** para usar HTTP. Certificados HTTPS son **gratuitos** (Let's Encrypt), fáciles de instalar (Certbot lo hace automáticamente) y necesarios para cualquier sitio moderno. Los navegadores activamente discriminan contra HTTP.

##### 1.7.1. ¿Cómo funciona HTTPS?

HTTPS = HTTP + SSL/TLS (cifrado)

**SSL/TLS** (Secure Sockets Layer / Transport Layer Security) son protocolos criptográficos que:

1. **Cifran** la comunicación entre cliente y servidor
2. **Autentican** la identidad del servidor
3. **Garantizan la integridad** de los datos (no han sido modificados)

**Proceso de establecimiento de conexión HTTPS:**

1. **Cliente** inicia conexión HTTPS al servidor

2. **Servidor** envía su certificado digital al cliente

3. **Cliente** verifica el certificado:
    
    - ¿Está firmado por una Autoridad de Certificación confiable?
    - ¿El dominio coincide?
    - ¿Está dentro de su período de validez?
    - ¿No está revocado?
    
4. **Cliente y servidor** negocian algoritmos de cifrado

5. **Intercambio de claves**: Se establece una clave de sesión compartida

6. **Comunicación cifrada**: Todos los datos se cifran con la clave de sesión

##### 1.7.1. Certificados digitales

Un **certificado digital** es un documento electrónico que vincula una clave pública a la identidad de un propietario (servidor web).

**Componentes de un certificado:**

- **Dominio**: Para qué sitio es válido (ej: `www.ejemplo.com`)
- **Organización**: Quién es el propietario
- **Clave pública**: Para cifrar datos hacia el servidor
- **Período de validez**: Fechas de inicio y fin
- **Emisor**: Qué Autoridad de Certificación lo firmó
- **Firma digital**: Garantiza autenticidad

**Autoridades de Certificación (CA):**

Son entidades de confianza que emiten y firman certificados:

- Let's Encrypt (gratuita)
- DigiCert
- GlobalSign
- Sectigo
- GoDaddy

Los navegadores tienen una lista de CAs en las que confían. Si un certificado no está firmado por una CA confiable, el navegador mostrará una advertencia.

##### 1.7.1. Tipos de certificados

**Por nivel de validación:**

1. **Domain Validation (DV)**: Valida solo que controlas el dominio
    
    - Rápido y económico (o gratuito con Let's Encrypt)
    - Suficiente para la mayoría de sitios
    
2. **Organization Validation (OV)**: Valida también la organización
    
    - Requiere verificar documentos de la empresa
    - Más confianza para usuarios
    
3. **Extended Validation (EV)**: Validación exhaustiva
    
    - Proceso de verificación riguroso
    - Mostraba barra verde en navegadores (ya no)
    - Para sitios de banca, e-commerce grande

**Por cobertura de dominios:**

1. **Single domain**: Solo para un dominio (`www.ejemplo.com`)

2. **Wildcard**: Para un dominio y todos sus subdominios (`*.ejemplo.com`)

3. **Multi-domain (SAN)**: Para múltiples dominios diferentes

##### 1.7.1. Let's Encrypt: certificados gratuitos

**Let's Encrypt** es una Autoridad de Certificación sin ánimo de lucro que proporciona certificados SSL/TLS **gratuitos y automáticos**.

**Ventajas:**

- **Gratuito**: Sin coste alguno
- **Automático**: Renovación automática cada 90 días
- **Abierto**: Software libre y proceso transparente
- **Fácil**: Herramientas como Certbot simplifican la instalación

**Instalación típica con Certbot:**

```bash
# Instalar Certbot
sudo apt install certbot python3-certbot-apache

# Obtener e instalar certificado para Apache
sudo certbot --apache -d www.ejemplo.com

# Renovación automática (ya está configurada)
sudo certbot renew --dry-run
```

##### 1.7.1. Impacto en el rendimiento

El cifrado SSL/TLS requiere recursos computacionales adicionales:

- **Handshake inicial**: Más lento que HTTP
- **Cifrado/descifrado**: Uso de CPU

**Mitigaciones:**

- Hardware moderno gestiona esto eficientemente
- **HTTP/2**: Mejora el rendimiento (solo funciona sobre HTTPS)
- **Session resumption**: Reutiliza claves de sesiones previas
- **TLS 1.3**: Versión más rápida del protocolo

!!! tip "HTTPS es más rápido que HTTP"
    Paradójicamente, con HTTP/2 (que requiere HTTPS), los sitios HTTPS modernos son **más rápidos** que los HTTP, a pesar del cifrado. HTTP/2 multiplexea peticiones, comprime cabeceras y permite server push.

##### 1.7.1. HTTPS en desarrollo

Durante el desarrollo es útil usar HTTPS también:

**Opciones:**

1. **Certificado autofirmado**: Para desarrollo local
    
    ```bash
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
        -keyout localhost.key -out localhost.crt
    ```
    
2. **mkcert**: Herramienta para certificados locales confiables
    
    ```bash
    # Instalar mkcert
    brew install mkcert  # macOS
    # sudo apt install mkcert  # Linux
    
    # Crear certificado para localhost
    mkcert localhost 127.0.0.1 ::1
    ```
    
3. **Túneles**: ngrok, localtunnel para exponer localhost con HTTPS

##### 1.7.1. Buenas prácticas HTTPS

1. **Usar siempre HTTPS**: Para todo el sitio, no solo el login

2. **HTTP Strict Transport Security (HSTS)**: Forzar HTTPS
    
    ```
    Strict-Transport-Security: max-age=31536000; includeSubDomains
    ```
    
3. **Redirigir HTTP a HTTPS**: Configuración en servidor
    
    ```apache
    # Apache
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^(.*)$ https://%{HTTP_HOST}/$1 [R=301,L]
    ```
    
4. **Mantener certificados actualizados**: Renovar antes de expirar

5. **Usar TLS 1.2 o superior**: Desactivar versiones antiguas inseguras

6. **Configurar correctamente**: Usar herramientas como [SSL Labs](https://www.ssllabs.com/ssltest/)

Como conclusión, podemos decir que:

1. **HTTP** es el protocolo fundamental de la web: sencillo, extensible y stateless.
2. **Las peticiones y respuestas HTTP** tienen una estructura clara con línea de estado, cabeceras y cuerpo.
3. **Las cabeceras HTTP** proporcionan metadatos esenciales sobre la comunicación.
4. **Los métodos HTTP** (GET, POST, PUT, DELETE, etc.) definen las acciones sobre recursos.
5. **Los códigos de estado** indican el resultado de una petición (2xx éxito, 4xx error cliente, 5xx error servidor).
6. **HTTPS** es esencial para la seguridad, cifrando la comunicación mediante SSL/TLS y certificados digitales.

HTTP y HTTPS son los cimientos sobre los que se construyen las aplicaciones web y las APIs modernas. Dominarlos es fundamental para cualquier desarrollador o ingeniero DevOps.



### 2. Páginas web estáticas vs dinámicas

Una vez que comprendemos cómo se comunican cliente y servidor mediante HTTP, surge una pregunta natural: **¿cómo se genera el contenido que viaja en esas respuestas HTTP?** No todo el contenido web se crea igual. Existe una diferencia fundamental entre el contenido que ya existe preformado y el contenido que se construye dinámicamente para cada petición. Esta distinción marca la diferencia entre la web estática de los años 90 y las aplicaciones web modernas que usamos hoy.

#### 2.1. La evolución: de lo estático a lo dinámico

Para comprender completamente las páginas web dinámicas, primero debemos entender de dónde venimos. La web no comenzó siendo dinámica; su evolución ha sido progresiva y responde a las crecientes necesidades de interactividad y personalización.

#### 2.2. El inicio: páginas web estáticas

En los primeros días de Internet (años 90), todas las páginas web eran **estáticas**. Tim Berners-Lee, cuando creó la primera página web en 1991, simplemente escribió un documento HTML que describía el proyecto World Wide Web. Ese archivo HTML se guardaba en un servidor y se enviaba exactamente igual a cualquier persona que lo solicitara.

**¿Qué es una página web estática?**

Una página web estática es como un libro impreso: su contenido está fijado en el momento de su creación y no cambia a menos que alguien edite manualmente el archivo. Son páginas compuestas por archivos predefinidos (HTML, CSS, JavaScript) que se almacenan directamente en el servidor.

**El proceso es extremadamente simple:**

1. Un desarrollador crea un archivo `index.html` con todo el contenido
2. El archivo se sube al servidor web
3. Cuando un usuario solicita la página, el servidor simplemente lee el archivo del disco y lo envía
4. Todos los usuarios reciben exactamente el mismo contenido

**Ejemplo de página estática simple:**

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Portfolio</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <header>
        <h1>Bienvenidos a mi portfolio</h1>
        <nav>
            <a href="index.html">Inicio</a>
            <a href="proyectos.html">Proyectos</a>
            <a href="contacto.html">Contacto</a>
        </nav>
    </header>
    
    <main>
        <h2>Sobre mí</h2>
        <p>Soy un desarrollador web con 5 años de experiencia...</p>
        
        <h2>Mis proyectos destacados</h2>
        <ul>
            <li>Aplicación de gestión de tareas</li>
            <li>Tienda online de productos artesanales</li>
            <li>Blog personal sobre tecnología</li>
        </ul>
    </main>
    
    <footer>
        <p>&copy; 2025 Mi Portfolio</p>
    </footer>
</body>
</html>
```

**Características de las páginas estáticas:**

- **Contenido fijo**: El contenido es idéntico para todos los usuarios
- **Velocidad excepcional**: No hay procesamiento, solo lectura y envío de archivos
- **Simplicidad**: Fáciles de crear y desplegar
- **Sin servidor de aplicaciones**: Solo se necesita un servidor web básico
- **Mantenimiento manual**: Cada cambio requiere editar el HTML y volver a subir

**Ventajas que aún hoy las hacen valiosas:**

- **Rendimiento óptimo**: Son las páginas más rápidas posibles
- **Seguridad**: Sin código del servidor, sin vulnerabilidades de ejecución
- **Coste mínimo**: Hosting muy económico (incluso gratuito en GitHub Pages)
- **Escalabilidad perfecta**: Sirven millones de usuarios con recursos mínimos
- **SEO excelente**: Fáciles de indexar por motores de búsqueda

**Limitaciones que motivaron la evolución:**

Sin embargo, las páginas estáticas tienen limitaciones fundamentales que rápidamente se hicieron evidentes:

- **Sin personalización**: Todos ven lo mismo
- **Sin interacción real**: No hay formularios funcionales, ni login, ni comentarios
- **Actualización tediosa**: Cambiar el contenido requiere editar archivos manualmente
- **Sin datos dinámicos**: No pueden mostrar información actualizada de bases de datos
- **Funcionalidad limitada**: No pueden ser tiendas online, redes sociales, o aplicaciones complejas

<figure markdown="span">
  ![Estático vs Dinámico](assets/what-can-be-static-or-dynamic.webp){ width="700" }
  <figcaption>Comparativa visual entre elementos que pueden ser estáticos (logo, layout, imágenes) y elementos que deben ser dinámicos (contenido de usuario, feeds personalizados, datos en tiempo real). La línea entre ambos mundos muestra dónde la web moderna necesita generar contenido al vuelo</figcaption>
</figure>

Estas limitaciones llevaron a una pregunta inevitable: **¿cómo podemos hacer que las páginas se adapten a cada usuario y situación?** La respuesta fue el desarrollo de las páginas web dinámicas.

#### 2.3. La revolución: páginas web dinámicas

A mediados de los años 90, surgió la necesidad de crear páginas que pudieran **cambiar su contenido** según diferentes factores: el usuario que las visita, la hora del día, datos almacenados en bases de datos, o las acciones del usuario.

**¿Qué es una página web dinámica?**

Una página web dinámica es aquella que **se genera en el momento** de la solicitud. El servidor no simplemente lee un archivo y lo envía; en su lugar, **ejecuta código** que construye la página HTML específicamente para esa petición.

Es como un chef que prepara cada plato al momento según las preferencias del cliente, en lugar de servir platos pre-cocinados.

**El cambio de paradigma:**

Lo revolucionario de las páginas dinámicas no es solo que el contenido cambie, sino que **se genera mediante programación**. Esto significa que el servidor ejecuta código (PHP, Python, Java, etc.) que:

1. Puede consultar bases de datos
2. Puede realizar cálculos
3. Puede tomar decisiones basadas en condiciones
4. Puede personalizar el contenido para cada usuario
5. Puede procesar datos enviados por formularios

**Ejemplo conceptual de la diferencia:**

**Página estática (todos ven lo mismo):**
```html
<h1>Bienvenido a nuestra web</h1>
<p>Últimas noticias del 15 de noviembre de 2025</p>
```

**Página dinámica (cada usuario ve contenido personalizado):**
```php
<?php
// Este código se ejecuta en el servidor
$nombreUsuario = obtenerNombreUsuarioSesion();
$fechaActual = date('d \de F \de Y');
?>

<h1>Bienvenido, <?php echo $nombreUsuario; ?></h1>
<p>Últimas noticias del <?php echo $fechaActual; ?></p>
```

**Características fundamentales de las páginas dinámicas:**

- **Contenido variable**: Diferente según usuario, hora, datos, etc.
- **Interactividad real**: Formularios funcionales, login, comentarios, búsquedas
- **Conexión con bases de datos**: Almacena y recupera información
- **Lógica de negocio**: Puede tomar decisiones y ejecutar procesos complejos
- **Actualización sencilla**: Cambiar datos en la BD actualiza automáticamente el sitio

Esta capacidad de generar contenido dinámicamente abrió las puertas a toda la web moderna que conocemos hoy: redes sociales, comercio electrónico, banca online, aplicaciones web complejas, y mucho más.

#### 2.4. Cómo funciona una página web dinámica: el proceso completo

Ahora que entendemos **por qué** necesitamos páginas dinámicas, profundicemos en **cómo** funcionan exactamente. El proceso es fascinante y es importante que lo comprendáis bien, ya que es la base de todo el desarrollo web backend.

#### 2.5. Los actores del proceso

Antes de ver el flujo completo, identifiquemos a los participantes:

**1. Cliente (Navegador)**
- El navegador del usuario que solicita la página
- Envía peticiones HTTP
- Recibe y renderiza el HTML final

**2. Servidor Web**
- Software como Apache o Nginx
- Recibe las peticiones HTTP
- Decide si la petición es para contenido estático o dinámico
- Sirve archivos estáticos directamente
- Delega páginas dinámicas al módulo correspondiente

**3. Módulo de Ejecución / Servidor de Aplicaciones**
- Ejecuta el código del lado del servidor
- Puede ser un módulo integrado (mod_php) o externo (Tomcat, Gunicorn)
- Procesa el código dinámico (PHP, Python, Java, etc.)

**4. Base de Datos**
- Almacena la información de la aplicación
- Responde a consultas del código dinámico
- MySQL, PostgreSQL, MongoDB, etc.

**5. Sistema de Archivos**
- Almacena los scripts del servidor y recursos estáticos
- El código dinámico lee archivos de plantillas, configuración, etc.

#### 2.6. El flujo completo: paso a paso

Veamos qué sucede exactamente cuando un usuario solicita una página dinámica. Imaginemos que un usuario quiere ver su perfil en una red social:

<figure markdown="span">
  ![Funcionamiento web dinámica](assets/how-dynamic-websites-work.webp){ width="700" }
  <figcaption>Diagrama del flujo completo de una petición web dinámica: el navegador solicita una página, el servidor web la recibe, el servidor de aplicaciones ejecuta el código, se consulta la base de datos, se genera el HTML dinámicamente y finalmente se envía al navegador del usuario</figcaption>
</figure>

**Paso 1: El usuario solicita la página**

```
Usuario hace clic en: https://redsocial.com/perfil/ana
```

El navegador envía una petición HTTP GET al servidor:

```http
GET /perfil/ana HTTP/1.1
Host: redsocial.com
Cookie: session_id=abc123def456
User-Agent: Mozilla/5.0 ...
```

**Paso 2: El servidor web recibe la petición**

El servidor web (por ejemplo, Apache) recibe la petición en el puerto 80 (HTTP) o 443 (HTTPS). Analiza la URL solicitada: `/perfil/ana`

El servidor web **toma una decisión**:
- Si fuera `/imagen.jpg` → Archivo estático, lo sirve directamente
- Si es `/perfil/ana` → Página dinámica, necesita procesamiento

Como es una página dinámica, el servidor web **no puede servirla directamente**. En su lugar, debe delegar la tarea.

**Paso 3: Delegación al módulo de ejecución**

El servidor web identifica qué tecnología debe manejar esta petición (basándose en la configuración y la extensión del archivo):

- Si es PHP: Llama a `mod_php` o PHP-FPM
- Si es Python: Llama a Gunicorn/uWSGI
- Si es Java: Redirige a Tomcat
- Si es Node.js: Redirige al proceso Node

El servidor web le dice al módulo: *"Ejecuta el script en /perfil/ana y dame el resultado"*

**Paso 4: El código dinámico se ejecuta**

Ahora el código del lado del servidor entra en acción. Veamos un ejemplo en PHP:

```php
<?php
// Archivo: perfil.php
session_start(); // Iniciar sesión

// 1. Obtener el nombre de usuario de la URL
$username = $_GET['usuario']; // "ana"

// 2. Verificar que el usuario está logueado
if (!isset($_SESSION['usuario_id'])) {
    header('Location: /login');
    exit();
}

// 3. Conectar a la base de datos
$db = new PDO('mysql:host=localhost;dbname=redsocial', 'user', 'pass');

// 4. Consultar información del usuario
$stmt = $db->prepare('SELECT * FROM usuarios WHERE username = ?');
$stmt->execute([$username]);
$usuario = $stmt->fetch();

// 5. Si el usuario no existe, mostrar error
if (!$usuario) {
    http_response_code(404);
    echo "Usuario no encontrado";
    exit();
}

// 6. Consultar las publicaciones del usuario
$stmt = $db->prepare('SELECT * FROM posts WHERE usuario_id = ? ORDER BY fecha DESC LIMIT 10');
$stmt->execute([$usuario['id']]);
$posts = $stmt->fetchAll();

// 7. Generar el HTML dinámicamente
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Perfil de <?php echo htmlspecialchars($usuario['nombre']); ?></title>
    <link rel="stylesheet" href="/css/estilos.css">
</head>
<body>
    <header>
        <h1>Red Social</h1>
        <nav>
            <a href="/inicio">Inicio</a>
            <a href="/perfil/<?php echo $_SESSION['username']; ?>">Mi Perfil</a>
            <a href="/logout">Salir</a>
        </nav>
    </header>
    
    <main>
        <div class="perfil">
            <img src="<?php echo htmlspecialchars($usuario['foto_perfil']); ?>" 
                 alt="Foto de perfil">
            <h2><?php echo htmlspecialchars($usuario['nombre']); ?></h2>
            <p><?php echo htmlspecialchars($usuario['bio']); ?></p>
            <p>Miembro desde: <?php echo date('d/m/Y', strtotime($usuario['fecha_registro'])); ?></p>
        </div>
        
        <section class="publicaciones">
            <h3>Publicaciones recientes</h3>
            <?php foreach ($posts as $post): ?>
                <article class="post">
                    <p><?php echo htmlspecialchars($post['contenido']); ?></p>
                    <small>Publicado el <?php echo date('d/m/Y H:i', strtotime($post['fecha'])); ?></small>
                </article>
            <?php endforeach; ?>
            
            <?php if (count($posts) == 0): ?>
                <p>Este usuario aún no ha publicado nada.</p>
            <?php endif; ?>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2025 Red Social</p>
    </footer>
</body>
</html>
```

**Lo que acaba de suceder es extraordinario:**

El servidor ha **construido una página HTML única** para esta petición específica:
- Verificó la sesión del usuario
- Consultó la base de datos para obtener información de "ana"
- Obtuvo sus publicaciones recientes
- Generó HTML personalizado con toda esa información
- Incluyó la fecha actual formateada
- Aplicó lógica condicional (si no hay posts, muestra un mensaje diferente)

**Paso 5: Consultas a la base de datos**

Durante la ejecución del código, se realizaron varias consultas SQL:

```sql
-- Primera consulta: obtener datos del usuario
SELECT * FROM usuarios WHERE username = 'ana';

-- Segunda consulta: obtener publicaciones
SELECT * FROM posts WHERE usuario_id = 42 ORDER BY fecha DESC LIMIT 10;
```

La base de datos busca en sus tablas, recupera los datos y los devuelve al código PHP. Estas operaciones pueden tomar desde milisegundos hasta segundos, dependiendo de:
- La complejidad de las consultas
- El tamaño de las tablas
- Los índices definidos
- La carga del servidor de base de datos

**Paso 6: Generación del HTML final**

El código PHP ha mezclado:
- **HTML estático**: Estructura básica, estilos, navegación
- **Datos de la base de datos**: Nombre, bio, publicaciones de Ana
- **Lógica condicional**: Mostrar u ocultar elementos según condiciones
- **Datos de sesión**: Identificar al usuario logueado
- **Fecha actual**: Generada en el momento

El resultado es un **documento HTML completo** listo para enviar al navegador.

**Paso 7: El servidor web envía la respuesta**

El módulo PHP devuelve el HTML generado al servidor web (Apache), que construye la respuesta HTTP completa:

```http
HTTP/1.1 200 OK
Date: Tue, 19 Nov 2025 19:30:00 GMT
Server: Apache/2.4.41
Content-Type: text/html; charset=utf-8
Content-Length: 2847
Set-Cookie: session_id=abc123def456; Path=/; HttpOnly

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Perfil de Ana García</title>
    ...
```

**Paso 8: El navegador recibe y renderiza**

El navegador del usuario recibe esta respuesta HTTP. Para el navegador, **no hay diferencia** entre una página estática y una dinámica: ambas llegan como HTML.

El navegador:
1. Parsea el HTML
2. Construye el DOM
3. Descarga CSS y JavaScript referenciados
4. Descarga imágenes
5. Renderiza la página visualmente
6. Ejecuta JavaScript del lado del cliente

El usuario ve su página personalizada, ¡sin saber todo el proceso que acaba de ocurrir!

#### 2.7. Diferencias clave en el tiempo de respuesta

Es importante entender que las páginas dinámicas son **más lentas** que las estáticas, pero esta "lentitud" es el precio de la funcionalidad:

**Página estática:**
```
Petición → Leer archivo del disco → Enviar
Tiempo típico: 5-20 ms
```

**Página dinámica:**
```
Petición → Ejecutar código → Consultar BD → Generar HTML → Enviar
Tiempo típico: 50-500 ms (o más si las consultas son complejas)
```

Sin embargo, esta diferencia es **totalmente aceptable** porque:
- Los usuarios esperan algo de delay para operaciones complejas
- Se pueden aplicar técnicas de caché
- El hardware moderno es muy rápido
- La funcionalidad obtenida justifica ampliamente el coste

!!! note "Optimización es clave"
    Aunque las páginas dinámicas son más lentas, un buen desarrollador debe optimizar:
    - Consultas SQL eficientes con índices
    - Caché de resultados frecuentes
    - Código eficiente sin operaciones innecesarias
    - Uso de CDN para recursos estáticos
    - Técnicas como lazy loading

#### 2.8. Tecnologías de generación de páginas web dinámicas

Ahora que comprendemos el proceso, exploremos las **tecnologías** que hacen posible la generación dinámica de contenido. A lo largo de la historia de la web, han surgido múltiples lenguajes y frameworks, cada uno con sus fortalezas y casos de uso ideales.

#### 2.9. Panorama general de tecnologías

El desarrollo web del lado del servidor ha evolucionado enormemente, pero todos los enfoques comparten el mismo objetivo fundamental: **ejecutar código en el servidor que genera HTML dinámicamente**.

Las principales familias de tecnologías son:

**1. PHP**: El lenguaje más popular de la web, presente en WordPress, Facebook inicial, Wikipedia
**2. Python**: Con frameworks como Django y Flask, usado por Instagram, Spotify
**3. Java**: Robusto y empresarial, con JSP, Servlets, Spring Boot
**4. JavaScript/Node.js**: JavaScript en el servidor, usado por Netflix, LinkedIn
**5. Ruby**: Con Ruby on Rails, usado por GitHub, Shopify
**6. C#/ASP.NET**: De Microsoft, popular en entornos empresariales Windows

Cada una de estas tecnologías representa una forma diferente de resolver el mismo problema, y la elección depende de múltiples factores: el equipo de desarrollo, los requisitos del proyecto, el ecosistema de librerías, y las preferencias personales.

#### 2.10. PHP: el lenguaje que construyó la web

PHP (Hypertext Preprocessor) es, sin lugar a dudas, el lenguaje más ubicuo en el desarrollo web. A pesar de las críticas que a veces recibe, PHP sigue siendo el motor detrás de una parte masiva de Internet.

**¿Por qué PHP tuvo tanto éxito?**

PHP fue diseñado específicamente para la web desde su creación en 1995. Su propuesta era simple: permitir a los desarrolladores **incrustar código directamente en HTML**. Esta simplicidad lo hizo extremadamente accesible.

**Ejemplo "Hola Mundo" en PHP:**

```php
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ejemplo PHP</title>
</head>
<body>
    <h1>Hola Mundo desde PHP</h1>
    
    <?php
    // Todo el código entre <?php y ?> se ejecuta en el servidor
    $nombre = "Estudiante";
    $hora = date('H');
    
    // Saludo personalizado según la hora
    if ($hora < 12) {
        $saludo = "Buenos días";
    } elseif ($hora < 20) {
        $saludo = "Buenas tardes";
    } else {
        $saludo = "Buenas noches";
    }
    
    echo "<p>$saludo, $nombre! Son las " . date('H:i') . "</p>";
    ?>
    
    <h2>Lista dinámica</h2>
    <ul>
    <?php
    $lenguajes = ['PHP', 'Python', 'JavaScript', 'Java', 'Ruby'];
    foreach ($lenguajes as $index => $lenguaje) {
        echo "<li>Lenguaje #" . ($index + 1) . ": $lenguaje</li>";
    }
    ?>
    </ul>
    
    <?php
    // Conectar a base de datos
    $db = new PDO('mysql:host=localhost;dbname=ejemplo', 'user', 'pass');
    $usuarios = $db->query('SELECT nombre FROM usuarios LIMIT 5')->fetchAll();
    ?>
    
    <h2>Usuarios registrados</h2>
    <ul>
    <?php foreach ($usuarios as $usuario): ?>
        <li><?php echo htmlspecialchars($usuario['nombre']); ?></li>
    <?php endforeach; ?>
    </ul>
</body>
</html>
```

**Frameworks PHP modernos:**

Aunque PHP puro es poderoso, los frameworks modernos añaden estructura y mejores prácticas:

**Laravel** - El framework PHP más popular actualmente:
```php
// routes/web.php
Route::get('/perfil/{username}', function ($username) {
    $usuario = Usuario::where('username', $username)->firstOrFail();
    return view('perfil', ['usuario' => $usuario]);
});

// resources/views/perfil.blade.php
<!DOCTYPE html>
<html>
<head>
    <title>Perfil de {{ $usuario->nombre }}</title>
</head>
<body>
    <h1>{{ $usuario->nombre }}</h1>
    <p>{{ $usuario->bio }}</p>
    
    @if($usuario->posts->count() > 0)
        <h2>Publicaciones</h2>
        @foreach($usuario->posts as $post)
            <article>
                <p>{{ $post->contenido }}</p>
                <small>{{ $post->created_at->diffForHumans() }}</small>
            </article>
        @endforeach
    @else
        <p>Sin publicaciones aún.</p>
    @endif
</body>
</html>
```

Laravel proporciona: ORM (Eloquent), sistema de plantillas (Blade), routing, autenticación, y mucho más.

**Ventajas de PHP:**
- Hosting económico y universal
- Curva de aprendizaje suave
- Enorme ecosistema (WordPress, Laravel, Symfony)
- Documentación exhaustiva
- Gran comunidad

**Desventajas:**
- Inconsistencias históricas en el lenguaje
- Rendimiento inferior a lenguajes compilados
- Algunas prácticas antiguas persisten

#### 2.11. Python: elegancia y versatilidad

Python se ha convertido en uno de los lenguajes más queridos para desarrollo web, especialmente con frameworks como Django y Flask.

**Django** - El framework "batteries included":

```python
# models.py
from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    bio = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Post(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='posts')
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Usuario

def perfil(request, username):
    usuario = get_object_or_404(Usuario, username=username)
    posts = usuario.posts.all().order_by('-fecha')[:10]
    
    context = {
        'usuario': usuario,
        'posts': posts
    }
    
    return render(request, 'perfil.html', context)

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('perfil/<str:username>/', views.perfil, name='perfil'),
]
```

```django
<!-- templates/perfil.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Perfil de {{ usuario.nombre }}</title>
</head>
<body>
    <h1>{{ usuario.nombre }}</h1>
    <p>@{{ usuario.username }}</p>
    <p>{{ usuario.bio }}</p>
    <p>Miembro desde: {{ usuario.fecha_registro|date:"d/m/Y" }}</p>
    
    <h2>Publicaciones</h2>
    {% if posts %}
        {% for post in posts %}
            <article>
                <p>{{ post.contenido }}</p>
                <small>{{ post.fecha|timesince }} atrás</small>
            </article>
        {% endfor %}
    {% else %}
        <p>Sin publicaciones todavía.</p>
    {% endif %}
</body>
</html>
```

**Flask** - El microframework minimalista:

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///redsocial.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    nombre = db.Column(db.String(100))
    bio = db.Column(db.Text)

@app.route('/perfil/<username>')
def perfil(username):
    usuario = Usuario.query.filter_by(username=username).first_or_404()
    posts = usuario.posts.order_by(Post.fecha.desc()).limit(10).all()
    return render_template('perfil.html', usuario=usuario, posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
```

**Ventajas de Python:**
- Sintaxis limpia y legible
- Excelente para aplicaciones complejas
- Fuerte en machine learning e IA
- Gran ecosistema científico

**Desventajas:**
- Hosting menos común que PHP
- Rendimiento (aunque mejora con PyPy)
- Global Interpreter Lock (GIL) limita concurrencia

#### 2.12. Java: robustez empresarial

Java ha sido durante décadas la opción preferida para aplicaciones empresariales de gran escala.

**JSP (JavaServer Pages)** - El enfoque clásico:

```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="com.ejemplo.modelo.Usuario, java.util.List" %>
<!DOCTYPE html>
<html>
<head>
    <title>Ejemplo JSP</title>
</head>
<body>
    <h1>Hola Mundo desde JSP</h1>
    
    <%
        String nombre = "Estudiante";
        int hora = java.time.LocalTime.now().getHour();
        String saludo;
        
        if (hora < 12) {
            saludo = "Buenos días";
        } else if (hora < 20) {
            saludo = "Buenas tardes";
        } else {
            saludo = "Buenas noches";
        }
    %>
    
    <p><%= saludo %>, <%= nombre %>!</p>
    
    <h2>Lista dinámica</h2>
    <ul>
    <%
        String[] lenguajes = {"Java", "Python", "JavaScript", "Ruby", "Go"};
        for (int i = 0; i < lenguajes.length; i++) {
            out.println("<li>Lenguaje #" + (i+1) + ": " + lenguajes[i] + "</li>");
        }
    %>
    </ul>
</body>
</html>
```

**Spring Boot** - El framework moderno:

```java
// Modelo
@Entity
public class Usuario {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String username;
    private String nombre;
    private String bio;
    
    @OneToMany(mappedBy = "usuario")
    private List<Post> posts;
    
    // Getters y setters...
}

// Controlador
@Controller
public class PerfilController {
    
    @Autowired
    private UsuarioRepository usuarioRepo;
    
    @GetMapping("/perfil/{username}")
    public String perfil(@PathVariable String username, Model model) {
        Usuario usuario = usuarioRepo.findByUsername(username)
                .orElseThrow(() -> new UsuarioNoEncontradoException());
        
        List<Post> posts = usuario.getPosts().stream()
                .sorted(Comparator.comparing(Post::getFecha).reversed())
                .limit(10)
                .collect(Collectors.toList());
        
        model.addAttribute("usuario", usuario);
        model.addAttribute("posts", posts);
        
        return "perfil";
    }
}
```

```html
<!-- perfil.html con Thymeleaf -->
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title th:text="${usuario.nombre}">Perfil</title>
</head>
<body>
    <h1 th:text="${usuario.nombre}">Nombre</h1>
    <p th:text="${usuario.bio}">Biografía</p>
    
    <h2>Publicaciones</h2>
    <div th:if="${#lists.isEmpty(posts)}">
        <p>Sin publicaciones.</p>
    </div>
    <div th:each="post : ${posts}">
        <article>
            <p th:text="${post.contenido}"></p>
            <small th:text="${#temporals.format(post.fecha, 'dd/MM/yyyy HH:mm')}"></small>
        </article>
    </div>
</body>
</html>
```

**Ventajas de Java:**
- Rendimiento excelente
- Tipado fuerte previene errores
- Ideal para aplicaciones grandes
- Ecosistema empresarial maduro

**Desventajas:**
- Verbosidad del código
- Curva de aprendizaje pronunciada
- Configuración compleja (aunque Spring Boot mejora esto)

#### 2.13. Node.js: JavaScript en todas partes

Node.js revolucionó el desarrollo web al permitir usar JavaScript tanto en el frontend como en el backend.

**Express.js** - El framework minimalista:

```javascript
const express = require('express');
const { sequelize, Usuario, Post } = require('./models');
const app = express();

// Motor de plantillas
app.set('view engine', 'ejs');

// Ruta del perfil
app.get('/perfil/:username', async (req, res) => {
    try {
        const usuario = await Usuario.findOne({
            where: { username: req.params.username },
            include: [{
                model: Post,
                limit: 10,
                order: [['fecha', 'DESC']]
            }]
        });
        
        if (!usuario) {
            return res.status(404).send('Usuario no encontrado');
        }
        
        res.render('perfil', { usuario });
    } catch (error) {
        console.error(error);
        res.status(500).send('Error del servidor');
    }
});

app.listen(3000, () => {
    console.log('Servidor escuchando en puerto 3000');
});
```

```html
<!-- views/perfil.ejs -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Perfil de <%= usuario.nombre %></title>
</head>
<body>
    <h1><%= usuario.nombre %></h1>
    <p>@<%= usuario.username %></p>
    <p><%= usuario.bio %></p>
    
    <h2>Publicaciones</h2>
    <% if (usuario.Posts && usuario.Posts.length > 0) { %>
        <% usuario.Posts.forEach(post => { %>
            <article>
                <p><%= post.contenido %></p>
                <small><%= new Date(post.fecha).toLocaleString() %></small>
            </article>
        <% }); %>
    <% } else { %>
        <p>Sin publicaciones aún.</p>
    <% } %>
</body>
</html>
```

**Ventajas de Node.js:**
- Un solo lenguaje (JavaScript) para todo
- Excelente para I/O intensivo
- NPM: el mayor ecosistema de paquetes
- Ideal para aplicaciones en tiempo real

**Desventajas:**
- Single-threaded (aunque asíncrono)
- JavaScript puede ser propenso a errores
- Menos maduro para aplicaciones empresariales tradicionales

#### 2.14. Tabla comparativa de tecnologías

| Tecnología   | Lenguaje   | Framework Popular | Paradigma           | Ventaja Principal        | Ideal Para                 |
|:-------------|:-----------|:------------------|:--------------------|:-------------------------|:---------------------------|
| **PHP**      | PHP        | Laravel           | Código embebido/MVC | Hosting universal        | Blogs, CMS, e-commerce     |
| **Python**   | Python     | Django, Flask     | MVC                 | Elegancia y versatilidad | Aplicaciones complejas, ML |
| **Java**     | Java       | Spring Boot       | MVC                 | Robustez empresarial     | Grandes empresas, banca    |
| **Node.js**  | JavaScript | Express           | Event-driven        | JavaScript everywhere    | APIs, tiempo real          |
| **Ruby**     | Ruby       | Rails             | MVC                 | Productividad dev        | Startups, MVPs             |
| **C#**       | C#         | ASP.NET Core      | MVC                 | Integración Microsoft    | Entornos Windows           |




Hasta ahora hemos explorado la diferencia fundamental entre contenido estático y dinámico, y las tecnologías que permiten generar páginas web dinámicas. Sin embargo, en el ecosistema web actual existe otra distinción crucial que debemos comprender: **la diferencia entre páginas web tradicionales, aplicaciones web y Progressive Web Apps**. Esta clasificación nos ayuda a entender mejor el espectro completo de experiencias que podemos crear en la web moderna.

#### 2.15. Página Web tradicional

Una **página web** es principalmente un documento de información que se visualiza en un navegador.

**Características:**

- **Contenido estático o poco dinámico**: El contenido cambia poco o nada
- **Interacción limitada**: Principalmente lectura de información
- **Navegación basada en páginas**: Cada clic carga una página nueva
- **Recarga completa**: Cada acción recarga toda la página
- **Enfoque en contenido**: Prioriza la presentación de información

**Ejemplos típicos:**

- Blogs personales
- Sitios web corporativos informativos
- Páginas de noticias simples
- Portafolios
- Documentación estática

**Tecnologías típicas:**

- HTML + CSS + JavaScript mínimo
- Generadores de sitios estáticos (Jekyll, Hugo)
- CMS simples (WordPress para blogs)

#### 2.16. Aplicación Web (Web App)

Una **aplicación web** es un software completo que se ejecuta en el navegador y proporciona funcionalidades complejas.

**Características:**

- **Contenido dinámico**: Cambia constantemente según las acciones del usuario
- **Alta interactividad**: El usuario puede realizar muchas acciones
- **Single Page Application (SPA)**: No recarga la página, solo actualiza partes
- **Estado de sesión**: Mantiene información del usuario durante su uso
- **Lógica compleja**: Realiza operaciones sofisticadas
- **Experiencia similar a app nativa**: Se comporta como software de escritorio

**Ejemplos típicos:**

- Gmail (cliente de correo)
- Google Maps (mapas interactivos)
- Netflix (streaming de video)
- Trello (gestión de proyectos)
- Figma (diseño colaborativo)
- Spotify Web (reproducción de música)

**Tecnologías típicas:**

- **Frontend**: React, Angular, Vue.js
- **Backend**: Node.js, Python/Django, Java/Spring
- **Base de datos**: PostgreSQL, MongoDB, MySQL
- **APIs RESTful o GraphQL**
- **WebSockets** para comunicación en tiempo real

#### 2.17. Progressive Web Apps (PWA)

Las **PWA** son aplicaciones web que incorporan características de aplicaciones nativas:

- **Instalables**: Se pueden "instalar" en el dispositivo
- **Funcionamiento offline**: Trabajan sin conexión gracias a Service Workers
- **Notificaciones push**: Pueden enviar notificaciones al usuario
- **Acceso a hardware**: Cámara, geolocalización, etc.
- **Responsive**: Se adaptan a cualquier tamaño de pantalla
- **Rápidas**: Carga optimizada y experiencia fluida

**Ventajas de las PWA:**

- No requieren instalación desde tiendas de apps
- Actualizaciones automáticas
- Menor consumo de recursos que apps nativas
- Una sola base de código para todas las plataformas
- Descubribles por motores de búsqueda

!!! tip "El futuro son las aplicaciones web"
    La tendencia actual es que cada vez más servicios se ofrecen como aplicaciones web en lugar de software tradicional. Esto facilita el acceso, las actualizaciones y reduce costes de desarrollo y mantenimiento.

#### 2.18. Tabla comparativa

| Aspecto               | Página Web            | Aplicación Web             | PWA                        |
|:----------------------|:----------------------|:---------------------------|:---------------------------|
| **Objetivo**          | Informar              | Proporcionar funcionalidad | Combinar lo mejor de ambas |
| **Interactividad**    | Baja                  | Alta                       | Alta                       |
| **Complejidad**       | Baja                  | Alta                       | Media-Alta                 |
| **Recarga de página** | Completa              | Parcial/Ninguna            | Parcial/Ninguna            |
| **Estado de sesión**  | Mínimo                | Complejo                   | Complejo                   |
| **Offline**           | No                    | Limitado                   | Sí                         |
| **Instalable**        | No                    | No                         | Sí                         |
| **Experiencia**       | Documento             | Aplicación                 | App nativa                 |
| **Ejemplos**          | Blog, web corporativa | Gmail, Trello              | Twitter Lite, Pinterest    |




---

## BLOQUE 2: COMPONENTES Y ARQUITECTURA

Con una comprensión sólida de HTTP y la diferencia entre contenido estático y dinámico, es momento de entender **cómo se estructuran las aplicaciones web modernas**. Ya no basta con generar HTML; necesitamos organizar nuestro código de forma que sea mantenible, escalable y robusto. En este bloque exploraremos cómo se dividen las responsabilidades entre cliente y servidor, qué arquitecturas de software existen, y qué patrones de diseño nos ayudan a escribir código de calidad.


### 3. Componentes de ejecución de código en el servidor y en el cliente

La lógica de una aplicación web se divide y ejecuta en dos entornos principales, cada uno con responsabilidades específicas: el lado del cliente y el lado del servidor. Entender esta división es fundamental para comprender cómo funcionan las aplicaciones web modernas.

#### 3.1. Código en el lado del cliente (Frontend)

El **código que se ejecuta en el lado del cliente** opera en el navegador web del usuario. Es lo que tradicionalmente conocemos como **Frontend**.

**Tecnologías principales:**

- **HTML (HyperText Markup Language)**: Define la estructura y el contenido de las páginas web
- **CSS (Cascading Style Sheets)**: Controla la presentación, el diseño y los estilos visuales
- **JavaScript**: Añade interactividad y lógica dinámica que se ejecuta en el navegador

**Responsabilidades del código cliente:**

- **Presentación visual**: Renderizar la interfaz de usuario que ve el usuario
- **Interactividad**: Responder a las acciones del usuario (clics, desplazamientos, entrada de texto)
- **Validación preliminar**: Comprobar datos antes de enviarlos al servidor
- **Manipulación del DOM**: Modificar dinámicamente el contenido de la página sin recargarla
- **Comunicación asíncrona**: Realizar peticiones al servidor en segundo plano (AJAX, Fetch API)

**Ventajas de la ejecución en el cliente:**

- **Respuesta inmediata**: No necesita comunicación con el servidor para acciones simples
- **Reducción de carga del servidor**: El navegador hace parte del trabajo
- **Mejor experiencia de usuario**: Interacciones fluidas y rápidas
- **Funcionamiento offline**: Algunas funcionalidades pueden trabajar sin conexión

**Limitaciones:**

- **Seguridad**: El código es visible y puede ser manipulado por el usuario
- **Recursos limitados**: Depende de la capacidad del dispositivo del usuario
- **Compatibilidad**: Debe funcionar en diferentes navegadores y versiones

!!! warning "Nunca confiar en el cliente"
    Es fundamental entender que **nunca se debe confiar completamente en las validaciones del lado del cliente**. Un usuario malintencionado puede desactivar JavaScript o manipular el código. Las validaciones críticas siempre deben realizarse también en el servidor.

#### 3.2. Código en el lado del servidor (Backend)

El **código que se ejecuta en el lado del servidor** corre en un servidor web o de aplicaciones. Es lo que conocemos como **Backend**.

**Lenguajes más utilizados:**

- **PHP**: Ampliamente utilizado, especialmente en WordPress y Laravel
- **Python**: Con frameworks como Django y Flask
- **Java**: Con Spring Boot, muy usado en empresas
- **JavaScript/Node.js**: Permite usar JavaScript tanto en cliente como en servidor
- **Ruby**: Con el framework Ruby on Rails
- **C#**: Con ASP.NET Core
- **Go**: Creciente popularidad por su rendimiento

**Responsabilidades del código servidor:**

- **Lógica de negocio**: Implementar las reglas y procesos del negocio
- **Acceso a datos**: Interactuar con bases de datos para leer y escribir información
- **Autenticación y autorización**: Verificar identidades y permisos de usuarios
- **Procesamiento de datos**: Realizar cálculos complejos y transformaciones
- **Generación de contenido dinámico**: Crear respuestas personalizadas para cada usuario
- **Integración con servicios externos**: Comunicarse con APIs de terceros
- **Seguridad**: Proteger datos sensibles y validar todas las entradas

**Ventajas de la ejecución en el servidor:**

- **Seguridad**: El código y la lógica no son visibles para el usuario
- **Control total**: Podemos confiar en que el código se ejecuta como esperamos
- **Recursos potentes**: Acceso a toda la capacidad del servidor
- **Centralización**: Facilita actualizaciones y mantenimiento
- **Persistencia**: Acceso directo a bases de datos y almacenamiento

#### 3.3. Colaboración entre cliente y servidor

Ambos modelos trabajan en conjunto para proporcionar una experiencia completa:

1. **El cliente realiza una petición** al servidor (por ejemplo, el usuario hace clic en "Enviar")

2. **El servidor procesa la petición**
    
    - Valida los datos recibidos
    - Ejecuta la lógica de negocio necesaria
    - Accede a la base de datos si es necesario
    - Prepara la respuesta
    
3. **El servidor envía la respuesta** al cliente

4. **El cliente recibe y procesa la respuesta**
    
    - Actualiza la interfaz de usuario
    - Muestra mensajes de confirmación o error
    - Puede hacer más peticiones si es necesario

<figure markdown="span">
  ![Anatomía de una aplicación web](assets/anatomia_web.gif){ width="700" }
  <figcaption>Flujo de comunicación en una aplicación web: el navegador (cliente) realiza peticiones al servidor, que procesa la información y devuelve respuestas. El diagrama muestra cómo interactúan las diferentes capas de la aplicación.</figcaption>
</figure>

!!! info "Responsabilidades compartidas: cliente vs servidor"
    Voy a explicarla como si estuviéramos montando una app web paso a paso, usando la imagen anterior como mapa.
    **0. Visión general**
    
    La imagen se titula **“Anatomía de una App Web moderna”** y muestra las piezas típicas:
    
    * **FrontEnd** → lo que ve el usuario.

        * **BackEnd** → la lógica y las reglas de negocio.
        * **Base de datos** → la memoria de la aplicación.
        * **CI/CD** → la automatización para construir, testear y desplegar.
        * **Alojamiento / Cloud** → dónde vive todo eso (los servidores).
    
    Y todo ello conectado principalmente a través de una **API**.
    
    Te lo cuento siguiendo un flujo lógico:
    👨‍💻 desarrollador → CI/CD → nube → usuario → FrontEnd → API → BackEnd → Base de datos → respuesta.
    
      
    **1. FrontEnd – “Lo que ves”**
    
    Bloque verde de la izquierda.
    
    Es la parte de la aplicación que se ejecuta en el **navegador del usuario**:
    
    * Tecnologías básicas:
        
        * **HTML** → estructura del contenido.
        * **CSS** → estilos, colores, maquetación.
        * **JavaScript** → interactividad, llamadas a APIs, etc.
    
    * Frameworks de FrontEnd (los iconos de la imagen):
        
        * **Angular**
        * **React**
        * **Vue**
    
    Estos frameworks ayudan a:
    
    * Organizar la interfaz en **componentes**.

        * Gestionar **rutas**, **estados**, formularios, validaciones…
        * Consumir la **API** del backend (peticiones HTTP/JSON).
    
    💡 Idea clave:
    El FrontEnd **no suele guardar datos importantes** ni tener la lógica “seria” de negocio.
    Su misión es:
    
    1. Mostrar información de forma agradable.
    2. Enviar peticiones al BackEnd por la API.
    3. Representar lo que venga del servidor.
    
    **2. BackEnd – “La lógica"**
    
    Bloque azul de la derecha.
    
    Es el código que se ejecuta en el **servidor**:
    
    * Lenguajes típicos de backend que aparecen:
        
        * **Node.js**
        * **Python**
        * **Java**
        * **Go**
        * **C# / .NET**
    
    * Frameworks que se ven en los logos:
        
        * Para Node.js → **Express (ex)**, **Nest**, etc.
        * Para Python → **Django**, **Flask**, …
        * Para C# → **.NET Core**
        * Para Go → frameworks ligeros (por ejemplo **Fiber**).
    
    Funciones del BackEnd:
    
    1. **Exponer una API** (normalmente REST o GraphQL):
        
        * Endpoints tipo `GET /api/usuarios`, `POST /api/login`, etc.

    2. **Aplicar reglas de negocio**:
       
        * “Un usuario no puede comprar si no está autenticado”.
        * “No puedes aplicar este descuento si ya se ha usado”.

    3. **Hablar con la base de datos**:
        
        * Leer, insertar, actualizar y borrar registros.

    4. **Gestionar seguridad**:
      
        * Autenticación, autorización, control de permisos.

    5. **Integrarse con otros servicios**:
     
        * Pasarelas de pago, servicios de correo, colas de mensajes, etc.
    
    💡 Idea clave:
    El BackEnd es el “cerebro” de la app.
    El FrontEnd le pregunta *“¿Puedo hacer esto?”* y el BackEnd decide **cómo** y **si** se hace.

    **3. Base de datos – “La memoria"****
    
    Bloque amarillo de la parte derecha inferior.
    
    Es donde se guardan los datos **persistentes**:
    
    * Tipos:
        
        * **SQL** (relacionales): tablas, filas, columnas, claves.
        * **NoSQL** (documentos, key-value, grafos, etc.).
    
    * Motores que aparecen:
        
        * Relacionales: **Oracle**, **MySQL**, **PostgreSQL**, **SQL Server**…
        * NoSQL (iconos tipo MongoDB, etc.).
    
    Funciones:
    
    * Guardar:
        
        * usuarios, pedidos, productos, posts, logs…
    * Permitir consultas:
        
        * “Dame todos los pedidos del usuario X”.

    * Mantener la integridad:
        
        * claves primarias, foráneas, restricciones, etc.
    
    En la imagen, las flechas muestran que **el BackEnd habla con la base de datos** (el FrontEnd nunca la toca directamente).
    
    💡 Idea clave: 
    Base de datos = **memoria a largo plazo** de la app.
    Si apagas el servidor pero la BD sigue, los datos permanecen.
     
    **4. La API – El pegamento entre FrontEnd y BackEnd**
    
    En el centro, las líneas de puntos indican la **API**.
    
    La API define **cómo se comunican** FrontEnd y BackEnd:
    
    * Formato habitual:

        * Peticiones **HTTP** con respuestas en **JSON**.

    * Ejemplos:
        
        * `GET /api/productos`
        * `POST /api/usuarios`
        * `PUT /api/pedidos/123`
    
    Flujo típico en ejecución:
    
    1. El usuario hace clic en un botón en el FrontEnd.
    2. El FrontEnd manda una petición a la **API del BackEnd**.
    3. El BackEnd procesa, consulta la BD si hace falta y devuelve un JSON.
    4. El FrontEnd actualiza la interfaz con esa información.
    
    💡 La API actúa como **contrato**:
    > “Si me llamas así, con estos parámetros, te devolveré esto”.
     
    **5. CI/CD – “La automatización”**
    
    Bloque circular gris de abajo a la izquierda.
    
    **CI/CD** = Integración Continua / Despliegue Continuo.
    
    Su misión es **automatizar el ciclo de vida del código** desde que el desarrollador hace un commit hasta que el código llega a producción.
    
    En la imagen se ve el flujo:
    
    1. **Commit**
        
        * El desarrollador sube código al repositorio (GitHub, GitLab, etc.).

    2. **Build**
        
        * Se compila el proyecto, se generan artefactos (por ejemplo, un `.jar`, una imagen Docker…).

    3. **Test**
        
        * Se ejecutan tests automáticos (unitarios, integración, etc.).

    4. **Artifact**
        
        * Se guarda el resultado listo para desplegar (en un registry, repositorio de artefactos…).

    5. **Deploy**
        
        * Se despliega automáticamente al entorno correspondiente (staging, producción…).

    6. **Monitoring**
        
        * Se monitoriza la app: logs, métricas, alertas.
    
    Herramientas que aparecen como iconos:
    
    * **Jenkins**

        * **GitLab CI**
        * **AWS CodePipeline**
        * **Argo**, etc.
    
    💡 Idea clave:
    CI/CD es el “**cinturón de montaje**” de tu aplicación.
    Te evita hacer deploys a mano y minimiza errores humanos.
    
    **6. Alojamiento / Cloud Service Provider – “El hogar”**
    
    En la parte inferior, los logos de:
    
    * **AWS**

        * **Google Cloud**
        * **Azure**
        * **IBM Cloud**
        * **Oracle Cloud**
        * **Alibaba Cloud**
    
    Estos proveedores ofrecen:
    
    * Máquinas virtuales, contenedores, Kubernetes…
    * Bases de datos gestionadas.
    * Balanceadores de carga.
    * Almacenamiento, CDN, etc.
    
    En la imagen se da a entender que:
    
    * Tu **FrontEnd**, tu **BackEnd** y tu **Base de datos** viven en alguno de estos proveedores de nube.
    * El pipeline de **CI/CD** despliega directamente ahí.
    
   
    **7. Poniéndolo todo junto: flujo completo**
    
    Imagina ahora el flujo end-to-end usando todos los bloques:
    
    1. 👨‍💻 **Desarrollo y CI/CD**
        
        * Tú desarrollas FrontEnd y BackEnd en tu equipo.
        * Haces un **commit**.
        * El pipeline de **CI/CD**:
            
            * construye el código,
            * ejecuta tests,
            * genera artefactos,
            * despliega FrontEnd + BackEnd + cambios de BD en la **nube** (AWS, Azure, etc.).
    
    2. ☁️ **Infraestructura en la nube**
        
        * El FrontEnd se sirve, por ejemplo, desde un bucket estático o un servidor web.
        * El BackEnd corre en contenedores, VMs o funciones serverless.
        * La Base de datos está en un servicio gestionado.
    
    3. 🌐 **Uso por parte del usuario**
        
        * El usuario abre el navegador y carga el **FrontEnd**.
        * El FrontEnd (HTML, CSS, JS) se muestra en pantalla.
        * Cuando el usuario interactúa:
            
            1. El FrontEnd llama a la **API**.
            2. La API llega al **BackEnd**.
            3. El BackEnd aplica reglas de negocio y consulta la **Base de datos**.
            4. El BackEnd devuelve un JSON al FrontEnd.
            5. El FrontEnd actualiza la vista.
    
    4. 🔁 **Ciclo continuo**
        
        * Encuentras un bug o quieres una nueva funcionalidad.
        * Modificas código → commit → CI/CD → nuevo deploy.
        * El usuario recibe la versión actualizada, casi sin darse cuenta.
    
    
    **8. Resumen rápido “para llevar”**
    
    * **FrontEnd**: lo que ve el usuario (HTML + CSS + JS, Angular/React/Vue).
    * **BackEnd**: la lógica y la API (Node, Python, Java, Django, .NET…).
    * **Base de datos**: la memoria (SQL/NoSQL: Oracle, MySQL, PostgreSQL, Mongo…).
    * **API**: el contrato entre FrontEnd y BackEnd.
    * **CI/CD**: la cadena de montaje que lleva tu código desde el commit hasta producción.
    * **Cloud**: la casa donde viven todas estas piezas.
    
    Si piensas en la app como una ciudad:
    
    * FrontEnd sería la fachada y las calles,
    * BackEnd la administración y las normas,
    * Base de datos el archivo municipal,
    * CI/CD las obras públicas que actualizan la ciudad sin cortarte siempre la calle,
    * y la nube… el terreno sobre el que está construida.


**Ejemplo práctico: formulario de login**

Veamos cómo se reparten las responsabilidades en un caso real:

**En el cliente (navegador):**
```javascript
// Validación preliminar en JavaScript
function validarFormulario() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    // Validación básica de formato
    if (email.length === 0) {
        alert('El email no puede estar vacío');
        return false;
    }
    
    if (password.length < 8) {
        alert('La contraseña debe tener al menos 8 caracteres');
        return false;
    }
    
    return true; // Permite enviar al servidor
}
```

**En el servidor (PHP):**
```php
<?php
// Validación y procesamiento en el servidor
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $_POST['email'];
    $password = $_POST['password'];
    
    // VALIDAR DE NUEVO en el servidor (¡crítico!)
    if (empty($email) || empty($password)) {
        die('Datos incompletos');
    }
    
    // Verificar credenciales en la base de datos
    $usuario = buscarUsuarioEnBD($email);
    
    if ($usuario && password_verify($password, $usuario['password_hash'])) {
        // Iniciar sesión
        $_SESSION['usuario_id'] = $usuario['id'];
        header('Location: dashboard.php');
    } else {
        echo 'Credenciales incorrectas';
    }
}
?>
```

**Otro ejemplo: verificación de contraseña**

Para verificar la longitud mínima de una contraseña:

- **En el cliente**: Es preferible verificar la longitud antes de enviar, para dar feedback inmediato al usuario sin necesidad de comunicación con el servidor
- **En el servidor**: Es OBLIGATORIO verificar de nuevo, porque no podemos confiar en que el cliente haya hecho su trabajo

!!! tip "Separación de responsabilidades"
    Una buena práctica es que el cliente se encargue de la experiencia de usuario (validaciones de formato, feedback visual, interactividad) mientras que el servidor se encarga de la seguridad, la lógica de negocio crítica y el acceso a datos.

#### 3.4. División de responsabilidades: Frontend, Backend y la división de responsabilidades

Ahora que entendemos los modelos de ejecución, profundicemos en los componentes principales de una aplicación web y cómo se relacionan entre sí.

#### 3.5. Frontend: la cara visible de la aplicación

El **Frontend** es todo lo que el usuario ve e interactúa directamente en su navegador. Es la interfaz de usuario (UI) y la experiencia de usuario (UX).

**Componentes del Frontend:**

- **Estructura (HTML)**
    
    - Define los elementos de la página
    - Organiza el contenido de forma semántica
    - Proporciona accesibilidad
    
- **Estilos (CSS)**
    
    - Controla colores, tipografías, espaciados
    - Diseño responsive para diferentes dispositivos
    - Animaciones y transiciones
    
- **Comportamiento (JavaScript)**
    
    - Manejo de eventos (clics, teclado, etc.)
    - Validación de formularios
    - Peticiones asíncronas (AJAX/Fetch)
    - Manipulación dinámica del contenido

**Frameworks y bibliotecas Frontend populares:**

- **React**: Biblioteca de JavaScript para construir interfaces de usuario
- **Angular**: Framework completo de TypeScript/JavaScript
- **Vue.js**: Framework progresivo y flexible
- **Svelte**: Compilador que genera código JavaScript optimizado

#### 3.6. Backend: el cerebro de la aplicación

El **Backend** es la parte que no ve el usuario. Es donde reside la lógica de negocio, se procesan los datos y se toman las decisiones importantes.

**Componentes del Backend:**

- **Servidor de aplicaciones**
    
    - Ejecuta el código de la aplicación
    - Procesa las peticiones HTTP
    - Genera respuestas dinámicas
    
- **Base de datos**
    
    - Almacena información de forma persistente
    - Permite consultas y modificaciones de datos
    - Garantiza la integridad de la información
    
- **APIs y servicios**
    
    - Proporcionan interfaces para la comunicación
    - Integración con servicios externos
    - Microservicios que dividen funcionalidades

**Responsabilidades del Backend:**

- **Autenticación y autorización**: ¿Quién es el usuario? ¿Qué puede hacer?
- **Lógica de negocio**: Reglas y procesos específicos de la aplicación
- **Procesamiento de datos**: Cálculos, transformaciones, validaciones
- **Persistencia**: Guardar y recuperar información
- **Seguridad**: Proteger datos y prevenir ataques
- **Integración**: Comunicarse con otros sistemas y servicios

#### 3.7. La universalidad del Backend

Una característica importante del Backend es su **universalidad**: puede servir a múltiples tipos de clientes simultáneamente.

<figure markdown="span">
  ![Frontend, Backend y API](assets/front-back-api.jpg){ width="700" }
  <figcaption>Diagrama que muestra cómo un único Backend (API) puede servir a múltiples frontends: aplicación web, aplicación móvil iOS, aplicación móvil Android y aplicaciones de escritorio. Todos consumen los mismos servicios del servidor.</figcaption>
</figure>

**Ventajas de un Backend universal:**

- **Reutilización**: Un mismo Backend puede servir a web, móvil, escritorio
- **Consistencia**: La lógica de negocio es la misma para todos los clientes
- **Mantenimiento**: Cambios en un solo lugar afectan a todos los clientes
- **Escalabilidad**: Podemos escalar el Backend independientemente de los clientes

**Ejemplo práctico:**

Una red social como Instagram tiene:

- **Un Backend único** que gestiona usuarios, publicaciones, likes, comentarios
- **Múltiples Frontends**:
    - Aplicación web (navegador)
    - App móvil iOS
    - App móvil Android
    - Versión lite para dispositivos con pocos recursos

Todos estos clientes se comunican con el mismo Backend a través de una API, obteniendo y enviando datos en formato JSON.



---

Habiendo comprendido los componentes básicos, es momento de explorar cómo se organizan en diferentes arquitecturas según las necesidades de cada proyecto.

### 4. Arquitecturas de software web

Las **arquitecturas de software** definen cómo se estructura y organiza una aplicación. A lo largo de la historia de la web, hemos visto evolucionar estos patrones arquitectónicos desde simples aplicaciones monolíticas hasta complejas redes de microservicios distribuidos. La elección de la arquitectura correcta es una de las decisiones más importantes en el desarrollo de una aplicación, ya que impactará directamente en su mantenibilidad, escalabilidad y coste operativo.

#### 4.1. Arquitectura monolítica

La arquitectura monolítica es el enfoque tradicional donde todos los componentes de una aplicación se agrupan en un solo bloque. Es como un edificio donde todas las oficinas, servicios y departamentos están bajo un mismo techo sin divisiones reales.

Imaginad una aplicación de comercio electrónico clásica: el código que gestiona el catálogo de productos, el carrito de compra, el procesamiento de pagos, la gestión de usuarios, y el sistema de envíos, todo está contenido en una única aplicación que se ejecuta como un proceso único.

**Características:**

- **Código fuente único y unificado**: Todo el código vive en un mismo repositorio y proyecto. Los desarrolladores trabajan en la misma base de código, lo que simplifica la coordinación pero puede crear cuellos de botella cuando el equipo crece.
    
- **Se despliega como una sola unidad**: No podéis desplegar solo una parte de la aplicación. Si cambiáis una línea de código en cualquier módulo, debéis redesplegar la aplicación completa. Esto significa que un pequeño cambio en el módulo de facturación requiere redesplegar también los módulos de catálogo, usuarios, etc.
    
- **Todos los componentes comparten recursos**: La memoria, la CPU, las conexiones a base de datos... todo se comparte entre los módulos. Esto puede ser eficiente, pero también significa que si un módulo consume muchos recursos, afecta a todos los demás.
    
- **Base de datos única**: Típicamente, una aplicación monolítica usa una sola base de datos relacional que almacena todos los datos. Todas las tablas están en el mismo esquema, lo que facilita las consultas complejas que cruzan múltiples dominios, pero también crea un acoplamiento fuerte a nivel de datos.

**Ventajas:**

- **Simple de desarrollar inicialmente**: Cuando empezáis un proyecto, no necesitáis configurar múltiples servicios, sistemas de mensajería, orquestadores ni gestión de redes complejas. Simplemente creáis un proyecto, definís vuestras rutas y empezáis a programar. Esto es ideal para startups, MVPs (Minimum Viable Products) o equipos pequeños que quieren validar una idea rápidamente.
    
- **Fácil de probar (todo en un lugar)**: Podéis levantar la aplicación completa en vuestro ordenador de desarrollo y probar el flujo completo de extremo a extremo sin necesidad de configurar docenas de servicios. Los tests de integración son más simples porque todo está en el mismo proceso.
    
- **Despliegue sencillo**: El proceso de despliegue es relativamente simple: generar un único artefacto (un WAR en Java, un directorio de archivos en PHP, un binario en Go) y copiarlo al servidor. No necesitáis coordinar el despliegue de 20 microservicios diferentes.
    
- **Rendimiento interno óptimo (llamadas en memoria)**: Cuando el módulo de carrito de compra necesita datos del módulo de productos, simplemente hace una llamada de función en memoria. No hay latencia de red, no hay serialización/deserialización de datos, no hay overhead de HTTP. Esto es significativamente más rápido que las llamadas entre microservicios.

**Desventajas:**

- **Difícil de escalar selectivamente**: Si necesitáis más capacidad para el módulo de búsqueda de productos (porque es donde está el cuello de botella), no podéis escalar solo ese módulo. Debéis replicar la aplicación completa, incluyendo todos los módulos que tal vez no necesitan más recursos. Esto desperdicia recursos y aumenta costes.
    
- **Cambios requieren redesplegar todo**: Cada cambio, por pequeño que sea, requiere un redespliegue completo de la aplicación. Esto significa downtime (tiempo de inactividad) o procesos complejos de despliegue blue-green. Además, aumenta el riesgo: un bug en una parte pequeña del código puede tumbar toda la aplicación.
    
- **Acoplamiento alto entre componentes**: Los módulos tienden a depender fuertemente entre sí porque comparten el mismo espacio de memoria, las mismas estructuras de datos y la misma base de datos. Cambiar una tabla o un modelo de datos puede requerir modificar código en múltiples módulos. Con el tiempo, este acoplamiento se vuelve tan fuerte que modificar cualquier cosa se convierte en una tarea arriesgada y costosa.
    
- **Difícil de mantener a medida que crece**: Conforme la aplicación crece (más líneas de código, más desarrolladores, más funcionalidades), la complejidad aumenta exponencialmente. El tiempo de compilación se alarga, los tests tardan más, los nuevos desarrolladores tardan semanas en entender el código, y cualquier cambio puede tener efectos secundarios inesperados en partes distantes de la aplicación.

**¿Cuándo usar arquitectura monolítica?**

✅ **Usar monolito cuando:**
- Estáis empezando un proyecto nuevo y no conocéis bien el dominio
- Tenéis un equipo pequeño (menos de 10 desarrolladores)
- La aplicación tiene requisitos simples y bien definidos
- El tráfico es predecible y moderado
- Queréis validar una idea rápidamente (MVP)

❌ **Evitar monolito cuando:**
- Necesitáis escalar componentes independientemente
- Equipos grandes trabajando simultáneamente
- Diferentes partes de la aplicación tienen requisitos tecnológicos muy distintos
- Necesitáis alta disponibilidad (el monolito es un punto único de fallo)

#### 4.2. Arquitectura de microservicios

En contraposición al monolito, los **microservicios** dividen la aplicación en pequeños servicios independientes, cada uno enfocado en una función específica del negocio. Si el monolito es un edificio único, los microservicios son un conjunto de pequeñas cabañas especializadas, cada una con su propósito específico, conectadas por caminos (APIs).

Pensad en nuestra aplicación de comercio electrónico anterior: en lugar de ser un bloque único, ahora tendríamos:
- **Servicio de Catálogo**: Gestiona productos, categorías, búsquedas
- **Servicio de Usuarios**: Autenticación, perfiles, preferencias
- **Servicio de Carrito**: Gestión del carrito de compra
- **Servicio de Pagos**: Procesamiento de transacciones
- **Servicio de Envíos**: Cálculo de costes, tracking
- **Servicio de Notificaciones**: Emails, SMS, push notifications

Cada uno de estos servicios es una aplicación independiente, con su propio código, su propia base de datos, y su propio ciclo de vida.

**Principios fundamentales:**

- **Servicios pequeños y enfocados**: Cada microservicio tiene una responsabilidad clara y limitada. El "Servicio de Notificaciones" solo se encarga de enviar notificaciones, nada más. Esta especialización hace que el código sea más simple, más fácil de entender y más fácil de mantener. Un desarrollador nuevo puede entender completamente un microservicio en días, mientras que entender un monolito puede llevar meses.
    
- **Despliegue independiente**: Podéis actualizar el "Servicio de Pagos" a una nueva versión sin tocar ningún otro servicio. Si hay un bug en el servicio de notificaciones, lo corregís y desplegáis solo ese servicio, sin riesgo de afectar al resto de la plataforma. Esto permite ciclos de desarrollo más rápidos: diferentes equipos pueden desplegar cambios múltiples veces al día sin coordinarse.
    
- **Comunicación vía APIs**: Los microservicios no comparten memoria ni se llaman directamente. Se comunican exclusivamente a través de APIs bien definidas, típicamente HTTP/REST o gRPC. Esto crea fronteras claras y reduce el acoplamiento. El "Servicio de Carrito" no necesita conocer cómo funciona internamente el "Servicio de Productos", solo necesita conocer su API pública.
    
- **Bases de datos descentralizadas**: Cada microservicio tiene su propia base de datos. El "Servicio de Usuarios" puede usar PostgreSQL, el "Servicio de Catálogo" puede usar Elasticsearch para búsquedas rápidas, y el "Servicio de Sesiones" puede usar Redis. Esta independencia permite optimizar cada servicio con la tecnología más adecuada, pero también complica las consultas que cruzan múltiples dominios.
    
- **Fallos aislados**: Si el "Servicio de Recomendaciones" se cae, el resto de la aplicación sigue funcionando. Los usuarios pueden seguir comprando, aunque no vean recomendaciones personalizadas. Esto mejora la resiliencia global de la plataforma. En un monolito, un fallo en cualquier módulo puede tumbar toda la aplicación.

**Ventajas:**

- **Escalabilidad granular**: Si el "Servicio de Búsqueda" recibe 10 veces más tráfico que los demás, podéis escalar solo ese servicio, ejecutándolo en 10 instancias mientras el resto corre en 1 o 2 instancias. Esto optimiza el uso de recursos y reduce costes. Con un monolito, tendrías que replicar toda la aplicación 10 veces, desperdiciando recursos en los módulos que no necesitan ese escalado.
    
- **Agilidad en desarrollo**: Equipos diferentes pueden trabajar en microservicios diferentes sin pisarse. El equipo de pagos puede usar Java + Spring Boot, mientras el equipo de notificaciones usa Python + FastAPI, sin conflictos. Cada equipo puede tomar decisiones técnicas independientes y avanzar a su propio ritmo.
    
- **Tecnologías heterogéneas**: Podéis usar el lenguaje y framework más adecuado para cada problema. Un servicio de procesamiento de imágenes puede estar en Go por su rendimiento, un servicio de machine learning en Python por su ecosistema, y un servicio de tiempo real en Node.js por su naturaleza asíncrona. No estáis atados a una única tecnología.
    
- **Resiliencia mejorada**: Los fallos se contienen. Podéis implementar patrones como circuit breakers (cortocircuitos) que detectan cuando un servicio falla y evitan sobrecargarlo. Si el "Servicio de Recomendaciones" está caído, el sistema puede degradar graciosamente mostrando recomendaciones genéricas o simplemente no mostrando esa sección, pero el resto funciona perfectamente.

**Desventajas:**

- **Complejidad operacional**: En lugar de gestionar 1 aplicación, ahora gestionáis 20, 50 o 100 servicios. Cada uno necesita monitorización, logs, métricas, alertas, balanceadores de carga, sistemas de descubrimiento de servicios, etc. Necesitáis herramientas como Kubernetes, service meshes (Istio), sistemas de logging centralizados (ELK), y sistemas de tracing distribuido (Jaeger). Esta infraestructura es compleja y requiere expertise especializado.
    
- **Latencia de red**: Cuando el "Servicio de Carrito" necesita información del "Servicio de Productos", debe hacer una llamada HTTP a través de la red. Esto añade latencia (milisegundos en lugar de nanosegundos de una llamada local en memoria). Si una operación requiere datos de 5 servicios diferentes, la latencia se acumula. Debéis diseñar cuidadosamente cómo minimizar estas llamadas en red.
    
- **Gestión de transacciones distribuidas**: En un monolito con una base de datos única, las transacciones ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad) son triviales. En microservicios, si una operación de "crear pedido" involucra actualizar el inventario (Servicio de Catálogo), procesar el pago (Servicio de Pagos) y crear el envío (Servicio de Logística), ¿cómo aseguráis que o todo sucede o nada sucede? Necesitáis patrones como Sagas, Eventos de dominio y Compensación, que son conceptualmente complejos.
    
- **Requiere DevOps maduro**: Para tener éxito con microservicios, necesitáis automatización avanzada: CI/CD pipelines, infraestructura como código (Terraform), contenedores (Docker), orquestación (Kubernetes), observabilidad (métricas, logs, trazas), y cultura DevOps. Sin estas capacidades, los microservicios se convierten rápidamente en una pesadilla operacional.

**Ejemplo: Netflix**

Netflix es el caso de estudio por excelencia de microservicios exitosos. Su plataforma se compone de más de **700 microservicios** que gestionan diferentes aspectos:

- **Autenticación y usuarios**: Gestión de cuentas, perfiles, suscripciones
- **Recomendaciones**: Algoritmos de ML que sugieren contenido personalizado
- **Streaming**: Transcodificación, CDN, gestión de calidad adaptativa
- **Facturación**: Procesamiento de pagos, renovaciones, upgrades
- **A/B Testing**: Experimentación continua de features
- **Búsqueda**: Indexación y búsqueda de contenido

Cada servicio puede actualizarse, desplegarse y escalarse independientemente. Netflix despliega código a producción **miles de veces al día** sin interrumpir el servicio. Cuando un servicio falla (y en un sistema tan grande, siempre hay algo fallando), el resto sigue funcionando. Esta arquitectura les permite servir a **más de 230 millones de suscriptores** en todo el mundo con alta disponibilidad.

Sin embargo, es importante notar que Netflix llegó a esta arquitectura después de años de evolución y crecimiento. No empezaron con 700 microservicios; comenzaron con un monolito y gradualmente lo descompusieron conforme sus necesidades lo requerían.

**¿Cuándo usar microservicios?**

✅ **Usar microservicios cuando:**
- La aplicación es grande y compleja
- Múltiples equipos (>20 desarrolladores) trabajando simultáneamente
- Necesitáis escalar componentes independientemente
- Diferentes partes requieren diferentes tecnologías
- Alta disponibilidad es crítica
- Tenéis capacidad DevOps madura

❌ **Evitar microservicios cuando:**
- Proyecto pequeño o MVP
- Equipo pequeño (<10 personas)
- Sin experiencia en sistemas distribuidos
- Infraestructura o presupuesto limitado
- No hay necesidad real de escalado independiente

#### 4.3. Otras arquitecturas modernas

Además de monolitos y microservicios, existen otros paradigmas arquitectónicos que resuelven problemas específicos o combinan características de ambos enfoques.

**Arquitectura de capas (Layered Architecture):**

Este es uno de los patrones más tradicionales y pedagógicos. Organiza el código en capas horizontales, donde cada capa solo se comunica con la inmediatamente inferior. Es como un pastel con capas bien definidas:

- **Capa de Presentación (UI)**: HTML, CSS, JavaScript que interactúa con el usuario
- **Capa de Aplicación (Controladores)**: Gestiona las peticiones, coordina las operaciones
- **Capa de Lógica de Negocio (Servicios)**: Implementa las reglas del negocio
- **Capa de Acceso a Datos (Repositorios)**: Interactúa con la base de datos
- **Capa de Datos**: La base de datos en sí

**Ventajas de la arquitectura de capas:**
- Separación clara de responsabilidades
- Fácil de entender para desarrolladores nuevos
- Facilita el testing (podéis mockear capas inferiores)
- Permite cambiar implementaciones de capas sin afectar las superiores

**Desventajas:**
- Puede llevar a código muy burocrático (demasiadas capas de indirección)
- Dificulta ciertas optimizaciones de rendimiento
- Tendencia a crear "god classes" en la capa de servicios

**Arquitectura serverless (Functions as a Service - FaaS):**

Serverless es un nombre engañoso: obviamente hay servidores, pero vosotros no los gestionáis. En lugar de desplegar y mantener servidores (o contenedores), escribís funciones individuales que el proveedor cloud ejecuta bajo demanda.

**Ejemplo con AWS Lambda:**

```javascript
// Función Lambda que procesa pedidos
exports.handler = async (event) => {
    const pedido = JSON.parse(event.body);
    
    // Validar pedido
    if (!validarPedido(pedido)) {
        return { statusCode: 400, body: 'Pedido inválido' };
    }
    
    // Guardar en DynamoDB
    await guardarPedido(pedido);
    
    // Enviar a cola SQS para procesamiento
    await enviarACola(pedido);
    
    return { statusCode: 200, body: 'Pedido recibido' };
};
```

Esta función solo se ejecuta cuando llega una petición. AWS Lambda la levanta, la ejecuta, y la apaga. Solo pagáis por el tiempo de ejecución real (facturado en milisegundos).

**Ventajas de serverless:**
- **Coste por uso real**: Solo pagáis cuando el código se ejecuta. Perfecto para aplicaciones con tráfico irregular
- **Escalado automático**: El proveedor escala automáticamente de 0 a miles de instancias según demanda
- **Cero gestión de servidores**: No instaláis sistemas operativos, no aplicáis parches, no gestionáis infraestructura
- **Ideal para workloads esporádicos**: Procesamiento de imágenes, webhooks, tareas programadas

**Desventajas:**
- **Cold starts**: La primera ejecución tras un período de inactividad es lenta (segundos)
- **Límites de tiempo**: Las funciones tienen tiempo máximo de ejecución (15 minutos en AWS Lambda)
- **Vendor lock-in**: Código acoplado al proveedor cloud específico
- **Debugging complejo**: Difícil reproducir el entorno localmente
- **Costes impredecibles**: Para tráfico muy alto constante, puede ser más caro que servidores tradicionales

**Casos de uso ideales:**
- Procesamiento de eventos (subida de imagen → generar thumbnails)
- APIs con tráfico irregular
- Tareas programadas (cron jobs)
- Webhooks de terceros
- Procesamiento batch

**Arquitectura event-driven (orientada a eventos):**

En lugar de llamadas síncronas directas entre componentes, los servicios se comunican mediante eventos asíncronos a través de un "bus de eventos" o sistema de mensajería (RabbitMQ, Apache Kafka, AWS EventBridge).

**Ejemplo de flujo event-driven en un e-commerce:**

1. **Usuario completa el pago** → Servicio de Pagos publica evento `PedidoCreado`
2. **Servicio de Inventario** escucha `PedidoCreado` → Reserva stock → Publica `StockReservado`
3. **Servicio de Logística** escucha `StockReservado` → Genera etiqueta de envío → Publica `EnvioPreparado`
4. **Servicio de Notificaciones** escucha `EnvioPreparado` → Envía email al cliente
5. **Servicio de Analytics** escucha todos los eventos → Actualiza dashboards en tiempo real

Ningún servicio llama directamente a otro. Todos publican eventos cuando algo importante sucede y escuchan los eventos que les interesan.

**Ventajas de event-driven:**
- **Desacoplamiento máximo**: Los servicios no necesitan conocerse entre sí
- **Escalabilidad excelente**: Fácil añadir nuevos consumidores de eventos sin modificar productores
- **Resiliencia**: Si un consumidor está caído, los eventos se encolan y se procesan cuando se recupere
- **Auditoría natural**: El log de eventos es una auditoría completa de todo lo que ha pasado
- **Extensibilidad**: Añadir nuevas funcionalidades es solo añadir nuevos consumidores

**Desventajas:**
- **Complejidad conceptual**: Más difícil razonar sobre flujos asíncronos que llamadas directas
- **Debugging complicado**: Seguir el rastro de un evento a través de múltiples servicios es complejo
- **Consistencia eventual**: No hay garantía de que todos los servicios vean los cambios instantáneamente
- **Requiere infraestructura robusta**: Necesitáis un sistema de mensajería confiable y escalable
- **Mensajes duplicados o fuera de orden**: Debéis diseñar servicios idempotentes

**Ejemplo real: Uber**

Uber usa una arquitectura event-driven extensamente. Cuando un conductor acepta un viaje:
- Servicio de Viajes publica `ViajeAceptado`
- Servicio de Notificaciones envía push al pasajero
- Servicio de Mapas inicia tracking en tiempo real
- Servicio de Pagos reserva el método de pago
- Servicio de Analytics registra la métrica

Todo sucede en paralelo, asíncronamente, sin bloqueos.

!!! tip "Arquitecturas híbridas"
    En la realidad, muchas aplicaciones modernas combinan varios de estos paradigmas. Podéis tener:
    - Partes monolíticas para funcionalidades simples y estables
    - Microservicios para componentes que necesitan escalar independientemente
    - Funciones serverless para tareas esporádicas
    - Comunicación síncrona (HTTP/REST) para operaciones críticas de baja latencia
    - Comunicación asíncrona (eventos) para operaciones de larga duración
    
    No hay arquitectura "perfecta" universal. La clave es entender los trade-offs y elegir la arquitectura que mejor se ajuste a vuestras necesidades específicas, capacidades de equipo y presupuesto.

---

### 5. Patrón MVC y principios de diseño

Independientemente de la arquitectura general elegida, necesitamos patrones que nos ayuden a organizar el código internamente. El patrón **Modelo-Vista-Controlador (MVC)** y los **principios SOLID** son fundamentales para escribir código mantenible y de calidad.

#### 5.1. El patrón MVC

MVC (Modelo-Vista-Controlador) es uno de los patrones de diseño más importantes y utilizados en el desarrollo web. Separa la aplicación en tres componentes principales con responsabilidades bien definidas. La idea central es: **separar la lógica de negocio de la presentación visual**, facilitando el mantenimiento, testing y escalabilidad del código.

Imaginad que estáis construyendo una aplicación de gestión de tareas (to-do list). Sin MVC, todo el código estaría mezclado: consultas SQL en medio de HTML, validaciones mezcladas con renderizado, lógica de negocio dispersa por doquier. Con MVC, cada responsabilidad tiene su lugar.

**Modelo (Model):**

El **Modelo** es el cerebro de la aplicación. Representa los datos y contiene toda la lógica de negocio.

**Responsabilidades:**
- **Representa los datos del dominio**: En nuestra app de tareas, el Modelo `Tarea` representa qué es una tarea: tiene un título, una descripción, una fecha límite, un estado (pendiente/completada), etc.
    
- **Gestiona el acceso a la base de datos**: El Modelo sabe cómo guardarse en la base de datos, cómo recuperarse, cómo actualizarse. Encapsula todas las consultas SQL o interacciones con ORMs (Object-Relational Mappers).
    
- **Contiene la lógica de negocio**: Todas las reglas del negocio viven aquí. Por ejemplo, "una tarea no puede tener fecha límite en el pasado", "solo el creador puede eliminar una tarea", "cuando una tarea se completa, notificar a los colaboradores". Esta lógica está en el Modelo, no dispersa por el código.
    
- **Independiente de la presentación**: El Modelo **no sabe nada** sobre HTML, CSS, JSON, vistas, o cómo se mostrará al usuario. Esta independencia es crucial: podéis cambiar completamente la interfaz sin tocar el Modelo.

**Ejemplo de Modelo en PHP:**

```php
class Tarea {
    private $id;
    private $titulo;
    private $descripcion;
    private $fechaLimite;
    private $completada = false;
    private $usuarioId;
    
    // Lógica de negocio
    public function completar() {
        if ($this->fechaLimite < new DateTime()) {
            throw new Exception("No puedes completar una tarea vencida");
        }
        $this->completada = true;
        $this->guardar();
        $this->notificarColaboradores();
    }
    
    // Acceso a datos
    public function guardar() {
        $db = Database::getConnection();
        if ($this->id) {
            // Actualizar
            $stmt = $db->prepare("UPDATE tareas SET titulo=?, descripcion=?, fecha_limite=?, completada=? WHERE id=?");
            $stmt->execute([$this->titulo, $this->descripcion, $this->fechaLimite, $this->completada, $this->id]);
        } else {
            // Insertar nuevo
            $stmt = $db->prepare("INSERT INTO tareas (titulo, descripcion, fecha_limite, usuario_id) VALUES (?, ?, ?, ?)");
            $stmt->execute([$this->titulo, $this->descripcion, $this->fechaLimite, $this->usuarioId]);
            $this->id = $db->lastInsertId();
        }
    }
    
    public static function buscarPorUsuario($usuarioId) {
        $db = Database::getConnection();
        $stmt = $db->prepare("SELECT * FROM tareas WHERE usuario_id = ? ORDER BY fecha_limite");
        $stmt->execute([$usuarioId]);
        $tareas = [];
        while ($row = $stmt->fetch()) {
            $tareas[] = self::fromArray($row);
        }
        return $tareas;
    }
}
```

Todo lo relacionado con datos y lógica de negocio está encapsulado en el Modelo.

**Vista (View):**

La **Vista** es la piel de la aplicación. Se encarga exclusivamente de la presentación visual.

**Responsabilidades:**
- **Presenta los datos al usuario**: Recibe datos del Controlador y los muestra. En nuestra app, la Vista toma una lista de tareas y genera el HTML para mostrarlas.
    
- **Renderiza la interfaz**: Contiene HTML, CSS, y la estructura visual. Decide cómo se ve cada elemento, los colores, la disposición.
    
- **NO contiene lógica de negocio**: La Vista **no decide** qué tareas mostrar, no valida datos, no hace consultas a la base de datos. Solo recibe datos y los presenta. La única "lógica" permitida son bucles para iterar datos y condicionales simples para mostrar/ocultar elementos.
    
- **Múltiples vistas para los mismos datos**: Podéis tener una Vista HTML para navegadores, una Vista JSON para APIs, una Vista XML para otros sistemas. Todas usan el mismo Modelo.

**Ejemplo de Vista en PHP (usando plantillas):**

```php
<!-- vista_lista_tareas.php -->
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Mis Tareas</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <h1>Mis Tareas</h1>
    
    <?php if (empty($tareas)): ?>
        <p>No tienes tareas pendientes. ¡Disfruta tu tiempo libre!</p>
    <?php else: ?>
        <ul class="lista-tareas">
            <?php foreach ($tareas as $tarea): ?>
                <li class="<?= $tarea->estaCompletada() ? 'completada' : 'pendiente' ?>">
                    <h3><?= htmlspecialchars($tarea->getTitulo()) ?></h3>
                    <p><?= htmlspecialchars($tarea->getDescripcion()) ?></p>
                    <span class="fecha">Fecha límite: <?= $tarea->getFechaLimite()->format('d/m/Y') ?></span>
                    
                    <?php if (!$tarea->estaCompletada()): ?>
                        <a href="/tareas/completar/<?= $tarea->getId() ?>">Marcar como completada</a>
                    <?php endif; ?>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>
</body>
</html>
```

La Vista solo presenta datos. No decide qué tareas cargar, no las valida, no las guarda.

**Controlador (Controller):**

El **Controlador** es el director de orquesta. Coordina el Modelo y la Vista, gestionando el flujo de la aplicación.

**Responsabilidades:**
- **Gestiona las peticiones del usuario**: Cuando el usuario hace clic en "Completar tarea", el Controlador recibe esa petición.
    
- **Coordina Modelo y Vista**: El Controlador pide datos al Modelo y se los pasa a la Vista apropiada. Actúa como intermediario.
    
- **Contiene la lógica de aplicación** (no de negocio): Decide qué Modelo usar, qué Vista renderizar, qué hacer según las peticiones. Pero **no** contiene reglas de negocio (esas están en el Modelo).
    
- **Maneja el flujo de navegación**: Decide a qué página redirigir después de una acción, qué mensajes mostrar, etc.

**Ejemplo de Controlador en PHP:**

```php
class TareasController {
    
    // Mostrar lista de tareas
    public function index() {
        // Obtener ID del usuario de la sesión
        $usuarioId = $_SESSION['usuario_id'];
        
        // Pedir datos al Modelo
        $tareas = Tarea::buscarPorUsuario($usuarioId);
        
        // Pasar datos a la Vista
        require 'vistas/vista_lista_tareas.php';
    }
    
    // Crear nueva tarea
    public function crear() {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            // Validar entrada
            $titulo = $_POST['titulo'] ?? '';
            $descripcion = $_POST['descripcion'] ?? '';
            $fechaLimite = $_POST['fecha_limite'] ?? '';
            
            if (empty($titulo)) {
                $_SESSION['error'] = 'El título es obligatorio';
                header('Location: /tareas/nueva');
                return;
            }
            
            // Crear y guardar nueva tarea
            $tarea = new Tarea();
            $tarea->setTitulo($titulo);
            $tarea->setDescripcion($descripcion);
            $tarea->setFechaLimite(new DateTime($fechaLimite));
            $tarea->setUsuarioId($_SESSION['usuario_id']);
            
            try {
                $tarea->guardar();
                $_SESSION['mensaje'] = 'Tarea creada con éxito';
                header('Location: /tareas');
            } catch (Exception $e) {
                $_SESSION['error'] = $e->getMessage();
                header('Location: /tareas/nueva');
            }
        } else {
            // Mostrar formulario
            require 'vistas/formulario_nueva_tarea.php';
        }
    }
    
    // Completar tarea
    public function completar($id) {
        $tarea = Tarea::buscarPorId($id);
        
        if (!$tarea) {
            $_SESSION['error'] = 'Tarea no encontrada';
            header('Location: /tareas');
            return;
        }
        
        // Verificar permisos
        if ($tarea->getUsuarioId() != $_SESSION['usuario_id']) {
            $_SESSION['error'] = 'No tienes permisos';
            header('Location: /tareas');
            return;
        }
        
        try {
            $tarea->completar();  // Lógica de negocio en el Modelo
            $_SESSION['mensaje'] = 'Tarea completada';
        } catch (Exception $e) {
            $_SESSION['error'] = $e->getMessage();
        }
        
        header('Location: /tareas');
    }
}
```

El Controlador orquesta todo: recibe la petición, usa el Modelo, elige la Vista.

**Flujo típico en MVC:**

Veamos el flujo completo cuando un usuario completa una tarea:

1. **Usuario hace clic** en "Marcar como completada" → Genera petición GET `/tareas/completar/42`

2. **El framework de routing** (parte del Controlador) interpreta la URL y llama a `TareasController::completar(42)`

3. **Controlador recibe la petición**:
   - Identifica que necesita la tarea con ID 42
   - Pide al Modelo: `$tarea = Tarea::buscarPorId(42)`

4. **Modelo ejecuta**:
   - Hace consulta SQL: `SELECT * FROM tareas WHERE id = 42`
   - Crea objeto `Tarea` con esos datos
   - Devuelve el objeto al Controlador

5. **Controlador valida permisos**:
   - Verifica que el usuario actual sea el dueño
   - Si no, muestra error y termina
   - Si sí, llama a `$tarea->completar()`

6. **Modelo ejecuta lógica de negocio**:
   - Valida que la fecha límite no haya pasado
   - Marca `completada = true`
   - Ejecuta SQL: `UPDATE tareas SET completada = 1 WHERE id = 42`
   - Notifica a colaboradores (lógica adicional)
   - Devuelve éxito al Controlador

7. **Controlador decide qué hacer**:
   - Establece mensaje de éxito en sesión
   - Redirige a `TareasController::index()`

8. **Controlador solicita lista actualizada**:
   - Pide al Modelo: `$tareas = Tarea::buscarPorUsuario($usuarioId)`
   - Modelo devuelve array de tareas

9. **Controlador selecciona Vista**:
   - Carga `vista_lista_tareas.php`
   - Pasa la variable `$tareas` a la Vista

10. **Vista renderiza**:
    - Recorre el array de tareas
    - Genera HTML para cada una
    - La tarea 42 ahora aparece con clase "completada"
    - Envía el HTML al navegador

11. **Usuario ve** la página actualizada con su tarea marcada como completada

**Ventajas de MVC:**

- **Separación de responsabilidades**: Cada componente tiene un propósito claro
- **Facilita el testing**: Podéis testear el Modelo sin interfaz, testear Controladores sin base de datos real
- **Trabajo en equipo**: Diseñadores pueden trabajar en Vistas, programadores en Modelos y Controladores
- **Reutilización**: Un Modelo puede usarse desde múltiples Vistas (web, API, móvil)
- **Mantenibilidad**: Cambios en una capa no afectan a las otras

!!! warning "MVC mal implementado"
    Muchas aplicaciones dicen usar MVC pero violan sus principios:
    - **Controladores con lógica de negocio**: Esto hace que la lógica no sea reutilizable
    - **Vistas con consultas SQL**: Esto acopla la presentación a la base de datos
    - **Modelos anémicos**: Modelos que solo son contenedores de datos sin lógica
    
    Un MVC bien implementado respeta estrictamente las responsabilidades de cada capa.

#### 5.2. Principios SOLID

Los **principios SOLID** son cinco reglas fundamentales para diseño orientado a objetos de calidad, formuladas por Robert C. Martin (Uncle Bob). Aunque nacieron en el contexto de programación orientada a objetos, sus conceptos son aplicables a cualquier paradigma de programación. Estos principios no son reglas absolutas que debáis seguir ciegamente, sino guías que os ayudarán a escribir código más mantenible, flexible y robusto.

Veámoslos uno por uno con ejemplos prácticos.

**S - Single Responsibility Principle (Principio de Responsabilidad Única)**

> "Una clase debe tener una, y solo una, razón para cambiar"

Esto significa que cada clase debe tener **una única responsabilidad**, un único propósito en el sistema. Si una clase hace demasiadas cosas, cambios en diferentes áreas del sistema requerirán modificar esa clase, aumentando la probabilidad de introducir bugs.

**❌ Violación de SRP:**

```php
class Usuario {
    private $nombre;
    private $email;
    private $password;
    
    // Responsabilidad 1: Gestión de datos de usuario
    public function setNombre($nombre) { ... }
    public function getEmail() { ... }
    
    // Responsabilidad 2: Persistencia en base de datos
    public function guardarEnBD() {
        $db = new PDO(...);
        $sql = "INSERT INTO usuarios ...";
        // ... código SQL ...
    }
    
    // Responsabilidad 3: Validación
    public function validar() {
        if (!filter_var($this->email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Email inválido");
        }
        if (strlen($this->password) < 8) {
            throw new Exception("Password débil");
        }
    }
    
    // Responsabilidad 4: Envío de emails
    public function enviarEmailBienvenida() {
        $mensaje = "Bienvenido " . $this->nombre;
        mail($this->email, "Bienvenida", $mensaje);
    }
}
```

Esta clase tiene **cuatro responsabilidades diferentes**. Si cambia la forma de validar emails, debemos modificar esta clase. Si cambiamos el sistema de base de datos, modificamos esta clase. Si cambiamos el sistema de envío de emails, modificamos esta clase. ¡Demasiadas razones para cambiar!

**✅ Respetando SRP:**

```php
// Responsabilidad 1: Representar datos de usuario
class Usuario {
    private $nombre;
    private $email;
    private $password;
    
    public function __construct($nombre, $email, $password) {
        $this->nombre = $nombre;
        $this->email = $email;
        $this->password = $password;
    }
    
    public function getNombre() { return $this->nombre; }
    public function getEmail() { return $this->email; }
    public function getPassword() { return $this->password; }
}

// Responsabilidad 2: Validación
class ValidadorUsuario {
    public function validar(Usuario $usuario) {
        if (!filter_var($usuario->getEmail(), FILTER_VALIDATE_EMAIL)) {
            throw new ValidationException("Email inválido");
        }
        if (strlen($usuario->getPassword()) < 8) {
            throw new ValidationException("Password débil");
        }
    }
}

// Responsabilidad 3: Persistencia
class RepositorioUsuario {
    private $db;
    
    public function guardar(Usuario $usuario) {
        $sql = "INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)";
        $stmt = $this->db->prepare($sql);
        $stmt->execute([
            $usuario->getNombre(),
            $usuario->getEmail(),
            password_hash($usuario->getPassword(), PASSWORD_BCRYPT)
        ]);
    }
}

// Responsabilidad 4: Notificaciones
class ServicioNotificaciones {
    public function enviarBienvenida(Usuario $usuario) {
        $mensaje = "Bienvenido " . $usuario->getNombre();
        mail($usuario->getEmail(), "Bienvenida", $mensaje);
    }
}
```

Ahora cada clase tiene **una única responsabilidad**. Cambios en validación solo afectan a `ValidadorUsuario`, cambios en base de datos solo a `RepositorioUsuario`, etc.

**O - Open/Closed Principle (Principio Abierto/Cerrado)**

> "Las entidades de software deben estar abiertas para extensión, pero cerradas para modificación"

Deberíais poder **añadir nueva funcionalidad sin modificar código existente**. Esto se logra mediante abstracciones (interfaces, clases abstractas) y polimorfismo.

**❌ Violación de OCP:**

```php
class ProcesadorPagos {
    public function procesar($tipo, $monto) {
        if ($tipo === 'tarjeta') {
            // Lógica para procesar tarjeta
            echo "Procesando $monto con tarjeta";
        } elseif ($tipo === 'paypal') {
            // Lógica para procesar PayPal
            echo "Procesando $monto con PayPal";
        } elseif ($tipo === 'bitcoin') {  // Nueva funcionalidad
            // Lógica para procesar Bitcoin
            echo "Procesando $monto con Bitcoin";
        }
        // Cada nuevo método de pago requiere modificar esta clase
    }
}
```

Para añadir un nuevo método de pago (Bitcoin, Apple Pay, etc.), debéis **modificar** la clase `ProcesadorPagos`. Esto viola OCP y es arriesgado: podéis introducir bugs en métodos que ya funcionaban.

**✅ Respetando OCP:**

```php
// Abstracción
interface MetodoPago {
    public function procesar($monto);
}

// Implementaciones concretas
class PagoConTarjeta implements MetodoPago {
    public function procesar($monto) {
        echo "Procesando $monto con tarjeta de crédito";
        // Lógica específica de tarjetas
    }
}

class PagoConPayPal implements MetodoPago {
    public function procesar($monto) {
        echo "Procesando $monto con PayPal";
        // Lógica específica de PayPal
    }
}

// Nueva funcionalidad SIN modificar código existente
class PagoConBitcoin implements MetodoPago {
    public function procesar($monto) {
        echo "Procesando $monto con Bitcoin";
        // Lógica específica de Bitcoin
    }
}

// Procesador usa la abstracción
class ProcesadorPagos {
    public function procesar(MetodoPago $metodoPago, $monto) {
        $metodoPago->procesar($monto);
    }
}

// Uso
$procesador = new ProcesadorPagos();
$procesador->procesar(new PagoConTarjeta(), 100);
$procesador->procesar(new PagoConPayPal(), 50);
$procesador->procesar(new PagoConBitcoin(), 0.005);  // Nueva sin cambiar ProcesadorPagos
```

Ahora podemos **añadir nuevos métodos de pago simplemente creando nuevas clases** que implementen `MetodoPago`. No necesitamos tocar `ProcesadorPagos`.

**L - Liskov Substitution Principle (Principio de Sustitución de Liskov)**

> "Los objetos de una clase derivada deben poder sustituir a los objetos de la clase base sin alterar el comportamiento del programa"

Si tenéis una función que acepta un objeto de tipo `Animal`, debe funcionar correctamente con cualquier subclase de `Animal` (`Perro`, `Gato`, etc.) sin necesidad de conocer la subclase específica.

**❌ Violación de LSP:**

```php
class Ave {
    public function volar() {
        echo "Volando...";
    }
}

class Aguila extends Ave {
    public function volar() {
        echo "El águila vuela alto";
    }
}

class Pinguino extends Ave {
    public function volar() {
        throw new Exception("Los pingüinos no pueden volar");
    }
}

// Uso
function hacerVolar(Ave $ave) {
    $ave->volar();  // ¡Explota si es un pingüino!
}

hacerVolar(new Aguila());    // ✓ Funciona
hacerVolar(new Pinguino());  // ✗ Lanza excepción
```

`Pinguino` es un `Ave`, pero no puede volar. Esto viola LSP porque `Pinguino` no puede sustituir a `Ave` sin romper el programa.

**✅ Respetando LSP:**

```php
interface Ave {
    public function comer();
    public function moverse();
}

interface AveVoladora extends Ave {
    public function volar();
}

class Aguila implements AveVoladora {
    public function comer() { echo "Comiendo peces"; }
    public function moverse() { $this->volar(); }
    public function volar() { echo "Volando alto"; }
}

class Pinguino implements Ave {
    public function comer() { echo "Comiendo pescado"; }
    public function moverse() { echo "Nadando"; }
    // NO implementa volar()
}

// Uso correcto
function alimentar(Ave $ave) {
    $ave->comer();  // Funciona con cualquier Ave
}

function hacerVolar(AveVoladora $ave) {
    $ave->volar();  // Solo acepta aves que pueden volar
}

alimentar(new Aguila());     // ✓
alimentar(new Pinguino());   // ✓
hacerVolar(new Aguila());    // ✓
// hacerVolar(new Pinguino()); // Error de compilación - Pinguino no es AveVoladora
```

Ahora el sistema de tipos previene errores. `Pinguino` no hereda comportamientos que no puede cumplir.

**I - Interface Segregation Principle (Principio de Segregación de Interfaces)**

> "Los clientes no deberían estar forzados a depender de interfaces que no usan"

Es mejor tener **muchas interfaces pequeñas y específicas** que una interfaz grande y general. Esto evita que las clases implementen métodos que no necesitan.

**❌ Violación de ISP:**

```php
interface Trabajador {
    public function trabajar();
    public function comer();
    public function recibirSalario();
    public function pedirVacaciones();
}

class Empleado implements Trabajador {
    public function trabajar() { echo "Trabajando..."; }
    public function comer() { echo "Comiendo..."; }
    public function recibirSalario() { echo "Recibiendo salario"; }
    public function pedirVacaciones() { echo "Solicitando vacaciones"; }
}

class Robot implements Trabajador {
    public function trabajar() { echo "Robot trabajando 24/7"; }
    
    // Un robot no come, no recibe salario, no pide vacaciones
    // Pero está FORZADO a implementar estos métodos
    public function comer() { throw new Exception("Los robots no comen"); }
    public function recibirSalario() { throw new Exception("Los robots no cobran"); }
    public function pedirVacaciones() { throw new Exception("Los robots no descansan"); }
}
```

`Robot` está forzado a implementar métodos que no tienen sentido para él. Esto viola ISP.

**✅ Respetando ISP:**

```php
interface Trabajador {
    public function trabajar();
}

interface Alimentable {
    public function comer();
}

interface Asalariado {
    public function recibirSalario();
}

interface ConDerecho aVacaciones {
    public function pedirVacaciones();
}

class Empleado implements Trabajador, Alimentable, Asalariado, ConDerechoAVacaciones {
    public function trabajar() { echo "Trabajando..."; }
    public function comer() { echo "Comiendo..."; }
    public function recibirSalario() { echo "Recibiendo salario"; }
    public function pedirVacaciones() { echo "Solicitando vacaciones"; }
}

class Robot implements Trabajador {
    public function trabajar() { echo "Robot trabajando 24/7"; }
    // Solo implementa lo que necesita
}
```

Ahora `Robot` solo implementa `Trabajador`, que es lo único que realmente hace. No está forzado a implementar métodos sin sentido.

**D - Dependency Inversion Principle (Principio de Inversión de Dependencias)**

> "Depender de abstracciones, no de implementaciones concretas. Los módulos de alto nivel no deben depender de módulos de bajo nivel, ambos deben depender de abstracciones"

Este es quizás el principio más importante para sistemas desacoplados y testeables.

**❌ Violación de DIP:**

```php
class MySQLDatabase {
    public function guardar($datos) {
        echo "Guardando en MySQL: $datos";
    }
}

class ServicioUsuarios {
    private $db;
    
    public function __construct() {
        // Dependencia DIRECTA de MySQLDatabase
        $this->db = new MySQLDatabase();
    }
    
    public function crearUsuario($nombre) {
        $this->db->guardar($nombre);
    }
}
```

`ServicioUsuarios` depende directamente de `MySQLDatabase`. Si queremos cambiar a PostgreSQL o MongoDB, debemos modificar `ServicioUsuarios`. Además, **no podemos testear** `ServicioUsuarios` sin una base de datos MySQL real.

**✅ Respetando DIP:**

```php
// Abstracción
interface Database {
    public function guardar($datos);
}

// Implementaciones concretas
class MySQLDatabase implements Database {
    public function guardar($datos) {
        echo "Guardando en MySQL: $datos";
    }
}

class PostgreSQLDatabase implements Database {
    public function guardar($datos) {
        echo "Guardando en PostgreSQL: $datos";
    }
}

class MongoDBDatabase implements Database {
    public function guardar($datos) {
        echo "Guardando en MongoDB: $datos";
    }
}

// Servicio depende de la ABSTRACCIÓN
class ServicioUsuarios {
    private $db;
    
    public function __construct(Database $db) {
        $this->db = $db;  // Inyección de dependencias
    }
    
    public function crearUsuario($nombre) {
        $this->db->guardar($nombre);
    }
}

// Uso - la dependencia concreta se inyecta desde fuera
$servicio = new ServicioUsuarios(new MySQLDatabase());
$servicio->crearUsuario("Ana");

// Cambiar de BD es trivial
$servicio = new ServicioUsuarios(new PostgreSQLDatabase());

// Para testing, inyectamos un mock
class MockDatabase implements Database {
    public function guardar($datos) {
        // Mock que no hace nada real
    }
}
$servicioTest = new ServicioUsuarios(new MockDatabase());
```

Ahora `ServicioUsuarios` **no conoce** la implementación concreta de la base de datos. Depende solo de la abstracción `Database`. Esto permite:
- Cambiar de base de datos sin modificar `ServicioUsuarios`
- Testear con mocks sin base de datos real
- Reutilizar `ServicioUsuarios` en diferentes contextos

**Resumen de SOLID:**

| Principio                    | Qué logra                                | Técnica principal            |
|:-----------------------------|:-----------------------------------------|:-----------------------------|
| **S**ingle Responsibility    | Código más enfocado y mantenible         | Una clase, una responsabilidad |
| **O**pen/Closed              | Extensibilidad sin riesgo                | Polimorfismo, interfaces     |
| **L**iskov Substitution      | Herencia correcta y segura               | Contratos consistentes       |
| **I**nterface Segregation    | Interfaces pequeñas y específicas        | Múltiples interfaces pequeñas |
| **D**ependency Inversion     | Bajo acoplamiento, alta testabilidad    | Inyección de dependencias    |

Estos principios son especialmente relevantes en arquitecturas modernas y microservicios, donde la mantenibilidad, testabilidad y flexibilidad son críticas.

---

## BLOQUE 3: TECNOLOGÍAS DE IMPLEMENTACIÓN

Teniendo clara la arquitectura y los patrones de diseño, es momento de elegir las herramientas concretas con las que construiremos nuestra aplicación. En este bloque exploraremos los lenguajes de programación del lado del servidor, sus modelos de ejecución, y las plataformas completas (stacks) que integran todos los componentes necesarios.

### 6. Lenguajes y frameworks del lado del servidor

No todos los lenguajes se ejecutan de la misma manera en el servidor. Comprender estas diferencias es crucial para elegir la tecnología adecuada y desplegarla correctamente.

#### 6.1. Modelos de ejecución

**Lenguajes interpretados (Scripting)**

Ejemplos: PHP, Python, Ruby, Perl

El código fuente se lee y ejecuta línea por línea en cada petición:
- Desarrollo rápido
- Sin compilación previa
- Portabilidad total del código fuente
- Rendimiento menor

**Lenguajes compilados a nativo**

Ejemplos: Go, Rust, C, C++

El código se compila completamente a código máquina:
- Rendimiento máximo
- Binario único autocontenido
- Ideal para microservicios de alto rendimiento
- Recompilación necesaria en cambios

**Lenguajes de código intermedio**

Ejemplos: Java, C#, Kotlin, Scala

El código se compila a bytecode que ejecuta una máquina virtual:
- Buen rendimiento (JIT compilation)
- Portabilidad del bytecode
- Ecosistema empresarial maduro
- Detección temprana de errores

#### 6.2. Principales lenguajes servidor

**PHP:**
- El más popular históricamente para web
- Fácil integración con HTML
- Frameworks: Laravel, Symfony
- Ideal para: CMS, blogs, e-commerce tradicional

**Python:**
- Sintaxis elegante y clara
- Frameworks: Django, Flask, FastAPI
- Ideal para: Aplicaciones complejas, ML/AI

**Java:**
- Robusto y empresarial
- Frameworks: Spring Boot, Jakarta EE
- Ideal para: Aplicaciones empresariales grandes

**JavaScript/Node.js:**
- Mismo lenguaje frontend y backend
- Framework: Express, NestJS
- Ideal para: APIs, tiempo real, microservicios

---

### 7. Plataformas web completas (Stacks)

Una aplicación web no es solo código; necesita un ecosistema completo de software trabajando en conjunto. Las **plataformas web** o **stacks** integran todos estos componentes.

#### 7.1. Los cuatro pilares

Toda plataforma web necesita:

1. **Sistema Operativo**: Linux, Windows Server
2. **Servidor Web**: Apache, Nginx, IIS
3. **Base de Datos**: MySQL, PostgreSQL, MongoDB
4. **Lenguaje/Framework**: PHP, Python, Java, Node.js

#### 7.2. LAMP: La plataforma que construyó la web

**LAMP** = Linux + Apache + MySQL + PHP

**Por qué tuvo tanto éxito:**
- Completamente gratuito y open source
- Fácil de aprender
- Hosting universal
- Comunidad masiva
- WordPress, Drupal, Joomla lo usan

**Flujo típico en LAMP:**
```
Cliente → Linux recibe conexión
        → Apache procesa HTTP
        → PHP ejecuta script
        → MySQL consulta datos
        → PHP genera HTML
        → Apache envía respuesta
```

#### 7.3. WISA: La alternativa Microsoft

**WISA** = Windows Server + IIS + SQL Server + ASP.NET

**Cuándo elegir WISA:**
- Ecosistema Microsoft existente
- Integración con productos Microsoft
- Aplicaciones empresariales con .NET
- Soporte comercial requerido

**Desventaja:** Coste de licencias

#### 7.4. Stacks modernos

**MEAN/MERN:** MongoDB + Express + Angular/React + Node.js
- Todo JavaScript
- Ideal para SPAs modernas

**JAMStack:** JavaScript + APIs + Markup
- Todo estático + APIs
- Extremadamente rápido y económico

---

## BLOQUE 4: SERVICIOS Y COMUNICACIÓN

Con nuestra aplicación construida, necesitamos que se comunique con otras aplicaciones y clientes. Las **APIs** (Application Programming Interfaces) son el pegamento que une el ecosistema digital moderno.

### 8. Servicios web y APIs

Un **servicio web** es una aplicación accesible a través de la red (normalmente usando HTTP) que expone una interfaz para que otros clientes (navegadores, apps móviles, otros servicios, etc.) puedan utilizar sus funcionalidades.

Cuando esa interfaz está pensada para que la consuman **otras aplicaciones** y devuelve datos estructurados (JSON, XML, etc.), hablamos de una **API web**.

Podemos distinguir dos grandes tipos de componentes en la web:

1. **Aplicaciones web orientadas a usuario**  

    - Generan HTML (y recursos estáticos) para que el navegador los muestre al usuario.
    - Suelen usar plantillas, frameworks MVC, etc.

2. **Servicios web / APIs orientadas a aplicaciones**

    - Devuelven datos estructurados (JSON, XML, etc.).
    - Están pensados para ser consumidos por código: SPAs, apps móviles, otros servicios, integraciones…

#### 8.1. Diferencia fundamental

**Página web dinámica (aplicación web):**
- Genera HTML para humanos.
- Incluye estilos y presentación.
- Se visualiza en el navegador.

**Servicio web / API:**
- Devuelve datos estructurados (JSON/XML, u otros formatos).
- No incluye presentación ni estilos.
- Está pensado para ser consumido por código, no directamente por humanos.

#### 8.2. Estilos y tecnologías de APIs web

Existen varios estilos y tecnologías para construir APIs web. Los más comunes son:

**REST (Representational State Transfer)**

El estilo más extendido para APIs web. Características:
- Usa métodos HTTP estándar (GET, POST, PUT, DELETE…).
- Las URLs representan recursos.
- Sin estado en el servidor respecto al cliente (stateless).
- Se puede aprovechar la caché HTTP.
- Formato típico de intercambio: JSON.

Ejemplo:
```http
GET /api/usuarios/123
→ Devuelve: {"id": 123, "nombre": "Ana", "email": "ana@ejemplo.com"}

POST /api/usuarios
{"nombre": "Carlos", "email": "carlos@ejemplo.com"}
→ Crea un nuevo usuario
````

**GraphQL**

Lenguaje de consulta para APIs. Características:

* El cliente pide exactamente los campos que necesita.
* Permite obtener datos relacionados en una sola petición.
* Es fuertemente tipado.
* Reduce problemas de sobrecarga de datos (over-fetching) o falta de datos (under-fetching).

**WebSockets**

Tecnología para comunicación bidireccional en tiempo real sobre una conexión persistente:

* Mantiene una conexión abierta entre cliente y servidor.
* Ideal para chat, juegos online, dashboards en vivo, notificaciones en tiempo real, etc.
* Baja latencia y comunicación en ambas direcciones.


---

### 9. Autenticación con JWT

Las APIs necesitan verificar la identidad de quién las consume. **JWT (JSON Web Token)** es el estándar moderno para autenticación stateless.

#### 9.1. Estructura de JWT

Un JWT tiene tres partes separadas por puntos:

```
header.payload.signature
```

**Header:** Tipo de token y algoritmo
```json
{"alg": "HS256", "typ": "JWT"}
```

**Payload:** Datos del usuario (claims)
```json
{
  "sub": "123",
  "nombre": "Ana",
  "rol": "admin",
  "exp": 1700086400
}
```

**Signature:** Firma digital para verificar autenticidad

#### 9.2. Flujo de autenticación

1. Usuario hace login con credenciales
2. Servidor verifica y genera JWT
3. Servidor devuelve JWT al cliente
4. Cliente incluye JWT en cada petición:
   ```
   Authorization: Bearer eyJhbGci...
   ```
5. Servidor verifica JWT y extrae información del usuario

**Ventajas:**
- Stateless (sin sesiones en servidor): No necesita almacenar estado
- Escalable: Fácil de usar en microservicios
- Portable: Se puede usar entre dominios
- Autocontenido: Toda la información está en el token

**Seguridad:**
- Siempre HTTPS: Evita intercepciones
- Tiempo de expiración corto: Limita validez del token
- No guardar datos sensibles en payload: Ocultar información crítica
- El payload es visible (solo codificado, no encriptado): no almacenar contraseñas u otros datos sensibles.

---

## BLOQUE 5: INFRAESTRUCTURA Y SERVIDORES

Nuestro código necesita ejecutarse en algún lugar. Los **servidores web** y **servidores de aplicaciones** son el software que hace posible que nuestro código responda a peticiones HTTP.

### 10. Servidores web: Apache y Nginx

#### 10.1. ¿Qué es un servidor web?

Un **servidor web** es un programa que:
- Se ejecuta continuamente
- Escucha en puertos (80 HTTP, 443 HTTPS)
- Recibe peticiones HTTP
- Devuelve respuestas (archivos estáticos o delega a código dinámico)

#### 10.2. Apache HTTP Server

El veterano (desde 1995):

**Ventajas:**
- Extremadamente configurable
- Arquitectura modular
- Comunidad masiva
- .htaccess para configuración por directorio

**Módulos importantes:**
- mod_php: Ejecuta PHP directamente
- mod_ssl: HTTPS
- mod_rewrite: URLs amigables
- mod_proxy: Proxy inverso

**Configuración virtual host:**
```apache
<VirtualHost *:80>
    ServerName miapp.com
    DocumentRoot /var/www/miapp
    
    <Directory /var/www/miapp>
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

#### 10.3. Nginx

El moderno (desde 2004):

**Ventajas:**
- Alto rendimiento
- Bajo consumo de memoria
- Excelente para contenido estático
- Proxy inverso eficiente
- Configuración más simple

**Configuración server block:**
```nginx
server {
    listen 80;
    server_name miapp.com;
    root /var/www/miapp;
    
    location / {
        try_files $uri $uri/ =404;
    }
    
    location ~ \.php$ {
        fastcgi_pass unix:/var/run/php-fpm.sock;
        include fastcgi_params;
    }
}
```

**Comparativa:**
- Apache: Más flexible, más módulos, más memoria
- Nginx: Más rápido, menos memoria, mejor para estático

---

### 11. Servidores de aplicaciones y bases de datos

#### 11.1. Servidores de aplicaciones

Para lenguajes como Java, necesitamos **servidores de aplicaciones** que ejecuten el código:

**Apache Tomcat:**
- Servidor de aplicaciones Java
- Ejecuta Servlets y JSP
- Se despliegan archivos WAR
- Puede trabajar con Apache/Nginx como proxy

**Otros:**
- Gunicorn (Python)
- uWSGI (Python)
- WildFly (Java EE)
- IIS (ASP.NET)

#### 11.2. Gestores de bases de datos

**MySQL/MariaDB:**
- Relacionales (SQL)
- Las más populares para web
- Gratuitas y open source

**PostgreSQL:**
- Relacional avanzada
- Características empresariales
- Más robusta que MySQL

**MongoDB:**
- NoSQL documental
- Esquema flexible
- Ideal para datos no estructurados

Cada aplicación necesita su SGBD corriendo y configurado.

---

## BLOQUE 6: DESPLIEGUE Y OPERACIONES

Tenemos el código, los servidores configurados. Ahora debemos **llevar todo a producción** y asegurarnos de que puede crecer con la demanda.

### 12. Estrategias de despliegue y escalabilidad

#### 12.1. El concepto de despliegue

**Desplegar** no es solo copiar archivos. Implica:
- Instalar dependencias
- Configurar entornos
- Gestionar bases de datos
- Configurar servidores
- Establecer DNS
- Implementar SSL/TLS
- Configurar monitorización

**Entornos:**
- **Development**: Local, datos de prueba
- **Testing**: Pruebas automatizadas
- **Staging**: Réplica de producción
- **Production**: Usuarios reales

#### 12.2. Escalabilidad vertical (Scale Up)

La escalabilidad vertical, o "scale up", es la estrategia más intuitiva cuando una aplicación necesita más recursos: **hacer más potente el servidor existente**. Es como cambiar el motor de un coche por uno más grande cuando necesitáis más velocidad.

**¿En qué consiste?**

Cuando vuestra aplicación se queda sin recursos, podéis mejorar el hardware del servidor:

- **Más CPU**: Pasar de 4 núcleos a 8, 16 o incluso 64 núcleos. Esto permite procesar más peticiones simultáneamente y ejecutar cálculos más rápido.

- **Más RAM**: Aumentar de 8GB a 32GB, 64GB o incluso 256GB. Esto permite mantener más datos en memoria (lo cual es muchísimo más rápido que acceder al disco), cachear más información y manejar más conexiones simultáneas.

- **Discos más rápidos**: Cambiar de discos tradicionales HDD a SSD, o de SSD SATA a NVMe. Esto acelera dramáticamente la lectura/escritura de datos, las consultas a bases de datos, y la carga de archivos.

**Ventajas de la escalabilidad vertical:**

- **Simplicidad extrema**: No necesitáis cambiar nada en vuestro código. La aplicación sigue funcionando exactamente igual, solo que más rápida. No hay que preocuparse por distribuir datos o sincronizar múltiples servidores.

- **Configuración mínima**: El mismo servidor, la misma IP, las mismas configuraciones. Solo cambiáis el hardware (o en cloud, seleccionáis una máquina más grande).

- **Sin problemas de consistencia**: Como todo sigue en un solo servidor, no hay problemas de datos desincronizados o sesiones distribuidas.

**Desventajas que debéis conocer:**

- **Límite físico inevitable**: No podéis añadir CPUs infinitamente. Llega un punto donde simplemente no existen servidores más potentes, o son prohibitivamente caros (un servidor con 128 núcleos y 1TB de RAM puede costar más de 50.000€).

- **Punto único de fallo**: Si ese único servidor se cae (fallo de hardware, error de software, mantenimiento), **toda vuestra aplicación se cae**. No hay redundancia.

- **Tiempo de inactividad al escalar**: Para mejorar el hardware, normalmente necesitáis apagar el servidor, instalar el nuevo hardware, y reiniciarlo. Esto significa minutos u horas de inactividad.

- **Coste no lineal**: Duplicar la potencia del servidor puede costar 3 o 4 veces más, no el doble.

**Cuándo usar escalabilidad vertical:**

- Aplicaciones pequeñas o medianas que aún no necesitan alta disponibilidad
- Bases de datos que requieren toda la información en un solo lugar
- Como primer paso antes de ir a horizontal (es más fácil de implementar)

#### 12.3. Escalabilidad horizontal (Scale Out)

La escalabilidad horizontal, o "scale out", adopta un enfoque completamente diferente: en lugar de hacer un servidor más potente, **añadís más servidores trabajando en equipo**. Es como contratar más empleados en lugar de pedirle a uno solo que trabaje más rápido.

**¿Cómo funciona?**

En lugar de tener un superservidor, tenéis múltiples servidores "normales" trabajando juntos. Pero necesitáis un componente adicional crucial: el **balanceador de carga**.

**El balanceador de carga: el director de orquesta**

El balanceador de carga es un servidor especial que recibe todas las peticiones de los clientes y las distribuye inteligentemente entre los servidores disponibles:

```
              Internet
                 |
           Balanceador de Carga
           (decide a dónde va
            cada petición)
              / | \
             /  |  \
           /    |    \
       Srv1   Srv2   Srv3
    (8GB RAM) (8GB) (8GB)
```

Cuando un usuario hace una petición, el balanceador decide qué servidor está menos ocupado o es más apropiado, y envía la petición ahí. El usuario nunca sabe cuántos servidores hay detrás; para él, es transparente.

**Ventajas poderosas:**

- **Sin límite teórico**: ¿Necesitáis el doble de capacidad? Añadís el doble de servidores. ¿Triple? Triple de servidores. Podéis escalar a cientos o miles de servidores si es necesario. Netflix, por ejemplo, usa miles de servidores.

- **Alta disponibilidad (HA)**: Si un servidor se cae, los otros siguen funcionando. El balanceador simplemente deja de enviar peticiones al servidor caído. Los usuarios ni siquiera notan el problema.

- **Tolerancia a fallos real**: Podéis actualizar los servidores uno por uno sin tiempo de inactividad. Actualizas Srv1 mientras Srv2 y Srv3 siguen funcionando, luego Srv2, luego Srv3. Despliegue sin caídas (zero-downtime deployment).

- **Escalado elástico**: En cloud, podéis añadir servidores automáticamente cuando hay mucho tráfico (por ejemplo, el Black Friday) y quitarlos cuando baja. Solo pagáis por lo que usáis.

**Desventajas y complejidades:**

- **Arquitectura más compleja**: Vuestro código debe estar preparado para ejecutarse en múltiples máquinas. No podéis asumir que dos peticiones del mismo usuario llegarán al mismo servidor.

- **Problema de sesiones compartidas**: Si un usuario inicia sesión en Srv1 y la siguiente petición va a Srv2, Srv2 no sabe que el usuario está logueado. Necesitáis soluciones como:
    - **Sticky sessions**: El balanceador envía al mismo usuario siempre al mismo servidor
    - **Sesiones en base de datos compartida**: Todos los servidores leen sesiones de Redis o una BD central
    - **Tokens JWT**: El estado viaja en el token, no en el servidor

- **Coste operacional mayor**: Más servidores significan más configuración, más monitorización, más complejidad en despliegues. Necesitáis herramientas de automatización (Ansible, Terraform, Kubernetes).

- **Sincronización de datos**: Si tenéis archivos subidos por usuarios, cachés, o datos temporales, necesitáis aseguraros de que todos los servidores tengan acceso a los mismos datos (mediante sistemas de archivos compartidos como NFS o S3).

**El escenario típico: horizontal + vertical**

En la práctica, las empresas suelen combinar ambas estrategias:

1. **Empiezas con un servidor decente** (escalabilidad vertical)
2. **Cuando llegas al límite, añades más servidores** (escalabilidad horizontal)
3. **Si cada servidor necesita más potencia, los mejoras** (vertical de nuevo)

Es un enfoque híbrido que ofrece lo mejor de ambos mundos. Por ejemplo, tener 10 servidores de 16GB RAM cada uno, en lugar de 1 servidor de 160GB o 100 servidores de 1.6GB.

---

### 13. Contenedores y orquestación

Si habéis trabajado en desarrollo, probablemente habéis oído la frase más frustrante del mundo: **"En mi máquina funciona"**. Un compañero os pasa su código, lo ejecutáis en vuestra máquina, y... error. ¿Por qué? Porque tiene Python 3.9 y vos tenéis 3.11. O usa una librería que no tenéis instalada. O su base de datos tiene configuraciones diferentes. Los **contenedores** nacieron para eliminar este problema de una vez por todas, y han revolucionado completamente cómo desplegamos aplicaciones modernas.

#### 13.1. Docker: empaquetando la consistencia

**¿Qué es realmente un contenedor?**

Pensad en un contenedor como una **cápsula autocontenida** que incluye absolutamente TODO lo que vuestra aplicación necesita para funcionar:

- **La aplicación en sí**: Vuestro código, ya sea Python, Node.js, Java, PHP...

- **Todas las dependencias**: Cada librería, cada paquete, cada módulo que vuestra aplicación necesita. Si usa Flask 2.0.1, el contenedor incluirá exactamente Flask 2.0.1, no otra versión.

- **El runtime**: El intérprete de Python, el motor de Node.js, la JVM de Java... todo lo que ejecuta vuestro código.

- **Configuración y sistema base**: Un sistema operativo Linux mínimo, variables de entorno, archivos de configuración.

Todo esto empaquetado en una "imagen" que podéis mover a cualquier máquina, y funcionará exactamente igual. Es como tener un ordenador virtual súper liviano dedicado exclusivamente a vuestra aplicación.

**Las ventajas que cambian todo:**

- **"Funciona en mi máquina" → funciona en TODAS las máquinas**: Si funciona en vuestro portátil, funcionará igual en el servidor de producción, en el ordenador de vuestro compañero, en AWS, en Google Cloud, en cualquier lado. Esto elimina el 90% de los problemas de despliegue.

- **Portabilidad total y real**: La misma imagen Docker puede ejecutarse en Windows, Mac, Linux, servidores físicos, máquinas virtuales, cualquier proveedor cloud. No importa dónde, funciona igual.

- **Despliegue consistente**: No más scripts de instalación complejos que fallan a mitad. No más "instala esto, configura aquello, espera que funcione". Solo haces `docker run` y listo.

- **Ligero comparado con máquinas virtuales**: Una máquina virtual completa puede ocupar varios GB y tardar minutos en arrancar. Un contenedor ocupa MB y arranca en segundos, porque comparte el kernel del sistema operativo host.

**Un ejemplo real de Dockerfile:**

```dockerfile
# Empezamos con una imagen base que ya tiene PHP 8.2 y Apache
FROM php:8.2-apache

# Copiamos nuestro código a la carpeta que Apache sirve
COPY . /var/www/html/

# Instalamos la extensión de MySQL que nuestra app necesita
RUN docker-php-ext-install mysqli

# Le decimos que la aplicación escucha en el puerto 80
EXPOSE 80
```

Con estas 5 líneas simples, habéis creado una imagen que cualquiera puede ejecutar y tendrá exactamente el mismo entorno que vosotros. Es poderoso en su simplicidad.

#### 13.2. Docker Compose: orquestando múltiples contenedores

La mayoría de aplicaciones reales no son un solo contenedor. Tenéis el servidor web, vuestra aplicación, la base de datos, quizás Redis para caché, quizás un servidor de colas... **Docker Compose** os permite definir y gestionar todas estas piezas juntas con elegancia.

**El poder de la declaración simple:**

En lugar de ejecutar múltiples comandos `docker run` con cientos de parámetros, definís todo en un archivo YAML legible:

```yaml
version: '3'
services:
  # Servidor web
  web:
    image: nginx
    ports:
      - "80:80"      # Puerto del host:Puerto del contenedor
    volumes:
      - ./config:/etc/nginx/conf.d
  
  # Aplicación PHP
  app:
    image: php:fpm
    volumes:
      - ./code:/var/www/html
  
  # Base de datos
  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: miapp
    volumes:
      - db-data:/var/lib/mysql

# Volúmenes persistentes
volumes:
  db-data:
```

Con un simple `docker-compose up`, los tres servicios arrancan, se conectan entre sí automáticamente, y vuestra aplicación está funcionando. Con `docker-compose down`, todo se detiene limpiamente. Es desarrollo y testing local simplificado al máximo.

**Por qué esto es revolucionario:**

- Cualquier desarrollador nuevo puede tener el entorno completo funcionando en 5 minutos
- No hay que instalar MySQL, PHP, Nginx en vuestra máquina
- Podéis tener 5 proyectos diferentes con versiones diferentes de MySQL sin conflictos
- El entorno de desarrollo es idéntico al de producción

#### 13.3. Kubernetes: cuando necesitáis escalar en serio

Docker Compose es perfecto para desarrollo local o aplicaciones pequeñas. Pero ¿qué pasa cuando tenéis que gestionar cientos o miles de contenedores en decenas de servidores? Ahí entra **Kubernetes** (abreviado como K8s).

**Orquestación a escala empresarial:**

Kubernetes es como el director de orquesta que coordina miles de músicos (contenedores) para que toquen en armonía:

- **Gestiona cientos o miles de contenedores**: K8s puede manejar un cluster de 1.000 servidores ejecutando 10.000 contenedores. Google usa Kubernetes para manejar billones de contenedores.

- **Escalado automático**: Si el CPU sube del 70%, K8s automáticamente crea más réplicas de tu contenedor. Si baja del 30%, las elimina. Todo automático, todo el tiempo.

- **Auto-recuperación (self-healing)**: Si un contenedor se cae, K8s lo detecta y automáticamente inicia uno nuevo. Si un servidor entero se cae, K8s mueve todos los contenedores de ese servidor a otros servidores sanos.

- **Rolling updates (actualizaciones sin caídas)**: Podéis desplegar una nueva versión de vuestra aplicación sin downtime. K8s va actualizando contenedores uno por uno, verificando que funcionen antes de continuar con el siguiente.

- **Service discovery automático**: Los contenedores no necesitan saber dónde están otros contenedores. K8s les proporciona nombres DNS automáticos que siempre funcionan.

**Conceptos clave de Kubernetes:**

- **Pod**: El contenedor (o grupo de contenedores) más pequeño que K8s gestiona. Es como el átomo de Kubernetes.

- **Deployment**: Define cómo debe ejecutarse vuestra aplicación: qué imagen usar, cuántas réplicas querer, etc.

- **Service**: Proporciona una dirección IP y nombre DNS estables para acceder a tus pods, aunque éstos se creen y destruyan constantemente.

- **Ingress**: Gestiona el tráfico HTTP/HTTPS externo, actuando como un reverse proxy inteligente.

**El precio de tanto poder:**

Kubernetes es extraordinariamente potente, pero también es complejo. La curva de aprendizaje es pronunciada. Por eso existen servicios gestionados como **Google Kubernetes Engine** (GKE), **Amazon EKS**, o **Azure AKS** que os quitan gran parte de la complejidad operacional.
- Rolling updates
- Service discovery

**Conceptos clave:**
- **Pod**: Grupo de contenedores
- **Deployment**: Definición de aplicación
- **Service**: Acceso a la aplicación
- **Ingress**: Routing HTTP

---

### 14. Cloud computing y CI/CD

#### 14.1. Cloud Computing

La **nube** proporciona infraestructura bajo demanda:

**Modelos:**
- **IaaS** (Infrastructure): Máquinas virtuales (EC2, Compute Engine)
- **PaaS** (Platform): Plataforma gestionada (Heroku, App Engine)
- **SaaS** (Software): Aplicación completa (Gmail, Office 365)

**Proveedores principales:**
- AWS (Amazon)
- Google Cloud Platform
- Microsoft Azure

**Ventajas:**
- Pago por uso
- Escalabilidad infinita
- Alta disponibilidad
- Sin gestión de hardware

#### 14.2. CI/CD (Integración y Despliegue Continuos)

**Continuous Integration:**
- Cada commit ejecuta tests automáticos
- Detecta errores rápidamente
- Integración frecuente

**Continuous Deployment:**
- Despliegue automático a producción
- Tras pasar todos los tests
- Entregas frecuentes

**Pipeline típico:**
```
Commit → Build → Test → Deploy → Monitor
```

**Herramientas:**
- GitHub Actions
- GitLab CI/CD
- Jenkins
- CircleCI

---

## BLOQUE 7: SEGURIDAD Y MONITORIZACIÓN

Una aplicación desplegada sin seguridad ni monitorización es un desastre esperando ocurrir. Este bloque final es crítico para operaciones profesionales.

### 15. Seguridad en servidores web

#### 15.1. Importancia de la seguridad

Las consecuencias de una brecha son devastadoras:
- Pérdida financiera (multas GDPR hasta €20M)
- Daño reputacional irreparable
- Responsabilidades legales
- Pérdida de datos

**Principios:**
- **Defensa en profundidad**: Múltiples capas de seguridad
- **Mínimo privilegio**: Solo permisos necesarios
- **Security by design**: Seguridad desde el diseño

#### 15.2. Autenticación HTTP

**Basic Authentication:**
```apache
<Directory /var/www/admin>
    AuthType Basic
    AuthName "Area Restringida"
    AuthUserFile /etc/apache2/.htpasswd
    Require valid-user
</Directory>
```

Crear archivo de contraseñas:
```bash
htpasswd -c /etc/apache2/.htpasswd admin
```

**Limitaciones:** Credenciales en Base64 (usar solo con HTTPS)

#### 15.3. Control de acceso por IP

```apache
<Directory /var/www/admin>
    Require ip 192.168.1.0/24
    Require ip 10.0.0.5
</Directory>
```

#### 15.4. HTTPS obligatorio

```apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}/$1 [R=301,L]
```

**Certificados:**
- Let's Encrypt (gratuito, automático)
- Certificados comerciales

---

### 16. Monitorización y análisis de logs

#### 16.1. ¿Por qué monitorizar?

- Detectar problemas antes de que afecten usuarios
- Entender el comportamiento del sistema
- Auditoría de seguridad
- Optimización de rendimiento

#### 16.2. Logs de Apache

**Access log:**
```
192.168.1.10 - - [27/Nov/2025:15:30:45 +0100] "GET /index.html HTTP/1.1" 200 1234
```

Formato CLF (Common Log Format):
- IP del cliente
- Fecha y hora
- Método y recurso
- Código de estado
- Tamaño de respuesta

**Error log:**
Registra errores del servidor, warnings, problemas de configuración.

#### 16.3. Análisis de logs

**Comandos útiles:**
```bash
# Ver últimas líneas en tiempo real
tail -f /var/log/apache2/access.log

# Contar peticiones por IP
awk '{print $1}' access.log | sort | uniq -c | sort -rn

# Filtrar errores 404
grep ' 404 ' access.log

# Ver códigos de estado más comunes
awk '{print $9}' access.log | sort | uniq -c | sort -rn
```

**Herramientas:**
- **AWStats**: Estadísticas web
- **GoAccess**: Análisis en tiempo real
- **ELK Stack**: Elasticsearch + Logstash + Kibana (profesional)

#### 16.4. Rotación de logs

Los logs crecen indefinidamente. Necesitamos **rotarlos**:

```bash
# /etc/logrotate.d/apache2
/var/log/apache2/*.log {
    daily
    missingok
    rotate 14
    compress
    delaycompress
    notifempty
    create 640 root adm
    sharedscripts
    postrotate
        /etc/init.d/apache2 reload > /dev/null
    endscript
}
```

Esto mantiene 14 días de logs, comprimidos.

#### 16.5. Monitorización del servidor

**Métricas clave:**
- CPU: Uso de procesador
- RAM: Memoria disponible
- Disco: Espacio libre
- Red: Ancho de banda

**Herramientas:**
- **Nagios**: Monitorización clásica
- **Zabbix**: Completo y open source
- **Prometheus + Grafana**: Stack moderno
- **New Relic / Datadog**: SaaS comercial

**Alertas:**
Configurar alertas cuando:
- CPU > 90% durante 5 minutos
- Disco < 10% libre
- Aplicación no responde
- Errores 5xx aumentan

---

## Resumen de la unidad

Hemos completado un viaje exhaustivo por el desarrollo y despliegue de aplicaciones web:

**BLOQUE 1 - FUNDAMENTOS:**
- HTTP/HTTPS es la base de toda comunicación web
- Contenido estático vs dinámico define capacidades

**BLOQUE 2 - ARQUITECTURA:**
- División cliente-servidor y responsabilidades
- Arquitecturas desde monolíticas a microservicios
- Patrones MVC y principios SOLID

**BLOQUE 3 - IMPLEMENTACIÓN:**
- Lenguajes servidor y sus modelos de ejecución
- Plataformas completas (LAMP, WISA, stacks modernos)

**BLOQUE 4 - COMUNICACIÓN:**
- APIs REST, GraphQL, WebSockets
- Autenticación con JWT

**BLOQUE 5 - INFRAESTRUCTURA:**
- Servidores web (Apache, Nginx)
- Servidores de aplicaciones y bases de datos

**BLOQUE 6 - DESPLIEGUE:**
- Estrategias de escalabilidad
- Contenedores (Docker, Kubernetes)
- Cloud y CI/CD

**BLOQUE 7 - OPERACIONES:**
- Seguridad en servidores
- Monitorización y logs

Este conocimiento os prepara para enfrentar los retos reales del desarrollo y despliegue de aplicaciones web modernas.

---

## Referencias y bibliografía

- [Jose Luis González](https://github.com/joseluisgs). *Despliegue de aplicaciones Web - 2025 2026*. [https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026](https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026)
- Fielding, R. T. (2000). *Architectural Styles and the Design of Network-based Software Architectures*
- Fowler, M. (2002). *Patterns of Enterprise Application Architecture*
- Martin, R. C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure*
- Newman, S. (2021). *Building Microservicios: Designing Fine-Grained Systems* (2nd ed.)
- Mozilla Developer Network. (2024). *Web Development*. [https://developer.mozilla.org](https://developer.mozilla.org)
- IETF. (2022). *RFC 9110: HTTP Semantics*
- IETF. (2015). *RFC 7519: JSON Web Token (JWT)*

## Recursos adicionales

- [MDN Web Docs](https://developer.mozilla.org/) - Documentación web completa
- [Docker Documentation](https://docs.docker.com/) - Guías de contenedores
- [Kubernetes Documentation](https://kubernetes.io/docs/) - Orquestación
- [AWS Documentation](https://docs.aws.amazon.com/) - Cloud computing
- [Nginx Documentation](https://nginx.org/en/docs/) - Servidor web
- [Let's Encrypt](https://letsencrypt.org/) - Certificados SSL gratuitos
- [Postman](https://www.postman.com/) - Testing de APIs
- [JWT.io](https://jwt.io/) - Herramienta JWT

