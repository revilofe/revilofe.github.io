# U3.1 - Desarrollo y Despliegue Web

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

### 7 Bloques

1. Fundamentos de la Web
2. Componentes y Arquitectura
3. Tecnologías de Implementación
4. Servicios y Comunicación
5. Infraestructura y Servidores
6. Despliegue y Operaciones
7. Seguridad y Monitorización

Note: Esta unidad cubre el ciclo completo: desde HTTP hasta monitorización en producción. Cada bloque construye sobre el anterior formando comprensión integral del desarrollo web moderno.

---

## BLOQUE 1: Fundamentos de la Web

Note: Empezamos con los fundamentos esenciales de la comunicación web.


### 1.1. Protocolo HTTP

* Base de toda comunicación web
* Texto legible y extensible
* Arquitectura cliente-servidor
* Request → Response
* Stateless por diseño
* Sencillo pero poderoso

Note: HTTP es el protocolo fundamental de la web. Su simplicidad textual facilita debugging, su naturaleza stateless permite escalabilidad, y su extensibilidad mediante cabeceras lo hace adaptable a cualquier necesidad moderna.


### 1.2. Características HTTP

* **Sencillo**: Texto plano legible
* **Extensible**: Cabeceras personalizadas
* **Stateless**: Sin memoria entre peticiones
* **Cacheable**: Mejora rendimiento
* **Proxy-friendly**: Intermediarios transparentes

Note: Cada característica aporta valor específico. Sencillez facilita aprendizaje y debugging. Extensibilidad permite evolución sin romper compatibilidad. Stateless escala fácilmente. Caché acelera respuestas. Proxies añaden funcionalidad sin modificar endpoints.


### 1.2. Características HTTP II

Stateless marca la evolución de la web moderna. Para poder tener aplicaciones que tengan memoria entre peticiones, se usan mecanismos externos como cookies, tokens JWT o sesiones en el servidor:

* **Cookies**: almacenan datos en cliente, enviados automáticamente en cada petición.
* **Sesiones**: almacenan estado en servidor, identificadas por cookies y permiten mantener login y preferencias.

Note: Es sencillo porque usa texto plano legible por humanos, facilitando debugging y desarrollo. Es extensible mediante cabeceras personalizadas que permiten añadir funcionalidades sin romper compatibilidad. Es stateless, lo que significa que cada petición es independiente, facilitando la escalabilidad horizontal. Es cacheable, permitiendo almacenar respuestas para mejorar el rendimiento y reducir la carga del servidor. Finalmente, es proxy-friendly, lo que permite el uso de intermediarios para funciones como balanceo de carga y seguridad sin afectar la comunicación entre cliente y servidor.


### 1.3. Estructura Petición HTTP

```
GET /usuarios/123 HTTP/1.1 
Host: api.ejemplo.com
Accept: application/json
Authorization: Bearer token...

[body opcional]
```

* Línea: MÉTODO RUTA VERSIÓN
* Cabeceras: metadatos
* Body opcional (POST/PUT)

Note: Toda petición sigue este formato. Línea de petición especifica acción, cabeceras proporcionan contexto, body contiene datos cuando necesario. Estructura simple pero potente.


### 1.4. Estructura Respuesta HTTP

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 156

{"id": 123, "nombre": "Ana"}
```

* Estado: VERSIÓN CÓDIGO TEXTO
* Cabeceras respuesta
* Body con contenido

Note: Respuestas con estructura similar. Código de estado indica resultado (2xx éxito, 4xx error cliente, 5xx error servidor). Cabeceras describen respuesta. Body contiene contenido solicitado o mensaje de error.


### 1.5. Cabeceras HTTP Importantes

**Petición:**
* Accept, Accept-Language
* Host, User-Agent
* Authorization, Cookie

**Respuesta:**
* Content-Type, Content-Length
* Cache-Control, Set-Cookie
* Server, Date

Note: Cabeceras son metadatos cruciales. Accept negocia contenido. Authorization autentica. Content-Type indica formato. Cache-Control optimiza rendimiento. Set-Cookie mantiene sesión.


### 1.6. Métodos HTTP: GET

* **Seguro**: No modifica servidor
* **Idempotente**: Mismo resultado siempre
* **Cacheable**: Por navegadores y proxies
* Parámetros en URL
* Solo lectura

```
GET /productos?categoria=libros&precio_max=30
```

Note: GET es el método más usado. NUNCA debe modificar estado. Perfecto para consultas. Navegadores precachean GET automáticamente. Parámetros visibles en URL permiten compartir enlaces. NUNCA usar GET para acciones que modifican datos.


### 1.6. Métodos HTTP: GET II

**Ejemplo Petición:**
```http
GET /api/usuarios/123 HTTP/1.1
Host: ejemplo.com
Accept: application/json
Authorization: Bearer eyJhbGci...
```

Note: Petición GET incluye método y ruta, cabeceras para negociación contenido y autenticación. Respuesta con código 200 OK indica éxito, Content-Type especifica formato JSON, body contiene datos solicitados.


### 1.6. Métodos HTTP: GET III

**Ejemplo Respuesta:**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{"id": 123, "nombre": "Ana", "email": "ana@ejemplo.com"}
```

Note: Petición GET incluye método y ruta, cabeceras para negociación contenido y autenticación. Respuesta con código 200 OK indica éxito, Content-Type especifica formato JSON, body contiene datos solicitados.


### 1.7. Métodos HTTP: POST

* **No idempotente**: Cada vez crea nuevo recurso
* Datos en body
* Respuesta: 201 Created + Location
* Para crear recursos
* Para formularios

```
POST /usuarios
{"nombre": "Ana", "email": "ana@ejemplo.com"}
→ 201 Created, Location: /usuarios/456
```

Note: POST crea nuevos recursos. No idempotente significa que repetir crea duplicados. Servidor genera ID. Ideal para formularios, subida archivos, operaciones complejas. Usar idempotency keys para operaciones críticas como pagos.


### 1.7. Métodos HTTP: POST II

**Ejemplo Petición:**
```http
POST /api/usuarios HTTP/1.1
Host: ejemplo.com
Content-Type: application/json
Authorization: Bearer eyJhbGci...

{"nombre": "María", "email": "maria@ejemplo.com", "edad": 25}
```

Note: POST envía datos en body. Servidor procesa, crea recurso, genera ID 456. Respuesta 201 Created indica éxito de creación. Cabecera Location proporciona URL del nuevo recurso creado.


### 1.7. Métodos HTTP: POST II

**Ejemplo Respuesta:**
```http
HTTP/1.1 201 Created
Location: /api/usuarios/456
Content-Type: application/json

{"id": 456, "nombre": "María", "email": "maria@ejemplo.com"}
```

Note: POST envía datos en body. Servidor procesa, crea recurso, genera ID 456. Respuesta 201 Created indica éxito de creación. Cabecera Location proporciona URL del nuevo recurso creado.


### 1.8. Métodos HTTP: PUT vs PATCH

**PUT** (reemplazo completo)
* Idempotente
* Reemplaza TODO el recurso
* Cliente especifica ID

**PATCH** (parcial)
* Modifica solo campos enviados
* Más eficiente
* Conserva campos no enviados

Note: PUT reemplaza recurso entero, PATCH solo campos específicos. PUT idempotente garantiza reintentos seguros. PATCH ahorra ancho de banda. Elegir según necesidad: actualización completa o parcial.


### 1.8. Métodos HTTP: PUT II

**Ejemplo Petición PUT:**
```http
PUT /api/usuarios/123 HTTP/1.1
Host: ejemplo.com
Content-Type: application/json

{"nombre": "Ana García", "email": "ana.garcia@ejemplo.com", 
 "edad": 30, "ciudad": "Madrid"}
```

Note: PUT reemplaza COMPLETAMENTE el recurso. Cliente debe enviar todos campos, incluso los no modificados. Si faltara campo "edad", se perdería. Respuesta 200 OK confirma actualización exitosa.


### 1.8. Métodos HTTP: PUT II

**Ejemplo Respuesta:**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{"id": 123, "nombre": "Ana García", 
 "email": "ana.garcia@ejemplo.com", "edad": 30, "ciudad": "Madrid"}
```

Note: PUT reemplaza COMPLETAMENTE el recurso. Cliente debe enviar todos campos, incluso los no modificados. Si faltara campo "edad", se perdería. Respuesta 200 OK confirma actualización exitosa.


### 1.8. Métodos HTTP: PATCH III

**Ejemplo Petición PATCH:**
```http
PATCH /api/usuarios/123 HTTP/1.1
Host: ejemplo.com
Content-Type: application/json

{"email": "nuevo.email@ejemplo.com"}
```

Note: PATCH modifica SOLO campos enviados. Otros campos (nombre, edad, ciudad) se conservan sin cambios. Más eficiente que PUT cuando solo actualizas pocos campos. Reduce payload de red.


### 1.8. Métodos HTTP: PATCH III

**Ejemplo Respuesta:**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{"id": 123, "nombre": "Ana", "email": "nuevo.email@ejemplo.com",
 "edad": 28, "ciudad": "Barcelona"}
```

Note: PATCH modifica SOLO campos enviados. Otros campos (nombre, edad, ciudad) se conservan sin cambios. Más eficiente que PUT cuando solo actualizas pocos campos. Reduce payload de red.


### 1.9. Métodos HTTP: DELETE

* Elimina recurso
* Idempotente (mismo resultado)
* Respuesta: 204 No Content
* **Soft delete vs Hard delete**
* Precauciones: autenticación fuerte

Note: DELETE borra recurso. Idempotente porque borrar algo ya borrado da mismo resultado final. Soft delete marca como eliminado (recuperable), hard delete borra físicamente. SIEMPRE verificar permisos antes de DELETE.


### 1.9. Métodos HTTP: DELETE II

**Ejemplo Petición DELETE:**
```http
DELETE /api/usuarios/123 HTTP/1.1
Host: ejemplo.com
Authorization: Bearer eyJhbGci...
```

Note: DELETE requiere autenticación fuerte. La header Authorization incluye token. Petición elimina usuario 123. 


### 1.9. Métodos HTTP: DELETE II

**Ejemplo Respuesta (exitosa):**
```http
HTTP/1.1 204 No Content
```

Note: Respuesta 204 No Content indica eliminación exitosa sin body. "No Content" significa que no hay datos que devolver. Cliente asume recurso eliminado. 


### 1.9. Métodos HTTP: DELETE II

**Ejemplo Respuesta (recurso no existe):**
```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{"error": "Usuario no encontrado"}
```

Note: Si recurso ya no existe, 404 Not Found pero operación sigue siendo exitosa (idempotente). En el body se puede incluir mensaje informativo.


### 1.10. Métodos HTTP: HEAD y OPTIONS

**HEAD**: Metadatos sin body
* Verificar existencia
* Comprobar tamaño
* Validar enlaces

**OPTIONS**: Capacidades disponibles
* Qué métodos acepta
* Preflight CORS
* Auto-documentación

Note: HEAD obtiene cabeceras sin descargar contenido, útil para validar recursos. OPTIONS descubre capacidades del servidor, crucial para CORS en navegadores. Ambos ayudan a optimizar y validar.


### 1.10. Métodos HTTP: HEAD II

**Ejemplo Petición HEAD:**
```http
HEAD /api/archivos/documento.pdf HTTP/1.1
Host: ejemplo.com
```

Note: HEAD devuelve SOLO cabeceras, sin body. Útil para verificar si archivo existe, conocer tamaño antes de descargar, comprobar si ha cambiado (Last-Modified, ETag). Ahorra ancho de banda.


### 1.10. Métodos HTTP: HEAD II

**Ejemplo Respuesta HEAD:**
```http
HTTP/1.1 200 OK
Content-Type: application/pdf
Content-Length: 2458624
Last-Modified: Mon, 09 Dec 2024 10:30:00 GMT
ETag: "abc123def456"
```

Note: HEAD devuelve SOLO cabeceras, sin body. Útil para verificar si archivo existe, conocer tamaño antes de descargar, comprobar si ha cambiado (Last-Modified, ETag). Ahorra ancho de banda.


### 1.10. Métodos HTTP: OPTIONS III

**Ejemplo Petición OPTIONS:**
```http
OPTIONS /api/usuarios HTTP/1.1
Host: ejemplo.com
Origin: https://app.ejemplo.com
```

Note: OPTIONS informa métodos permitidos en recurso. Crucial para CORS (preflight): navegador pregunta si origen permitido antes de petición real. Allow lista métodos disponibles. Access-Control-* configuran CORS.


### 1.10. Métodos HTTP: OPTIONS III

**Ejemplo Respuesta OPTIONS:**
```http
HTTP/1.1 204 No Content
Allow: GET, POST, PUT, DELETE, OPTIONS
Access-Control-Allow-Origin: https://app.ejemplo.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
```

Note: OPTIONS informa métodos permitidos en recurso. Crucial para CORS (preflight): navegador pregunta si origen permitido antes de petición real. Allow lista métodos disponibles. Access-Control-* configuran CORS.


### 1.11. Códigos de Estado HTTP

* **2xx**: Éxito (200 OK, 201 Created, 204 No Content)
* **3xx**: Redirección (301 Permanent, 302 Temporary, 304 Not Modified)
* **4xx**: Error cliente (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found)
* **5xx**: Error servidor (500 Internal Error, 503 Service Unavailable)

Note: Códigos organizados por familias. 2xx todo bien. 3xx seguir otro enlace. 4xx culpa del cliente. 5xx culpa del servidor. Usar códigos correctos facilita debugging y permite a clientes tomar decisiones apropiadas.


### 1.11. Códigos Estado: 2xx Éxito

**200 OK - Petición exitosa:**
```http
HTTP/1.1 200 OK
Content-Type: application/json
{"mensaje": "Operación exitosa"}
```

Note: 200 OK más común para GET, PUT, PATCH exitosos. 201 Created específico para POST que crea recurso, incluye Location. 204 No Content para DELETE exitoso o actualizaciones sin datos que devolver.


### 1.11. Códigos Estado: 2xx Éxito

**201 Created - Recurso creado:**
```http
HTTP/1.1 201 Created
Location: /api/usuarios/789
{"id": 789, "nombre": "Pedro"}
```

Note: 200 OK más común para GET, PUT, PATCH exitosos. 201 Created específico para POST que crea recurso, incluye Location. 204 No Content para DELETE exitoso o actualizaciones sin datos que devolver.


### 1.11. Códigos Estado: 2xx Éxito

**204 No Content - Éxito sin respuesta:**
```http
HTTP/1.1 204 No Content
```

Note: 200 OK más común para GET, PUT, PATCH exitosos. 201 Created específico para POST que crea recurso, incluye Location. 204 No Content para DELETE exitoso o actualizaciones sin datos que devolver.


### 1.11. Códigos Estado: 3xx Redirección

**301 Moved Permanently:**
```http
HTTP/1.1 301 Moved Permanently
Location: https://ejemplo.com/nueva-ubicacion
```

Note: 301 redirige permanentemente, navegadores actualizan marcadores. 302 redirige temporalmente, mantener URL original. 304 indica recurso no modificado desde última petición, usa caché local. Ahorra ancho de banda.


### 1.11. Códigos Estado: 3xx Redirección

**302 Found (Temporary):**
```http
HTTP/1.1 302 Found
Location: https://ejemplo.com/temporal
```

Note: 301 redirige permanentemente, navegadores actualizan marcadores. 302 redirige temporalmente, mantener URL original. 304 indica recurso no modificado desde última petición, usa caché local. Ahorra ancho de banda.


### 1.11. Códigos Estado: 3xx Redirección

**304 Not Modified:**
```http
HTTP/1.1 304 Not Modified
ETag: "abc123"
```

Note: 301 redirige permanentemente, navegadores actualizan marcadores. 302 redirige temporalmente, mantener URL original. 304 indica recurso no modificado desde última petición, usa caché local. Ahorra ancho de banda.


### 1.11. Códigos Estado: 4xx Error Cliente

**400 Bad Request:**
```http
HTTP/1.1 400 Bad Request
{"error": "Formato JSON inválido"}
```

Note: 400 para datos mal formados, validaciones fallidas. 401 para autenticación fallida/ausente, incluye WWW-Authenticate indicando método requerido. 403 usuario autenticado pero sin permisos suficientes. Diferencia importante 401 vs 403.


### 1.11. Códigos Estado: 4xx Error Cliente

**401 Unauthorized:**
```http
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer
{"error": "Token inválido o expirado"}
```

Note: 400 para datos mal formados, validaciones fallidas. 401 para autenticación fallida/ausente, incluye WWW-Authenticate indicando método requerido. 403 usuario autenticado pero sin permisos suficientes. Diferencia importante 401 vs 403.


### 1.11. Códigos Estado: 4xx Error Cliente

**403 Forbidden:**
```http
HTTP/1.1 403 Forbidden
{"error": "No tienes permisos para este recurso"}
```

Note: 400 para datos mal formados, validaciones fallidas. 401 para autenticación fallida/ausente, incluye WWW-Authenticate indicando método requerido. 403 usuario autenticado pero sin permisos suficientes. Diferencia importante 401 vs 403.


### 1.11. Códigos Estado: 4xx Error Cliente II

**404 Not Found:**
```http
HTTP/1.1 404 Not Found
{"error": "Usuario con ID 999 no encontrado"}
```

Note: 404 recurso no existe, más común. 409 conflicto con estado actual, útil para duplicados, restricciones negocio. 429 rate limiting, demasiadas peticiones, Retry-After indica cuándo reintentar. Protege servidor de abuso.


### 1.11. Códigos Estado: 4xx Error Cliente II

**409 Conflict:**
```http
HTTP/1.1 409 Conflict
{"error": "Email ya registrado"}
```

Note: 404 recurso no existe, más común. 409 conflicto con estado actual, útil para duplicados, restricciones negocio. 429 rate limiting, demasiadas peticiones, Retry-After indica cuándo reintentar. Protege servidor de abuso.


### 1.11. Códigos Estado: 4xx Error Cliente II

**429 Too Many Requests:**
```http
HTTP/1.1 429 Too Many Requests
Retry-After: 3600
{"error": "Límite de peticiones excedido"}
```

Note: 404 recurso no existe, más común. 409 conflicto con estado actual, útil para duplicados, restricciones negocio. 429 rate limiting, demasiadas peticiones, Retry-After indica cuándo reintentar. Protege servidor de abuso.


### 1.11. Códigos Estado: 5xx Error Servidor

**500 Internal Server Error:**
```http
HTTP/1.1 500 Internal Server Error
{"error": "Error interno del servidor"}
```

Note: 500 error genérico servidor, excepción no controlada. 502 proxy/gateway recibió respuesta inválida de servidor upstream. 503 servidor temporalmente no disponible, mantenimiento o sobrecarga, Retry-After sugiere cuándo reintentar. Nunca culpa del cliente.


### 1.11. Códigos Estado: 5xx Error Servidor

**502 Bad Gateway:**
```http
HTTP/1.1 502 Bad Gateway
{"error": "Servidor upstream no responde"}
```

Note: 500 error genérico servidor, excepción no controlada. 502 proxy/gateway recibió respuesta inválida de servidor upstream. 503 servidor temporalmente no disponible, mantenimiento o sobrecarga, Retry-After sugiere cuándo reintentar. Nunca culpa del cliente.


### 1.11. Códigos Estado: 5xx Error Servidor

**503 Service Unavailable:**
```http
HTTP/1.1 503 Service Unavailable
Retry-After: 300
{"error": "Servicio en mantenimiento"}
```

Note: 500 error genérico servidor, excepción no controlada. 502 proxy/gateway recibió respuesta inválida de servidor upstream. 503 servidor temporalmente no disponible, mantenimiento o sobrecarga, Retry-After sugiere cuándo reintentar. Nunca culpa del cliente.


### 1.12. HTTPS: Seguridad Esencial

* HTTP + SSL/TLS
* **Cifrado** de comunicación
* **Autenticación** del servidor
* **Integridad** de datos
* Certificados digitales
* Let's Encrypt: gratuito

Note: HTTPS ya no es opcional. Cifra toda comunicación evitando espionaje. Autentica servidor previniendo suplantación. Let's Encrypt ofrece certificados gratuitos y automatizados. Navegadores penalizan HTTP. APIs modernas requieren HTTPS.


### 1.13. Contenido Estático vs Dinámico

**Estático:**
* Archivos fijos (HTML, CSS, JS, imágenes)
* Mismo contenido para todos
* Rapidísimo
* Económico

**Dinámico:**
* Generado por servidor
* Personalizado por usuario
* Consulta BD
* Lógica de negocio

Note: Estático es contenido preexistente, velocidad máxima. Dinámico se genera al vuelo, permite personalización. Modernamente se combinan: frontend estático consume API dinámica (JAMstack).


### 1.14. Flujo Página Dinámica

1. Cliente solicita URL
2. Servidor web recibe petición
3. Delega a módulo ejecución (PHP, Python...)
4. Código ejecuta lógica
5. Consulta base de datos
6. Genera HTML dinámico
7. Devuelve respuesta
8. Navegador renderiza

Note: Proceso completo implica múltiples componentes. Servidor web (Apache, Nginx) recibe petición y delega a runtime apropiado. Código ejecuta lógica de negocio, consulta datos, construye respuesta personalizada. Más lento que estático pero permite funcionalidad rica.


### 1.15. Tecnologías Server-Side

* **PHP**: El más popular, LAMP stack   
* **Python**: Django, Flask, elegante   
* **Java**: Spring Boot, empresarial   
* **Node.js**: JavaScript everywhere  
* **Ruby**: Rails, productividad  

Note: Cada tecnología tiene fortalezas. PHP domina hosting compartido, fácil aprender. Python excelente para apps complejas. Java robusto para enterprise. Node.js mismo lenguaje frontend/backend. Ruby optimiza desarrollo rápido.

---

## BLOQUE 2: Componentes y Arquitectura

Note: Comprendiendo cómo se estructura y organiza el código.


### 2.1. Cliente vs Servidor

**Cliente (Frontend):**
* Navegador ejecuta
* HTML, CSS, JavaScript
* Presentación e interacción
* Validación preliminar

**Servidor (Backend):**
* Código en servidor
* Lógica de negocio
* Acceso a datos
* Seguridad y validación

Note: División clara de responsabilidades. Cliente gestiona interfaz y experiencia usuario. Servidor gestiona datos, seguridad, lógica crítica. NUNCA confiar solo en validaciones cliente, siempre revalidar en servidor.


### 2.2. Arquitectura Monolítica

* Todo en una aplicación
* Base de datos única
* Despliegue de bloque
* Simple inicialmente
* Difícil escalar selectivamente
* Acoplamiento alto

Note: Monolito tradicional: todo junto. Ventajas: simple desarrollo inicial, fácil desplegar, llamadas internas rápidas. Desventajas: escala todo o nada, cambios requieren redespliegue completo, acoplamiento creciente dificulta mantenimiento.


### 2.3. Arquitectura Microservicios

* Servicios pequeños independientes
* Base de datos por servicio
* Despliegue independiente
* Comunicación vía APIs
* Escalabilidad granular
* Equipos autónomos

Note: Microservicios dividen aplicación en servicios especializados. Ventajas: escala componentes independientemente, tecnologías heterogéneas, equipos autónomos, fallos aislados. Desventajas: complejidad operacional, latencia red, transacciones distribuidas complejas.


### 2.4. Cuándo Usar Cada Arquitectura

**Monolito:**
* MVP y proyectos nuevos
* Equipo pequeño (<10)
* Dominio simple
* Recursos limitados

**Microservicios:**
* Aplicación grande compleja
* Múltiples equipos (>20)
* Escala independiente necesaria
* DevOps maduro

Note: No hay arquitectura única correcta. Monolito perfecto para comenzar, validar idea rápidamente. Microservicios cuando escala y complejidad lo justifican. Muchas empresas grandes empezaron monolito y evolucionaron gradualmente.


### 2.5. Patrón MVC
Componentes: 
* **Modelo**: Datos y lógica negocio. Esta acargo de gestionar el acceso a la base de datos, las reglas de negocio y la lógica de la aplicación.
* **Vista**: Presentación UI. Esta encargada de mostrar los datos al usuario y de manejar la interacción con él.
* **Controlador**: Coordina Modelo-Vista. Esta recibe las peticiones del usuario, invoca el Modelo para procesar datos y selecciona la Vista adecuada para mostrar la respuesta.

Note: MVC organiza código en tres componentes con roles claros. Modelo encapsula datos y reglas negocio. Vista solo presenta. Controlador orquesta. 


### 2.5. Patrón MVC II
Características:
- Separa responsabilidades claramente: Modelo, Vista, Controlador
- Facilita mantenimiento y testing: componentes aislados
- Trabajo en equipo eficiente: frontend/backend

Note: La separación permite cambiar UI sin tocar lógica negocio, testear componentes aisladamente, equipos trabajar en paralelo.


### 2.6. Principios SOLID

* **S**ingle Responsibility
* **O**pen/Closed
* **L**iskov Substitution
* **I**nterface Segregation
* **D**ependency Inversion

Código mantenible y flexible

Note: SOLID son cinco principios fundamentales para código de calidad. Una clase una responsabilidad. Abierto extensión cerrado modificación. Subtipos deben sustituir supertipo. Interfaces pequeñas específicas. Depender de abstracciones no implementaciones. Aplicar SOLID mejora mantenibilidad drásticamente.

---

## BLOQUE 3: Tecnologías

Note: Herramientas concretas para construir aplicaciones web.


### 3.1. Modelos de Ejecución

**Interpretados**: PHP, Python, Ruby
* Código fuente directo
* Desarrollo rápido
* Sin compilación

**Compilados**: Java, C#, Go
* Bytecode o nativo
* Mayor rendimiento
* Tipado fuerte

Note: Lenguajes interpretados ejecutan código directamente, ciclo desarrollo rápido. Lenguajes compilados generan bytecode/binario, mejor rendimiento. Java/C# usan VM con JIT. Go/Rust compilan a nativo, máximo rendimiento.


### 3.2. LAMP Stack

* **L**inux: Sistema operativo
* **A**pache: Servidor web
* **M**ySQL: Base de datos
* **P**HP: Lenguaje

Completamente gratuito y open source
Hosting universal disponible
WordPress, Drupal, Joomla lo usan

Note: LAMP es el stack clásico que construyó la web. Totalmente gratuito, hosting económico abundante, comunidad masiva. Aunque antiguo, sigue siendo relevante y funcional para millones de sitios.


### 3.3. Stacks Modernos

**MEAN/MERN**:
* MongoDB, Express, Angular/React, Node.js
* Todo JavaScript

**JAMstack**:
* JavaScript, APIs, Markup
* Estático + APIs

Note: Stacks modernos optimizan para casos de uso específicos. MEAN/MERN unifica lenguaje frontend/backend. JAMstack maximiza velocidad sirviendo estático y consumiendo APIs. Elegir stack según requisitos proyecto y experiencia equipo.

---

## BLOQUE 4: Servicios y Comunicación

Note: Cómo aplicaciones se comunican entre sí.


### 4.1. APIs Web

**Aplicación Web**: Genera HTML para humanos

**API Web**: Devuelve datos (JSON/XML) para código

APIs permiten:
* Apps móviles consumir servicios
* SPAs consultar backend
* Integración entre sistemas

Note: APIs son interfaces para que código consuma servicios. Devuelven datos estructurados no HTML. Permiten mismo backend servir web, móvil, integraciones. Fundamental en arquitectura moderna.


### 4.2. REST (Representational State Transfer)

* Recursos con URLs
* Métodos HTTP estándar
* Stateless
* JSON típicamente
* Cacheable

```
GET /api/usuarios
POST /api/usuarios
PUT /api/usuarios/123
DELETE /api/usuarios/123
```

Note: REST es estilo arquitectónico dominante para APIs. Usa métodos HTTP correctamente. URLs representan recursos. Stateless facilita escalabilidad. Cacheable aprovecha HTTP. Simple, universal, bien entendido.


### 4.2. REST II - Ejemplo Completo CRUD

**Listar usuarios:**
```http
GET /api/usuarios HTTP/1.1
→ 200 OK
[{"id": 1, "nombre": "Ana"}, {"id": 2, "nombre": "Luis"}]
```

Note: Ejemplo completo CRUD (Create, Read, Update, Delete) con REST. URLs representan recursos (usuarios), métodos HTTP indican acción. Respuestas con códigos apropiados. Stateless: cada petición autocontenida con toda información necesaria.


### 4.2. REST II - Ejemplo Completo CRUD

**Crear usuario:**
```http
POST /api/usuarios
{"nombre": "María"}
→ 201 Created, Location: /api/usuarios/3
```

Note: Ejemplo completo CRUD (Create, Read, Update, Delete) con REST. URLs representan recursos (usuarios), métodos HTTP indican acción. Respuestas con códigos apropiados. Stateless: cada petición autocontenida con toda información necesaria.


### 4.2. REST II - Ejemplo Completo CRUD

**Actualizar usuario:**
```http
PUT /api/usuarios/3
{"nombre": "María García"}
→ 200 OK
```

Note: Ejemplo completo CRUD (Create, Read, Update, Delete) con REST. URLs representan recursos (usuarios), métodos HTTP indican acción. Respuestas con códigos apropiados. Stateless: cada petición autocontenida con toda información necesaria.


### 4.2. REST II - Ejemplo Completo CRUD

**Eliminar usuario:**
```http
DELETE /api/usuarios/3
→ 204 No Content
```

Note: Ejemplo completo CRUD (Create, Read, Update, Delete) con REST. URLs representan recursos (usuarios), métodos HTTP indican acción. Respuestas con códigos apropiados. Stateless: cada petición autocontenida con toda información necesaria.


### 4.3. GraphQL

* Cliente pide exactamente campos necesarios
* Una petición obtiene datos relacionados
* Fuertemente tipado
* Evita over-fetching y under-fetching
* Alternativa a REST

Note: GraphQL lenguaje consulta para APIs. Cliente especifica estructura exacta datos necesarios. Evita múltiples peticiones REST. Reduce transferencia datos. Más complejo que REST pero potente para clientes con necesidades diversas.


### 4.4. WebSockets

* Conexión persistente bidireccional
* Comunicación tiempo real
* Ideal para: chat, juegos, notificaciones, dashboards
* Baja latencia
* Push del servidor

Note: WebSockets mantienen conexión abierta permitiendo comunicación bidireccional tiempo real. Servidor puede enviar datos sin esperar petición cliente. Perfecto para aplicaciones que necesitan actualizaciones instantáneas.


### 4.5. Autenticación JWT

**JWT = JSON Web Token**

```
header.payload.signature
```

* Header: algoritmo
* Payload: datos usuario
* Signature: verificación

Stateless, portable, autocontenido

Note: JWT token cifrado conteniendo información usuario. Stateless significa servidor no guarda sesión. Cliente incluye token en cada petición. Servidor verifica firma y extrae datos. Escalable, funciona entre dominios, ideal microservicios.


### 4.5. Autenticación JWT II - Estructura

**Token JWT real:**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFuYSIsImFkbWluIjp0cnVlfQ.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

**Header (decodificado):**
```json
{"alg": "HS256", "typ": "JWT"}
```

Note: JWT compuesto de tres partes separadas por punto. Header especifica algoritmo (HS256, RS256). Payload contiene claims (datos usuario, expiración). Signature previene manipulación. Base64 codificado pero NO cifrado, no datos sensibles en payload.


### 4.5. Autenticación JWT II - Estructura

**Payload (decodificado):**
```json
{"sub": "1234567890", "name": "Ana", "admin": true, "exp": 1735689600}
```

**Signature:** Verifica integridad

Note: JWT compuesto de tres partes separadas por punto. Header especifica algoritmo (HS256, RS256). Payload contiene claims (datos usuario, expiración). Signature previene manipulación. Base64 codificado pero NO cifrado, no datos sensibles en payload.


### 4.6. Flujo Autenticación JWT

1. Usuario login con credenciales
2. Servidor verifica y genera JWT
3. Cliente guarda JWT
4. Cliente incluye JWT en cada petición:
   `Authorization: Bearer token...`
5. Servidor verifica JWT
6. Procesa petición

Note: Proceso simple y eficaz. Login genera token. Cliente almacena y envía en cada petición. Servidor valida token sin consultar BD. Expira automáticamente por seguridad. Renovar antes de expirar para sesión continua.


### 4.6. Flujo Autenticación JWT II - Ejemplo

**1. Login:**
```http
POST /api/login
{"username": "ana", "password": "secreto123"}
→ 200 OK
{"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."}
```

Note: Login devuelve token JWT. Cliente almacena (localStorage, cookie httpOnly). Incluye en Authorization header con prefijo Bearer en peticiones protegidas. Servidor valida firma y expiración. Token expirado devuelve 401, cliente debe renovar o reautenticar.


### 4.6. Flujo Autenticación JWT II - Ejemplo

**2. Petición autenticada:**
```http
GET /api/usuarios/me HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
→ 200 OK
{"id": 123, "nombre": "Ana", "email": "ana@ejemplo.com"}
```

Note: Login devuelve token JWT. Cliente almacena (localStorage, cookie httpOnly). Incluye en Authorization header con prefijo Bearer en peticiones protegidas. Servidor valida firma y expiración. Token expirado devuelve 401, cliente debe renovar o reautenticar.


### 4.6. Flujo Autenticación JWT II - Ejemplo

**3. Token expirado:**
```http
GET /api/usuarios/me
Authorization: Bearer token_expirado
→ 401 Unauthorized
{"error": "Token expirado"}
```

Note: Login devuelve token JWT. Cliente almacena (localStorage, cookie httpOnly). Incluye en Authorization header con prefijo Bearer en peticiones protegidas. Servidor valida firma y expiración. Token expirado devuelve 401, cliente debe renovar o reautenticar.

---

## BLOQUE 5: Infraestructura

Note: Software que ejecuta nuestras aplicaciones.


### 5.1. Servidor Web

**Apache HTTP Server**:
* Veterano (1995)
* Muy configurable
* Módulos abundantes
* .htaccess

**Nginx**:
* Moderno (2004)
* Alto rendimiento
* Bajo consumo memoria
* Proxy inverso eficiente

Note: Servidores web reciben peticiones HTTP y responden. Apache flexible con toneladas módulos. Nginx más rápido y eficiente. Nginx excelente para contenido estático y proxy. Apache para compatibilidad máxima.


### 5.2. Servidores de Aplicaciones

**Para código dinámico:**
* Tomcat (Java)
* Gunicorn (Python)
* uWSGI (Python)
* IIS (ASP.NET)

Ejecutan lógica aplicación
Generan respuestas dinámicas
Integran con servidor web

Note: Servidores aplicaciones ejecutan código dinámico. Servidor web recibe petición y delega a servidor aplicación. Este ejecuta código, consulta BD, genera respuesta. Separación permite optimizar cada capa.


### 5.3. Bases de Datos

**SQL (Relacionales)**:
* MySQL, PostgreSQL
* Esquema rígido
* Transacciones ACID
* Consultas complejas

Note: SQL para datos estructurados, relaciones complejas, consistencia fuerte. NoSQL para flexibilidad esquema, escala masiva, datos variados. Elegir según naturaleza datos y requisitos aplicación.


### 5.3. Bases de Datos

**NoSQL**:
* MongoDB, Redis
* Esquema flexible
* Escalabilidad horizontal
* Datos no estructurados

Note: SQL para datos estructurados, relaciones complejas, consistencia fuerte. NoSQL para flexibilidad esquema, escala masiva, datos variados. Elegir según naturaleza datos y requisitos aplicación.

---

## BLOQUE 6: Despliegue

Note: Llevando código a producción y gestionando crecimiento.


### 6.1. Entornos de Despliegue

* **Development**: Local, datos prueba
* **Testing**: Pruebas automatizadas
* **Staging**: Réplica producción
* **Production**: Usuarios reales

Separación previene errores
Permite validar antes de producción

Note: Múltiples entornos aíslan cambios. Development para desarrollar. Testing para CI/CD. Staging idéntico a producción para validar. Production donde usuarios reales. Promoción gradual minimiza riesgo.


### 6.2. Escalabilidad Vertical

**Scale Up**: Servidor más potente

* Más CPU, RAM, disco rápido
* Simple: no cambiar código
* Límite físico inevitable
* Punto único de fallo
* Tiempo inactividad al escalar

Note: Escalabilidad vertical mejora hardware servidor existente. Simple implementar pero limitado. Llega punto donde no hay servidores más potentes. Si servidor cae, todo cae. Primera estrategia antes de horizontal.


### 6.3. Escalabilidad Horizontal

**Scale Out**: Más servidores

* Múltiples servidores idénticos
* Balanceador de carga distribuye
* Sin límite teórico
* Alta disponibilidad
* Más complejo configurar

Note: Escalabilidad horizontal añade servidores trabajando juntos. Balanceador distribuye peticiones. Sin límite escalado, alta disponibilidad, tolera fallos. Requiere arquitectura stateless, sesiones compartidas, mayor complejidad operacional.


### 6.4. Docker: Contenedores

```dockerfile
FROM php:8.2-apache
COPY . /var/www/html/
RUN docker-php-ext-install mysqli
EXPOSE 80
```

* Empaqueta app + dependencias
* "Funciona en mi máquina" → funciona everywhere
* Ligero vs VMs
* Portable universalmente

Note: Docker empaqueta aplicación con todas dependencias en imagen. Elimina problemas "funciona en mi máquina". Imagen corre idénticamente en cualquier lugar. Más ligero que VMs, arranca segundos. Fundamental en despliegue moderno.


### 6.4. Docker: Contenedores II - Ejemplo Completo

**Dockerfile completo:**
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

Note: Dockerfile define imagen: base Node.js Alpine ligera, establece directorio trabajo, copia package.json, instala dependencias, copia código, expone puerto, define comando arranque. Build crea imagen. Run ejecuta contenedor, -d background, -p mapea puertos, --name nombra contenedor.


### 6.4. Docker: Contenedores II - Ejemplo Completo

**Construir y ejecutar:**
```bash
docker build -t mi-app:1.0 .
docker run -d -p 3000:3000 --name mi-app-container mi-app:1.0
```

**Ver logs:**
```bash
docker logs mi-app-container
```

Note: Dockerfile define imagen: base Node.js Alpine ligera, establece directorio trabajo, copia package.json, instala dependencias, copia código, expone puerto, define comando arranque. Build crea imagen. Run ejecuta contenedor, -d background, -p mapea puertos, --name nombra contenedor.


### 6.5. Docker Compose

```yaml
services:
  web:
    image: nginx
  app:
    image: php:fpm
  db:
    image: mysql:8
```

* Define múltiples contenedores
* Networking automático
* Volúmenes persistentes
* `docker-compose up` arranca todo

Note: Docker Compose orquesta múltiples contenedores. Define servicios, redes, volúmenes en YAML. Un comando arranca stack completo. Perfecto desarrollo local y aplicaciones pequeñas.


### 6.5. Docker Compose II - Ejemplo Completo

```yaml
version: '3.8'
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - app
  
  app:
    build: .
    environment:
      - DB_HOST=db
      - DB_USER=root
      - DB_PASS=secret
    depends_on:
      - db
  
  db:
    image: mysql:8
    environment:
      - MYSQL_ROOT_PASSWORD=secret
      - MYSQL_DATABASE=miapp
    volumes:
      - db_data:/var/lib/mysql

volumes:
  db_data:
```

Note: Compose define stack completo: Nginx proxy, aplicación custom, MySQL. depends_on establece orden arranque. environment configura variables. volumes persisten datos BD. Networking automático entre servicios por nombre. Un comando `docker-compose up -d` arranca todo el stack.


### 6.6. Kubernetes (K8s)

* Orquestación contenedores escala producción
* Gestiona miles de contenedores
* Auto-escalado
* Auto-recuperación (self-healing)
* Rolling updates sin downtime
* Service discovery

Note: Kubernetes orquesta contenedores a escala empresarial. Detecta fallos y reinicia. Escala automáticamente según carga. Actualiza sin caídas. Complejo pero potente. Servicios gestionados (GKE, EKS) simplifican.


### 6.7. Cloud Computing
3 modelos principales:
* **IaaS**: Infraestructura (VMs, redes)
* **PaaS**: Plataforma (runtime gestionado)
* **SaaS**: Software (app completa)

**Proveedores**: AWS, Google Cloud, Azure

* Pago por uso
* Escalabilidad infinita
* Sin gestión hardware

Note: Cloud ofrece recursos bajo demanda. IaaS para control total. PaaS para deployment simple. SaaS listo usar. Ventajas: elasticidad, pago por uso, global, sin CAPEX. Fundamental en arquitecturas modernas.


### 6.8. CI/CD

**Continuous Integration**:
* Integrar código frecuentemente
* Tests automáticos en cada commit
* Detecta errores rápido

**Continuous Deployment**:
* Despliegue automático a producción
* Tras pasar tests
* Entregas frecuentes

Note: CI/CD automatiza build, test y deploy. CI integra código continuamente ejecutando tests. CD despliega automáticamente tras validar. Reduce errores, acelera entregas, mejora calidad. Herramientas: GitHub Actions, GitLab CI, Jenkins.

---

## BLOQUE 7: Seguridad y Monitorización

Note: Protegiendo y supervisando aplicaciones en producción.


### 7.1. Seguridad Básica

* **HTTPS siempre**: Cifrado obligatorio
* **Autenticación HTTP**: Basic, Bearer tokens
* **Control de acceso**: Verificar permisos
* **Validar inputs**: NUNCA confiar cliente
* **Principio mínimo privilegio**: Solo permisos necesarios

Note: Seguridad debe diseñarse desde inicio. HTTPS ya no opcional. Autenticar usuarios. Autorizar cada acción. Validar toda entrada. Denegar por defecto, permitir explícitamente. Defensa en profundidad.


### 7.2. Autenticación HTTP Basic

```apache
<Directory /admin>
    AuthType Basic
    AuthName "Área Restringida"
    AuthUserFile /etc/.htpasswd
    Require valid-user
</Directory>
```

- Simple pero limitado 
- Solo con HTTPS
- Para áreas administrativas

Note: Basic Auth simple: usuario/contraseña. Credenciales en Base64, fácil interceptar. SOLO con HTTPS. Útil para proteger áreas admin simples. Para producción seria usar JWT, OAuth2.


### 7.3. Logs y Monitorización

**Access Log**: Todas las peticiones
**Error Log**: Errores y warnings

Analizar con: `tail`, `grep`, `awk`

**Métricas clave**:
* CPU, RAM, disco, red
* Tiempo respuesta
* Tasa errores

Note: Logs registran todo lo que sucede. Access log para análisis tráfico. Error log para debugging. Monitorear métricas detecta problemas antes que afecten usuarios. Alertas automáticas en umbrales críticos.


### 7.4. Rotación de Logs

```
/var/log/apache2/*.log {
    daily
    rotate 14
    compress
}
```
Logs crecen indefinidamente, llenan disco.
- Rotación periódica
- Comprimir antiguos
- Eliminar muy antiguos

Note: Sin rotación logs llenan disco. Configurar rotación automática: diaria, mantener últimos 14 días, comprimir. Balancea necesidad auditoría con espacio disponible.


### 7.5. Herramientas Monitorización

* **Prometheus + Grafana**: Métricas y dashboards
* **ELK Stack**: Logs centralizados
* **Nagios**: Alertas tradicional
* **New Relic/Datadog**: SaaS completo

Observabilidad = Logs + Metrics + Traces

Note: Herramientas profesionales cruciales en producción. Prometheus recolecta métricas. Grafana visualiza dashboards. ELK centraliza logs de múltiples servidores. Observabilidad completa requiere logs, métricas y trazas distribuidas.

---

## Resumen Final

### Del Protocolo a la Producción

1. **HTTP/HTTPS**: Comunicación base
2. **Contenido dinámico**: Personalización
3. **Arquitecturas**: Organizar código
4. **Tecnologías**: Herramientas construcción
5. **APIs**: Comunicación entre sistemas
6. **Servidores**: Ejecutar aplicaciones
7. **Despliegue**: Llevar a producción
8. **Seguridad y logs**: Proteger y supervisar

Note: Hemos recorrido ciclo completo desarrollo y despliegue web. Desde protocolo HTTP hasta monitorización producción. Cada bloque fundamental para profesional completo. Continuar profundizando cada área según necesidades proyecto.
