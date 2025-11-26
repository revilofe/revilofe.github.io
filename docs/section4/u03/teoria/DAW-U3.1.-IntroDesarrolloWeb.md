---
title: "UD 3 - 3.1 Introducción al Desarrollo Web en Entorno Servidor"
description: Introducción al desarrollo web moderno, componentes de una aplicación web y diferencias entre frontend y backend
summary: Desarrollo web actual, modelos de ejecución cliente-servidor, componentes frontend y backend, diferencias entre páginas y aplicaciones web
authors:
    - Eduardo Fdez
date: 2025-11-19
icon: "material/file-document-outline"
permalink: /daw/unidad3/3.1
categories:
    - DAW
tags:
    - Desarrollo Web
    - Frontend
    - Backend
    - Cliente-Servidor
    - Aplicaciones Web
---

## 3.1. Introducción al Desarrollo Web en Entorno Servidor

¿Alguna vez habéis pensado lo que pasa una vez que dais al botón de "Enviar" en un formulario web? ¿O cómo es posible que podáis ver vuestro perfil en una red social, comprar en una tienda online o ver una película en streaming desde cualquier dispositivo? ¿O qué pasa cuando ponéis una URL en el navegador? 

Detrás de estas acciones aparentemente simples, hay un complejo ecosistema de tecnologías y procesos que hacen posible la experiencia web moderna. En esta unidad vamos a descubrir cómo funcionan realmente las aplicaciones web y cuál es el papel fundamental que juega el servidor en todo este proceso.

<figure markdown="span">
  ![Portada servicios web](assets/servicios.png){ width="600" }
  <figcaption>Representación visual de los diferentes servicios y componentes que interactúan en el desarrollo web moderno</figcaption>
</figure>

### 1. El desarrollo web actual

El desarrollo web moderno es un campo en constante evolución que abarca la creación y mantenimiento de sitios web y aplicaciones que operan a través de Internet. En la actualidad, el desarrollo no solo se enfoca en la funcionalidad, sino también en cómo estas aplicaciones se pondrán a disposición de los usuarios, un proceso crucial conocido como **despliegue**.

Este proceso es fundamental para la viabilidad de cualquier proyecto web, ya que permite que la aplicación pase del entorno de desarrollo a un entorno de producción, donde será accesible para los usuarios finales.

#### 1.1. Objetivos del despliegue de aplicaciones web

Los principales objetivos del despliegue son:

- **Accesibilidad**: Garantizar que la aplicación esté disponible para los usuarios en todo momento y desde cualquier lugar.
    
    - Los usuarios deben poder acceder a la aplicación 24/7
    - Debe funcionar desde diferentes dispositivos y ubicaciones geográficas
    - Los tiempos de carga deben ser óptimos
    
- **Estabilidad**: Asegurar que la aplicación funcione de manera consistente y sin errores.
    
    - Minimizar los tiempos de inactividad
    - Garantizar que las actualizaciones no rompan funcionalidades existentes
    - Implementar sistemas de monitorización y alertas
    
- **Escalabilidad**: Permitir que la aplicación pueda crecer y adaptarse a un mayor número de usuarios o carga de trabajo.
    
    - Capacidad de soportar picos de tráfico
    - Posibilidad de añadir recursos según demanda
    - Arquitectura que permita crecimiento horizontal o vertical
    
- **Seguridad**: Proteger la aplicación y los datos de los usuarios frente a amenazas y vulnerabilidades.
    
    - Cifrado de comunicaciones (HTTPS)
    - Autenticación y autorización robustas
    - Protección contra ataques comunes (SQL injection, XSS, CSRF)
    - Copias de seguridad y planes de recuperación

#### 1.2. Ventajas de un despliegue eficiente

Un despliegue eficiente aporta múltiples beneficios tanto a los desarrolladores como a las organizaciones:

- **Rapidez en el Time-to-Market**: Permite a las empresas lanzar productos más rápidamente al mercado.
    
    - Reducción del tiempo desde el desarrollo hasta la producción
    - Capacidad de responder rápidamente a las necesidades del mercado
    - Ventaja competitiva al ser los primeros en ofrecer nuevas funcionalidades
    
- **Iteración rápida**: Facilita la entrega continua de nuevas funcionalidades y mejoras.
    
    - Despliegues frecuentes con cambios pequeños
    - Feedback rápido de los usuarios
    - Corrección ágil de errores
    
- **Automatización**: Reduce los errores humanos y aumenta la eficiencia.
    
    - Scripts y pipelines automatizados
    - Pruebas automáticas antes del despliegue
    - Rollback automático en caso de fallos
    
- **Competitividad**: Mejora la posición de la empresa al proporcionar un servicio fiable y de alta calidad.
    
    - Mejor experiencia de usuario
    - Mayor confianza del cliente
    - Reducción de costes operativos
    
- **Documentación**: Mantener documentados todos los procesos de despliegue es indispensable.
    
    - Facilita la replicación de entornos
    - Ayuda en la resolución de problemas
    - Esencial para la formación de nuevos miembros del equipo
    - Cumplimiento de normativas y auditorías

<figure markdown="span">
  ![Desarrollo web moderno](assets/webdev.png){ width="600" }
  <figcaption>Ecosistema del desarrollo web moderno, mostrando la interconexión entre diferentes tecnologías, herramientas y procesos</figcaption>
</figure>

!!! note "Conexión con DevOps"
    Recordad que en la Unidad 1 estudiamos DevOps y CI/CD. Todos estos conceptos de despliegue eficiente están directamente relacionados con las prácticas DevOps que ya habéis aprendido.

### 2. Modelos de ejecución de código en el servidor y en el cliente

La lógica de una aplicación web se divide y ejecuta en dos entornos principales, cada uno con responsabilidades específicas: el lado del cliente y el lado del servidor. Entender esta división es fundamental para comprender cómo funcionan las aplicaciones web modernas.

#### 2.1. Código en el lado del cliente (Frontend)

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

#### 2.2. Código en el lado del servidor (Backend)

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

#### 2.3. Colaboración entre cliente y servidor

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

### 3. Componentes de una web: Frontend, Backend y la división de responsabilidades

Ahora que entendemos los modelos de ejecución, profundicemos en los componentes principales de una aplicación web y cómo se relacionan entre sí.

#### 3.1. Frontend: la cara visible de la aplicación

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

#### 3.2. Backend: el cerebro de la aplicación

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

#### 3.3. La universalidad del Backend

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

### 4. Página Web vs. Aplicación Web

Es importante distinguir entre una página web tradicional y una aplicación web moderna, ya que tienen características y comportamientos muy diferentes.

#### 4.1. Página Web tradicional

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

#### 4.2. Aplicación Web (Web App)

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

#### 4.3. Progressive Web Apps (PWA)

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

#### 4.4. Tabla comparativa

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



### 5. Clics en la web: ¿Qué sucede realmente?

Para comprender mejor todo lo que hemos visto, analicemos paso a paso qué ocurre cuando hacemos clic en un enlace o botón en una aplicación web:

<figure markdown="span">
  ![Clic en la web](assets/clic.gif){ width="500" }
  <figcaption>Representación animada de lo que ocurre cuando un usuario hace clic en una aplicación web: desde la interacción en el navegador hasta el procesamiento en el servidor y la respuesta de vuelta</figcaption>
</figure>

**Flujo completo de una petición web:**

Te explico la imagen anterior como si estuviéramos en clase delante de la pizarra, siguiendo el dibujo de izquierda a derecha y de arriba abajo.

**1. Escribes la URL en el navegador**

* Tú tecleas, por ejemplo, `http://google.com` o `https://www.example.com`.
* El **navegador** entiende:
    
    * Protocolo: HTTP/HTTPS
    * Nombre de dominio: `google.com`
    * (Y si lo hubiera, puerto y ruta: `/login`, etc.)

Antes de hablar con nadie en Internet, el navegador necesita saber **a qué dirección IP** tiene que ir.

**2. Búsqueda de la IP: resolución DNS + cachés**

En la imagen, esa parte es el bloque “DNS” y la columna **Cache → Browser → OS → Router → ISP**.

1. **Cachés DNS**
   El objetivo es evitar hacer trabajo extra.
   El navegador pregunta, en este orden:
    
    * ¿Lo tengo en la **caché del propio navegador**?
    * ¿Lo tiene la **caché del sistema operativo**?
    * ¿Lo tiene el **router**?
    * ¿Lo tiene el **ISP**?
   
2. Si alguna de esas capas tiene la IP guardada, tenemos un **cache hit** ✅ y se termina la búsqueda ahí.
3. Si **nadie** lo sabe (**cache hit failed** ❌), entra en juego el **servidor DNS** “de verdad”:
    
    * Pregunta primero a un **root name server** (los de la parte superior izquierda: saben dónde están los `.com`, `.org`, etc.).
    * Luego a un **Top Level Domain server** (el que lleva `.com` por ejemplo).
    * Luego a un **servidor autoritativo** del dominio (`example.com` en el dibujo).
    * Finalmente, uno de ellos responde: *“`example.com` es la IP 8.9.0.1”* (la que se ve en la imagen).

4. Esa IP se devuelve hacia atrás y se va copiando en las cachés intermedias para que la próxima vez vaya más rápido.

Resultado de esta fase: Ya sabemos que `example.com` = `8.9.0.1`.

**3. Establecer la conexión TCP (3-way handshake)**

Parte central del diagrama: “Initiate TCP Connection” y los mensajes **SYN / SYN-ACK / ACK**.

Antes de enviar HTTP, el navegador necesita abrir una **conexión TCP** con el servidor:

1. **SYN**: el **cliente** (tu navegador) manda un paquete a `8.9.0.1` diciendo “quiero hablar contigo”.
2. **SYN-ACK**: el **servidor** responde “vale, he recibido tu petición y también quiero hablar”.
3. **ACK**: el cliente confirma “perfecto, ya estamos sincronizados”.

Con eso se crea el **canal fiable** entre cliente y servidor.
(Si fuera HTTPS, aquí además vendría el **handshake TLS** para cifrar la comunicación, aunque en la imagen no lo detallen.)

**4. Enviar la petición HTTP**

Una vez abierta la conexión TCP, pasamos al bloque “HTTP Request”.

El navegador envía algo del estilo:

```http
GET / HTTP/1.1
Host: www.example.com
User-Agent: ...
Accept-Language: ...
...
```

Es decir:

* Método (`GET`, `POST`, …)
* Ruta (`/`, `/login`, …)
* Cabeceras (idioma, tipo de contenido, cookies, etc.)

**5. El servidor procesa y responde**

En la parte derecha se ve “Server Response” y los códigos 1xx, 2xx, 3xx, 4xx, 5xx.

El servidor:

1. Recibe la petición HTTP.
2. Ejecuta la lógica necesaria (leer de BD, plantillas, etc.).
3. Genera una **respuesta HTTP**, por ejemplo:

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: ...

<html>...</html>
```

Los códigos se agrupan como indica el esquema:

* **1xx** – Información
* **2xx** – Éxito (200 OK, 201 Created…)
* **3xx** – Redirecciones (301, 302…)
* **4xx** – Errores del cliente (404 Not Found, 403 Forbidden…)
* **5xx** – Errores del servidor (500, 503…)

El cuerpo de la respuesta suele ser **HTML**, y a menudo dentro de ese HTML hay referencias a **CSS** y **JavaScript** y otros recursos.


**6. El navegador recibe HTML + CSS + JS**

Parte inferior izquierda: cuadro “HTML + CSS + JS” y las flechas a los parsers.

El navegador ya tiene:

* Un **documento HTML**.
* Uno o varios **CSS** enlazados.
* Uno o varios ficheros **JavaScript** enlazados.

Ahora empieza el “trabajo sucio” del navegador: **interpretar y pintar**.


**7. Parsing y construcción de estructuras internas**

El navegador transforma el texto en estructuras de datos:

1. **Parsear HTML → DOM Tree**
    
    * Pasa el HTML por un **tokenizer** (analizador léxico).
    * Con esos tokens construye el **DOM Tree** (árbol de nodos: `<html>`, `<body>`, `<div>`, etc.).

2. **Parsear CSS → CSSOM Tree**
    
    * Cada hoja de estilos se parsea (otro tokenizer).
    * Se genera el **CSSOM Tree**, que representa todas las reglas de estilos.

En paralelo:

3. **JavaScript**
    
    * Se “load & evaluate”: se carga el JS y se ejecuta.
    * El JS puede **modificar el DOM** y el **CSSOM** (añadir nodos, cambiar estilos, etc.), por eso en la imagen sale el ciclo entre JavaScript y los árboles.

**8. Render tree, layout y painting**

Parte central inferior: “Render Tree → Layout → Painting”.

Una vez que tiene DOM + CSSOM, el navegador:

1. **Crea el Render Tree**
    
    * Combina DOM y CSSOM para deducir qué elementos se deben **dibujar** y con qué estilo (color, fuente, etc.).
    * Elementos como `<head>` que no se pintan, se excluyen.

2. **Layout (reflow)**
    
    * Calcula **posiciones y tamaños** de cada elemento en la página:
        
        * coordenadas X/Y,
        * anchuras, alturas,
        * márgenes, paddings…
    
3. **Painting**
    
    * Finalmente **pinta** los píxeles en la pantalla:
        
        * fondos, bordes, texto, imágenes, sombras…

Todo esto lo hace el **Render Engine** del navegador, coordinado con:

* **User Interface** (la ventana, pestañas, barra de direcciones…),
* **Browser Engine** (coordina las partes),
* **Networking** (las descargas),
* **JS Engine** (ejecuta tu JavaScript).


**9. Página mostrada al usuario**

Al final de todo el recorrido (parte inferior “Web Page Successfully Loaded”):

* La conexión TCP sigue abierta un tiempo por si hay más peticiones (reutilización).
* El navegador puede seguir pidiendo recursos (imágenes, más JS o CSS, fuentes…).
* JavaScript puede seguir modificando el DOM, provocando nuevos layouts y repaints.

Pero desde tu punto de vista como usuario, lo que ves es sencillo:

* Has escrito una URL en el navegador…
* Y ha aparecido una página web “como por arte de magia”.

Solo que, como ves, la “magia” tiene bastantes pasos por debajo.

!!! note "Diferencias entre páginas y aplicaciones"
En una **página web tradicional**, todo el proceso resulta en una recarga completa de la página. En una **aplicación web moderna** (SPA), solo se actualiza la parte necesaria, haciendo la experiencia mucho más fluida y rápida.


### 6. Resumen de la unidad

En esta unidad hemos aprendido:

1. **El desarrollo web moderno** se enfoca tanto en la funcionalidad como en el despliegue eficiente de aplicaciones.
2. **El código se ejecuta en dos lugares**: cliente (navegador) y servidor, cada uno con responsabilidades específicas.
3. **Frontend** es lo que el usuario ve e interactúa, mientras que **Backend** es donde reside la lógica de negocio y los datos.
4. **Un Backend universal** puede servir a múltiples tipos de clientes (web, móvil, escritorio).
5. **Páginas web** son principalmente informativas, mientras que **aplicaciones web** proporcionan funcionalidad compleja y experiencias interactivas.
6. **Cada clic** en la web desencadena un flujo complejo de comunicaciones entre cliente y servidor.

Estos fundamentos son esenciales para comprender las arquitecturas web que estudiaremos en las siguientes secciones y para entender cómo desplegar aplicaciones correctamente.

## Referencias y bibliografía

- [Jose Luis González](https://github.com/joseluisgs). *Despliegue de aplicaciones Web - 2025 2026*. [https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026](https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026)
- Duckett, J. (2014). *HTML and CSS: Design and Build Websites
- Mozilla Developer Network (MDN). (2024). *Web Development*. [https://developer.mozilla.org](https://developer.mozilla.org)
- W3C. (2024). *Web Architecture*. [https://www.w3.org/standards/webarch/](https://www.w3.org/standards/webarch/)
- Fielding, R. T. (2000). *Architectural Styles and the Design of Network-based Software Architectures*. Doctoral dissertation, University of California, Irvine.

## Presentación

Puedes acceder a la presentación de esta unidad aquí:

[Presentación DAW-U3.1 - Introducción al Desarrollo Web](https://revilofe.github.io/slides/section4-daw/DAW-U3.1.-IntroDesarrolloWeb.html)

## Recursos adicionales

- [MDN Web Docs](https://developer.mozilla.org/) - Documentación completa sobre tecnologías web
- [Web.dev](https://web.dev/) - Guías y mejores prácticas de Google
- [Can I Use](https://caniuse.com/) - Compatibilidad de tecnologías web en navegadores
- [HTTP Status Dogs](https://httpstatusdogs.com/) - Forma divertida de aprender códigos HTTP
