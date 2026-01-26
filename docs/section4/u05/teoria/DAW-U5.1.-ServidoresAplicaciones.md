---
title: "UD 5 - 5.1 Servidores de aplicaciones"
description: Conceptos, arquitectura y despliegue en servidores de aplicaciones, con foco en RA3.
summary: Servidores de aplicaciones, despliegue, JavaEE, Node.js, buenas prácticas y CI/CD.
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

En la unidad 3 vimos la base de las arquitecturas web, el protocolo HTTP y los servidores web. En esta unidad damos un paso más: trabajamos con **servidores de aplicaciones**, su papel en la arquitectura, su configuración y el despliegue seguro de aplicaciones, alineado con el **RA3** del módulo.

El objetivo es que el alumnado entienda **qué hace un servidor de aplicaciones**, por qué es necesario y cómo se integra con el servidor web y con la base de datos para ofrecer un servicio estable, seguro y escalable.

### 1. Resultado de aprendizaje y criterios de evaluación (RA3)

El **RA3** establece que el alumnado debe ser capaz de implantar aplicaciones web en servidores de aplicaciones, configurarlas con seguridad y documentar el proceso.

#### 1.1. Criterios de evaluación asociados

- a) Describir componentes y funcionamiento de los servicios del servidor.
- b) Identificar archivos principales de configuración y bibliotecas compartidas.
- c) Configurar cooperación con el servidor web.
- d) Activar mecanismos de seguridad del servidor de aplicaciones.
- e) Configurar y usar componentes web del servidor de aplicaciones.
- f) Ajustar parámetros necesarios para el despliegue.
- g) Probar funcionamiento y rendimiento de la aplicación.
- h) Elaborar documentación de administración y recomendaciones.
- i) Usar virtualización, nube o contenedores en el despliegue.

!!! info "Relación con la unidad 3"
    En la unidad 3 ya tratamos servidores web, despliegue y seguridad básica. Aquí ampliamos esos conceptos con **servidores de aplicaciones** y un enfoque práctico en **configuración, seguridad y pruebas**.

### 2. Concepto y papel del servidor de aplicaciones

#### 2.1. Definición y ubicación en la arquitectura

Un servidor de aplicaciones es una plataforma software que permite **ejecutar aplicaciones web** y ofrecer servicios adicionales al servidor web, como gestión de sesiones, seguridad, transacciones, recursos compartidos y logs.

Se puede ver como un **middleware**: un entorno que une la petición del cliente con la lógica de negocio y los datos, aportando servicios comunes que la aplicación no debería implementar una y otra vez.

Suele situarse entre el servidor web y el servidor de bases de datos, actuando como intermediario para procesar **lógica de negocio** y peticiones dinámicas.

<figure markdown>
  ![](../assets/application-server1.webp)
  <figcaption>Ubicación del servidor de aplicaciones en una arquitectura clásica.</figcaption>
</figure>

#### 2.2. Terminología básica

Esta terminología la usaremos durante la unidad:

| Término           | Descripción                                           |
|-------------------|-------------------------------------------------------|
| Servidor web      | Sirve contenido estático y gestiona peticiones HTTP.  |
| Cliente web       | Navegador o app que solicita recursos.                |
| HTTPS             | Protocolo seguro entre cliente y servidor.            |
| JSON              | Formato ligero para el intercambio de datos.          |
| Lógica de negocio | Reglas del dominio y procesamiento de datos.          |
| Aplicación        | Software que consume datos y los presenta al usuario. |

#### 2.3. Por qué necesitamos servidores de aplicaciones

Los servidores web son ligeros y eficientes para contenido estático, pero **las peticiones dinámicas** requieren más potencia y servicios avanzados. El servidor de aplicaciones aporta:

- Ejecución de lógica de negocio.
- Gestión de sesiones y usuarios.
- Pools de conexiones y recursos compartidos.
- Transacciones distribuidas y servicios de mensajería.
- Diagnóstico, registros y seguridad avanzada.

En otras palabras, mientras el servidor web se centra en **servir**, el servidor de aplicaciones se centra en **procesar**.

#### 2.4. Optimización del tráfico y seguridad

El servidor de aplicaciones mejora el rendimiento y reduce riesgos al separar el tráfico dinámico del estático. También añade una capa extra de protección frente a ataques, ya que las peticiones llegan filtradas antes de tocar los datos sensibles.

Esta separación permite aplicar controles más estrictos en la capa de negocio sin penalizar la entrega de contenido estático.

<figure markdown>
  ![](../assets/serv_apl.png)
  <figcaption>Servidor de aplicaciones como capa de seguridad y control.</figcaption>
</figure>

#### 2.5. Componentes y servicios habituales

Aunque cada producto tiene su propia arquitectura, suelen existir piezas comunes:

- **Contenedor web**: gestiona servlets, JSP o frameworks equivalentes.
- **Conectores**: reciben las peticiones del servidor web o del cliente.
- **Motor de aplicaciones**: ejecuta la lógica de negocio.
- **Gestor de sesiones**: mantiene el estado del usuario entre peticiones.
- **Recursos compartidos**: pools de conexiones y colas de mensajes.
- **Logs y diagnóstico**: trazas de acceso y errores para auditoría.

En servidores Java como Tomcat, estos elementos se agrupan en estructuras como **Service**, **Connector**, **Engine**, **Host** y **Context**. Comprender estas piezas es clave para el criterio a) del RA3.

#### 2.6. Tendencias actuales

El uso de servidores de aplicaciones continúa su expansión por dos razones principales:

- La migración a entornos cloud y contenedores.
- La necesidad de aplicaciones distribuidas que se actualizan con frecuencia.

Esto implica que los administradores deben dominar despliegues reproducibles, automatizados y con buenas prácticas de seguridad.

### 3. Funcionamiento general en una arquitectura web

En esta sección vemos cómo interactúan el servidor web y el servidor de aplicaciones en una arquitectura web típica.

#### 3.1. Flujo de peticiones en un servidor Java

En un servidor JavaEE, el flujo típico es este:

1. El cliente abre un navegador y solicita una página.
2. El servidor web recibe la petición HTTP.
3. Si es contenido estático, responde directamente.
4. Si es contenido dinámico, reenvía la petición al servidor de aplicaciones.
5. El servidor de aplicaciones convierte la petición en una solicitud de servlet.
6. El servlet realiza consultas al servidor de base de datos o ejecuta lógica de negocio.
7. El servidor de aplicaciones envía la respuesta HTTP generada al servidor web.
8. El servidor web entrega la respuesta al cliente.

Este flujo permite **aislar la lógica de negocio** del servidor web y mantener cada capa con responsabilidades claras. El servidor web optimiza la entrega de archivos, y el servidor de aplicaciones optimiza el procesamiento.

<figure markdown>
  ![](../assets/capas.webp)
  <figcaption>Capas de servidor web y servidor de aplicaciones.</figcaption>
</figure>

#### 3.2. Servidor web vs servidor de aplicaciones

| Aspecto             | Servidor de aplicaciones                             | Servidor web                              |
|---------------------|------------------------------------------------------|-------------------------------------------|
| Diseñado para       | Lógica de negocio compleja y generación dinámica     | Servir contenido estático y HTTP rápido   |
| Almacena            | Aplicaciones, lógica y conexiones a base de datos    | Archivos estáticos (HTML, CSS, imágenes)  |
| Consumo de recursos | Alto (runtime completo)                              | Bajo y optimizado para concurrencia       |
| Soporta             | Servlets, JSP, EJB, transacciones, colas             | HTTP/HTTPS, proxy inverso, balanceo       |

En escenarios reales se suele usar **ambos**: el servidor web como frontal y el servidor de aplicaciones como backend.

!!! definition "Servlet"
    Un **servlet** es un programa Java que se ejecuta en un **contenedor web** dentro del servidor de aplicaciones y genera contenido dinámico.
    A diferencia de enfoques antiguos donde se iniciaba un proceso por petición, los servlets usan hilos ligeros para atender múltiples solicitudes.

#### 3.3. Servicios comunes del servidor de aplicaciones

A continuación se presenta el conjunto **completo** de servicios que puede proporcionar un servidor de aplicaciones. Es cierto que, en entornos sencillos, esta lista suele reducirse a lo mínimo imprescindible para que la aplicación “arranque y responda”. Sin embargo, cuando esa simplificación recorta demasiado, se terminan omitiendo **servicios empresariales críticos** que marcan la diferencia entre un **servidor de aplicaciones real** (por ejemplo, WildFly) y un **mero contenedor de servlets** (como una instalación básica de Tomcat).

A continuación se muestra la **lista de referencia** de servicios comunes que conviene dominar si el objetivo es trabajar un temario con enfoque profesional.

##### 3.3.1. Contenedor web (Servlets, JSP)

Es el motor encargado de gestionar el ciclo de vida de los componentes web.

Función: recibe peticiones HTTP, crea objetos `Request` y `Response`, e invoca el servlet o la página JSP correspondiente.

Importancia: aísla al programador de escuchar en puertos y parsear HTTP manualmente, traduciendo peticiones a objetos del lenguaje.

##### 3.3.2. Gestión de sesiones y autenticación

El servidor ofrece mecanismos nativos para identificar usuarios y mantener su estado.

Sesiones: guarda datos (por ejemplo, un carrito de la compra) asociados a un usuario mediante cookies (JSESSIONID) o reescritura de URL, sin gestionar memoria manualmente.

Autenticación: proporciona **realms** para validar usuarios contra bases de datos, LDAP o ficheros planos, con seguridad declarativa (por ejemplo, en `web.xml`) en lugar de repetir lógica de login.

##### 3.3.3. Conectores y pools de conexiones

Optimiza la comunicación con sistemas externos, especialmente bases de datos.

Pool de conexiones: abrir una conexión es costoso, por lo que el servidor mantiene una piscina de conexiones listas. La aplicación pide una prestada y la devuelve al terminar.

Beneficio: mejora rendimiento y evita saturar la base de datos.

##### 3.3.4. Gestión de transacciones y mensajería

Servicios críticos para la integridad de datos en entornos empresariales.

Transacciones (JTA): agrupa operaciones en una unidad atómica. Si una falla, el servidor realiza rollback automático.

Mensajería (JMS): permite enviar mensajes a colas para procesamiento asíncrono (por ejemplo, enviar un email) sin bloquear al usuario.

##### 3.3.5. Logs, diagnóstico y monitorización

Herramientas para controlar la salud del servidor en producción.

Logs unificados: centraliza errores y eventos de todas las aplicaciones desplegadas.

JMX (Java Management Extensions): permite ver uso de memoria, usuarios activos o reiniciar servicios en caliente.

##### 3.3.6. Servicio de Nombres y Directorio (JNDI)

Es una agenda interna para localizar recursos por nombre lógico (por ejemplo, `jdbc/MiBaseDeDatos`) en lugar de direcciones IP y contraseñas en código.

Esto facilita cambiar configuraciones sin recompilar ni modificar la aplicación.

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

Después de entender el papel del servidor de aplicaciones, es clave dominar el **despliegue**: mover cambios entre entornos de trabajo hasta llegar a producción. Desplegar, de forma sencilla, sería realizar todas las operaciones necesarias para llevar una versión de una aplicación desde un entorno de desarrollo hasta el entorno de producción. Ya hemos visto en la unidad 3 cómo desplegar aplicaciones web en servidores web. También, en la unidad 1, vimos cómo GitHub Actions puede ayudarnos a automatizar el despliegue. En esta unidad vamos a profundizar en el despliegue de aplicaciones web en servidores de aplicaciones, con foco en buenas prácticas y seguridad.

#### 4.1. Qué es el despliegue y qué entornos existen

El despliegue consiste en mover cambios entre entornos de trabajo. Los más habituales son:

- **Entorno local**: donde cada persona desarrolla y prueba sus cambios.
- **Entorno de desarrollo**: integra cambios de varios miembros del equipo.
- **Entorno de preproducción**: replica el entorno real para pruebas finales.
- **Entorno de producción**: el sistema que usan las personas usuarias.

El flujo más habitual es avanzar cambios de izquierda a derecha, hasta llegar a producción.

Este modelo permite que el equipo valide los cambios en entornos cada vez más cercanos al real. Si algo falla en un entorno intermedio, se corrige antes de impactar a las personas usuarias.

<figure markdown>
  ![](../assets/deploy.png)
  <figcaption>Modelo clásico de despliegue entre entornos.</figcaption>
</figure>

#### 4.2. Pasos del proceso de despliegue

El flujo del proceso de despliegue consta de **5 pasos**: **planificación, desarrollo, pruebas, despliegue y supervisión**.

Antes de entrar en detalle, una nota importante: este flujo cubre los **aspectos fundamentales** y se presenta como una **simplificación didáctica**. No significa que sea la única forma de desplegar, sino una base clara para comprender el proceso y poder adaptarlo a cada caso.

1. **Planificación** del despliegue y sus reglas.
2. **Desarrollo** en entornos locales o de desarrollo.
3. **Pruebas** progresivas en entornos intermedios.
4. **Despliegue** en producción.
5. **Supervisión** tras el lanzamiento.

##### 4.2.1. Planificación del despliegue

Para que el proceso sea fluido, es clave contar con un **plan de despliegue** que se siga siempre. Esto ayuda a que todo se haga de la misma forma en cada cambio, especialmente cuando varias personas trabajan en el mismo proyecto.

Un plan debe definir:

- Cuando se pasa de local a desarrollo o preproducción.
- Horarios o ventanas en las que se permite desplegar a producción.
- Criterios de aceptación y responsables del despliegue.

En proyectos abiertos, un buen plan permite incluso preparar **release candidates** y dejar que la comunidad pruebe antes del lanzamiento. Además, cada cambio debe planificarse: poco para cambios pequeños y más detalle para cambios grandes.

##### 4.2.2. Desarrollo del cambio

Con el plan definido, llega el desarrollo real. Para evitar conflictos y errores, el trabajo debe hacerse en **entornos locales o de desarrollo**.

Una vez finalizado el cambio, se prepara para pasar a la siguiente fase y se integra en el flujo de despliegue previsto.

##### 4.2.3. Pruebas progresivas

Las pruebas son esenciales para evitar fallos en producción. No se pueden hacer pruebas reales sin desplegar los cambios en entornos nuevos.

Cuando el cambio funciona en local o desarrollo, se despliega al siguiente entorno y se vuelve a validar. El objetivo es llegar a **preproducción**, un entorno muy parecido al real, donde se realiza el control de calidad final.

Si se detectan errores en cualquier fase, el cambio vuelve a desarrollo, se corrige y se repite el ciclo.

##### 4.2.4. Despliegue en entorno real

Tras superar las pruebas, se despliega en producción. En teoría es un paso seguro, pero siempre puede aparecer algún problema inesperado.

Por eso es imprescindible que el despliegue se haga siguiendo el plan y con un criterio claro de vuelta atrás si algo falla.

##### 4.2.5. Supervisión y monitorización

Una vez en producción, toca **supervisar**. Hay que observar logs, comportamiento de usuarios y rendimiento del sistema para detectar incidencias.

Un buen consejo es desplegar en momentos de baja actividad y con personal disponible para reaccionar. Así se minimiza el impacto en usuarios y se puede corregir o revertir rápidamente si es necesario.

Si hay que revertir cambios, se debe actuar con calma y seguir un proceso claro, igual de riguroso que el despliegue.

Cada paso reduce el riesgo. Si se detectan fallos en un entorno intermedio, se vuelve al desarrollo y se corrige antes de afectar a producción. En despliegues grandes, la planificación incluye ventanas de despliegue, criterios de aceptación y un plan claro de rollback.

Durante las pruebas es clave verificar que la aplicación funciona en condiciones similares a producción. Esto incluye datos de ejemplo, configuraciones reales y pruebas de rendimiento básicas para detectar cuellos de botella.

#### 4.3. Tipos de despliegue

- **Metadatos**: cambios en código, plantillas o configuraciones. Disponible para desarrolladores.
- **Contenido**: textos, imágenes y recursos editables. Disponible para editores o administradores y no requiere conocimientos técnicos.

Separar ambos tipos ayuda a minimizar riesgos. El contenido suele moverse con más frecuencia y con menos impacto técnico.

#### 4.4. Ventajas de trabajar con múltiples entornos

- Reducción del riesgo en producción. Cuando tienes múltiples entornos, los errores catastróficos ocurren en un entorno seguro (Desarrollo o Pruebas) y nunca llegan al usuario final. Así debería de ser siempre.
- Ahorro de tiempo en pruebas. Tener entornos separados permite paralizar el trabajo sin bloquearse mutuamente. Cada equipo puede trabajar en su entorno sin interferir con otros.
- Mejor gestión de contenidos sensibles al tiempo. Prepara el lanzamiento antes de la fecha. En entornos como comercio electrónico o noticias, es vital probar cambios de contenido antes de publicarlos. Los entornos separados facilitan esta tarea.

Cuando los cambios pasan por varios entornos, el equipo gana control y puede detectar errores antes de que lleguen a las personas usuarias.

#### 4.5. Supervisar y reaccionar

Después de desplegar hay que **supervisar**: revisar logs, estado del servicio y respuesta del sistema. Si algo falla, es clave tener preparado un plan de **rollback** y un protocolo claro de comunicación.

Un buen despliegue no termina cuando se publica el cambio, sino cuando se confirma que el servicio responde correctamente y no hay errores en los registros. En equipos profesionales, la monitorización continua forma parte del proceso de despliegue.

!!! info "Importancia de la monitorización"
    La monitorización post-despliegue es crucial para detectar problemas que no se ven en pruebas. Un buen sistema de alertas ayuda a reaccionar rápido y minimizar el impacto en usuarios.

#### 4.6. Buenas prácticas específicas del proceso

Además de los pasos básicos, hay recomendaciones concretas que ayudan a reducir incidencias. Las desarrollamos en detalle en el **punto 5**:

- Trabajar con control de versiones y ramas.
- Probar en local antes de mover cambios.
- Revisar diferencias antes de producción.
- Definir roles y un plan de rollback.
- Elegir la mejor franja de despliegue.

Estas prácticas convierten el despliegue en un proceso predecible y repetible.

### 5. Buenas prácticas de despliegue

Cuando se trabaja con entornos de despliegue, es importante, como se ha mencionado anteriormente, tener un plan y un proceso claro en el equipo. Para ampliar ese proceso, se recogen algunas mejores prácticas recomendadas.

Se ha de tener en cuenta que las siguientes prácticas se refieren principalmente al desarrollo de software y de la web. En otros tipos de desarrollo puede haber otros factores a considerar en el flujo de trabajo.

#### 5.1. Usar control de versiones (Git)

Esto puede parecer obvio, pero tener un sistema de control de versiones es inestimable para cualquier flujo de despliegue. Sin él, es probable que se produzcan errores si se trabaja en equipo.

Incluso si eres la única persona que trabaja en un proyecto, es muy recomendable utilizar Git en caso de que necesites volver a versiones anteriores o si alguien nuevo se une al equipo.

Sin Git será difícil asegurar la consistencia en el flujo de trabajo de despliegue y puede llevar a que se cometan más errores por desplegar código inacabado o por no tener a todos los miembros del equipo trabajando en la misma versión.

#### 5.2. Trabajar en ramas

Como regla general, el equipo debería trabajar en ramas. Hacerlo permite trabajar en varias tareas al mismo tiempo sin que se afecten entre sí.

Un ejemplo es cuando se encuentra un error que debe ser corregido. Si un desarrollador está utilizando una rama para trabajar en una nueva característica, puede crear otra rama para el arreglo. De este modo, habrá dos ramas diferentes que no chocarán ni crearán posibles conflictos de fusión más adelante.

Trabajar con ramas también ayuda al equipo en preproducción: tener los cambios en ramas separadas y fusionarlas permite a quienes prueban ver con claridad qué se ha empujado y qué deben validar.

#### 5.3. Desarrollar en local antes de desplegar

Aunque es posible trabajar directamente en un entorno de desarrollo, en la mayoría de los casos se ahorra mucho tiempo trabajando localmente. Al instalar el proyecto en local, se puede trabajar de forma más eficiente y acelerar las pruebas y la verificación del código.

No hay que confirmar, subir y desplegar constantemente un cambio antes de poder verificar si funciona. Cuando algo no funciona, hay que revertirlo, subirlo de nuevo y volver a desplegar.

En lugar de eso, se puede ejecutar todo en local y, una vez que funcione, empujarlo directamente al entorno de preparación para una prueba más rigurosa.

#### 5.4. Revisar diferencias antes de producir

Una vez que el equipo de pruebas se ha asegurado de que todo funciona en el entorno de pruebas, es el momento de desplegar el código en el entorno real. Pero antes del despliegue final, es importante hacer una revisión de las diferencias entre el entorno actual en producción y el entorno de desarrollo o preproducción.

Incluso después de las pruebas exhaustivas y el control de calidad, las cosas pueden ir mal al llegar al entorno real. Una revisión final reduce la necesidad de correcciones urgentes o de una reversión completa.

#### 5.5. Limitar permisos de despliegue

Puede ser buena idea restringir quién puede desplegar en vivo. En equipos más grandes y con niveles de experiencia variados, es recomendable que solo perfiles senior desplieguen en producción.

Esto asegura un mayor nivel de control sobre el flujo de releases y significa que al menos un par de ojos senior han revisado lo que llega al entorno real. En enfoques muy iterativos puede ralentizar un poco, pero suele compensar al evitar errores.

#### 5.6. Gestionar errores y rollback

Si algo falla en producción, no hay que entrar en pánico. Antes de aplicar hotfixes o revertir, hay que comprobar si un rollback realmente arreglaría el problema.

En algunas situaciones, los cambios son irreversibles o el fallo no se debe al despliegue. Si la parte rota no estaba en la nueva versión, un rollback no ayudará. Por eso es clave tener un plan claro y mantener la calma para actuar con criterio.

#### 5.7. Escoger la mejor franja de despliegue

En caso de que algo se rompa en producción, es importante encontrar el mejor momento para desplegar. Para decidirlo, conviene responder a dos preguntas:

- ¿Cuándo hay menos usuarios activos?
- ¿Cuándo hay alguien preparado para supervisar y solucionar problemas después del despliegue?

Por lo general, se busca que el menor número de personas se vea afectado. Esto puede analizarse con herramientas de analítica para ver horas punta y horas de baja actividad, tanto por franja horaria como por días de la semana.

Muchas veces la conclusión es desplegar de noche, pero eso solo es buena idea si hay equipo disponible para reaccionar. En lugar de eso, se debe encontrar un equilibrio entre el número de usuarios activos y la disponibilidad del equipo.

Por este motivo, en muchas empresas se trabaja con guardias rotativas para asegurar disponibilidad y respuesta rápida.

!!! warning "Sin un plan, el despliegue se convierte en improvisación"
    Define responsables, horario de despliegue y protocolo de rollback. Esto reduce el impacto de incidencias en producción.

### 6. Despliegue de aplicaciones Java

El despliegue de aplicaciones JavaEE en servidores de aplicaciones es un proceso habitual en entornos empresariales. En esta sección se describen los conceptos clave y los pasos para empaquetar y desplegar aplicaciones JavaEE.

#### 6.1. Servlets y JSP

En aplicaciones JavaEE, los servlets y las páginas JSP gestionan peticiones HTTP y generan contenido dinámico.

Un servlet suele encargarse de la lógica, mientras que una JSP se centra en la presentación. En proyectos modernos, las JSP se sustituyen por frameworks, pero el concepto sigue siendo el mismo: **recibir una petición, procesarla y devolver una respuesta**.

!!! note "Servlet vs JSP"
    Un servlet es un componente Java que maneja peticiones y respuestas HTTP, mientras que una JSP es una página que combina HTML con código Java para generar contenido dinámico. **Actualmente, las JSP se usan menos en favor de frameworks más modernos.**

#### 6.2. Estructura básica de una aplicación JavaEE

Una aplicación web JavaEE suele contener:

- Directorio raíz con páginas HTML o JSP.
- Directorio `WEB-INF` con configuración y clases.
- Recursos (imágenes, CSS, JS) en la estructura necesaria.

Cada aplicación web se considera un **contexto** dentro del servidor. Este contexto define la ruta base con la que se accede a la aplicación.

#### 6.3. Empaquetamiento en WAR

El formato **WAR** es el estándar para distribuir aplicaciones web JavaEE. Se crea empaquetando el directorio de la aplicación con la herramienta `jar`.

Un WAR contiene páginas, clases compiladas, librerías y archivos de configuración, todo preparado para que el servidor lo despliegue de forma automática.

#### 6.4. Despliegue de WAR

Los servidores JavaEE permiten desplegar un WAR desde consola de administración o copiándolo en un directorio de despliegue.

En entornos reales, el despliegue suele automatizarse con pipelines (github actions) o con herramientas del propio servidor, para asegurar que el proceso sea reproducible.

#### 6.5. Herramientas de build: Maven y Gradle

En el ecosistema Java, las dos herramientas más comunes para automatizar la compilación, pruebas, empaquetado y despliegue son **Maven** y **Gradle**. Ambas resuelven problemas similares, pero con enfoques distintos.

##### 6.5.1. Maven

Maven es una herramienta open-source creada en 2001 con el objetivo de simplificar los procesos de build. Antes de Maven, compilar y generar ejecutables requería entender manualmente dependencias, librerías y pasos de compilación, lo que podía llevar desde minutos hasta horas en proyectos complejos.

Con Maven, la build de un proyecto se reduce a ejecutar un comando, por ejemplo:

```bash
mvn install
```

Maven es más que una herramienta de build: gestiona el ciclo completo del proyecto, desde validación de código hasta despliegue, incluyendo pruebas y generación de informes. Para ello, define ciclos de build con fases encadenadas. En el ciclo por defecto, las fases principales son:

- validate
- compile
- test
- package
- integration-test
- verify
- install
- deploy

Si ejecutas `mvn package`, Maven ejecutará de forma encadenada todas las fases anteriores. La configuración se define en `pom.xml` (Project Object Model), donde se declaran módulos y dependencias.

Maven facilita la gestión de dependencias gracias a repositorios remotos como **Maven Central**, desde donde se descargan automáticamente librerías y versiones necesarias.

Además, establece una estructura común de directorios, por ejemplo:

- `src/main/java`
- `src/main/resources`
- `src/test/java`

<figure markdown>
  ![](../assets/maven-logo.png)
  <figcaption>Maven y sus ciclos de build.</figcaption>
</figure>

##### 6.5.2. Gradle

Gradle es una herramienta open-source más moderna (2007) que combina la gestión de dependencias de Maven con la flexibilidad de Ant. Su configuración se hace con un **DSL** (Groovy o Kotlin) en `build.gradle`, lo que permite escribir lógica y condiciones en la propia build.

Una diferencia clave es el **Gradle Wrapper**, que permite ejecutar proyectos sin instalar Gradle en la máquina. El comando habitual es:

```bash
./gradlew build
```

Gradle no depende de un ciclo de fases rígido. Funciona con un **grafo de tareas** (tasks) y dependencias entre ellas. Aun así, con el plugin Java incluye tareas estándar similares a Maven:

- `compileJava`
- `test`
- `assemble`
- `check`

En dependencias, Gradle también usa repositorios como **Maven Central**, pero con una sintaxis más concisa y potente para gestionar conflictos de versiones.

Uno de sus puntos fuertes es el rendimiento: aplica **compilación incremental**, evitando repetir tareas si no ha cambiado el código. En proyectos grandes esto puede acelerar el build de forma notable.

Por defecto, Gradle respeta la misma estructura de directorios que Maven.

### 7. Despliegue de aplicaciones Node.js con Express

#### 7.1. Node.js

Node.js es un **entorno de ejecución** para JavaScript en el servidor. No es un lenguaje ni un framework.

Aunque dispone de módulos nativos como `http` y `fs` para manejar peticiones y servir archivos, en entornos profesionales se usan frameworks como Express (o alternativas como Fastify o NestJS) para simplificar el enrutado y los middlewares.

<figure markdown>
  ![](../assets/nodejs-new-pantone-black.svg)
  <figcaption>Node.js como entorno de ejecución.</figcaption>
</figure>

#### 7.2. Express

Express es un framework ligero que simplifica la creación de APIs y aplicaciones web en Node.js.

Se encarga del enrutado, la gestión de middlewares y la definición de endpoints, dejando al desarrollador centrarse en la lógica de negocio.

<figure markdown>
  ![](../assets/express-logo.png)
  <figcaption>Express como framework de Node.js.</figcaption>
</figure>

#### 7.3. npm y gestión de paquetes

npm es el gestor de paquetes por defecto en Node.js. Permite instalar dependencias, publicar paquetes y definir scripts.

En un despliegue real, npm ayuda a fijar versiones, reproducir instalaciones y ejecutar tareas de build o pruebas.

NPM convive con alternativas enfocadas en rendimiento y eficiencia como **Yarn**, **pnpm** o el runtime **Bun**.

<figure markdown>
  ![](../assets/npm-logo.png)
  <figcaption>npm como gestor de paquetes.</figcaption>
</figure>

Un ejemplo de `package.json` con scripts sería:

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

CI/CD es un conjunto de prácticas que automatizan integración, pruebas, distribución y despliegue.

El objetivo es reducir errores humanos y entregar cambios de forma frecuente, segura y medible.

<figure markdown>
  ![](../assets/ci-cd-flow-desktop.png)
  <figcaption>Flujo general de CI/CD.</figcaption>
</figure>

#### 8.2. Diferencias entre CI, CD y despliegue continuo

- **CI**: integra cambios frecuentes y ejecuta pruebas automatizadas.
- **CD**: distribuye artefactos listos para producción.
- **Despliegue continuo**: publica en producción sin intervención manual.

En la práctica, muchas organizaciones empiezan con CI y evolucionan a CD cuando las pruebas y los procesos son fiables.

#### 8.3. Integración continua

<figure markdown>
  ![](../assets/ci.png)
  <figcaption>Integración continua.</figcaption>
</figure>

La CI evita conflictos al integrar cambios a diario y validar con pruebas automatizadas. Así se detectan fallos temprano, antes de llegar a producción.

#### 8.4. Distribución continua

<figure markdown>
  ![](../assets/cd.png)
  <figcaption>Distribución continua.</figcaption>
</figure>

La CD automatiza la entrega de artefactos listos para desplegar en producción. El equipo de operaciones puede desplegar cuando lo considere oportuno.

#### 8.5. Implementación continua

<figure markdown>
  ![](../assets/cd2.png)
  <figcaption>Implementación continua.</figcaption>
</figure>

El despliegue continuo publica cambios automáticamente tras superar pruebas. Para que funcione, las pruebas deben ser completas y confiables.

### 9. Evidencias habituales para evaluar el RA3

- Esquemas o explicaciones del servidor de aplicaciones.
- Configuración localizada y justificada (server.xml, context.xml, etc.).
- Integración con servidor web mediante proxy o reverse proxy.
- Usuarios, roles y accesos configurados y probados.
- Aplicación desplegada y funcionando con logs correctos.
- Ajustes aplicados (puertos, rutas, variables, permisos).
- Pruebas de funcionamiento y rendimiento básicas.
- Documentación reproducible de la instalación y uso.
- Despliegue en contenedor o nube si aplica.

## Referencias y bibliografía

- [What is an application server? (I)](https://www.itpro.co.uk/strategy/29643/what-is-an-application-server)
- [What is an application server? (II)](https://www.serverwatch.com/guides/application-server/)
- [What is deployment in software and web development](https://umbraco.com/knowledge-base/deployment/)
- [Simple y rápido. Entiende qué es Maven en menos de 10 min.](https://www.javiergarzas.com/2014/06/maven-en-10-min.html)
- [Maven in 5 Minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
- [Apuntes JavaEE](http://www.jtech.ua.es/j2ee/restringido/cw/sesion01-apuntes.html)
- [Qué es Node.js y por qué debería usarlo](https://kinsta.com/es/base-de-conocimiento/que-es-node-js/)
- [Qué son la integración y la distribución continuas (CI/CD)](https://www.redhat.com/es/topics/devops/what-is-ci-cd)

## Recursos adicionales

- Documentación oficial de Apache Tomcat y WildFly.
- Guías de despliegue de Node.js en producción.
