# DAW-U3.3 - El Protocolo HTTP y HTTPS

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice I

1. Introducción
2. Características del Protocolo HTTP
3. Formato de Peticiones y Respuestas
4. Cabeceras HTTP
5. Métodos HTTP


## Índice II

6. Códigos de Estado HTTP
7. El Protocolo HTTPS
8. Resumen y Conclusiones
9. Preguntas

---

## 1. Introducción

Note: Bienvenidos a la unidad sobre HTTP y HTTPS. Si las arquitecturas web definen "cómo" se estructura una aplicación, HTTP define "cómo" se comunican sus componentes. Es el lenguaje universal de Internet. Cada clic, cada formulario, cada API que llamáis utiliza HTTP. Entenderlo es esencial para desplegar y depurar aplicaciones web.


### HTTP: El Lenguaje de la Web

**El protocolo que hace posible Internet**

- Cada URL que escribís usa HTTP
- Cada clic en un enlace es una petición HTTP
- Cada API REST se basa en HTTP
- Fundamento de aplicaciones web y móviles

Note: HTTP es literalmente el idioma que hablan los navegadores y servidores. Cuando escribís "www.google.com", cuando hacéis clic en un botón, cuando una app móvil carga datos, todo eso son peticiones HTTP. Es un protocolo sencillo pero potente, y dominarlo os convertirá en mejores desarrolladores y administradores de sistemas.

---

## 2. Características del Protocolo HTTP

Note: HTTP fue creado por Tim Berners-Lee en 1989 y se ha mantenido sorprendentemente estable. Su diseño simple pero extensible explica su éxito durante más de 30 años. Veamos qué hace especial a HTTP.


### Definición y Concepto

**HyperText Transfer Protocol**

- Protocolo de capa de aplicación
- No orientado a la conexión
- Basado en texto legible por humanos
- Define cómo se estructuran los mensajes

Note: HTTP opera en la capa de aplicación, sobre TCP/IP. Es "no orientado a la conexión" porque cada petición es independiente: el servidor no recuerda peticiones anteriores. Esto simplifica el diseño pero crea el desafío de mantener sesiones de usuario, que resolveremos con cookies.


### Arquitectura Básica

**Los componentes de HTTP**

- **Cliente**: navegador que inicia peticiones
- **Servidor**: aplicación que responde
- **Recursos**: documentos, imágenes, datos
- **Mensajes**: requests y responses

Note: La arquitectura es simple: el cliente (normalmente un navegador) hace una petición, el servidor la procesa y devuelve una respuesta. Los recursos pueden ser páginas HTML, imágenes, JSON de una API, etc. Esta simplicidad es una de las claves del éxito de HTTP.


### Características Clave

**¿Por qué HTTP es tan exitoso?**

1. **Sencillo**: Texto plano, fácil de depurar
2. **Extensible**: Se pueden añadir cabeceras personalizadas
3. **Sin estado (Stateless)**: Cada petición es independiente
4. **Universal**: Funciona en cualquier plataforma

Note: HTTP es tan simple que podéis leer y entender una petición HTTP sin herramientas especiales. Es extensible, permitiendo evolucionar sin romper compatibilidad. Ser stateless facilita escalabilidad: cualquier servidor puede atender cualquier petición. Y es universal: el mismo protocolo funciona en Windows, Mac, Linux, móviles, IoT.


### Ventajas de HTTP

**Beneficios del protocolo**

✅ Control de caché (mejora velocidad)
✅ Autenticación integrada
✅ Soporte para proxies
✅ Mantenimiento de sesiones (con cookies)
✅ Negociación de contenido

Note: HTTP incluye mecanismos para cachear contenido y reducir transferencias. Soporta autenticación básica, digest y bearer tokens. Permite usar proxies transparentes para caché, filtrado y seguridad. Aunque es stateless, las cookies permiten mantener sesiones de usuario. Y permite negociar el formato de respuesta según las capacidades del cliente.

---

## 3. Formato de Peticiones y Respuestas

Note: Ahora entramos en detalle técnico. Vamos a ver exactamente cómo se estructura una petición HTTP y una respuesta. Entender esto os permitirá depurar problemas, diseñar APIs correctamente y usar herramientas como curl o Postman con soltura.


### Estructura de una Petición HTTP

**Componentes de un request**

```
[MÉTODO] [RUTA] [VERSIÓN]
Cabecera1: valor1
Cabecera2: valor2
[línea en blanco]
[Cuerpo opcional]
```

Note: Toda petición HTTP tiene esta estructura. La primera línea indica qué queremos hacer (GET), sobre qué recurso (/usuarios) y qué versión de HTTP usamos. Luego vienen las cabeceras con metadatos. Una línea en blanco separa las cabeceras del cuerpo. El cuerpo es opcional y contiene datos que enviamos al servidor.


### Ejemplo de Petición

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

Note: Este es un ejemplo real de petición de login. POST indica que estamos enviando datos. /api/login es el recurso. HTTP/1.1 es la versión del protocolo. Las cabeceras indican el host, el tipo de contenido JSON, su tamaño, y el navegador usado. Tras la línea en blanco viene el cuerpo con los datos de login en formato JSON.


### Estructura de una Respuesta HTTP

**Componentes de un response**

```
[VERSIÓN] [CÓDIGO] [TEXTO]
Cabecera1: valor1
Cabecera2: valor2
[línea en blanco]
[Cuerpo]
```

Note: Las respuestas tienen estructura similar. La línea de estado incluye la versión HTTP, un código numérico (200, 404, 500...) y texto descriptivo. Las cabeceras aportan metadatos de la respuesta. Y el cuerpo contiene el contenido solicitado: HTML, JSON, imagen, etc.


### Ejemplo de Respuesta

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 89
Server: nginx/1.18.0

{
    "status": "success",
    "mensaje": "Login correcto",
    "token": "eyJhbGci..."
}
```

Note: Esta es la respuesta al login anterior. 200 OK indica éxito. Content-Type dice que devolvemos JSON. Content-Length especifica el tamaño. Server identifica el servidor web. Y el cuerpo JSON confirma el login exitoso y devuelve un token de autenticación para futuras peticiones.


### Herramientas de Desarrollo

**Cómo ver HTTP en acción**

- **Navegador**: F12 → Pestaña "Red/Network"
- **curl**: línea de comandos
- **Postman**: GUI para probar APIs
- **HTTPie**: curl mejorado

Note: Todos los navegadores modernos tienen herramientas de desarrollo (pulsa F12). La pestaña "Red" o "Network" muestra todas las peticiones y respuestas HTTP. curl es una herramienta de línea de comandos muy potente. Postman es una aplicación gráfica ideal para probar APIs. Y HTTPie es como curl pero más amigable. Aprended a usar estas herramientas, os ahorrarán horas de depuración.

---

## 4. Cabeceras HTTP

Note: Las cabeceras HTTP son metadatos que viajan tanto en peticiones como en respuestas. Hay decenas de cabeceras estándar y podéis crear las vuestras propias. Veamos las más importantes que necesitáis conocer.


### ¿Qué son las Cabeceras?

**Metadatos de la comunicación**

- Proporcionan información adicional
- Tanto en peticiones como respuestas
- Formato: `Nombre: valor`
- Extensibles: podéis crear las vuestras

Note: Las cabeceras son líneas clave-valor que añaden contexto a la petición o respuesta. Indican cosas como qué tipo de contenido estamos enviando, qué formatos acepta el cliente, autenticación, cookies, control de caché, y mucho más. Son la forma de HTTP de transmitir metadatos sin contaminar el cuerpo del mensaje.


### Cabeceras de Petición Comunes

**Cliente → Servidor**

- `Host`: dominio al que nos dirigimos
- `User-Agent`: identificación del navegador
- `Accept`: tipos de contenido aceptados
- `Accept-Language`: idiomas preferidos
- `Authorization`: credenciales de autenticación
- `Cookie`: cookies almacenadas

Note: Host es obligatoria en HTTP/1.1 y permite alojar múltiples sitios en un mismo servidor. User-Agent identifica el navegador, útil para adaptar la respuesta. Accept indica qué formatos puede procesar el cliente. Accept-Language permite servir contenido en el idioma del usuario. Authorization lleva tokens o credenciales. Cookie envía datos de sesión almacenados previamente.


### Cabeceras de Respuesta Comunes

**Servidor → Cliente**

- `Content-Type`: tipo del contenido devuelto
- `Content-Length`: tamaño en bytes
- `Server`: identificación del servidor
- `Cache-Control`: directivas de caché
- `Set-Cookie`: establece cookies
- `Location`: redirecciones

Note: Content-Type es crucial: le dice al navegador cómo interpretar el contenido (HTML, JSON, imagen...). Content-Length indica el tamaño total. Server identifica el software servidor, a veces se oculta por seguridad. Cache-Control controla el cacheo. Set-Cookie almacena datos en el navegador. Location se usa en redirecciones para indicar la nueva URL.


### Tipos MIME Importantes

**Identificación de formatos**

| Tipo MIME                 | Uso                 |
|:--------------------------|:--------------------|
| `text/html`               | Páginas web         |
| `application/json`        | APIs REST           |
| `application/xml`         | Datos XML           |
| `image/jpeg, png, gif`    | Imágenes            |
| `application/pdf`         | Documentos PDF      |
| `text/css`                | Hojas de estilo     |
| `application/javascript`  | Código JS           |
<!-- .element.table: style="font-size:75%;" -->

Note: Los tipos MIME (Multipurpose Internet Mail Extensions) identifican inequívocamente el formato del contenido. Son esenciales en la cabecera Content-Type. text/html para páginas web. application/json es el rey en APIs modernas. Las imágenes tienen sus tipos específicos. CSS y JavaScript también. Especificar correctamente el tipo MIME evita que el navegador malinterprete el contenido.

---

## 5. Métodos HTTP

Note: Los métodos HTTP, también llamados verbos, definen QUÉ acción queremos realizar sobre un recurso. Son fundamentales en el diseño de APIs REST. Cada método tiene una semántica específica que debemos respetar.


### Verbos HTTP Principales

**Acciones sobre recursos**

- **GET**: Obtener/leer
- **POST**: Crear
- **PUT**: Actualizar completo
- **PATCH**: Actualizar parcial
- **DELETE**: Eliminar
- **HEAD**: Metadatos sin cuerpo
- **OPTIONS**: Opciones disponibles

Note: GET lee datos sin modificar nada. POST crea nuevos recursos. PUT reemplaza completamente un recurso existente. PATCH actualiza solo algunos campos. DELETE elimina. HEAD es como GET pero solo devuelve cabeceras, útil para verificar existencia. OPTIONS lista qué métodos soporta un recurso, importante en CORS.


### GET - Obtener Recursos

**Leer sin modificar**

```http
GET /api/usuarios/123 HTTP/1.1
Host: miapp.com
```

✅ Idempotente (llamarlo N veces = mismo resultado)
✅ Seguro (no modifica el servidor)
✅ Cacheable
❌ Sin cuerpo (parámetros en URL)

Note: GET es para leer datos. Es idempotente: puedes llamarlo mil veces y obtienes el mismo resultado. Es seguro: no cambia nada en el servidor. Las respuestas pueden cachearse, mejorando rendimiento. Los parámetros van en la URL como query strings, no en el cuerpo. Nunca uséis GET para modificar datos, es una mala práctica grave.


### POST - Crear Recursos

**Enviar datos para crear**

```http
POST /api/usuarios HTTP/1.1
Content-Type: application/json

{
    "nombre": "María",
    "email": "maria@ejemplo.com"
}
```

❌ No idempotente (cada llamada crea uno nuevo)
❌ No seguro (modifica el servidor)
✅ Con cuerpo (datos en el body)

Note: POST envía datos al servidor para crear recursos nuevos. Cada llamada crea un recurso adicional, por eso no es idempotente. Los datos van en el cuerpo de la petición, típicamente en JSON. La respuesta suele incluir código 201 Created y la ubicación del nuevo recurso. POST también se usa para login, subir archivos y enviar formularios.


### PUT - Actualizar Completo

**Reemplazar recurso entero**

```http
PUT /api/usuarios/123 HTTP/1.1
Content-Type: application/json

{
    "nombre": "María García López",
    "email": "maria.garcia@ejemplo.com",
    "rol": "profesor"
}
```

✅ Idempotente
❌ No seguro
✅ Reemplazo total

Note: PUT actualiza un recurso existente reemplazándolo completamente. Es idempotente: llamarlo varias veces con los mismos datos produce el mismo resultado. La diferencia con POST es que con PUT el cliente especifica el ID del recurso en la URL. Hay que enviar todos los campos del recurso, no solo los que cambian.


### PATCH - Actualización Parcial

**Modificar solo algunos campos**

```http
PATCH /api/usuarios/123 HTTP/1.1
Content-Type: application/json

{
    "email": "nuevo.email@ejemplo.com"
}
```

Solo envías los campos que cambian

Note: PATCH es para actualizaciones parciales. Solo enviáis los campos que queréis cambiar, no todo el recurso. Es más eficiente que PUT cuando solo necesitáis modificar uno o dos campos de un objeto grande. En la práctica, muchas APIs modernas prefieren PATCH sobre PUT.


### DELETE - Eliminar Recursos

**Borrar del servidor**

```http
DELETE /api/usuarios/123 HTTP/1.1
```

Respuesta típica:
```http
HTTP/1.1 204 No Content
```

✅ Idempotente (borrar varias veces = mismo efecto)

Note: DELETE elimina un recurso del servidor. Es idempotente: borrar algo que ya no existe sigue siendo un estado válido (normalmente 404 o 204). La respuesta típica es 204 No Content si no hay cuerpo, o 200 OK con un mensaje de confirmación. Importante: implementad DELETE con cuidado y siempre con autenticación/autorización adecuadas.


### Tabla Resumen de Métodos

| Método     | Propósito   | Idempotente | Seguro | Cuerpo |
|:-----------|:------------|:------------|:-------|:-------|
| **GET**    | Leer        | ✓           | ✓      | No     |
| **POST**   | Crear       | ✗           | ✗      | Sí     |
| **PUT**    | Actualizar  | ✓           | ✗      | Sí     |
| **PATCH**  | Modificar   | ✗           | ✗      | Sí     |
| **DELETE** | Eliminar    | ✓           | ✗      | No     |
<!-- .element.table: style="font-size:75%;" -->

Note: Esta tabla resume las propiedades clave de cada método. Idempotente significa que llamarlo N veces produce el mismo resultado que llamarlo una vez. Seguro significa que no modifica el servidor. Estos conceptos son fundamentales para diseñar APIs REST bien estructuradas y predecibles.

---

## 6. Códigos de Estado HTTP

Note: Después de cada petición, el servidor responde con un código de estado: un número de tres dígitos que indica qué pasó. Los códigos están organizados en familias según el primer dígito. Conocerlos os ayudará a depurar problemas y diseñar mejores APIs.


### Familias de Códigos

**Clasificación por primer dígito**

- **1xx**: Informativos (petición recibida, procesando)
- **2xx**: Éxito (todo OK)
- **3xx**: Redirección (necesita acción adicional)
- **4xx**: Error del cliente (problema en la petición)
- **5xx**: Error del servidor (problema en el servidor)

Note: Los códigos se agrupan en cinco familias. 1xx son raros, indican que el proceso continúa. 2xx significa éxito total. 3xx son redirecciones. 4xx indican que el cliente hizo algo mal: URL incorrecta, sin permisos, etc. 5xx significan que el servidor tiene un problema. Entender esta clasificación os ayudará a diagnosticar errores rápidamente.


### Familia 2xx - Éxito

**La petición fue exitosa**

| Código  | Nombre      | Uso                           |
|:--------|:------------|:------------------------------|
| **200** | OK          | GET exitoso, hay contenido    |
| **201** | Created     | POST creó un recurso          |
| **202** | Accepted    | Procesamiento asíncrono       |
| **204** | No Content  | Éxito sin contenido (DELETE)  |
<!-- .element.table: style="font-size:75%;" -->

Note: 200 OK es el código más común: todo fue bien y hay contenido en la respuesta. 201 Created se usa cuando POST crea un recurso nuevo, idealmente con un header Location indicando su URL. 202 Accepted indica que la petición se aceptó pero el procesamiento es asíncrono. 204 No Content es éxito pero sin cuerpo en la respuesta, típico en DELETE.


### Familia 3xx - Redirecciones

**El recurso está en otra ubicación**

| Código  | Nombre             | Uso                              |
|:--------|:-------------------|:---------------------------------|
| **301** | Moved Permanently  | El recurso se movió para siempre |
| **302** | Found              | Redirección temporal             |
| **304** | Not Modified       | Usa tu copia cacheada            |
| **307** | Temporary Redirect | Similar a 302, más estricto      |
<!-- .element.table: style="font-size:75%;" -->

Note: 301 Moved Permanently indica que el recurso cambió de URL definitivamente, el navegador debe actualizar sus enlaces. 302 Found es redirección temporal. 304 Not Modified es especial: le dice al navegador "tu copia cacheada sigue siendo válida, úsala". Esto ahorra ancho de banda. El header Location indica la nueva URL en 301, 302 y 307.


### Familia 4xx - Errores del Cliente

**El problema está en la petición**

| Código  | Nombre             | Significado                             |
|:--------|:-------------------|:----------------------------------------|
| **400** | Bad Request        | Petición malformada (JSON inválido)     |
| **401** | Unauthorized       | Autenticación requerida o fallida       |
| **403** | Forbidden          | Sin permisos (aunque estés autenticado) |
| **404** | Not Found          | El recurso no existe                    |
| **429** | Too Many Requests  | Rate limiting activado                  |
<!-- .element.table: style="font-size:75%;" -->

Note: 400 Bad Request indica que la petición está mal formada: JSON inválido, parámetros incorrectos. 401 Unauthorized significa "no sé quién eres, autentícate". 403 Forbidden significa "sé quién eres pero no puedes hacer esto". 404 Not Found es el famoso error de recurso no encontrado. 429 Too Many Requests indica que el cliente está haciendo demasiadas peticiones muy rápido.


### 401 vs 403: Diferencia Clave

**Autenticación vs Autorización**

🔴 **401 Unauthorized**
"No sé quién eres, identifícate"
→ Necesitas login

🔴 **403 Forbidden**
"Sé quién eres, pero no puedes hacer esto"
→ Sin permisos suficientes

Note: Esta es una distinción importante que muchos confunden. 401 es un problema de autenticación: el servidor no sabe quién eres, necesitas loguearte o tu token expiró. 403 es autorización: el servidor sabe perfectamente quién eres, pero no tienes permisos para realizar esa acción. Por ejemplo, un estudiante no puede eliminar cursos aunque esté logueado.


### Familia 5xx - Errores del Servidor

**El problema está en el servidor**

| Código  | Nombre                | Causa común                              |
|:--------|:----------------------|:-----------------------------------------|
| **500** | Internal Server Error | Excepción no capturada, bug              |
| **502** | Bad Gateway           | Proxy no puede contactar backend         |
| **503** | Service Unavailable   | Servidor sobrecargado o en mantenimiento |
| **504** | Gateway Timeout       | Backend no responde a tiempo             |
<!-- .element.table: style="font-size:75%;" -->

Note: 500 Internal Server Error es el error genérico: algo explotó en el servidor. Puede ser una excepción no capturada, un bug, problemas de base de datos. 502 Bad Gateway aparece cuando hay un proxy/balanceador y el servidor backend está caído. 503 Service Unavailable indica sobrecarga o mantenimiento. 504 Gateway Timeout ocurre cuando el backend tarda demasiado en responder. Los errores 5xx NUNCA son culpa del cliente.


### Códigos HTTP en Gatos

**HTTP Cat**

[http.cat](https://http.cat/)

😸 Una forma divertida de recordar códigos
😸 404 = gato escondido
😸 500 = gato en error

Note: HTTP Cat es un sitio web divertido que representa cada código de estado HTTP con una imagen de un gato. Es una forma memorable de aprender los códigos. 404 muestra un gato escondido, 500 un gato con el ordenador en llamas. Es entretenido y educativo. También existe HTTP Status Dogs para los amantes de los perros.

---

## 7. El Protocolo HTTPS

Note: HTTP transmite datos en texto plano. Cualquiera que intercepte la comunicación puede leer contraseñas, datos bancarios, todo. Esto es inaceptable hoy día. HTTPS añade cifrado a HTTP mediante SSL/TLS, protegiendo la privacidad y seguridad de los usuarios.


### ¿Por qué HTTPS?

**HTTP es inseguro**

🔓 HTTP transmite en texto plano
⚠️ Contraseñas visibles
⚠️ Datos bancarios legibles
⚠️ Cookies robables
⚠️ Man-in-the-Middle posible

Note: HTTP no cifra nada. Si os conectáis a una red WiFi pública y usáis HTTP, cualquiera con herramientas simples puede capturar vuestras contraseñas, cookies de sesión, números de tarjeta. Los ataques Man-in-the-Middle permiten a un atacante interceptar y modificar los datos. HTTPS soluciona todo esto con cifrado.


### HTTPS = HTTP + SSL/TLS

**Cifrado de la comunicación**

- **SSL/TLS**: protocolos criptográficos
- **Cifra** toda la comunicación
- **Autentica** la identidad del servidor
- **Garantiza integridad** (datos no modificados)

Note: HTTPS es simplemente HTTP más una capa de cifrado SSL/TLS. SSL (Secure Sockets Layer) es el nombre antiguo, TLS (Transport Layer Security) es el moderno, pero todavía decimos SSL habitualmente. Este cifrado protege tres cosas: confidencialidad (nadie puede leer), autenticación (es realmente el servidor que dice ser), e integridad (los datos no han sido modificados en tránsito).


### Proceso de Conexión HTTPS

**El handshake SSL/TLS**

1. Cliente inicia conexión HTTPS
2. Servidor envía su certificado digital
3. Cliente verifica el certificado
4. Negociación de algoritmos de cifrado
5. Intercambio de claves de sesión
6. Comunicación cifrada establecida

Note: Cuando os conectáis a un sitio HTTPS, primero ocurre un "handshake" o apretón de manos. El servidor presenta su certificado digital que lo identifica. El navegador verifica que el certificado es válido, está firmado por una autoridad confiable, el dominio coincide y no ha expirado. Luego acuerdan qué algoritmos usar y generan claves de sesión. Todo este proceso toma milisegundos y es transparente para el usuario.


### Certificados Digitales

**Identidad verificada del servidor**

Componentes de un certificado:

- Dominio al que corresponde
- Organización propietaria
- Clave pública del servidor
- Período de validez
- Firma de la Autoridad Certificadora (CA)

Note: Un certificado digital es como un DNI del servidor. Vincula una clave pública con la identidad del propietario del sitio. Incluye el dominio, información de la organización, fechas de validez y está firmado digitalmente por una Autoridad Certificadora (CA) en la que los navegadores confían. Sin esta firma, el navegador mostraría una advertencia de seguridad.


### Autoridades de Certificación

**¿Quién firma los certificados?**

CAs principales:

- **Let's Encrypt** 🆓 (gratuita, automática)
- DigiCert
- GlobalSign
- Sectigo
- GoDaddy

Note: Las Autoridades de Certificación son organizaciones de confianza que verifican identidades y firman certificados. Los navegadores tienen una lista de CAs en las que confían. Let's Encrypt revolucionó el panorama ofreciendo certificados gratuitos y renovación automática. Es perfecta para la mayoría de sitios. Las CAs comerciales ofrecen certificados con validación más exhaustiva para bancos y e-commerce grandes.


### Let's Encrypt: Certificados Gratis

**HTTPS para todos**

✅ Completamente gratuito
✅ Renovación automática (cada 90 días)
✅ Muy fácil con Certbot
✅ Ampliamente aceptado

```bash
sudo certbot --apache -d www.ejemplo.com
```

Note: Let's Encrypt es una CA sin ánimo de lucro que democratizó HTTPS. Proporciona certificados gratuitos y herramientas como Certbot que automatizan completamente la instalación y renovación. Con un solo comando podéis tener HTTPS funcionando. Los certificados duran 90 días pero se renuevan automáticamente. Es la opción recomendada para la mayoría de proyectos.


### Tipos de Certificados

**Nivel de validación**

1. **Domain Validation (DV)**: Verifica que controlas el dominio
   → Rápido, económico, suficiente para la mayoría

2. **Organization Validation (OV)**: Verifica la organización
   → Requiere documentación de la empresa

3. **Extended Validation (EV)**: Validación exhaustiva
   → Para banca, e-commerce grande

Note: Los certificados DV solo verifican que controlas el dominio, son los que ofrece Let's Encrypt. Son perfectos para blogs, aplicaciones web, APIs. Los OV verifican también la existencia legal de la organización. Los EV tienen el proceso de validación más riguroso, antes mostraban una barra verde en navegadores. Para la mayoría de proyectos, DV es suficiente.


### HTTPS: Buenas Prácticas

**Configuración correcta**

1. ✅ Usar HTTPS en todo el sitio
2. ✅ Redirigir HTTP → HTTPS
3. ✅ Activar HSTS (HTTP Strict Transport Security)
4. ✅ Renovar certificados antes de expirar
5. ✅ Usar TLS 1.2 o superior
6. ✅ Verificar configuración con SSL Labs

Note: Usad HTTPS en todo el sitio, no solo en el login. Configurad redirecciones automáticas de HTTP a HTTPS. Activad HSTS para que el navegador siempre use HTTPS incluso si el usuario escribe http://. Automatizad la renovación de certificados. Desactivad versiones antiguas de SSL/TLS que tienen vulnerabilidades. Y probad vuestra configuración con herramientas como SSL Labs para obtener una calificación A+.


### HTTPS y Rendimiento

**¿Es más lento?**

🚀 **Con HTTP/2: HTTPS es MÁS RÁPIDO**

- Hardware moderno cifra eficientemente
- HTTP/2 solo funciona con HTTPS
- HTTP/2: multiplexación, compresión, server push
- TLS 1.3 reduce latencia del handshake

Note: Es un mito que HTTPS sea más lento. En hardware moderno, el cifrado tiene un coste mínimo. Y HTTP/2, que requiere HTTPS, es significativamente más rápido que HTTP/1.1 gracias a multiplexación de peticiones, compresión de cabeceras y otras optimizaciones. Además, TLS 1.3 reduce la latencia del handshake inicial. Así que HTTPS moderno es más rápido Y más seguro.

---

## 8. Resumen y Conclusiones

Note: Hemos cubierto mucho material técnico. Vamos a repasar los conceptos clave que debéis llevaros de esta unidad. HTTP y HTTPS son la base de todo lo que hagáis en desarrollo y despliegue de aplicaciones web.


### Conceptos Clave

**Lo esencial de esta unidad**

1. ✅ HTTP es el protocolo fundamental de la web
2. ✅ Peticiones y respuestas tienen estructura clara
3. ✅ Las cabeceras HTTP aportan metadatos
4. ✅ Los métodos definen acciones (GET, POST, PUT, DELETE)
5. ✅ Los códigos de estado indican resultados
6. ✅ HTTPS es imprescindible para seguridad

Note: HTTP es sencillo pero potente, base de toda comunicación web. Las peticiones y respuestas tienen formato estándar con línea de estado, cabeceras y cuerpo. Las cabeceras transportan metadatos cruciales. Los métodos HTTP tienen semántica específica que debemos respetar en APIs REST. Los códigos de estado nos dicen qué pasó: 2xx éxito, 4xx error del cliente, 5xx error del servidor. Y HTTPS no es opcional: es obligatorio para proteger a los usuarios.


### Aplicación Práctica

**Usaréis esto constantemente**

- 🔧 Depurar aplicaciones web
- 🔧 Diseñar APIs RESTful
- 🔧 Configurar servidores web
- 🔧 Implementar autenticación
- 🔧 Optimizar rendimiento
- 🔧 Garantizar seguridad

Note: Todo lo que hemos visto tiene aplicación práctica inmediata. Cuando depuréis por qué una aplicación no funciona, revisaréis peticiones HTTP en las herramientas de desarrollo. Cuando diseñéis APIs, elegiréis los métodos y códigos de estado correctos. Al configurar servidores, implementaréis HTTPS correctamente. Para autenticación usaréis cabeceras Authorization. Para optimizar cachearéis con cabeceras Cache-Control. HTTP es fundamental en vuestro día a día.


### Próximos Pasos

**Seguimos construyendo**

- APIs REST en profundidad
- WebSockets para comunicación en tiempo real
- GraphQL como alternativa a REST
- HTTP/2 y HTTP/3 (QUIC)
- Despliegue de aplicaciones HTTPS

Note: Esta unidad os ha dado la base. En próximas unidades profundizaremos en APIs REST, veremos WebSockets para comunicación bidireccional en tiempo real, exploraremos GraphQL como alternativa a REST, aprenderemos sobre las versiones modernas HTTP/2 y HTTP/3. Y por supuesto, desplegaremos aplicaciones con HTTPS correctamente configurado en servidores reales.


### Recursos para Profundizar

**Continúa aprendando**

- 📚 Mozilla Developer Network (MDN): documentación HTTP
- 🛠️ Postman: probar APIs
- 🛠️ curl: peticiones desde terminal
- 🔍 Browser DevTools: inspeccionar HTTP
- 🔐 SSL Labs: analizar configuración HTTPS

Note: MDN tiene la mejor documentación sobre HTTP, muy completa y con ejemplos. Postman es indispensable para probar APIs. curl es una herramienta de línea de comandos muy potente que todo desarrollador debe dominar. Las herramientas de desarrollo del navegador (F12) son vuestro mejor amigo para depurar. Y SSL Labs os permite analizar y puntuar vuestra configuración HTTPS. Explorad estos recursos.

---

## 9. Preguntas

**¿Preguntas?**

📧 Contacto
🌐 Recursos adicionales en la documentación

Note: Gracias por vuestra atención. HTTP y HTTPS son fundamentales y los usaréis todos los días. Practicad con las herramientas de desarrollo del navegador, experimentad con curl y Postman, configurad HTTPS en vuestros proyectos. ¿Alguna pregunta sobre peticiones, respuestas, métodos, códigos de estado o HTTPS? Estoy aquí para resolver vuestras dudas.
