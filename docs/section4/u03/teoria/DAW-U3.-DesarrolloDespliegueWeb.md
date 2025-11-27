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

---

## BLOQUE 1: FUNDAMENTOS DE LA WEB

Antes de construir aplicaciones complejas, debemos entender perfectamente cómo se comunican y qué tipos de contenido pueden generar. Este primer bloque establece los cimientos sobre los que construiremos todo lo demás.

### 1. Protocolo HTTP/HTTPS y comunicación web

En las unidades anteriores hemos aprendido sobre los componentes de una aplicación web y cómo se divide el código entre cliente y servidor. Pero, ¿cómo se comunican realmente estos dos componentes? La respuesta está en el **protocolo HTTP**, el lenguaje universal de la web.

Cada vez que escribís una URL en el navegador, hacéis clic en un enlace o enviáis un formulario, estáis utilizando HTTP. Es el protocolo que hace posible que podáis leer esta página, ver vídeos en YouTube o comprar en Amazon. Entenderlo es fundamental para cualquier profesional del desarrollo y despliegue de aplicaciones web.

#### 1.1. Características y ventajas del protocolo HTTP

El **Protocolo HTTP (HyperText Transfer Protocol)** es la base de la comunicación en la World Wide Web. Fue creado por Tim Berners-Lee en 1989 y se ha convertido en el estándar para la transferencia de información en Internet.

#### 1.2. Definición y concepto

HTTP es un protocolo de **capa de aplicación** que define cómo se estructuran y envían los mensajes entre clientes y servidores web. Es un protocolo **no orientado a la conexión**, lo que significa que cada petición entre cliente y servidor es independiente y no requiere mantener una conexión continua.

**Arquitectura básica:**

- **Cliente**: Típicamente un navegador web que inicia las peticiones
- **Servidor**: Aplicación que escucha y responde a las peticiones
- **Recursos**: Documentos, imágenes, datos que se intercambian
- **Mensajes**: Peticiones (requests) y respuestas (responses)

#### 1.3. Características principales

HTTP tiene características que lo hacen ideal para la web:

**Sencillo**

- Es un protocolo en modo texto legible por humanos
- Fácil de entender y depurar
- Se puede probar directamente con herramientas simples como `curl` o `telnet`

```bash
# Ejemplo de petición HTTP manual con curl
curl -v http://www.ejemplo.com
```

**Extensible**

- Se pueden añadir cabeceras personalizadas
- Permite enviar metadatos adicionales más allá de los estándares
- Facilita la evolución del protocolo sin romper compatibilidad

**Sin estado (Stateless)**

- Cada petición es independiente de las anteriores
- El servidor no guarda información sobre peticiones previas
- Simplifica el diseño del servidor y mejora la escalabilidad

!!! warning "El problema del estado"
    Que HTTP sea stateless presenta un desafío: ¿cómo mantener la sesión de un usuario (por ejemplo, en un carrito de compra)? La solución son las **cookies** y las **sesiones**, que estudiaremos en detalle más adelante.

#### 1.4. Ventajas del protocolo HTTP

HTTP ofrece múltiples ventajas que lo han convertido en el protocolo estándar de Internet:

**Control de caché**

- Permite especificar cómo y cuándo se almacenan temporalmente los recursos
- Mejora significativamente la velocidad de carga
- Reduce el consumo de ancho de banda
- Las cabeceras `Cache-Control` y `Expires` controlan este comportamiento

**Autenticación**

- Soporta varios mecanismos de autenticación (Basic, Digest, Bearer)
- Permite verificar la identidad de los usuarios
- Protege recursos sensibles

**Uso de proxies**

- Facilita el uso transparente de servidores intermediarios
- Permite filtrado, caché compartida, balanceo de carga
- Mejora la seguridad y el rendimiento

**Mantenimiento de sesiones**

- Aunque HTTP es stateless, soporta cookies
- Las cookies permiten mantener el estado entre peticiones
- Esencial para aplicaciones web modernas

**Negociación de contenido**

- El cliente puede indicar qué formatos acepta
- El servidor puede responder en el formato más adecuado
- Facilita la internacionalización y la adaptación a dispositivos

<figure markdown="span">
  ![Protocolo HTTP](assets/http.png){ width="700" }
  <figcaption>Diagrama del protocolo HTTP mostrando el flujo de comunicación entre cliente y servidor: el cliente envía una petición (request) con método, URL y cabeceras; el servidor responde con un código de estado, cabeceras y el contenido solicitado</figcaption>
</figure>

#### 1.5. Importancia en arquitecturas modernas

HTTP es fundamental en las arquitecturas web actuales:

- **APIs REST**: Se basan completamente en HTTP y sus métodos
- **Microservicios**: Utilizan HTTP para comunicarse entre sí
- **Aplicaciones web**: Toda interacción usa HTTP/HTTPS
- **Internet de las Cosas (IoT)**: Muchos dispositivos usan HTTP para comunicarse

!!! tip "HTTP es universal"
    HTTP es tan universal que incluso aplicaciones que no son web (como aplicaciones móviles o de escritorio) suelen usar HTTP para comunicarse con sus servidores, aprovechando su simplicidad y las herramientas existentes.

#### 1.6. Formato de peticiones y respuestas HTTP

La interacción en la web se basa en un intercambio constante de **peticiones** (requests) y **respuestas** (responses) HTTP entre el navegador del cliente y el servidor. Entender su estructura es fundamental.

#### 1.7. Estructura de una petición HTTP

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

#### 1.8. Estructura de una respuesta HTTP

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

#### 1.9. Cabeceras HTTP

Las cabeceras HTTP son líneas de metadatos que se envían tanto en las peticiones como en las respuestas. Proporcionan información crucial sobre la comunicación entre cliente y servidor.

#### 1.10. Cabeceras de petición comunes

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

#### 1.11. Cabeceras de respuesta comunes

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

#### 1.12. Tipos MIME más comunes

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

#### 1.13. Métodos HTTP (verbos HTTP)

Los métodos HTTP, también llamados **verbos HTTP**, definen la acción que un cliente desea realizar sobre un recurso en el servidor. Son fundamentales para el diseño de APIs RESTful.

<figure markdown="span">
  ![Métodos HTTP](assets/http-metodos.gif){ width="600" }
  <figcaption>Representación visual de los principales métodos HTTP y sus acciones: GET para obtener, POST para crear, PUT para actualizar, DELETE para eliminar. Cada método tiene un propósito específico en la manipulación de recursos del servidor</figcaption>
</figure>

#### 1.14. GET - Obtener recursos

**Propósito**: Obtener o recuperar un recurso del servidor.

**Características:**

- **Idempotente**: Múltiples peticiones idénticas tienen el mismo efecto que una sola
- **Seguro**: No modifica el estado del servidor
- **Cacheable**: Las respuestas pueden ser cacheadas
- **Sin cuerpo**: Los parámetros van en la URL (query string)

**Ejemplos:**

```http
GET /usuarios HTTP/1.1
Host: api.ejemplo.com
```

```http
GET /usuarios/123 HTTP/1.1
Host: api.ejemplo.com
```

```http
GET /productos?categoria=electronica&precio_max=500 HTTP/1.1
Host: api.ejemplo.com
```

**Usos típicos:**

- Listar recursos: `GET /productos`
- Obtener un recurso específico: `GET /productos/42`
- Búsquedas: `GET /buscar?q=laptop`
- Cargar páginas web

!!! warning "GET no debe modificar"
    Aunque técnicamente es posible, **nunca** se debe usar GET para operaciones que modifiquen el estado del servidor (crear, actualizar, borrar). Esto viola el principio de que GET es un método seguro.

#### 1.15. POST - Crear recursos

**Propósito**: Enviar datos al servidor, típicamente para crear un nuevo recurso.

**Características:**

- **No idempotente**: Múltiples peticiones crean múltiples recursos
- **No seguro**: Modifica el estado del servidor
- **No cacheable** por defecto
- **Con cuerpo**: Los datos van en el cuerpo de la petición

**Ejemplo:**

```http
POST /usuarios HTTP/1.1
Host: api.ejemplo.com
Content-Type: application/json
Content-Length: 85

{
    "nombre": "María García",
    "email": "maria@ejemplo.com",
    "rol": "estudiante"
}
```

**Respuesta típica:**

```http
HTTP/1.1 201 Created
Location: /usuarios/456
Content-Type: application/json

{
    "id": 456,
    "nombre": "María García",
    "email": "maria@ejemplo.com",
    "rol": "estudiante",
    "creado": "2025-11-19T15:30:00Z"
}
```

**Usos típicos:**

- Crear recursos: `POST /productos`
- Enviar formularios: `POST /contacto`
- Subir archivos: `POST /uploads`
- Login: `POST /api/login`

#### 1.16. PUT - Actualizar recursos

**Propósito**: Actualizar o reemplazar completamente un recurso existente.

**Características:**

- **Idempotente**: Múltiples peticiones idénticas tienen el mismo efecto
- **No seguro**: Modifica el estado del servidor
- **Reemplaza completamente**: Sustituye el recurso entero

**Ejemplo:**

```http
PUT /usuarios/456 HTTP/1.1
Host: api.ejemplo.com
Content-Type: application/json

{
    "nombre": "María García López",
    "email": "maria.garcia@ejemplo.com",
    "rol": "profesor"
}
```

**Diferencia con POST:**

- **POST**: Crea un nuevo recurso (el servidor decide el ID)
- **PUT**: Actualiza un recurso existente (el cliente especifica el ID)

#### 1.17. PATCH - Actualización parcial

**Propósito**: Actualizar parcialmente un recurso.

**Características:**

- **No idempotente** necesariamente
- **No seguro**: Modifica el estado del servidor
- **Actualiza parcialmente**: Solo modifica los campos especificados

**Ejemplo:**

```http
PATCH /usuarios/456 HTTP/1.1
Host: api.ejemplo.com
Content-Type: application/json

{
    "email": "nuevo.email@ejemplo.com"
}
```

Con PUT habría que enviar todos los campos del usuario, con PATCH solo los que cambian.

#### 1.18. DELETE - Eliminar recursos

**Propósito**: Borrar un recurso del servidor.

**Características:**

- **Idempotente**: Borrar varias veces tiene el mismo efecto
- **No seguro**: Modifica el estado del servidor

**Ejemplo:**

```http
DELETE /usuarios/456 HTTP/1.1
Host: api.ejemplo.com
```

**Respuesta típica:**

```http
HTTP/1.1 204 No Content
```

O también:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "mensaje": "Usuario eliminado correctamente"
}
```

#### 1.19. HEAD - Obtener metadatos

**Propósito**: Solicitar las mismas cabeceras que GET, pero sin el cuerpo de la respuesta.

**Características:**

- **Idempotente** y **seguro**
- Útil para verificar la existencia de un recurso
- Útil para obtener metadatos sin descargar el contenido

**Ejemplo:**

```http
HEAD /archivos/documento.pdf HTTP/1.1
Host: cdn.ejemplo.com
```

**Respuesta:**

```http
HTTP/1.1 200 OK
Content-Type: application/pdf
Content-Length: 2456789
Last-Modified: Mon, 18 Nov 2025 10:00:00 GMT
```

**Usos típicos:**

- Verificar si un recurso existe sin descargarlo
- Obtener el tamaño de un archivo antes de descargarlo
- Verificar si un recurso ha sido modificado

#### 1.20. OPTIONS - Opciones disponibles

**Propósito**: Obtener los métodos HTTP soportados por un recurso.

**Ejemplo:**

```http
OPTIONS /api/usuarios HTTP/1.1
Host: api.ejemplo.com
```

**Respuesta:**

```http
HTTP/1.1 200 OK
Allow: GET, POST, PUT, DELETE, OPTIONS
```

Es especialmente importante en **CORS** (Cross-Origin Resource Sharing).

#### 1.21. Tabla resumen de métodos HTTP

| Método      | Propósito            | Idempotente  | Seguro  | Con cuerpo  | Cacheable  |
|:------------|:---------------------|:-------------|:--------|:------------|:-----------|
| **GET**     | Obtener recurso      | ✓            | ✓       | No          | ✓          |
| **POST**    | Crear recurso        | ✗            | ✗       | Sí          | ✗          |
| **PUT**     | Actualizar completo  | ✓            | ✗       | Sí          | ✗          |
| **PATCH**   | Actualizar parcial   | ✗            | ✗       | Sí          | ✗          |
| **DELETE**  | Eliminar recurso     | ✓            | ✗       | No          | ✗          |
| **HEAD**    | Obtener metadatos    | ✓            | ✓       | No          | ✓          |
| **OPTIONS** | Opciones disponibles | ✓            | ✓       | No          | ✗          |

!!! tip "Diseño de APIs RESTful"
    El uso correcto de los métodos HTTP es fundamental para diseñar APIs RESTful bien estructuradas. Cada método tiene un propósito específico y debe usarse según su semántica.

#### 1.22. Códigos de estado HTTP

Después de cada petición, el servidor envía una respuesta que incluye un **código de estado HTTP**. Este código es un número de tres dígitos que indica el resultado de la petición.

<figure markdown="span">
  ![Códigos de estado HTTP](assets/status-code.png){ width="700" }
  <figcaption>Clasificación de los códigos de estado HTTP organizados por familias: 1xx (Informativos), 2xx (Éxito), 3xx (Redirección), 4xx (Errores del cliente), 5xx (Errores del servidor). Cada familia indica un tipo diferente de resultado de la petición</figcaption>
</figure>

#### 1.23. Familia 1xx - Respuestas informativas

Indican que la petición ha sido recibida y el proceso continúa.

| Código  | Nombre              | Descripción                                            |
|:--------|:--------------------|:-------------------------------------------------------|
| **100** | Continue            | El cliente puede continuar con su petición             |
| **101** | Switching Protocols | El servidor acepta cambiar de protocolo                |
| **102** | Processing          | El servidor está procesando, pero aún no hay respuesta |

**Uso poco común**: Raramente se encuentran estos códigos en aplicaciones web típicas.

#### 1.24. Familia 2xx - Operaciones exitosas

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

#### 1.25. Familia 3xx - Redirecciones

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

#### 1.26. Familia 4xx - Errores del cliente

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

#### 1.27. Familia 5xx - Errores del servidor

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

#### 1.28. El protocolo HTTPS: seguridad en la web

**HTTPS (HyperText Transfer Protocol Secure)** es la versión segura del protocolo HTTP. En la web moderna, HTTPS no es opcional: es **esencial** para la seguridad y privacidad de los usuarios.

#### 1.29. ¿Por qué es necesario HTTPS?

HTTP transmite datos en **texto plano**, lo que significa que cualquiera que intercepte la comunicación puede leer todo:

- Contraseñas
- Números de tarjetas de crédito
- Mensajes privados
- Cookies de sesión
- Cualquier dato enviado o recibido

**Amenazas sin HTTPS:**

- **Eavesdropping (escucha)**: Un atacante puede leer toda la comunicación
- **Man-in-the-Middle (MITM)**: Un atacante puede interceptar y modificar los datos
- **Suplantación**: Un atacante puede hacerse pasar por el servidor
- **Session hijacking**: Robo de cookies de sesión

!!! danger "HTTP está obsoleto"
    Los navegadores modernos marcan los sitios HTTP como "No seguros". Google penaliza en SEO a los sitios sin HTTPS. Algunas APIs (como geolocalización) solo funcionan en HTTPS.

#### 1.30. ¿Cómo funciona HTTPS?

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

#### 1.31. Certificados digitales

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

#### 1.32. Tipos de certificados

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

#### 1.33. Let's Encrypt: certificados gratuitos

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

#### 1.34. Impacto en el rendimiento

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

#### 1.35. HTTPS en desarrollo

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

#### 1.36. Buenas prácticas HTTPS

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

## Resumen de la unidad

En esta unidad hemos aprendido:

1. **HTTP** es el protocolo fundamental de la web: sencillo, extensible y stateless.

2. **Las peticiones y respuestas HTTP** tienen una estructura clara con línea de estado, cabeceras y cuerpo.

3. **Las cabeceras HTTP** proporcionan metadatos esenciales sobre la comunicación.

4. **Los métodos HTTP** (GET, POST, PUT, DELETE, etc.) definen las acciones sobre recursos.

5. **Los códigos de estado** indican el resultado de una petición (2xx éxito, 4xx error cliente, 5xx error servidor).

6. **HTTPS** es esencial para la seguridad, cifrando la comunicación mediante SSL/TLS y certificados digitales.

HTTP y HTTPS son los cimientos sobre los que se construyen las aplicaciones web y las APIs modernas. Dominarlos es fundamental para cualquier desarrollador o ingeniero DevOps.


---

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

**Características:**
- Código fuente único y unificado
- Se despliega como una sola unidad
- Todos los componentes comparten recursos
- Base de datos única

**Ventajas:**
- Simple de desarrollar inicialmente
- Fácil de probar (todo en un lugar)
- Despliegue sencillo
- Rendimiento interno óptimo (llamadas en memoria)

**Desventajas:**
- Difícil de escalar selectivamente
- Cambios requieren redesplegar todo
- Acoplamiento alto entre componentes
- Difícil de mantener a medida que crece

#### 4.2. Arquitectura de microservicios

En contraposición al monolito, los **microservicios** dividen la aplicación en pequeños servicios independientes, cada uno enfocado en una función específica del negocio.

**Principios fundamentales:**
- Servicios pequeños y enfocados
- Despliegue independiente
- Comunicación vía APIs
- Bases de datos descentralizadas
- Fallos aislados

**Ventajas:**
- Escalabilidad granular
- Agilidad en desarrollo
- Tecnologías heterogéneas
- Resiliencia mejorada

**Desventajas:**
- Complejidad operacional
- Latencia de red
- Gestión de transacciones distribuidas
- Requiere DevOps maduro

**Ejemplo: Netflix**

Netflix es el caso de estudio por excelencia de microservicios exitosos. Su plataforma se compone de cientos de microservicios que gestionan diferentes aspectos: autenticación, recomendaciones, streaming, facturación, etc. Cada servicio puede actualizarse, desplegarse y escalarse independientemente.

#### 4.3. Otras arquitecturas modernas

**Arquitectura de capas:**
Organiza el código en capas horizontales (presentación, lógica, datos), donde cada capa solo se comunica con la inmediatamente inferior.

**Arquitectura serverless:**
Elimina la gestión de servidores delegándola al proveedor cloud. El código se ejecuta en funciones individuales activadas por eventos.

**Arquitectura event-driven:**
Los componentes se comunican mediante eventos asíncronos, mejorando el desacoplamiento y la escalabilidad.

---

### 5. Patrón MVC y principios de diseño

Independientemente de la arquitectura general elegida, necesitamos patrones que nos ayuden a organizar el código internamente. El patrón **Modelo-Vista-Controlador (MVC)** y los **principios SOLID** son fundamentales para escribir código mantenible y de calidad.

#### 5.1. El patrón MVC

MVC separa la aplicación en tres componentes principales:

**Modelo (Model):**
- Representa los datos y la lógica de negocio
- Gestiona el acceso a la base de datos
- Independiente de la presentación

**Vista (View):**
- Presenta los datos al usuario
- Renderiza la interfaz
- No contiene lógica de negocio

**Controlador (Controller):**
- Gestiona las peticiones del usuario
- Coordina Modelo y Vista
- Contiene la lógica de aplicación

**Flujo típico:**
1. Usuario interactúa con la Vista
2. Vista notifica al Controlador
3. Controlador procesa y solicita datos al Modelo
4. Modelo ejecuta lógica y devuelve datos
5. Controlador selecciona Vista apropiada
6. Vista renderiza datos y muestra al usuario

#### 5.2. Principios SOLID

Los **principios SOLID** son cinco reglas fundamentales para diseño orientado a objetos de calidad:

**S - Single Responsibility (Responsabilidad Única)**
Cada clase debe tener una única razón para cambiar. Una clase, una responsabilidad.

**O - Open/Closed (Abierto/Cerrado)**
Abierto para extensión, cerrado para modificación. Añadir funcionalidad sin cambiar código existente.

**L - Liskov Substitution (Sustitución de Liskov)**
Los objetos de una clase derivada deben poder sustituir a los de la clase base sin alterar el comportamiento.

**I - Interface Segregation (Segregación de Interfaces)**
Muchas interfaces específicas son mejores que una interfaz general. No forzar a implementar métodos innecesarios.

**D - Dependency Inversion (Inversión de Dependencias)**
Depender de abstracciones, no de implementaciones concretas. Facilita el cambio y el testing.

Estos principios son especialmente relevantes en arquitecturas modernas y microservicios.

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

Un **servicio web** es una API que permite a otra aplicación comunicarse remotamente para acceder a un servicio. Es la diferencia entre una aplicación aislada y una aplicación que puede integrarse con el mundo.

#### 8.1. Diferencia fundamental

**Página web dinámica:**
- Genera HTML para humanos
- Incluye estilos y presentación
- Se visualiza en navegador

**Servicio web (API):**
- Devuelve datos estructurados (JSON/XML)
- Sin presentación ni estilos
- Consumido por código, no por humanos

#### 8.2. Protocolos de API

**REST (Representational State Transfer)**

El más popular. Características:
- Usa métodos HTTP estándar (GET, POST, PUT, DELETE)
- URLs representan recursos
- Sin estado (stateless)
- Cacheable
- Formato típico: JSON

Ejemplo:
```http
GET /api/usuarios/123
→ Devuelve: {"id": 123, "nombre": "Ana", "email": "ana@ejemplo.com"}

POST /api/usuarios
{"nombre": "Carlos", "email": "carlos@ejemplo.com"}
→ Crea nuevo usuario
```

**GraphQL**

Lenguaje de consulta para APIs. Características:
- Cliente pide exactamente lo que necesita
- Una sola petición para datos relacionados
- Tipado fuerte
- Sin sobre-fetching ni under-fetching

**WebSockets**

Comunicación bidireccional en tiempo real:
- Conexión persistente
- Ideal para chat, gaming, dashboards en vivo
- Baja latencia

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
- Stateless (sin sesiones en servidor)
- Escalable
- Portable
- Autocontenido

**Seguridad:**
- Siempre HTTPS
- Tiempo de expiración corto
- No guardar datos sensibles en payload
- El payload es visible (solo codificado, no encriptado)

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

Hacer más potente el servidor existente:
- Más CPU
- Más RAM
- Discos más rápidos

**Ventajas:** Simple
**Desventajas:** Límite físico, punto único de fallo

#### 12.3. Escalabilidad horizontal (Scale Out)

Añadir más servidores:

**Balanceador de carga:**
Distribuye peticiones entre múltiples servidores.

```
           Balanceador
              / | \
             /  |  \
       Srv1  Srv2  Srv3
```

**Ventajas:**
- Sin límite teórico
- Alta disponibilidad
- Tolerancia a fallos

**Desventajas:**
- Más complejo
- Sesiones compartidas
- Coste mayor

---

### 13. Contenedores y orquestación

Los **contenedores** revolucionaron el despliegue moderno.

#### 13.1. Docker

**¿Qué es un contenedor?**
Paquete que incluye:
- Aplicación
- Dependencias
- Runtime
- Configuración

Todo lo necesario para ejecutar, aislado del sistema host.

**Ventajas:**
- "Funciona en mi máquina" → funciona en todas
- Portabilidad total
- Despliegue consistente
- Ligero (vs máquinas virtuales)

**Dockerfile ejemplo:**
```dockerfile
FROM php:8.2-apache
COPY . /var/www/html/
RUN docker-php-ext-install mysqli
EXPOSE 80
```

#### 13.2. Docker Compose

Para aplicaciones multi-contenedor:

```yaml
version: '3'
services:
  web:
    image: nginx
    ports:
      - "80:80"
  app:
    image: php:fpm
  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: secret
```

#### 13.3. Kubernetes

**Orquestación a gran escala:**
- Gestiona cientos/miles de contenedores
- Escalado automático
- Auto-recuperación
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

