---
title: "UD 3 - 3.3 El Protocolo HTTP y HTTPS"
description: Protocolo HTTP, métodos, códigos de estado, cabeceras y seguridad con HTTPS
summary: Características del protocolo HTTP, formato de peticiones y respuestas, cabeceras HTTP, métodos GET/POST/PUT/DELETE, códigos de estado y protocolo HTTPS con SSL/TLS
authors:
    - Eduardo Fdez
date: 2025-11-19
icon: "material/file-document-outline"
permalink: /daw/unidad3/3.3
categories:
    - DAW
tags:
    - HTTP
    - HTTPS
    - Protocolos
    - SSL
    - TLS
    - APIs
---

## 3.3. El Protocolo HTTP y HTTPS

En las unidades anteriores hemos aprendido sobre los componentes de una aplicación web y cómo se divide el código entre cliente y servidor. Pero, ¿cómo se comunican realmente estos dos componentes? La respuesta está en el **protocolo HTTP**, el lenguaje universal de la web.

Cada vez que escribís una URL en el navegador, hacéis clic en un enlace o enviáis un formulario, estáis utilizando HTTP. Es el protocolo que hace posible que podáis leer esta página, ver vídeos en YouTube o comprar en Amazon. Entenderlo es fundamental para cualquier profesional del desarrollo y despliegue de aplicaciones web.

### 1. Características y ventajas del protocolo HTTP

El **Protocolo HTTP (HyperText Transfer Protocol)** es la base de la comunicación en la World Wide Web. Fue creado por Tim Berners-Lee en 1989 y se ha convertido en el estándar para la transferencia de información en Internet.

#### 1.1. Definición y concepto

HTTP es un protocolo de **capa de aplicación** que define cómo se estructuran y envían los mensajes entre clientes y servidores web. Es un protocolo **no orientado a la conexión**, lo que significa que cada petición entre cliente y servidor es independiente y no requiere mantener una conexión continua.

**Arquitectura básica:**

- **Cliente**: Típicamente un navegador web que inicia las peticiones
- **Servidor**: Aplicación que escucha y responde a las peticiones
- **Recursos**: Documentos, imágenes, datos que se intercambian
- **Mensajes**: Peticiones (requests) y respuestas (responses)

#### 1.2. Características principales

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

#### 1.3. Ventajas del protocolo HTTP

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

#### 1.4. Importancia en arquitecturas modernas

HTTP es fundamental en las arquitecturas web actuales:

- **APIs REST**: Se basan completamente en HTTP y sus métodos
- **Microservicios**: Utilizan HTTP para comunicarse entre sí
- **Aplicaciones web**: Toda interacción usa HTTP/HTTPS
- **Internet de las Cosas (IoT)**: Muchos dispositivos usan HTTP para comunicarse

!!! tip "HTTP es universal"
    HTTP es tan universal que incluso aplicaciones que no son web (como aplicaciones móviles o de escritorio) suelen usar HTTP para comunicarse con sus servidores, aprovechando su simplicidad y las herramientas existentes.

### 2. Formato de peticiones y respuestas HTTP

La interacción en la web se basa en un intercambio constante de **peticiones** (requests) y **respuestas** (responses) HTTP entre el navegador del cliente y el servidor. Entender su estructura es fundamental.

#### 2.1. Estructura de una petición HTTP

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

#### 2.2. Estructura de una respuesta HTTP

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

### 3. Cabeceras HTTP

Las cabeceras HTTP son líneas de metadatos que se envían tanto en las peticiones como en las respuestas. Proporcionan información crucial sobre la comunicación entre cliente y servidor.

#### 3.1. Cabeceras de petición comunes

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

#### 3.2. Cabeceras de respuesta comunes

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

#### 3.3. Tipos MIME más comunes

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

### 4. Métodos HTTP (verbos HTTP)

Los métodos HTTP, también llamados **verbos HTTP**, definen la acción que un cliente desea realizar sobre un recurso en el servidor. Son fundamentales para el diseño de APIs RESTful.

<figure markdown="span">
  ![Métodos HTTP](assets/http-metodos.gif){ width="600" }
  <figcaption>Representación visual de los principales métodos HTTP y sus acciones: GET para obtener, POST para crear, PUT para actualizar, DELETE para eliminar. Cada método tiene un propósito específico en la manipulación de recursos del servidor</figcaption>
</figure>

#### 4.1. GET - Obtener recursos

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

#### 4.2. POST - Crear recursos

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

#### 4.3. PUT - Actualizar recursos

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

#### 4.4. PATCH - Actualización parcial

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

#### 4.5. DELETE - Eliminar recursos

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

#### 4.6. HEAD - Obtener metadatos

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

#### 4.7. OPTIONS - Opciones disponibles

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

#### 4.8. Tabla resumen de métodos HTTP

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

### 5. Códigos de estado HTTP

Después de cada petición, el servidor envía una respuesta que incluye un **código de estado HTTP**. Este código es un número de tres dígitos que indica el resultado de la petición.

<figure markdown="span">
  ![Códigos de estado HTTP](assets/status-code.png){ width="700" }
  <figcaption>Clasificación de los códigos de estado HTTP organizados por familias: 1xx (Informativos), 2xx (Éxito), 3xx (Redirección), 4xx (Errores del cliente), 5xx (Errores del servidor). Cada familia indica un tipo diferente de resultado de la petición</figcaption>
</figure>

#### 5.1. Familia 1xx - Respuestas informativas

Indican que la petición ha sido recibida y el proceso continúa.

| Código  | Nombre              | Descripción                                            |
|:--------|:--------------------|:-------------------------------------------------------|
| **100** | Continue            | El cliente puede continuar con su petición             |
| **101** | Switching Protocols | El servidor acepta cambiar de protocolo                |
| **102** | Processing          | El servidor está procesando, pero aún no hay respuesta |

**Uso poco común**: Raramente se encuentran estos códigos en aplicaciones web típicas.

#### 5.2. Familia 2xx - Operaciones exitosas

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

#### 5.3. Familia 3xx - Redirecciones

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

#### 5.4. Familia 4xx - Errores del cliente

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

#### 5.5. Familia 5xx - Errores del servidor

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

### 6. El protocolo HTTPS: seguridad en la web

**HTTPS (HyperText Transfer Protocol Secure)** es la versión segura del protocolo HTTP. En la web moderna, HTTPS no es opcional: es **esencial** para la seguridad y privacidad de los usuarios.

#### 6.1. ¿Por qué es necesario HTTPS?

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

#### 6.2. ¿Cómo funciona HTTPS?

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

#### 6.3. Certificados digitales

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

#### 6.4. Tipos de certificados

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

#### 6.5. Let's Encrypt: certificados gratuitos

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

#### 6.6. Impacto en el rendimiento

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

#### 6.7. HTTPS en desarrollo

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

#### 6.8. Buenas prácticas HTTPS

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

## Referencias y bibliografía

- [Jose Luis González](https://github.com/joseluisgs). *Despliegue de aplicaciones Web - 2025 2026*. [https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026](https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026)
- Fielding, R., et al. (2022). *RFC 9110: HTTP Semantics*. IETF.
- Mozilla Developer Network. (2024). *HTTP Documentation*. [https://developer.mozilla.org/en-US/docs/Web/HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- Let's Encrypt. (2024). *How It Works*. [https://letsencrypt.org/how-it-works/](https://letsencrypt.org/how-it-works/)

## Recursos adicionales

- [HTTP Status Codes](https://httpstat.us/) - Servicio para probar códigos de estado
- [Postman](https://www.postman.com/) - Herramienta para probar APIs
- [curl](https://curl.se/) - Herramienta de línea de comandos para peticiones HTTP
- [SSL Labs Server Test](https://www.ssllabs.com/ssltest/) - Analizar configuración HTTPS
- [HTTP Cat](https://http.cat/) - Códigos HTTP con gatos
