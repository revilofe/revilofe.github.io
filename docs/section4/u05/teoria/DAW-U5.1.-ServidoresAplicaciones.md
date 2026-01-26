---
title: "UD 5 - 5.1 Servidores de aplicaciones"
description: Conceptos, arquitectura y despliegue en servidores de aplicaciones, con foco en RA3.
summary: Servidores de aplicaciones, despliegue, JavaEE, Node.js, buenas practicas y CI/CD.
authors:
    - Eduardo Fdez
date: 2025-02-01
icon: "material/file-document-outline"
permalink: /daw/unidad5/5.1
categories:
    - DAW
tags:
    - Servidores de aplicaciones
    - Despliegue
    - JavaEE
    - Node.js
    - CI/CD
---

## 5.1. Servidores de aplicaciones

En la unidad 3 vimos la base de las arquitecturas web, el protocolo HTTP y los servidores web. En esta unidad damos un paso mas: trabajamos con **servidores de aplicaciones**, su papel en la arquitectura, su configuracion y el despliegue seguro de aplicaciones, alineado con el **RA3** del modulo.

El objetivo es que el alumnado entienda **que hace un servidor de aplicaciones**, por que es necesario y como se integra con el servidor web y con la base de datos para ofrecer un servicio estable, seguro y escalable.

### 1. Resultado de aprendizaje y criterios de evaluacion (RA3)

El **RA3** establece que el alumnado debe ser capaz de implantar aplicaciones web en servidores de aplicaciones, configurarlas con seguridad y documentar el proceso.

#### 1.1. Criterios de evaluacion asociados

- a) Describir componentes y funcionamiento de los servicios del servidor.
- b) Identificar archivos principales de configuracion y bibliotecas compartidas.
- c) Configurar cooperacion con el servidor web.
- d) Activar mecanismos de seguridad del servidor de aplicaciones.
- e) Configurar y usar componentes web del servidor de aplicaciones.
- f) Ajustar parametros necesarios para el despliegue.
- g) Probar funcionamiento y rendimiento de la aplicacion.
- h) Elaborar documentacion de administracion y recomendaciones.
- i) Usar virtualizacion, nube o contenedores en el despliegue.

!!! info "Relacion con la unidad 3"
    En la unidad 3 ya tratamos servidores web, despliegue y seguridad basica. Aqui ampliamos esos conceptos con **servidores de aplicaciones** y un enfoque practico en **configuracion, seguridad y pruebas**.

### 2. Concepto y papel del servidor de aplicaciones

#### 2.1. Definicion y ubicacion en la arquitectura

Un servidor de aplicaciones es una plataforma software que permite **ejecutar aplicaciones web** y ofrecer servicios adicionales al servidor web, como gestion de sesiones, seguridad, transacciones, recursos compartidos y logs.

Se puede ver como un **middleware**: un entorno que une la peticion del cliente con la logica de negocio y los datos, aportando servicios comunes que la aplicacion no deberia implementar una y otra vez.

Suele situarse entre el servidor web y el servidor de bases de datos, actuando como intermediario para procesar **logica de negocio** y peticiones dinamicas.

<figure markdown>
  ![](../assets/application-server1.webp)
  <figcaption>Ubicacion del servidor de aplicaciones en una arquitectura clasica.</figcaption>
</figure>

#### 2.2. Terminologia basica

Esta terminología la usaremos durante la unidad:

| Termino           | Descripcion                                           |
|-------------------|-------------------------------------------------------|
| Servidor web      | Sirve contenido estatico y gestiona peticiones HTTP.  |
| Cliente web       | Navegador o app que solicita recursos.                |
| HTTPS             | Protocolo seguro entre cliente y servidor.            |
| JSON              | Formato ligero para el intercambio de datos.          |
| Logica de negocio | Reglas del dominio y procesamiento de datos.          |
| Aplicacion        | Software que consume datos y los presenta al usuario. |

#### 2.3. Por que necesitamos servidores de aplicaciones

Los servidores web son ligeros y eficientes para contenido estatico, pero **las peticiones dinamicas** requieren mas potencia y servicios avanzados. El servidor de aplicaciones aporta:

- Ejecución de lógica de negocio.
- Gestion de sesiones y usuarios.
- Pools de conexiones y recursos compartidos.
- Transacciones distribuidas y servicios de mensajeria.
- Diagnostico, registros y seguridad avanzada.

En otras palabras, mientras el servidor web se centra en **servir**, el servidor de aplicaciones se centra en **procesar**.

#### 2.4. Optimización del tráfico y seguridad

El servidor de aplicaciones mejora el rendimiento y reduce riesgos al separar el trafico dinamico del estatico. Tambien añade una capa extra de proteccion frente a ataques, ya que las peticiones llegan filtradas antes de tocar los datos sensibles.

Esta separacion permite aplicar controles mas estrictos en la capa de negocio sin penalizar la entrega de contenido estatico.

<figure markdown>
  ![](../assets/serv_apl.png)
  <figcaption>Servidor de aplicaciones como capa de seguridad y control.</figcaption>
</figure>

#### 2.5. Componentes y servicios habituales

Aunque cada producto tiene su propia arquitectura, suelen existir piezas comunes:

- **Contenedor web**: gestiona servlets, JSP o frameworks equivalentes.
- **Conectores**: reciben las peticiones del servidor web o del cliente.
- **Motor de aplicaciones**: ejecuta la logica de negocio.
- **Gestor de sesiones**: mantiene el estado del usuario entre peticiones.
- **Recursos compartidos**: pools de conexiones y colas de mensajes.
- **Logs y diagnostico**: trazas de acceso y errores para auditoria.

En servidores Java como Tomcat, estos elementos se agrupan en estructuras como **Service**, **Connector**, **Engine**, **Host** y **Context**. Comprender estas piezas es clave para el criterio a) del RA3.

#### 2.6. Tendencias actuales

El uso de servidores de aplicaciones continua su expansion por dos razones principales:

- La migracion a entornos cloud y contenedores.
- La necesidad de aplicaciones distribuidas que se actualizan con frecuencia.

Esto implica que los administradores deben dominar despliegues reproducibles, automatizados y con buenas practicas de seguridad.

### 3. Funcionamiento general en una arquitectura web

En esta sección vemos como interactúan el servidor web y el servidor de aplicaciones en una arquitectura web típica.

#### 3.1. Flujo de peticiones en un servidor Java

En un servidor JavaEE, el flujo tipico es este:

1. El cliente abre un navegador y solicita una página.
2. El servidor web recibe la petición HTTP.
3. Si es contenido estático, responde directamente.
4. Si es contenido dinámico, reenvía la petición al servidor de aplicaciones.
5. El servidor de aplicaciones convierte la petición en una solicitud de servlet.
6. El servlet realiza consultas al servidor de base de datos o ejecuta logica de negocio.
7. El servidor de aplicaciones envia la respuesta HTTP generada al servidor web.
8. El servidor web entrega la respuesta al cliente.

Este flujo permite **aislar la logica de negocio** del servidor web y mantener cada capa con responsabilidades claras. El servidor web optimiza la entrega de archivos, y el servidor de aplicaciones optimiza el procesamiento.

<figure markdown>
  ![](../assets/capas.webp)
  <figcaption>Capas de servidor web y servidor de aplicaciones.</figcaption>
</figure>

#### 3.2. Servidor web vs servidor de aplicaciones

| Aspecto             | Servidor de aplicaciones                             | Servidor web                              |
|---------------------|------------------------------------------------------|-------------------------------------------|
| Diseñado para       | Logica de negocio compleja y generacion dinamica     | Servir contenido estatico y HTTP rapido   |
| Almacena            | Aplicaciones, logica y conexiones a base de datos    | Archivos estaticos (HTML, CSS, imagenes)  |
| Consumo de recursos | Alto (runtime completo)                              | Bajo y optimizado para concurrencia       |
| Soporta             | Servlets, JSP, EJB, transacciones, colas             | HTTP/HTTPS, proxy inverso, balanceo       |

En escenarios reales se suele usar **ambos**: el servidor web como frontal y el servidor de aplicaciones como backend.

!!! definition "Servlet"
    Un **servlet** es un programa Java que se ejecuta en un **contenedor web** dentro del servidor de aplicaciones y genera contenido dinamico.
    A diferencia de enfoques antiguos donde se iniciaba un proceso por peticion, los servlets usan hilos ligeros para atender multiples solicitudes.

#### 3.3. Servicios comunes del servidor de aplicaciones

A continuación se presenta el conjunto **completo** de servicios que puede proporcionar un servidor de aplicaciones. Es cierto que, en entornos sencillos, esta lista suele reducirse a lo mínimo imprescindible para que la aplicación “arranque y responda”. Sin embargo, cuando esa simplificación recorta demasiado, se terminan omitiendo **servicios empresariales críticos** que marcan la diferencia entre un **servidor de aplicaciones real** (por ejemplo, WildFly) y un **mero contenedor de servlets** (como una instalación básica de Tomcat).

A continuación se muestra la **lista de referencia** de servicios comunes que conviene dominar si el objetivo es trabajar un temario con enfoque profesional.

##### 3.3.1. Contenedor web (Servlets, JSP)

Es el motor encargado de gestionar el ciclo de vida de los componentes web.

Función: recibe peticiones HTTP, crea objetos `Request` y `Response`, e invoca el servlet o la pagina JSP correspondiente.

Importancia: aísla al programador de escuchar en puertos y parsear HTTP manualmente, traduciendo peticiones a objetos del lenguaje.

##### 3.3.2. Gestion de sesiones y autenticación

El servidor ofrece mecanismos nativos para identificar usuarios y mantener su estado.

Sesiones: guarda datos (por ejemplo, un carrito de la compra) asociados a un usuario mediante cookies (JSESSIONID) o reescritura de URL, sin gestionar memoria manualmente.

Autenticación: proporciona **realms** para validar usuarios contra bases de datos, LDAP o ficheros planos, con seguridad declarativa (por ejemplo, en `web.xml`) en lugar de repetir logica de login.

##### 3.3.3. Conectores y pools de conexiones

Optimiza la comunicacion con sistemas externos, especialmente bases de datos.

Pool de conexiones: abrir una conexion es costoso, por lo que el servidor mantiene una piscina de conexiones listas. La aplicacion pide una prestada y la devuelve al terminar.

Beneficio: mejora rendimiento y evita saturar la base de datos.

##### 3.3.4. Gestion de transacciones y mensajería

Servicios críticos para la integridad de datos en entornos empresariales.

Transacciones (JTA): agrupa operaciones en una unidad atomica. Si una falla, el servidor realiza rollback automatico.

Mensajería (JMS): permite enviar mensajes a colas para procesamiento asincrono (por ejemplo, enviar un email) sin bloquear al usuario.

##### 3.3.5. Logs, diagnostico y monitorización

Herramientas para controlar la salud del servidor en produccion.

Logs unificados: centraliza errores y eventos de todas las aplicaciones desplegadas.

JMX (Java Management Extensions): permite ver uso de memoria, usuarios activos o reiniciar servicios en caliente.

##### 3.3.6. Servicio de Nombres y Directorio (JNDI)

Es una agenda interna para localizar recursos por nombre logico (por ejemplo, `jdbc/MiBaseDeDatos`) en lugar de direcciones IP y contraseñas en codigo.

Esto facilita cambiar configuraciones sin recompilar ni modificar la aplicacion.

##### 3.3.7. Alta Disponibilidad (Clustering)

Permite que varios servidores trabajen como si fueran uno solo.

Replicación de sesión: si un servidor cae, otro mantiene el estado y el usuario no pierde su trabajo.

##### 3.3.8. Servicios Web y Remoting (SOAP/REST/RMI)

Incluye mecanismos para exponer y consumir servicios remotos mediante API.

Son claves para integraciones entre sistemas y arquitecturas distribuidas.

#### 3.4. Separación de responsabilidades

Separar servidor web y servidor de aplicaciones aporta ventajas claras:

- El servidor web puede centrarse en **contenido estático** y caché.
- El servidor de aplicaciones puede escalar de forma independiente.
- Se puede aplicar seguridad específica a la capa de negocio.
- Permite balanceo y redundancia sin afectar al frontal.

### 4. Despliegue de aplicaciones web

Después de entender el papel del servidor de aplicaciones, es clave dominar el **despliegue**: mover cambios entre entornos de trabajo hasta llegar a producción. Desplegar, de forma sencilla, sería realizar todas las operaciones necesarias para llevar una versión de una aplicación desde un entorno de desarrollo hasta el entorno de producción. Ya hemos visto en la unidad 3 como desplegar aplicaciones web en servidores web. También, en la unidad 1, vimos como github actions puede ayudarnos a automatizar el despliegue. En esta unidad vamos a profundizar en el despliegue de aplicaciones web en servidores de aplicaciones, con foco en buenas prácticas y seguridad. 

#### 4.1. Que es el despliegue y que entornos existen

El despliegue consiste en mover cambios entre entornos de trabajo. Los más habituales son:

- **Entorno local**: donde cada persona desarrolla y prueba sus cambios.
- **Entorno de desarrollo**: integra cambios de varios miembros del equipo.
- **Entorno de preproducción**: replica el entorno real para pruebas finales.
- **Entorno de producción**: el sistema que usan las personas usuarias.

El flujo mas habitual es avanzar cambios de izquierda a derecha, hasta llegar a producción.

Este modelo permite que el equipo valide los cambios en entornos cada vez mas cercanos al real. Si algo falla en un entorno intermedio, se corrige antes de impactar a las personas usuarias.

<figure markdown>
  ![](../assets/deploy.png)
  <figcaption>Modelo clásico de despliegue entre entornos.</figcaption>
</figure>

#### 4.2. Pasos del proceso de despliegue

El flujo del proceso de despliegue consta de **5 pasos**: **planificacion, desarrollo, pruebas, despliegue y supervision**.

Antes de entrar en detalle, una nota importante: este flujo cubre los **aspectos fundamentales** y se presenta como una **simplificacion didactica**. No significa que sea la unica forma de desplegar, sino una base clara para comprender el proceso y poder adaptarlo a cada caso.

1. **Planificación** del despliegue y sus reglas.
2. **Desarrollo** en entornos locales o de desarrollo.
3. **Pruebas** progresivas en entornos intermedios.
4. **Despliegue** en producción.
5. **Supervision** tras el lanzamiento.

##### 4.2.1. Planificación del despliegue

Para que el proceso sea fluido, es clave contar con un **plan de despliegue** que se siga siempre. Esto ayuda a que todo se haga de la misma forma en cada cambio, especialmente cuando varias personas trabajan en el mismo proyecto.

Un plan debe definir:

- Cuando se pasa de local a desarrollo o preproduccion.
- Horarios o ventanas en las que se permite desplegar a produccion.
- Criterios de aceptacion y responsables del despliegue.

En proyectos abiertos, un buen plan permite incluso preparar **release candidates** y dejar que la comunidad pruebe antes del lanzamiento. Ademas, cada cambio debe planificarse: poco para cambios pequeños y mas detalle para cambios grandes.

##### 4.2.2. Desarrollo del cambio

Con el plan definido, llega el desarrollo real. Para evitar conflictos y errores, el trabajo debe hacerse en **entornos locales o de desarrollo**.

Una vez finalizado el cambio, se prepara para pasar a la siguiente fase y se integra en el flujo de despliegue previsto.

##### 4.2.3. Pruebas progresivas

Las pruebas son esenciales para evitar fallos en produccion. No se pueden hacer pruebas reales sin desplegar los cambios en entornos nuevos.

Cuando el cambio funciona en local o desarrollo, se despliega al siguiente entorno y se vuelve a validar. El objetivo es llegar a **preproduccion**, un entorno muy parecido al real, donde se realiza el control de calidad final.

Si se detectan errores en cualquier fase, el cambio vuelve a desarrollo, se corrige y se repite el ciclo.

##### 4.2.4. Despliegue en entorno real

Tras superar las pruebas, se despliega en produccion. En teoria es un paso seguro, pero siempre puede aparecer algun problema inesperado.

Por eso es imprescindible que el despliegue se haga siguiendo el plan y con un criterio claro de vuelta atrás si algo falla.

##### 4.2.5. Supervisión y monitorización

Una vez en producción, toca **supervisar**. Hay que observar logs, comportamiento de usuarios y rendimiento del sistema para detectar incidencias.

Un buen consejo es desplegar en momentos de baja actividad y con personal disponible para reaccionar. Asi se minimiza el impacto en usuarios y se puede corregir o revertir rápidamente si es necesario.

Si hay que revertir cambios, se debe actuar con calma y seguir un proceso claro, igual de riguroso que el despliegue.

Cada paso reduce el riesgo. Si se detectan fallos en un entorno intermedio, se vuelve al desarrollo y se corrige antes de afectar a producción. En despliegues grandes, la planificación incluye ventanas de despliegue, criterios de aceptación y un plan claro de rollback.

Durante las pruebas es clave verificar que la aplicación funciona en condiciones similares a producción. Esto incluye datos de ejemplo, configuraciones reales y pruebas de rendimiento básicas para detectar cuellos de botella.

#### 4.3. Tipos de despliegue

- **Metadatos**: cambios en código, plantillas o configuraciones. Disponible para desarrolladores.
- **Contenido**: textos, imágenes y recursos editables. Disponible para editores o administradores y no requiere conocimientos técnicos.

Separar ambos tipos ayuda a minimizar riesgos. El contenido suele moverse con más frecuencia y con menos impacto técnico.

#### 4.4. Ventajas de trabajar con multiples entornos

- Reducción del riesgo en producción. Cuando tienes múltiples entornos, los errores catastróficos ocurren en un entorno seguro (Desarrollo o Pruebas) y nunca llegan al usuario final. Así debería de ser siempre.
- Ahorro de tiempo en pruebas. Tener entornos separados permite paralizar el trabajo sin bloquearse mutuamente. Cada equipo puede trabajar en su entorno sin interferir con otros.
- Mejor gestion de contenidos sensibles al tiempo. Prepara el lanzamiento antes de la fecha. En entornos como comercio electrónico o noticias, es vital probar cambios de contenido antes de publicarlos. Los entornos separados facilitan esta tarea.

Cuando los cambios pasan por varios entornos, el equipo gana control y puede detectar errores antes de que lleguen a las personas usuarias.

#### 4.5. Supervisar y reaccionar

Después de desplegar hay que **supervisar**: revisar logs, estado del servicio y respuesta del sistema. Si algo falla, es clave tener preparado un plan de **rollback** y un protocolo claro de comunicación.

Un buen despliegue no termina cuando se publica el cambio, sino cuando se confirma que el servicio responde correctamente y no hay errores en los registros. En equipos profesionales, la monitorización continua forma parte del proceso de despliegue.

!!! info "Importancia de la monitorización"
    La monitorización post-despliegue es crucial para detectar problemas que no se ven en pruebas. Un buen sistema de alertas ayuda a reaccionar rápido y minimizar el impacto en usuarios.

#### 4.6. Buenas prácticas específicas del proceso

Además de los pasos básicos, hay recomendaciones concretas que ayudan a reducir incidencias:

- Definir un horario de despliegue con baja actividad de usuarios. Elegir momentos tranquilos minimiza el impacto si algo falla. 
- Revisar diferencias entre desarrollo y producción antes de publicar.
- Establecer roles para decidir quien puede desplegar en entornos críticos.
- Mantener un procedimiento claro para revertir cambios.

Estas prácticas convierten el despliegue en un proceso predecible y repetible, que es el objetivo principal del modulo.

### 5. Buenas prácticas de despliegue

#### 5.1. Usar control de versiones (Git)

Git permite trabajar en equipo y recuperar versiones estables en caso de error. Sin control de versiones, el riesgo de conflictos aumenta de forma critica.

Un repositorio bien organizado facilita comparar cambios entre entornos y saber que version se ha desplegado en cada momento.

#### 5.2. Trabajar en ramas

Separar funcionalidades en ramas evita interferencias entre tareas y facilita las pruebas previas a produccion.

Ademas, permite que distintos equipos prueben funcionalidades en paralelo sin romper el entorno principal.

#### 5.3. Desarrollar en local antes de desplegar

Trabajar en local acelera pruebas y reduce el numero de despliegues necesarios para validar un cambio.

El objetivo es llegar al entorno de desarrollo con un cambio ya estable, no para "ver si funciona".

#### 5.4. Revisar diferencias antes de producir

Comparar entorno de desarrollo y produccion antes de lanzar evita errores de ultima hora y despliegues fallidos.

Una revision final puede detectar cambios no documentados, configuraciones olvidadas o recursos faltantes.

#### 5.5. Limitar permisos de despliegue

En equipos grandes, es recomendable que solo perfiles senior puedan desplegar en produccion para reducir riesgos.

No se trata de frenar al equipo, sino de asegurar que el despliegue sigue un criterio comun y se revisa antes del paso a produccion.

#### 5.6. Gestionar errores y rollback

Si algo falla en produccion, no hay que entrar en panico. Hay que evaluar si un rollback es viable y aplicar un plan de contingencia.

No siempre el rollback arregla el problema. Antes hay que confirmar que la incidencia proviene del cambio desplegado.

#### 5.7. Escoger la mejor franja de despliegue

El mejor momento suele ser cuando hay menos usuarios activos y el equipo esta disponible para reaccionar.

En muchos equipos se planifican despliegues con guardias rotativas, para asegurar respuesta rapida ante fallos.

!!! warning "Sin un plan, el despliegue se convierte en improvisación"
    Define responsables, horario de despliegue y protocolo de rollback. Esto reduce el impacto de incidencias en producción.

### 6. Despliegue de aplicaciones Java

#### 6.1. Servlets y JSP

En aplicaciones JavaEE, los servlets y las paginas JSP gestionan peticiones HTTP y generan contenido dinamico.

Un servlet suele encargarse de la logica, mientras que una JSP se centra en la presentacion. En proyectos modernos, las JSP se sustituyen por frameworks, pero el concepto sigue siendo el mismo: **recibir una peticion, procesarla y devolver una respuesta**.

#### 6.2. Estructura basica de una aplicacion JavaEE

Una aplicacion web JavaEE suele contener:

- Directorio raiz con paginas HTML o JSP.
- Directorio `WEB-INF` con configuración y clases.
- Recursos (imágenes, CSS, JS) en la estructura necesaria.

Cada aplicacion web se considera un **contexto** dentro del servidor. Este contexto define la ruta base con la que se accede a la aplicacion.

#### 6.3. Empaquetamiento en WAR

El formato **WAR** es el estandar para distribuir aplicaciones web JavaEE. Se crea empaquetando el directorio de la aplicacion con la herramienta `jar`.

Un WAR contiene paginas, clases compiladas, librerias y archivos de configuracion, todo preparado para que el servidor lo despliegue de forma automatica.

#### 6.4. Despliegue de WAR

Los servidores JavaEE permiten desplegar un WAR desde consola de administracion o copiandolo en un directorio de despliegue.

En entornos reales, el despliegue suele automatizarse con pipelines o con herramientas del propio servidor, para asegurar que el proceso sea reproducible.

#### 6.5. Maven como herramienta de build

Maven es una herramienta open-source cuyo lanzamiento estable 1.0 fue en 2004, creada para simplificar la compilacion, pruebas y despliegue de proyectos.

<figure markdown>
  ![](../assets/maven-logo.png)
  <figcaption>Maven y sus ciclos de build.</figcaption>
</figure>

Ciclos habituales en Maven:

- validate
- compile
- test
- package
- integration-test
- verify
- install
- deploy

Ejemplo de ejecucion:

```bash
mvn package
```

Maven utiliza un archivo `pom.xml` para definir dependencias y estructura del proyecto.

### 7. Despliegue de aplicaciones Node.js con Express

#### 7.1. Node.js

Node.js es un **entorno de ejecucion** para JavaScript en el servidor. No es un lenguaje ni un framework.

Aunque dispone de modulos nativos como `http` y `fs` para manejar peticiones y servir archivos, en entornos profesionales se usan frameworks como Express (o alternativas como Fastify o NestJS) para simplificar el enrutado y los middlewares.

<figure markdown>
  ![](../assets/nodejs-new-pantone-black.svg)
  <figcaption>Node.js como entorno de ejecucion.</figcaption>
</figure>

#### 7.2. Express

Express es un framework ligero que simplifica la creacion de APIs y aplicaciones web en Node.js.

Se encarga del enrutado, la gestion de middlewares y la definicion de endpoints, dejando al desarrollador centrarse en la logica de negocio.

<figure markdown>
  ![](../assets/express-logo.png)
  <figcaption>Express como framework de Node.js.</figcaption>
</figure>

#### 7.3. npm y gestion de paquetes

npm es el gestor de paquetes por defecto en Node.js. Permite instalar dependencias, publicar paquetes y definir scripts.

En un despliegue real, npm ayuda a fijar versiones, reproducir instalaciones y ejecutar tareas de build o pruebas.

NPM convive con alternativas enfocadas en rendimiento y eficiencia como **Yarn**, **pnpm** o el runtime **Bun**.

<figure markdown>
  ![](../assets/npm-logo.png)
  <figcaption>npm como gestor de paquetes.</figcaption>
</figure>

Un ejemplo de `package.json` con scripts seria:

```json
{
  "scripts": {
    "build": "tsc",
    "format": "prettier --write **/*.ts",
    "format-check": "prettier --check **/*.ts",
    "lint": "eslint src/**/*.ts",
    "pack": "ncc build",
    "test": "jest",
    "all": "npm run build && npm run format && npm run lint && npm run pack && npm test"
  }
}
```

### 8. CI/CD en el despliegue moderno

#### 8.1. Concepto general

CI/CD es un conjunto de practicas que automatizan integracion, pruebas, distribucion y despliegue.

El objetivo es reducir errores humanos y entregar cambios de forma frecuente, segura y medible.

<figure markdown>
  ![](../assets/ci-cd-flow-desktop.png)
  <figcaption>Flujo general de CI/CD.</figcaption>
</figure>

#### 8.2. Diferencias entre CI, CD y despliegue continuo

- **CI**: integra cambios frecuentes y ejecuta pruebas automatizadas.
- **CD**: distribuye artefactos listos para produccion.
- **Despliegue continuo**: publica en produccion sin intervencion manual.

En la practica, muchas organizaciones empiezan con CI y evolucionan a CD cuando las pruebas y los procesos son fiables.

#### 8.3. Integracion continua

<figure markdown>
  ![](../assets/ci.png)
  <figcaption>Integracion continua.</figcaption>
</figure>

La CI evita conflictos al integrar cambios a diario y validar con pruebas automatizadas. Asi se detectan fallos temprano, antes de llegar a produccion.

#### 8.4. Distribucion continua

<figure markdown>
  ![](../assets/cd.png)
  <figcaption>Distribucion continua.</figcaption>
</figure>

La CD automatiza la entrega de artefactos listos para desplegar en produccion. El equipo de operaciones puede desplegar cuando lo considere oportuno.

#### 8.5. Implementacion continua

<figure markdown>
  ![](../assets/cd2.png)
  <figcaption>Implementacion continua.</figcaption>
</figure>

El despliegue continuo publica cambios automaticamente tras superar pruebas. Para que funcione, las pruebas deben ser completas y confiables.

### 9. Evidencias habituales para evaluar el RA3

- Esquemas o explicaciones del servidor de aplicaciones.
- Configuracion localizada y justificada (server.xml, context.xml, etc.).
- Integracion con servidor web mediante proxy o reverse proxy.
- Usuarios, roles y accesos configurados y probados.
- Aplicacion desplegada y funcionando con logs correctos.
- Ajustes aplicados (puertos, rutas, variables, permisos).
- Pruebas de funcionamiento y rendimiento basicas.
- Documentacion reproducible de la instalacion y uso.
- Despliegue en contenedor o nube si aplica.

## Referencias y bibliografia

- [What is an application server? (I)](https://www.itpro.co.uk/strategy/29643/what-is-an-application-server)
- [What is an application server? (II)](https://www.serverwatch.com/guides/application-server/)
- [What is deployment in software and web development](https://umbraco.com/knowledge-base/deployment/)
- [Simple y rapido. Entiende que es Maven en menos de 10 min.](https://www.javiergarzas.com/2014/06/maven-en-10-min.html)
- [Maven in 5 Minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
- [Apuntes JavaEE](http://www.jtech.ua.es/j2ee/restringido/cw/sesion01-apuntes.html)
- [Que es Node.js y por que deberia usarlo](https://kinsta.com/es/base-de-conocimiento/que-es-node-js/)
- [Que son la integracion y la distribucion continuas (CI/CD)](https://www.redhat.com/es/topics/devops/what-is-ci-cd)

## Recursos adicionales

- Documentacion oficial de Apache Tomcat y WildFly.
- Guias de despliegue de Node.js en produccion.
