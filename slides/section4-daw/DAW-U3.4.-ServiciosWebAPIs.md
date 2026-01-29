# DAW-U3.4 - Servicios Web y Comunicación con APIs

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice I

1. ¿Qué es un servicio web y qué aporta?
2. Diferencia entre servicio web y página web dinámica
3. Protocolos de comunicación de API
4. JWT: autenticación y autorización

## Índice II

5. Ejemplo: arquitectura de Netflix
6. Resumen y Conclusiones
7. Preguntas

---

## 1. ¿Qué es un servicio web y qué aporta?

Note: Las APIs son el pegamento del ecosistema digital moderno. Cada vez que usáis una app bancaria, compartís en redes sociales o pedís comida, hay APIs trabajando en segundo plano. Un servicio web es básicamente una API que permite a aplicaciones comunicarse entre sí a través de Internet. Entender cómo funcionan es fundamental para cualquier ingeniero DevOps o desarrollador moderno.


### 1.1. Definición y conceptos fundamentales

**Servicio web: comunicación máquina-a-máquina**

- Sistema para interacción entre aplicaciones
- API: conjunto de reglas de interacción
- Endpoint: URL específica del servicio
- Ejemplo: `https://api.ejemplo.com/usuarios`

Note: Un servicio web es un sistema diseñado para que diferentes aplicaciones se comuniquen automáticamente sin intervención humana. Una API (Application Programming Interface) es el contrato que define cómo debe ser esa comunicación. Cada funcionalidad de la API tiene un endpoint, que es simplemente una URL donde está disponible. Por ejemplo, si queremos gestionar usuarios, tendríamos un endpoint en `/usuarios`, para productos en `/productos`, etc.


### 1.2. Características de los servicios web

**Fundamentos técnicos**

- Protocolos web estándar: HTTP/HTTPS
- Formatos de datos: JSON, XML
- Acceso mediante URLs únicas
- Independencia de plataforma
- Comunicación petición-respuesta

Note: Los servicios web se construyen sobre tecnologías estándar que todos los sistemas conocen. Usan HTTP como transporte, igual que las páginas web. Los datos se intercambian típicamente en JSON o XML, formatos estructurados y legibles. Cada recurso tiene su propia URL. Lo brillante es que no importa si el cliente es Java y el servidor Python: ambos hablan HTTP y JSON.


### 1.3. ¿Qué aportan los servicios web? - Integración

**Conectando sistemas diversos**

- Diferentes aplicaciones comparten funcionalidades
- Una app de escritorio puede publicar en Twitter
- E-commerce integra pasarelas de pago
- Sistemas empresariales se conectan entre departamentos

Note: La integración es quizás el beneficio más importante. Imaginad una tienda online: necesita integrarse con PayPal para cobros, con Google Maps para direcciones, con SendGrid para enviar emails, y con su propio sistema de inventario. Gracias a las APIs, cada sistema expone su funcionalidad y otros pueden consumirla. Sin APIs, cada integración requeriría desarrollo custom complejo.


### 1.3. ¿Qué aportan los servicios web? - Flexibilidad

**Escalabilidad y evolución**

- Aplicaciones más robustas y modulares
- Escalar componentes de forma independiente
- Actualizar servicios sin afectar otros
- Soportar múltiples clientes simultáneos

Note: Los servicios web facilitan construir aplicaciones modulares donde cada parte puede evolucionar independientemente. Si vuestro servicio de usuarios tiene mucha carga, podéis escalarlo sin tocar el servicio de pagos. Si necesitáis actualizar el algoritmo de recomendaciones, lo hacéis en su servicio sin desplegar toda la aplicación. Esta flexibilidad es clave para aplicaciones grandes y equipos distribuidos.


### 1.3. ¿Qué aportan los servicios web? - Reutilización

**Un backend, múltiples clientes**

- El mismo servicio para web, móvil, smartwatch
- Cada cliente implementa su propia interfaz
- Backend único y centralizado
- Lógica de negocio no duplicada

Note: Esta es una de las grandes ventajas: escribís vuestra lógica de negocio una vez en el backend, y luego podéis crear clientes para cualquier plataforma. La app web de Instagram, la app iOS y la app Android consumen todas la misma API. Cada una presenta los datos de forma diferente, pero la lógica está centralizada. Esto reduce bugs, facilita el mantenimiento y acelera el desarrollo.


### 1.3. ¿Qué aportan los servicios web? - Agnosticismo

**Backend independiente del cliente**

- El servidor no conoce al cliente
- Entrega datos que cada cliente representa a su manera
- No importa si es web, móvil o IoT
- Cada cliente evoluciona independientemente

Note: El backend se vuelve agnóstico: no le importa quién consume sus datos. Entrega JSON y cada cliente decide cómo mostrarlo. Esto permite que el equipo web trabaje independientemente del equipo móvil. Mañana podéis lanzar una app para smartwatch sin tocar el backend. El día que aparezca una nueva plataforma, simplemente creáis un nuevo cliente.

---

## 2. Diferencia entre servicio web y página web dinámica

Note: Es crucial entender esta diferencia. Ambos usan HTTP, ambos viven en servidores web, pero tienen propósitos completamente diferentes. Una confusión común es pensar que son lo mismo porque ambos responden a URLs.


### 2.1. Página web dinámica

**Contenido para humanos**

- Genera contenido HTML visualizable
- Proporciona interfaz gráfica
- Se visualiza directamente en navegador
- Incluye estilos (CSS) y comportamiento (JavaScript)

Note: Una página web dinámica está diseñada para que un humano la vea en su navegador. El servidor genera HTML completo con estilos CSS y JavaScript. Por ejemplo, cuando vais a Amazon.com, el servidor genera una página HTML hermosa con imágenes, botones y formularios listos para que interactuéis con el ratón y el teclado.


### 2.1. Ejemplo de respuesta página web

```http
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>Productos</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <h1>Productos disponibles</h1>
    <ul>
        <li>Laptop - 899€</li>
        <li>Ratón - 29€</li>
    </ul>
</body>
</html>
```

Note: Aquí veis una respuesta típica de una página web dinámica. El Content-Type es text/html. El cuerpo contiene HTML completo con estructura, referencias a CSS, y contenido formateado para visualización. Un navegador procesa esto y muestra una página bonita. Pero si una aplicación necesita estos datos, tiene que parsear HTML, que es complejo y frágil.


### 2.2. Servicio web (API)

**Datos para máquinas**

- Expone datos y funcionalidades
- Interfaz programática para código
- Devuelve datos estructurados (JSON, XML)
- Consumido por aplicaciones, no humanos

Note: Un servicio web, en cambio, está diseñado para ser consumido por código. No genera HTML bonito ni estilos. Simplemente entrega datos estructurados que otra aplicación puede procesar fácilmente. Es como la diferencia entre un informe en PDF (para humanos) y una hoja Excel (para procesar).


### 2.2. Ejemplo de respuesta servicio web

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "productos": [
        {
            "id": 1,
            "nombre": "Laptop",
            "precio": 899,
            "stock": 15
        },
        {
            "id": 2,
            "nombre": "Ratón",
            "precio": 29,
            "stock": 50
        }
    ]
}
```

Note: Aquí tenéis una respuesta típica de API. El Content-Type es application/json. Los datos están estructurados en formato JSON, fácil de parsear por cualquier lenguaje. Incluye campos adicionales como ID y stock que serían útiles para una aplicación pero no necesariamente visibles al usuario. Una app móvil puede tomar estos datos y mostrarlos como quiera en su interfaz.


### 2.3. Comparativa

| Aspecto       | Página Web         | API                  |
|---------------|--------------------|----------------------|
| Audiencia     | Humanos            | Máquinas             |
| Respuesta     | HTML+CSS+JS        | JSON/XML             |
| Visualización | En navegador       | Procesada por código |
| Propósito     | Interacción visual | Datos                |
<!-- .element.table: style="font-size:75%;" -->

Note: Esta tabla resume las diferencias clave. Las páginas web están optimizadas para experiencia de usuario visual. Las APIs están optimizadas para eficiencia de datos y facilidad de procesamiento. No hay una mejor que otra: son herramientas para trabajos diferentes. De hecho, las aplicaciones modernas usan ambas: el frontend consume APIs para obtener datos y los presenta bonito al usuario.


### 2.4. Arquitectura moderna

**Trabajando juntos**

- API proporciona los datos
- Aplicación web (SPA) consume y presenta
- Apps móviles consumen la misma API
- Otros servicios pueden integrarse

Note: En arquitecturas modernas, ambos conceptos trabajan en armonía. Tenéis un backend que expone APIs con los datos. Luego tenéis múltiples frontends: una Single Page Application web, una app iOS, una app Android, todos consumiendo la misma API. Cada cliente presenta los datos de forma óptima para su plataforma. Esta es la arquitectura de Netflix, Spotify, Twitter y básicamente cualquier aplicación moderna exitosa.

---

## 3. Protocolos de comunicación de API

Note: La elección del protocolo de comunicación es una decisión arquitectónica crítica. Afectará al rendimiento, la escalabilidad, la experiencia del usuario e incluso los costes de vuestro proyecto. No hay un protocolo "mejor": cada uno tiene sus casos de uso ideales.


### 3.1. REST - Introducción

**Representational State Transfer**

- Estilo arquitectónico, no protocolo
- El más popular y usado actualmente
- Basado en principios simples
- Usa HTTP de forma estándar

Note: REST es el protocolo más popular para APIs modernas. Fue definido por Roy Fielding en el año 2000 en su tesis doctoral. No es un protocolo formal como HTTP, sino un conjunto de principios arquitectónicos. Su popularidad viene de su simplicidad: si sabes HTTP, ya sabes gran parte de REST. Empresas como Twitter, GitHub, Stripe y miles más exponen APIs REST.


### 3.1. REST - Principios fundamentales I

**Bases de REST**

- Arquitectura cliente-servidor separada
- Sin estado (Stateless): cada petición es completa
- Cacheable: respuestas pueden ser cacheadas
- Interfaz uniforme: URLs y métodos estándar

Note: REST se basa en varios principios. Cliente y servidor están claramente separados. Stateless significa que cada petición contiene toda la información necesaria: el servidor no recuerda peticiones anteriores. Esto facilita escalar porque cualquier servidor puede atender cualquier petición. Las respuestas pueden marcarse como cacheables para mejorar rendimiento. Y usa una interfaz uniforme con métodos HTTP estándar.


### 3.1. REST - Principios fundamentales II

**Más características REST**

- Sistema en capas: permite intermediarios
- Recursos identificables: cada uno tiene URL única
- CRUD mapping: operaciones se mapean a HTTP
- Formato típico: JSON (aunque puede ser XML)

Note: REST permite sistemas en capas: entre cliente y servidor pueden haber proxies, balanceadores, cachés, sin que el cliente lo sepa. Cada recurso tiene una URL única: `/usuarios/123` identifica al usuario 123. Las operaciones CRUD (Create, Read, Update, Delete) se mapean naturalmente a métodos HTTP (POST, GET, PUT, DELETE). Y aunque REST no obliga a ningún formato, JSON es el estándar de facto.


### 3.1. REST - Ejemplo GET

```http
# Obtener todos los usuarios
GET /api/usuarios HTTP/1.1
Host: ejemplo.com
Accept: application/json

# Respuesta
HTTP/1.1 200 OK
Content-Type: application/json

[
    {"id": 1, "nombre": "Ana", "email": "ana@ejemplo.com"},
    {"id": 2, "nombre": "Luis", "email": "luis@ejemplo.com"}
]
```

Note: Este es un ejemplo clásico de REST. Usamos GET para obtener recursos. La URL `/usuarios` representa la colección de usuarios. El servidor responde con 200 OK y un array JSON con todos los usuarios. Es simple, predecible y fácil de entender. GET es idempotente: llamarlo múltiples veces produce el mismo resultado sin efectos secundarios.


### 3.1. REST - Ejemplo POST

```http
# Crear un nuevo usuario
POST /api/usuarios HTTP/1.1
Content-Type: application/json

{
    "nombre": "Carlos",
    "email": "carlos@ejemplo.com",
    "rol": "usuario"
}

# Respuesta
HTTP/1.1 201 Created
Location: /api/usuarios/3
Content-Type: application/json

{"id": 3, "nombre": "Carlos", "email": "carlos@ejemplo.com"}
```

Note: Para crear recursos usamos POST. Enviamos los datos del nuevo usuario en el body en formato JSON. El servidor responde con 201 Created, indicando que se creó exitosamente. Incluye un header Location con la URL del nuevo recurso y devuelve el objeto creado con su ID asignado. Esto sigue las mejores prácticas REST: POST para creación, 201 para éxito, Location para el recurso creado.


### 3.1. REST - Ventajas

**¿Por qué usar REST?**

✅ Simplicidad: fácil de entender y usar
✅ Compatibilidad universal: cualquier cliente HTTP
✅ Cacheable: aprovecha caché HTTP estándar
✅ Escalable: sin estado facilita escalabilidad
✅ Maduro: ampliamente documentado y con herramientas

Note: REST tiene ventajas importantes. Es simple de entender: si sabéis HTTP, entendéis REST. Cualquier lenguaje y plataforma tiene clientes HTTP, así que cualquiera puede consumir vuestra API. El caché HTTP estándar funciona perfectamente. Al ser stateless, es fácil escalar horizontalmente: añadir más servidores. Y hay toneladas de documentación, librerías y herramientas disponibles.


### 3.1. REST - Desventajas

**Limitaciones de REST**

❌ Sobre-fetching: devuelve más datos de los necesarios
❌ Under-fetching: requiere múltiples peticiones
❌ Sin esquema estricto: no hay validación de tipos
❌ Versionado: gestionar versiones puede ser complejo

Note: Pero REST no es perfecto. Sobre-fetching significa que a veces obtenéis datos que no necesitáis: pedís un usuario y os devuelve 20 campos cuando solo queríais el nombre. Under-fetching es lo contrario: necesitáis datos de varias entidades relacionadas y tenéis que hacer múltiples peticiones. No hay validación de tipos automática: toca validar manualmente. Y gestionar versiones de API puede volverse complejo con el tiempo.


### 3.2. GraphQL - Introducción

**El lenguaje de consulta flexible**

- Desarrollado por Facebook en 2012
- Lenguaje de consulta para APIs
- El cliente pide exactamente lo que necesita
- Tipado fuerte con esquema definido

Note: GraphQL es la alternativa moderna a REST, creada por Facebook para sus necesidades móviles. La idea central es simple pero poderosa: en lugar de que el servidor decida qué datos enviar, el cliente especifica exactamente qué quiere. Esto resuelve los problemas de sobre-fetching y under-fetching de REST. Tiene tipado fuerte: defines un esquema con tipos y el sistema valida automáticamente.


### 3.2. GraphQL - Características

**¿Qué hace especial a GraphQL?**

- Consultas precisas: solo datos necesarios
- Una sola petición para datos relacionados
- Introspección: la API se auto-documenta
- Evolución sin breaking changes

Note: GraphQL brilla por su precisión. El cliente pide exactamente los campos que necesita, ni más ni menos. Podéis obtener datos de múltiples recursos relacionados en una sola consulta: usuario, sus posts y sus comentarios, todo de una vez. La introspección permite que herramientas auto-generen documentación. Y podéis añadir campos nuevos sin romper clientes existentes: cada cliente pide solo lo que conoce.


### 3.2. GraphQL - Ejemplo consulta

```graphql
query {
  usuario(id: "1") {
    nombre
    email
    posts {
      titulo
      fecha
      comentarios {
        autor
        texto
      }
    }
  }
}
```

Note: Aquí veis una consulta GraphQL. Es declarativa: describís qué queréis. Pedimos un usuario con ID 1, pero solo queremos su nombre y email. También queremos sus posts, pero solo título y fecha. Y de cada post, queremos los comentarios con autor y texto. Todo esto en una sola petición. En REST, esto serían al menos 3 peticiones diferentes.


### 3.2. GraphQL - Ejemplo respuesta

```json
{
  "data": {
    "usuario": {
      "nombre": "Ana",
      "email": "ana@ejemplo.com",
      "posts": [{
        "titulo": "Mi primer post",
        "fecha": "2025-11-19",
        "comentarios": [{
          "autor": "Luis",
          "texto": "Gran post!"
        }]
      }]
    }
  }
}
```

Note: Y aquí está la respuesta. La estructura coincide exactamente con la consulta. Solo los campos pedidos están presentes. Los datos anidados están todos incluidos en una sola respuesta. Esto es especialmente valioso en móviles donde cada petición HTTP tiene latencia y consume batería. Una petición en lugar de tres hace la app más rápida y eficiente.


### 3.2. GraphQL - Ventajas

**Beneficios de GraphQL**

✅ Flexibilidad: el cliente pide lo que necesita
✅ Eficiencia: una petición para datos relacionados
✅ Tipado fuerte: validación automática
✅ Documentación automática: el esquema es la doc
✅ Sin versionado: evolución sin breaking changes

Note: Las ventajas de GraphQL son significativas. La flexibilidad permite a diferentes clientes pedir diferentes datos de la misma API: la web necesita más info, el móvil menos. Una sola petición reduce latencia dramáticamente. El tipado fuerte detecta errores en desarrollo, no en producción. El esquema sirve como documentación siempre actualizada. Y no necesitáis versionar la API: simplemente añadís campos nuevos y deprecáis los viejos gradualmente.


### 3.2. GraphQL - Desventajas

**Limitaciones de GraphQL**

❌ Complejidad: curva de aprendizaje pronunciada
❌ Caché: más difícil que REST
❌ Overhead: consultas complejas pueden ser costosas
❌ Seguridad: rate limiting más complejo

Note: Pero GraphQL no es perfecto. Es más complejo de aprender y de implementar que REST. El caché es más difícil porque no usas URLs simples: cada consulta puede ser diferente. Consultas muy complejas pueden sobrecargar el servidor si no implementáis límites. Y el rate limiting es más difícil: en REST limitáis por endpoint, en GraphQL todo va a un endpoint. Necesitáis analizar la complejidad de cada consulta.


### 3.3. WebSockets - Introducción

**Comunicación en tiempo real**

- Comunicación bidireccional full-duplex
- Conexión persistente sobre TCP
- Protocolo diferente a HTTP (aunque comienza con HTTP)
- Ideal para aplicaciones en tiempo real

Note: WebSockets es completamente diferente a REST y GraphQL. Mientras esos usan el modelo petición-respuesta de HTTP, WebSockets establece una conexión persistente bidireccional. Es como una llamada telefónica: una vez conectados, ambos lados pueden hablar cuando quieran. Esto es perfecto para chats, juegos, dashboards en vivo, cualquier cosa que necesite updates instantáneos.


### 3.3. WebSockets - Características

**¿Qué hace especial a WebSockets?**

- Conexión persistente: se mantiene abierta
- Bidireccional: cliente y servidor envían libremente
- Baja latencia: sin overhead de HTTP repetido
- Tiempo real: actualizaciones instantáneas

Note: La conexión WebSocket se establece una vez y se mantiene abierta. Tanto cliente como servidor pueden enviar mensajes en cualquier momento sin esperar a ser preguntados. No hay overhead de crear conexión HTTP repetidamente. Esto reduce la latencia a milisegundos. Es la tecnología detrás de WhatsApp Web, juegos online, herramientas colaborativas como Google Docs, y cualquier aplicación que necesite updates en tiempo real.


### 3.3. WebSockets - Casos de uso

**¿Cuándo usar WebSockets?**

- Chats en tiempo real
- Juegos multijugador online
- Notificaciones push
- Dashboards con datos en vivo
- Colaboración en tiempo real (Google Docs)

Note: WebSockets brilla en escenarios específicos. Los chats necesitan mensajes instantáneos bidireccionales. Los juegos online necesitan sincronizar posiciones de jugadores en tiempo real. Las notificaciones push requieren que el servidor inicie la comunicación. Los dashboards financieros o de monitorización necesitan updates constantes. Y las herramientas colaborativas necesitan sincronizar cambios entre usuarios instantáneamente.


### 3.3. WebSockets - Ejemplo código

```javascript
const socket = new WebSocket('wss://ejemplo.com/chat');

socket.onopen = function(event) {
    console.log('Conectado');
    socket.send('Hola servidor!');
};

socket.onmessage = function(event) {
    console.log('Mensaje:', event.data);
};

socket.onerror = function(error) {
    console.error('Error:', error);
};
```

Note: Aquí veis cómo usar WebSockets en JavaScript. Es simple: creáis un objeto WebSocket con la URL del servidor (wss es WebSocket seguro, como https). Cuando se abre la conexión, podéis enviar mensajes con send(). Cuando llegan mensajes del servidor, se dispara onmessage. Y podéis manejar errores con onerror. Es API simple pero poderosa. Y lo mejor: funciona en todos los navegadores modernos.


### 3.3. WebSockets - Ventajas

**Beneficios de WebSockets**

✅ Tiempo real: latencia mínima
✅ Bidireccional: comunicación en ambos sentidos
✅ Eficiente: sin overhead de HTTP repetido
✅ Escalable: para muchas conexiones simultáneas

Note: Las ventajas de WebSockets son claras para sus casos de uso. La latencia es mínima: milisegundos entre enviar y recibir. La comunicación bidireccional permite al servidor notificar al cliente sin polling. Es eficiente: una conexión en lugar de miles de peticiones HTTP. Y con la infraestructura correcta, escala a millones de conexiones simultáneas, como demuestra WhatsApp.


### 3.3. WebSockets - Desventajas

**Limitaciones de WebSockets**

❌ Complejidad: más difícil que REST
❌ Balanceo: requiere sticky sessions
❌ Firewall: algunos pueden bloquear
❌ Sin caché: no aprovecha caché HTTP

Note: Pero WebSockets tiene desventajas. Es más complejo de implementar y depurar que REST. El balanceo de carga es más difícil: necesitáis sticky sessions para que un cliente siempre vaya al mismo servidor. Algunos firewalls corporativos bloquean WebSockets. Y no se beneficia del caché HTTP: cada mensaje es único. Por eso WebSockets se usa específicamente para tiempo real, no como reemplazo general de REST.


### 3.4. Comparativa de protocolos

| Aspecto      | REST             | GraphQL          | WebSockets    |
|--------------|------------------|------------------|---------------|
| Comunicación | Request-Response | Request-Response | Bidireccional |
| Tiempo real  | No               | No               | Sí            |
| Complejidad  | Baja             | Media-Alta       | Alta          |
| Caché        | Excelente        | Limitado         | No aplica     |
<!-- .element.table: style="font-size:75%;" -->

Note: Esta tabla resume las diferencias clave. REST y GraphQL son petición-respuesta: el cliente pregunta, el servidor responde. WebSockets es bidireccional: ambos pueden iniciar comunicación. Solo WebSockets es realmente tiempo real. REST es el más simple, GraphQL medio, WebSockets el más complejo. REST tiene caché excelente, GraphQL limitado, WebSockets no aplica porque cada mensaje es único.


### 3.5. ¿Qué protocolo elegir?

**Recomendaciones**

- **REST**: API pública, CRUD simple, necesitas caché
- **GraphQL**: datos complejos, múltiples clientes
- **WebSockets**: tiempo real, chat, juegos, dashboards
- **gRPC**: microservicios internos alto rendimiento

Note: No hay un protocolo "mejor": depende del caso de uso. REST es perfecto para APIs públicas, operaciones CRUD estándar, cuando el caché es importante. GraphQL brilla cuando tenéis datos complejos relacionados y múltiples clientes con necesidades diferentes. WebSockets para cualquier cosa en tiempo real. Y gRPC, que no hemos cubierto en detalle, es excelente para comunicación entre microservicios internos donde rendimiento es crítico.

---

## 4. JWT: autenticación y autorización

Note: JSON Web Tokens es el estándar moderno para autenticación en APIs. Ha reemplazado en gran medida a las sesiones tradicionales. Entender JWT es esencial porque lo encontraréis en prácticamente cualquier API moderna: GitHub, Google, Amazon, todas usan JWT o algo similar.


### 4.1. ¿Qué es JWT?

**JSON Web Token**

- Estándar abierto (RFC 7519)
- Token de acceso para intercambio seguro
- Formato: `header.payload.signature`
- Permite autenticación sin estado

Note: JWT es un estándar abierto definido en el RFC 7519. Es básicamente un token que contiene información sobre un usuario y que está firmado digitalmente para garantizar que no ha sido modificado. El nombre describe su formato: es JSON, es Web (se usa en web), y es un Token (un credencial de acceso). Lo brillante es que permite autenticación stateless: el servidor no necesita recordar quién está conectado.


### 4.1. Estructura de JWT

**Tres partes separadas por puntos**

1. **Header**: tipo de token y algoritmo de firma
2. **Payload**: datos (claims) sobre el usuario
3. **Signature**: firma digital para verificar autenticidad

Note: JWT tiene tres partes claramente diferenciadas, separadas por puntos. El header especifica que es un JWT y qué algoritmo se usó para firmarlo, típicamente HS256 o RS256. El payload contiene los claims, que son afirmaciones sobre el usuario: su ID, email, rol, etc. Y la signature es la firma digital que garantiza que nadie ha modificado el header o payload. Las tres partes están codificadas en Base64.


### 4.1. JWT - Ejemplo Header

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

**Header codificado:**
`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9`

Note: El header es simple. Especifica el algoritmo de firma y el tipo de token. HS256 significa HMAC con SHA-256, un algoritmo simétrico: la misma clave se usa para firmar y verificar. RS256 sería RSA asimétrico: clave privada para firmar, pública para verificar. Este JSON se codifica en Base64URL y forma la primera parte del JWT.


### 4.1. JWT - Ejemplo Payload

```json
{
  "sub": "1234567890",
  "name": "Ana García",
  "email": "ana@ejemplo.com",
  "rol": "admin",
  "iat": 1700000000,
  "exp": 1700086400
}
```

Note: El payload contiene los claims sobre el usuario. Hay claims estándar como sub (subject, típicamente el ID de usuario), iat (issued at, cuando se emitió), y exp (expiration, cuando expira). Y podéis añadir claims custom como name, email, rol, etc. IMPORTANTE: este payload no está encriptado, solo codificado. Cualquiera puede decodificarlo y leer su contenido. Por eso NUNCA ponéis contraseñas o datos sensibles en un JWT.


### 4.1. JWT - Signature

**¿Cómo se crea la firma?**

```javascript
HMACSHA256(
  base64UrlEncode(header) + "." + 
  base64UrlEncode(payload),
  secret_key
)
```

Note: La signature se crea tomando el header codificado, un punto, el payload codificado, y firmando todo esto con una clave secreta usando el algoritmo especificado en el header. Esta firma garantiza dos cosas: que el token fue creado por alguien que conoce la clave secreta (autenticación), y que el contenido no ha sido modificado (integridad). Sin la clave secreta correcta, no se puede crear una firma válida.


### 4.2. Flujo de autenticación JWT I

**Pasos del proceso**

1. Usuario hace login con credenciales
2. Servidor verifica credenciales en BD
3. Servidor genera JWT con info del usuario
4. Servidor devuelve JWT al cliente

Note: El flujo de autenticación con JWT es simple. Primero, el usuario envía sus credenciales (email y password) al servidor. El servidor verifica estas credenciales contra la base de datos: comprueba que el usuario existe y que el hash de la contraseña coincide. Si todo está correcto, el servidor genera un JWT que contiene información sobre el usuario: su ID, email, rol, etc. Y devuelve este JWT al cliente.


### 4.2. Flujo de autenticación JWT II

**Uso del token**

5. Cliente almacena JWT (localStorage o cookie)
6. Peticiones incluyen: `Authorization: Bearer TOKEN`
7. Servidor verifica JWT en cada petición
8. Servidor extrae información del usuario

Note: El cliente almacena el JWT, típicamente en localStorage o en una cookie httpOnly. En cada petición posterior a recursos protegidos, el cliente incluye el JWT en el header Authorization con el formato "Bearer TOKEN". El servidor verifica la firma del JWT: si es válida, el token es legítimo. Extrae la información del usuario del payload y ya sabe quién está haciendo la petición. No necesita consultar la base de datos ni mantener sesiones en memoria.


### 4.2. JWT - Ejemplo implementación I

```javascript
// Generar JWT al hacer login
app.post('/api/login', async (req, res) => {
    const { email, password } = req.body;
    
    const usuario = await buscarUsuario(email);
    const valido = await verificarPassword(
        password, usuario.passwordHash
    );
    
    if (!valido) {
        return res.status(401).json({
            error: 'Credenciales inválidas'
        });
    }
    // ... continúa
});
```

Note: Aquí veis cómo implementar el login. Recibimos email y password del cliente. Buscamos el usuario en la base de datos por email. Verificamos que el password proporcionado coincide con el hash almacenado usando bcrypt o similar. Si las credenciales son inválidas, devolvemos 401 Unauthorized. Si son válidas, continuamos generando el JWT.


### 4.2. JWT - Ejemplo implementación II

```javascript
// Continuación del login
const token = jwt.sign(
    {
        sub: usuario.id,
        email: usuario.email,
        rol: usuario.rol
    },
    SECRET_KEY,
    { expiresIn: '24h' }
);

res.json({ token });
```

Note: Aquí generamos el JWT usando la librería jsonwebtoken. Incluimos en el payload el ID del usuario, su email y rol. Firmamos con nuestra clave secreta. Y especificamos que expira en 24 horas: después de ese tiempo, el token no será válido y el usuario tendrá que hacer login de nuevo. Finalmente devolvemos el token al cliente. El cliente lo guardará y lo usará en peticiones futuras.


### 4.2. JWT - Middleware verificación

```javascript
function verificarToken(req, res, next) {
    const header = req.headers['authorization'];
    if (!header) {
        return res.status(401).json({
            error: 'Token no proporcionado'
        });
    }
    
    const token = header.split(' ')[1]; // "Bearer TOKEN"
    
    try {
        const decoded = jwt.verify(token, SECRET_KEY);
        req.usuario = decoded;
        next();
    } catch (error) {
        return res.status(401).json({error: 'Token inválido'});
    }
}
```

Note: Este middleware verifica el JWT en cada petición a rutas protegidas. Primero comprueba que el header Authorization existe. Extrae el token quitando el prefijo "Bearer ". Verifica el token con jwt.verify: esto comprueba la firma y que no ha expirado. Si es válido, decodifica el payload y lo añade al objeto request para que las rutas siguientes puedan acceder a la info del usuario. Si algo falla, devuelve 401 Unauthorized.


### 4.3. JWT - Ventajas

**¿Por qué usar JWT?**

✅ Stateless: sin sesiones en servidor
✅ Escalable: facilita escalar horizontalmente
✅ Portable: funciona en cualquier plataforma
✅ Autocontenido: lleva toda la info necesaria
✅ Seguro: firmado digitalmente

Note: Las ventajas de JWT son significativas para APIs modernas. Stateless significa que el servidor no necesita almacenar sesiones: todo está en el token. Esto facilita enormemente escalar horizontalmente: cualquier servidor puede verificar cualquier token sin coordinación. Es portable: el mismo token funciona en web, móvil, IoT. Es autocontenido: no necesitáis consultar la BD en cada petición. Y es seguro cuando se implementa correctamente.


### 4.4. JWT - Buenas prácticas

**Seguridad con JWT**

✅ Usar HTTPS siempre
✅ Tiempo de expiración corto
✅ No almacenar info sensible en payload
✅ Usar algoritmos seguros (RS256 > HS256)
✅ Implementar refresh tokens
✅ Validar siempre la firma

Note: Para usar JWT de forma segura, seguid estas prácticas. HTTPS es obligatorio: sin él, el token puede ser interceptado. Usad expiración corta: 15 minutos para access tokens. No pongáis contraseñas o datos sensibles en el payload: es legible por cualquiera. RS256 es más seguro que HS256 para producción. Implementad refresh tokens para renovar access tokens sin re-login. Y siempre verificad la firma: nunca confiéis en un token sin verificar.


### 4.4. JWT - Qué NO hacer

**Errores comunes**

❌ Almacenar contraseñas en JWT
❌ Usar el mismo secret para todo
❌ Confiar en JWT sin verificar firma
❌ Almacenar en localStorage si hay riesgo XSS
❌ JWT sin expiración

Note: Y estos son errores que NUNCA debéis cometer. Nunca almacenéis contraseñas en JWT: el payload es visible. No uséis el mismo secret para desarrollo y producción. Siempre verificad la firma: el contenido del JWT es fácil de modificar, pero sin el secret no se puede crear una firma válida. Si vuestra app es vulnerable a XSS, mejor usad httpOnly cookies en lugar de localStorage. Y siempre poned expiración: tokens eternos son un riesgo de seguridad.


### 4.4. JWT - Advertencia importante

**JWT NO es encriptación**

> JWT está **codificado en Base64**, no encriptado.
> Cualquiera puede decodificar y leer el contenido.
> La firma garantiza **integridad**, no **confidencialidad**.

Note: Este es el malentendido más común sobre JWT. JWT NO encripta vuestros datos. El payload está simplemente codificado en Base64, que es reversible. Podéis ir a jwt.io ahora mismo y pegar cualquier JWT: veréis su contenido claramente. La firma solo garantiza que no ha sido modificado, no que sea secreto. Por eso es crítico no poner información sensible en JWT y siempre usar HTTPS.

---

## 5. Ejemplo: arquitectura de Netflix

Note: Netflix es un ejemplo paradigmático de arquitectura moderna a escala masiva. Sirven a más de 200 millones de suscriptores en todo el mundo, con miles de millones de horas de streaming al año. Su arquitectura es un caso de estudio de cómo construir sistemas escalables, resilientes y eficientes. Veamos cómo lo hacen.


### 5.1. Arquitectura de microservicios

**Cientos de servicios independientes**

- Cada función es un servicio separado
- Despliegues independientes sin downtime
- Equipos autónomos por servicio
- Tolerancia a fallos: uno cae, otros siguen

Note: Netflix usa arquitectura de microservicios a escala extrema: tienen cientos de servicios independientes. Autenticación es un servicio, recomendaciones otro, streaming otro, perfiles otro, búsqueda otro, etc. Cada equipo gestiona sus servicios completamente: desarrollan, despliegan, monitorean, todo. Pueden desplegar un servicio sin afectar otros. Y si un servicio falla, los demás siguen funcionando: esto es tolerancia a fallos por diseño.


### 5.1. Microservicios clave de Netflix

**Servicios principales**

- Autenticación: login, sesiones
- Perfiles: gestión de perfiles de usuario
- Recomendaciones: algoritmos de sugerencias
- Metadatos: información sobre contenido
- Streaming: entrega de vídeo
- Facturación: suscripciones y pagos

Note: Estos son algunos de los microservicios clave. El servicio de autenticación maneja login y sesiones. Perfiles gestiona los múltiples perfiles por cuenta. Recomendaciones ejecuta algoritmos de machine learning para sugerencias personalizadas. Metadatos mantiene toda la información sobre películas y series. Streaming maneja la entrega del vídeo adaptativo. Facturación gestiona suscripciones y pagos. Y hay cientos más: búsqueda, subtítulos, analytics, pruebas A/B, etc.


### 5.2. Infraestructura cloud AWS

**Todo en Amazon Web Services**

- Escalabilidad dinámica según demanda
- Alta disponibilidad en múltiples regiones
- Recuperación ante desastres automática
- Coste optimizado: pago por uso

Note: Netflix migró completamente a AWS, una decisión valiente en su momento. Esto les da escalabilidad dinámica: pueden añadir servidores en minutos cuando hay demanda, como el estreno de una serie popular. Tienen alta disponibilidad desplegando en múltiples regiones AWS: si una región falla, las otras continúan. Los backups y recuperación ante desastres son automáticos. Y solo pagan por lo que usan: no necesitan sobreprovisionar hardware.


### 5.2. Servicios AWS utilizados

**Componentes clave**

- EC2: máquinas virtuales para microservicios
- S3: almacenamiento de contenido
- DynamoDB: base de datos NoSQL
- CloudFront: CDN global
- ELB: balanceadores de carga

Note: Netflix usa intensivamente varios servicios AWS. EC2 proporciona las máquinas virtuales donde corren los microservicios. S3 almacena contenido y backups. DynamoDB, la base de datos NoSQL de AWS, almacena metadatos y preferencias de usuario. CloudFront es el CDN de AWS para distribución global. Y ELB son balanceadores de carga que distribuyen tráfico entre servidores. Esta infraestructura les permite operar globalmente sin gestionar hardware físico.


### 5.3. Open Connect: CDN propio

**Red de distribución de contenido**

- Servidores en ISPs locales
- Contenido cerca del usuario final
- Reduce latencia y mejora calidad
- Ahorra bandwidth de Internet

Note: Aunque Netflix usa AWS para la lógica de negocio, crearon su propia CDN llamada Open Connect para el streaming. Colocan servidores directamente en los ISPs de todo el mundo. Cuando queréis ver una película, Netflix os redirige al servidor más cercano, quizás uno dentro de vuestro propio proveedor de Internet. Esto reduce latencia, mejora calidad, y ahorra enormes cantidades de bandwidth de Internet. Es un sistema híbrido brillante.


### 5.3. Funcionamiento de Open Connect

**Flujo de streaming**

1. Contenido popular se replica en servidores locales
2. Usuario solicita una película
3. Netflix redirige al servidor más cercano
4. Streaming desde servidor local del ISP

Note: El flujo es inteligente. Netflix analiza qué contenido es popular en cada región y lo replica proactivamente en los servidores locales durante la noche cuando hay poca carga. Cuando solicitáis una película, el servicio de Netflix en AWS determina qué servidor de Open Connect está más cerca de vosotros. Os redirige a ese servidor. Y el streaming viene directamente del servidor local, que puede estar literalmente dentro del data center de vuestro ISP. Por eso Netflix funciona tan fluido.


### 5.4. Frontend: tecnologías client-side

**Aplicaciones para usuarios**

- **Web**: React, JavaScript, HTML5/CSS3
- **iOS**: Swift, Objective-C
- **Android**: Kotlin, Java
- **Smart TVs**: JavaScript, frameworks específicos

Note: Netflix tiene múltiples frontends para diferentes plataformas. La web usa React para la interfaz de usuario, con JavaScript moderno, HTML5 y CSS3. Las apps móviles usan tecnologías nativas: Swift y Objective-C para iOS, Kotlin y Java para Android. Para Smart TVs usan diferentes tecnologías según la plataforma. Todos estos clientes consumen las mismas APIs del backend. Es el ejemplo perfecto de un backend que sirve múltiples clientes.


### 5.5. Backend: tecnologías server-side I

**Lenguajes y frameworks**

- **Java**: lenguaje principal del backend
- **Spring Boot**: framework para microservicios
- **Node.js**: servicios en tiempo real
- **Python**: scripts, análisis, ML

Note: El backend de Netflix es principalmente Java con Spring Boot, que es el stack estándar para microservicios en la industria. Java ofrece rendimiento, robustez y un ecosistema maduro. Spring Boot facilita crear microservicios. También usan Node.js para algunos servicios que necesitan tiempo real. Y Python es usado extensivamente para scripts, análisis de datos, y machine learning. Es un stack diverso pero bien elegido para sus necesidades.


### 5.5. Backend: tecnologías server-side II

**Bases de datos**

- **Cassandra**: BD distribuida principal
- **MySQL**: algunos datos relacionales
- **EVCache**: sistema de caché distribuido

Note: Para bases de datos, Netflix usa principalmente Cassandra, una base de datos NoSQL distribuida diseñada para escalabilidad masiva sin punto único de fallo. Es perfecta para sus necesidades de alta disponibilidad. También usan MySQL para algunos datos que se benefician de relaciones. Y EVCache es su sistema de caché distribuido basado en Memcached, crucial para rendimiento: muchas peticiones se resuelven desde caché sin tocar la base de datos.


### 5.6. Chaos Engineering: Simian Army

**Probando la resiliencia**

- **Chaos Monkey**: apaga servidores aleatorios
- **Chaos Kong**: simula caída de región completa
- **Latency Monkey**: introduce latencia artificial
- **Objetivo**: asegurar que el sistema resiste fallos

Note: Netflix desarrolló una práctica llamada Chaos Engineering. La idea es simple pero radical: causar fallos en producción intencionalmente para asegurar que el sistema los puede manejar. Chaos Monkey apaga servidores aleatorios durante el día. Chaos Kong simula que una región entera de AWS cae. Latency Monkey introduce latencia artificial. Si el sistema sigue funcionando con estos fallos, tenéis confianza de que manejará fallos reales. Es contrainstintivo pero brillante.


### 5.6. Lecciones de Netflix

**Aprendizajes clave**

1. Microservicios permiten escala pero añaden complejidad
2. Cloud es fundamental para escalabilidad global
3. Automatización es clave para operar a escala
4. Diseñad asumiendo que las cosas fallarán
5. Monitorización extensiva es esencial

Note: Estas son las lecciones clave de Netflix. Los microservicios les permiten escalar y tener equipos autónomos, pero añaden complejidad operacional significativa. El cloud es esencial: no podrían operar globalmente con data centers propios. Todo debe ser automatizable: no podéis gestionar cientos de servicios manualmente. Diseñad asumiendo fallos: porque fallarán. Y necesitáis monitorización extensiva de todo: sin visibilidad no podéis operar sistemas distribuidos complejos.

---

## 6. Resumen y Conclusiones

Note: Hemos cubierto mucho terreno en esta unidad. Desde los conceptos básicos de APIs hasta arquitecturas complejas como Netflix. Vamos a consolidar los puntos clave.


### Puntos clave I

**Conceptos fundamentales**

- Servicios web permiten integración entre aplicaciones
- APIs proporcionan flexibilidad y reutilización
- Diferencia clave: páginas web para humanos, APIs para máquinas
- Backend agnóstico sirve múltiples clientes

Note: Los servicios web y APIs son el pegamento del ecosistema digital moderno. Permiten que aplicaciones se comuniquen, compartan funcionalidades y datos. La diferencia fundamental entre páginas web y APIs es su audiencia: unas sirven HTML para humanos, otras sirven datos para máquinas. Esta separación permite que un backend único sirva web, móvil, IoT, todos con interfaces optimizadas para cada plataforma.


### Puntos clave II

**Protocolos de comunicación**

- REST: el más popular, simple y escalable
- GraphQL: flexible, para datos complejos
- WebSockets: tiempo real bidireccional
- Elegir según caso de uso específico

Note: No hay un protocolo "mejor": hay que elegir según las necesidades. REST es perfecto para la mayoría de APIs públicas: simple, cacheable, bien entendido. GraphQL brilla cuando tenéis clientes con necesidades diversas y datos complejos relacionados. WebSockets para cualquier cosa que necesite updates en tiempo real. La clave es entender las fortalezas y debilidades de cada uno y elegir apropiadamente.


### Puntos clave III

**Autenticación moderna**

- JWT es el estándar para APIs stateless
- Permite escalabilidad sin sesiones
- Firmado digitalmente pero no encriptado
- Requiere buenas prácticas de seguridad

Note: JWT se ha convertido en el estándar para autenticación en APIs modernas. Su naturaleza stateless facilita enormemente la escalabilidad: no necesitáis coordinar sesiones entre servidores. Pero es crucial entender que JWT no encripta datos: está firmado pero el contenido es visible. Usadlo correctamente con HTTPS, tiempos de expiración cortos, y sin datos sensibles en el payload.


### Puntos clave IV

**Arquitecturas modernas**

- Netflix ejemplifica microservicios a escala
- Cloud computing es fundamental
- Tolerancia a fallos por diseño
- Automatización y monitorización esenciales

Note: Netflix nos enseña cómo construir sistemas a escala masiva. Los microservicios permiten equipos autónomos y despliegues independientes, pero añaden complejidad operacional. El cloud proporciona la infraestructura flexible necesaria. Hay que diseñar asumiendo que los componentes fallarán. Y necesitáis automatización extensiva y monitorización de todo para operar efectivamente. Estos principios aplican no solo a Netflix, sino a cualquier sistema distribuido moderno.


### Aplicación práctica

**Habilidades desarrolladas**

- Diseñar APIs RESTful efectivas
- Elegir protocolo apropiado según caso de uso
- Implementar autenticación con JWT
- Comprender arquitecturas de microservicios

Note: Con lo aprendido en esta unidad, podéis diseñar APIs RESTful siguiendo mejores prácticas. Sabéis cuándo usar REST, GraphQL o WebSockets. Podéis implementar autenticación segura con JWT. Y entendéis los principios detrás de arquitecturas de microservicios modernas. Estas son habilidades esenciales para cualquier desarrollador o ingeniero DevOps trabajando con sistemas distribuidos.


### Próximos pasos

**Continuando el aprendizaje**

- Practicar diseñando APIs propias
- Experimentar con diferentes protocolos
- Estudiar casos de estudio de empresas reales
- Implementar proyectos usando estas tecnologías

Note: La teoría es importante, pero la práctica es esencial. Os animo a diseñar vuestras propias APIs, experimentar con REST, GraphQL y WebSockets. Estudiad arquitecturas de empresas como Netflix, Spotify, Twitter. Implementad proyectos reales usando estas tecnologías. Solo construyendo sistemas distribuidos entenderéis realmente los desafíos y mejores prácticas. El conocimiento de APIs es fundamental para prácticamente cualquier carrera en desarrollo de software moderno.

---

## 7. Preguntas

**¿Dudas o consultas?**

Note: Este es el momento para preguntas. ¿Algo no ha quedado claro? ¿Queréis profundizar en algún tema? ¿Tenéis curiosidad sobre casos de uso específicos? Las APIs y servicios web son un tema amplio y fascinante. No dudéis en preguntar cualquier cosa sobre los conceptos, protocolos, JWT, o arquitecturas que hemos cubierto. También podemos discutir casos prácticos específicos que tengáis en mente.
