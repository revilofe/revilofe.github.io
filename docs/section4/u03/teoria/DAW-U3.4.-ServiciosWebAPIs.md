---
title: "UD 3 - 3.4 Servicios Web y Comunicación con APIs"
description: Servicios web, APIs REST, protocolos de comunicación, JWT y arquitecturas modernas
summary: Conceptos de servicios web y APIs, diferencias con páginas dinámicas, protocolos REST/GraphQL/WebSockets, autenticación JWT, ejemplo arquitectura Netflix
authors:
    - Eduardo Fdez
date: 2025-11-19
icon: "material/file-document-outline"
permalink: /daw/unidad3/3.4
categories:
    - DAW
tags:
    - APIs
    - REST
    - GraphQL
    - WebSockets
    - JWT
    - Microservicios
---

## 3.4. Servicios Web y Comunicación con APIs

En las unidades anteriores hemos visto cómo funciona HTTP, el protocolo base de la comunicación web. Ahora vamos a profundizar en cómo las aplicaciones modernas se comunican entre sí mediante **APIs** (Application Programming Interfaces) y **servicios web**.

Las APIs son el pegamento que une el ecosistema digital moderno. Cuando usáis una app móvil de banco, cuando compartís una foto en redes sociales, cuando pedís comida a domicilio, detrás de todo eso hay APIs trabajando. Entender cómo funcionan es fundamental para cualquier desarrollador o ingeniero DevOps.

<figure markdown="span">
  ![APIs portada](assets/api_portada.jpg){ width="700" }
  <figcaption>Representación visual de APIs conectando diferentes aplicaciones y servicios, mostrando cómo actúan como puentes de comunicación entre sistemas diversos</figcaption>
</figure>

### 1. ¿Qué es un servicio web y qué aporta?

Un **servicio web** (o Web Service) es una **API** que permite a otra aplicación comunicarse remotamente para acceder a un servicio. Son conjuntos de reglas y protocolos que permiten a diferentes aplicaciones o sistemas comunicarse y compartir datos a través de la web.

#### 1.1. Definición y conceptos fundamentales

**Servicio web**: Sistema software diseñado para soportar la interacción máquina-a-máquina a través de una red.

**API (Application Programming Interface)**: Conjunto de definiciones y protocolos que especifica cómo los componentes de software deben interactuar.

**Endpoint**: URL específica donde un servicio web está disponible. Cada funcionalidad o servicio expuesto por una API se identifica mediante un endpoint.

**Ejemplos de endpoints:**
```
https://api.ejemplo.com/usuarios
https://api.ejemplo.com/productos
https://api.ejemplo.com/pedidos/123
```

#### 1.2. Características de los servicios web

Los servicios web se basan en:

- **Protocolos web estándar**: Principalmente HTTP/HTTPS
- **Formatos de intercambio de datos**: JSON, XML, o incluso texto plano
- **Acceso a través de URLs**: Cada recurso tiene su propia dirección
- **Independencia de plataforma**: No importa el lenguaje o sistema operativo
- **Comunicación mediante mensajes**: Petición-respuesta

#### 1.3. ¿Qué aportan los servicios web?

Los servicios web son **fundamentales en el desarrollo de aplicaciones modernas**. Aportan:

**Integración**

- Permiten que diferentes sistemas se conecten y compartan funcionalidades
- Una aplicación de escritorio puede publicar en Twitter vía su API
- Un e-commerce puede integrarse con pasarelas de pago
- Sistemas empresariales pueden comunicarse entre departamentos

**Ejemplo práctico:**
Una tienda online puede integrar:
- API de PayPal para pagos
- API de Google Maps para direcciones
- API de SendGrid para emails
- API de un sistema de inventario propio

**Flexibilidad y escalabilidad**

- Facilitan la creación de aplicaciones más robustas
- Permiten escalar componentes de forma independiente
- Se puede actualizar un servicio sin afectar a otros
- Soportan múltiples clientes simultáneamente

**Reutilización**

- Un mismo servicio puede ser consumido por múltiples clientes
- Aplicación web, móvil iOS, móvil Android, smartwatch
- Cada cliente implementa su propia interfaz
- El backend permanece único y centralizado

**Agnosticismo del cliente**

- El backend se vuelve agnóstico al cliente
- Entrega datos que cada cliente representa a su manera
- No necesita saber si el cliente es web, móvil o IoT
- Cada cliente puede evolucionar independientemente

<figure markdown="span">
  ![APIs conectando sistemas](assets/apis.gif){ width="600" }
  <figcaption>Visualización animada de cómo las APIs actúan como interfaces que conectan diferentes aplicaciones, servicios y sistemas, permitiendo el flujo de datos entre ellos de forma estandarizada y segura</figcaption>
</figure>

!!! tip "El poder de las APIs"
    Las empresas tecnológicas más exitosas del mundo (Google, Amazon, Facebook, Netflix) basan gran parte de su negocio en APIs. Algunas incluso monetizan sus APIs directamente.

### 2. Diferencia entre servicio web y página web dinámica

Es crucial entender la diferencia entre estos dos conceptos, ya que aunque ambos usan HTTP, tienen propósitos completamente diferentes.

#### 2.1. Página web dinámica

Una **página web dinámica** está diseñada para:

- **Generar contenido HTML** (u otros formatos interpretables por un navegador)
- Proporcionar una **interfaz gráfica** para usuarios humanos
- Ser visualizada directamente en un navegador
- Incluir estilos (CSS) y comportamiento (JavaScript)

**Ejemplo de respuesta:**
```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

<!DOCTYPE html>
<html>
<head>
    <title>Lista de Productos</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <h1>Productos disponibles</h1>
    <ul>
        <li>Laptop - 899€</li>
        <li>Ratón - 29€</li>
        <li>Teclado - 79€</li>
    </ul>
</body>
</html>
```

#### 2.2. Servicio web (API)

Un **servicio web** está diseñado para:

- **Exponer datos y funcionalidades** a otras aplicaciones
- Proporcionar una **interfaz programática** para máquinas
- Devolver **datos estructurados** (JSON, XML)
- Ser consumido por código, no por humanos directamente

**Ejemplo de respuesta:**
```http
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
        },
        {
            "id": 3,
            "nombre": "Teclado",
            "precio": 79,
            "stock": 32
        }
    ]
}
```

#### 2.3. Comparativa

| Aspecto           | Página Web Dinámica  | Servicio Web (API)       |
|:------------------|:---------------------|:-------------------------|
| **Audiencia**     | Usuarios humanos     | Otras aplicaciones       |
| **Respuesta**     | HTML + CSS + JS      | JSON, XML (datos)        |
| **Visualización** | Directa en navegador | Procesada por código     |
| **Propósito**     | Interacción visual   | Intercambio de datos     |
| **Presentación**  | Incluida (estilos)   | Solo datos (sin estilos) |
| **Consumo**       | Navegador web        | Cualquier cliente HTTP   |

#### 2.4. Arquitectura moderna: trabajando juntos

En una arquitectura moderna, ambos conceptos trabajan juntos:

1. **El servicio web (API)** proporciona los datos
2. **La aplicación web (SPA)** consume la API y presenta los datos
3. **Aplicaciones móviles** también consumen la misma API
4. **Otros servicios** pueden integrar esta API

**Flujo típico:**
```
Usuario → Navegador (SPA) → API (Servicio Web) → Base de Datos
                  ↓
          App Móvil → API (Servicio Web) → Base de Datos
```

!!! note "Separación de responsabilidades"
    Esta separación entre datos (API) y presentación (cliente) es la base de las arquitecturas modernas. Permite flexibilidad, escalabilidad y múltiples interfaces para los mismos datos.

### 3. Protocolos de comunicación de API

La elección del protocolo de comunicación de API es una decisión arquitectónica crítica que impactará el rendimiento, la escalabilidad, la experiencia del usuario e incluso los costes del proyecto.

#### 3.1. REST (Representational State Transfer)

**REST** es un estilo arquitectónico (no un protocolo) para diseñar APIs basadas en HTTP. Es el más popular y ampliamente usado.

**Principios fundamentales de REST:**

1. **Arquitectura cliente-servidor**: Separación clara de responsabilidades
2. **Sin estado (Stateless)**: Cada petición contiene toda la información necesaria
3. **Cacheable**: Las respuestas pueden marcarse como cacheables
4. **Interfaz uniforme**: URLs y métodos HTTP estándar
5. **Sistema en capas**: Permite intermediarios (proxies, balanceadores)
6. **Recursos identificables**: Cada recurso tiene una URL única

**Características de REST:**

- **Usa métodos HTTP estándar**: GET, POST, PUT, DELETE, PATCH
- **URLs representan recursos**: `/usuarios`, `/productos/123`
- **Formato típico**: JSON (aunque puede ser XML)
- **Sin estado**: No mantiene sesión en el servidor entre peticiones
- **CRUD mapping**: Operaciones se mapean a métodos HTTP

**Ejemplo de API REST:**

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

```http
# Obtener un usuario específico
GET /api/usuarios/1 HTTP/1.1

# Respuesta
HTTP/1.1 200 OK
Content-Type: application/json

{"id": 1, "nombre": "Ana", "email": "ana@ejemplo.com", "rol": "admin"}
```

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

{"id": 3, "nombre": "Carlos", "email": "carlos@ejemplo.com", "rol": "usuario"}
```

**Ventajas de REST:**

- **Simplicidad**: Fácil de entender y usar
- **Compatibilidad universal**: Funciona con cualquier cliente HTTP
- **Cacheable**: Aprovecha el caché HTTP estándar
- **Escalable**: Sin estado facilita la escalabilidad
- **Maduro**: Ampliamente documentado y con muchas herramientas

**Desventajas de REST:**

- **Sobre-fetching**: Puede devolver más datos de los necesarios
- **Under-fetching**: Puede requerir múltiples peticiones para datos relacionados
- **Falta de esquema estricto**: No hay validación de tipos por defecto
- **Versionado**: Gestionar versiones de API puede ser complejo

#### 3.2. GraphQL

**GraphQL** es un lenguaje de consulta para APIs y un runtime para ejecutar esas consultas, desarrollado por Facebook.

**Características principales:**

- **Consultas precisas**: El cliente pide exactamente los datos que necesita
- **Una sola petición**: Puede obtener datos relacionados en una consulta
- **Tipado fuerte**: Esquema definido con tipos
- **Introspección**: La API describe sus propias capacidades

**Ejemplo de consulta GraphQL:**

```graphql
# Consulta
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

```json
// Respuesta
{
  "data": {
    "usuario": {
      "nombre": "Ana",
      "email": "ana@ejemplo.com",
      "posts": [
        {
          "titulo": "Mi primer post",
          "fecha": "2025-11-19",
          "comentarios": [
            {
              "autor": "Luis",
              "texto": "Gran post!"
            }
          ]
        }
      ]
    }
  }
}
```

**Ventajas de GraphQL:**

- **Flexibilidad**: El cliente pide exactamente lo que necesita
- **Eficiencia**: Una sola petición para datos relacionados
- **Tipado fuerte**: Validación automática
- **Documentación automática**: El esquema es la documentación
- **Versionado innecesario**: Evolución sin breaking changes

**Desventajas de GraphQL:**

- **Complejidad**: Curva de aprendizaje más pronunciada
- **Caché**: Más difícil de cachear que REST
- **Overhead**: Consultas complejas pueden ser costosas
- **Seguridad**: Rate limiting más complejo

#### 3.3. WebSockets

**WebSockets** proporciona comunicación bidireccional full-duplex sobre una única conexión TCP.

**Características:**

- **Conexión persistente**: Se mantiene abierta
- **Bidireccional**: Cliente y servidor pueden enviar mensajes en cualquier momento
- **Baja latencia**: Sin overhead de HTTP repetido
- **Tiempo real**: Ideal para actualizaciones instantáneas

**Casos de uso:**

- Chats en tiempo real
- Juegos multijugador online
- Notificaciones push
- Dashboards con datos en vivo
- Colaboración en tiempo real (Google Docs)

**Ejemplo de implementación:**

```javascript
// Cliente
const socket = new WebSocket('wss://ejemplo.com/chat');

// Evento: conexión establecida
socket.onopen = function(event) {
    console.log('Conectado al servidor');
    socket.send('Hola servidor!');
};

// Evento: mensaje recibido
socket.onmessage = function(event) {
    console.log('Mensaje del servidor:', event.data);
};

// Evento: error
socket.onerror = function(error) {
    console.error('Error WebSocket:', error);
};

// Evento: conexión cerrada
socket.onclose = function(event) {
    console.log('Conexión cerrada');
};
```

**Ventajas de WebSockets:**

- **Tiempo real**: Latencia mínima
- **Bidireccional**: Comunicación en ambos sentidos
- **Eficiente**: Sin overhead de HTTP repetido
- **Escalable**: Para muchas conexiones simultáneas

**Desventajas:**

- **Complejidad**: Más difícil de implementar que REST
- **Balanceo**: Requiere sticky sessions o soluciones especiales
- **Firewall**: Algunos firewalls pueden bloquear
- **Sin caché**: No aprovecha caché HTTP

#### 3.4. Tabla comparativa de protocolos

| Aspecto            | REST             | GraphQL             | WebSockets          |
|:-------------------|:-----------------|:--------------------|:--------------------|
| **Comunicación**   | Request-Response | Request-Response    | Bidireccional       |
| **Formato datos**  | JSON, XML        | JSON                | Cualquiera          |
| **Tiempo real**    | No (polling)     | No                  | Sí                  |
| **Complejidad**    | Baja             | Media-Alta          | Alta                |
| **Caché**          | Excelente        | Limitado            | No aplica           |
| **Sobre-fetching** | Común            | No                  | No aplica           |
| **Uso típico**     | APIs CRUD        | Consultas complejas | Chat, gaming        |
| **Madurez**        | Muy maduro       | Maduro              | Maduro              |
| **Escalabilidad**  | Excelente        | Buena               | Buena (con cuidado) |

#### 3.5. Otros protocolos importantes

**gRPC (Google Remote Procedure Call)**

- Basado en HTTP/2
- Usa Protocol Buffers (binario, muy eficiente)
- Ideal para microservicios
- Soporta streaming bidireccional

**SOAP (Simple Object Access Protocol)**

- Protocolo XML estricto
- Estándares WS-* para seguridad
- Usado en sistemas empresariales legacy
- Más verboso y complejo que REST

**MQTT (Message Queuing Telemetry Transport)**

- Protocolo ligero publish-subscribe
- Diseñado para dispositivos con recursos limitados
- Estándar para IoT
- Ideal para redes de bajo ancho de banda

**Server-Sent Events (SSE)**

- Actualizaciones unidireccionales del servidor al cliente
- Más simple que WebSockets para flujos unidireccionales
- Usa HTTP estándar
- Ideal para notificaciones

!!! tip "Elegir el protocolo adecuado"
    - **REST**: API pública, operaciones CRUD simples, necesitas caché
    - **GraphQL**: Datos relacionados complejos, múltiples clientes con necesidades distintas
    - **WebSockets**: Tiempo real, chat, juegos, dashboards en vivo
    - **gRPC**: Microservicios internos de alto rendimiento

### 4. JWT: autenticación y autorización

Un **JSON Web Token (JWT)** es un estándar abierto (RFC 7519) para crear tokens de acceso que permiten intercambiar información de forma segura entre dos partes.

#### 4.1. Estructura de un JWT

Un JWT consta de **tres partes** separadas por puntos:

```
header.payload.signature
```

<figure markdown="span">
  ![Estructura JWT](assets/jwt-structure.png){ width="700" }
  <figcaption>Estructura de un JSON Web Token mostrando sus tres componentes: Header (encabezado con tipo y algoritmo), Payload (datos y claims), y Signature (firma digital para verificar autenticidad). Cada parte está codificada en Base64URL</figcaption>
</figure>

**1. Header (Encabezado)**

Contiene el tipo de token y el algoritmo de firma:

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

**2. Payload (Carga útil)**

Contiene las "claims" (declaraciones) sobre una entidad:

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

**Claims estándar:**
- `iss` (issuer): Emisor del token
- `sub` (subject): Sujeto (típicamente ID de usuario)
- `aud` (audience): Audiencia
- `exp` (expiration): Fecha de expiración
- `iat` (issued at): Fecha de emisión
- `nbf` (not before): No válido antes de

**3. Signature (Firma)**

Se crea tomando el header y payload codificados, y firmándolos con una clave secreta:

```javascript
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  secret
)
```

**JWT completo:**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFuYSBHYXJjw61hIiwiZW1haWwiOiJhbmFAZWplbXBsby5jb20iLCJyb2wiOiJhZG1pbiIsImlhdCI6MTcwMDAwMDAwMCwiZXhwIjoxNzAwMDg2NDAwfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

#### 4.2. Flujo de autenticación con JWT

1. **Usuario hace login** con credenciales

2. **Servidor verifica** credenciales en la base de datos

3. **Servidor genera JWT** con información del usuario

4. **Servidor devuelve JWT** al cliente

5. **Cliente almacena JWT** (normalmente en localStorage o cookie)

6. **Peticiones posteriores** incluyen el JWT en el header:
   ```
   Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   ```

7. **Servidor verifica JWT** en cada petición:

   - Verifica la firma
   - Comprueba que no ha expirado
   - Extrae información del usuario

**Ejemplo de implementación:**

```javascript
// Servidor - Generar JWT al hacer login
app.post('/api/login', async (req, res) => {
    const { email, password } = req.body;
    
    // Verificar credenciales
    const usuario = await buscarUsuario(email);
    const passwordValido = await verificarPassword(password, usuario.passwordHash);
    
    if (!passwordValido) {
        return res.status(401).json({ error: 'Credenciales inválidas' });
    }
    
    // Crear JWT
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
});

// Middleware para verificar JWT
function verificarToken(req, res, next) {
    const header = req.headers['authorization'];
    
    if (!header) {
        return res.status(401).json({ error: 'Token no proporcionado' });
    }
    
    const token = header.split(' ')[1]; // "Bearer TOKEN"
    
    try {
        const decoded = jwt.verify(token, SECRET_KEY);
        req.usuario = decoded; // Añadir info de usuario a la petición
        next();
    } catch (error) {
        return res.status(401).json({ error: 'Token inválido' });
    }
}

// Ruta protegida
app.get('/api/perfil', verificarToken, (req, res) => {
    // req.usuario contiene la info del JWT
    res.json({
        usuario: req.usuario.email,
        rol: req.usuario.rol
    });
});
```

#### 4.3. Ventajas de JWT

- **Stateless**: No requiere almacenar sesiones en el servidor
- **Escalable**: Facilita la escalabilidad horizontal
- **Portable**: Funciona en cualquier plataforma
- **Autocontenido**: Lleva toda la información necesaria
- **Seguro**: Firmado digitalmente

#### 4.4. Consideraciones de seguridad

**Buenas prácticas:**

- Usar HTTPS siempre
- Establecer tiempo de expiración corto
- No almacenar información sensible en el payload
- Usar algoritmos seguros (RS256 mejor que HS256 para producción)
- Implementar refresh tokens para renovar
- Validar siempre la firma

**Nunca hacer:**

- Almacenar contraseñas en el JWT
- Usar el mismo secret para todo
- Confiar en JWT sin verificar la firma
- Almacenar JWT en localStorage si hay riesgo XSS (mejor httpOnly cookies)

!!! warning "JWT no es encriptación"
    JWT está **codificado en Base64**, no encriptado. Cualquiera puede decodificar y leer el contenido. La firma solo garantiza que no ha sido modificado, no que sea secreto.

### 5. Ejemplo: arquitectura de Netflix

Netflix es un ejemplo paradigmático de arquitectura de microservicios a escala masiva. Estudiemos cómo han estructurado su sistema.

<figure markdown="span">
  ![Arquitectura Netflix](assets/netflix-2.gif){ width="700" }
  <figcaption>Diagrama simplificado de la arquitectura de microservicios de Netflix mostrando cómo diferentes servicios (autenticación, recomendaciones, streaming, perfiles) trabajan de forma independiente pero coordinada, utilizando APIs para comunicarse entre sí y con los clientes</figcaption>
</figure>

#### 5.1. Arquitectura de microservicios

Netflix utiliza una arquitectura orientada a **microservicios** que les permite operar a escala global.

**Características principales:**

- **Cientos de microservicios**: Cada función es un servicio independiente
- **Despliegues independientes**: Actualizar sin afectar al resto
- **Equipos autónomos**: Cada equipo gestiona sus servicios
- **Tolerancia a fallos**: Un servicio caído no tumba todo

**Microservicios clave:**

1. **Servicio de autenticación**: Login, gestión de sesiones
2. **Servicio de perfiles**: Gestión de perfiles de usuario
3. **Servicio de recomendaciones**: Algoritmos de sugerencias personalizadas
4. **Servicio de metadatos**: Información sobre contenido
5. **Servicio de streaming**: Entrega de vídeo
6. **Servicio de facturación**: Gestión de suscripciones
7. **Servicio de búsqueda**: Motor de búsqueda interno

#### 5.2. Infraestructura cloud (AWS)

Netflix migró completamente a **Amazon Web Services (AWS)**:

- **Escalabilidad dinámica**: Recursos según demanda
- **Alta disponibilidad**: Múltiples zonas geográficas
- **Recuperación ante desastres**: Backups automáticos
- **Coste optimizado**: Pago por uso

**Servicios AWS utilizados:**

- **EC2**: Máquinas virtuales para microservicios
- **S3**: Almacenamiento de contenido
- **DynamoDB**: Base de datos NoSQL
- **CloudFront**: CDN global
- **ELB**: Balanceadores de carga

#### 5.3. Open Connect: CDN propio

**Open Connect** es la red de distribución de contenido (CDN) propia de Netflix:

- **Servidores en ISPs**: Contenido cerca del usuario
- **Reduce latencia**: Streaming más rápido
- **Ahorra bandwidth**: Menos tráfico por Internet
- **Mejora calidad**: Streaming sin interrupciones

**Funcionamiento:**

1. Contenido popular se replica en servidores locales
2. Usuario solicita una película
3. Netflix redirige al servidor más cercano
4. Streaming desde servidor local del ISP

#### 5.4. Frontend: tecnologías client-side

**Aplicación web:**

- **React**: Biblioteca principal para UI
- **JavaScript**: Lenguaje de programación
- **HTML5/CSS3**: Estructura y estilos
- **Responsive design**: Adaptación a dispositivos

**Aplicaciones móviles:**

- **iOS**: Swift, Objective-C
- **Android**: Kotlin, Java
- **Smart TVs**: JavaScript, frameworks específicos

#### 5.5. Backend: tecnologías server-side

**Lenguajes y frameworks:**

- **Java**: Lenguaje principal del backend
- **Spring Boot**: Framework para microservicios
- **Node.js**: Para algunos servicios en tiempo real
- **Python**: Scripts, análisis de datos, ML

**Bases de datos:**

- **Cassandra**: Base de datos distribuida principal
- **MySQL**: Para algunos datos relacionales
- **EVCache**: Sistema de caché distribuido

#### 5.6. Chaos Engineering: Simian Army

Netflix desarrolló **Chaos Engineering** para probar la resiliencia:

**Chaos Monkey**: Apaga servidores aleatorios en producción

**Chaos Kong**: Simula caída de una región completa de AWS

**Latency Monkey**: Introduce latencia artificial

**Objetivo**: Asegurar que el sistema resiste fallos inesperados

!!! tip "Lecciones de Netflix"
    1. **Microservicios permiten escala**: Pero añaden complejidad
    2. **Cloud es fundamental**: Para escalabilidad global
    3. **Automatización es clave**: Todo debe ser automatizable
    4. **Resiliencia por diseño**: Asumir que las cosas fallarán
    5. **Monitorización extensiva**: Observabilidad en todo

## Resumen de la unidad

En esta unidad hemos aprendido:

1. **Los servicios web** permiten que aplicaciones se comuniquen entre sí mediante APIs, proporcionando integración, flexibilidad y reutilización.

2. **Diferencia clave**: Páginas web dinámicas sirven HTML para humanos; servicios web sirven datos (JSON/XML) para máquinas.

3. **REST** es el estilo arquitectónico más popular, simple y escalable para APIs basadas en HTTP.

4. **GraphQL** permite consultas flexibles y precisas, ideal para datos complejos y relacionados.

5. **WebSockets** proporciona comunicación bidireccional en tiempo real, esencial para chats y aplicaciones colaborativas.

6. **JWT** es el estándar para autenticación stateless en APIs modernas, permitiendo escalabilidad.

7. **Netflix** ejemplifica una arquitectura de microservicios a escala global, con cientos de servicios independientes coordinados.

El conocimiento de APIs y servicios web es fundamental para cualquier desarrollador moderno, ya que son la base de la comunicación entre aplicaciones en el ecosistema digital actual.

## Referencias y bibliografía

- [Jose Luis González](https://github.com/joseluisgs). *Despliegue de aplicaciones Web - 2025 2026*. [https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026](https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026)
- Fielding, R. T. (2000). *REST: Architectural Styles and the Design of Network-based Software Architectures*
- Facebook. (2024). *GraphQL Specification*. [https://spec.graphql.org/](https://spec.graphql.org/)
- IETF. (2015). *RFC 7519: JSON Web Token (JWT)*
- Cockcroft, A. (2016). *Microservices at Netflix*. Netflix Tech Blog

## Recursos adicionales

- [REST API Tutorial](https://restfulapi.net/) - Guía completa sobre REST
- [GraphQL.org](https://graphql.org/) - Documentación oficial de GraphQL
- [JWT.io](https://jwt.io/) - Decodificador y documentación de JWT
- [Netflix Tech Blog](https://netflixtechblog.com/) - Blog técnico de Netflix
- [Postman](https://www.postman.com/) - Herramienta para probar APIs
