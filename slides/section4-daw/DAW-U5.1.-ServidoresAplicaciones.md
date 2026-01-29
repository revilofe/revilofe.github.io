# DAW-U5.1 - Servidores de aplicaciones

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" -->

---

## Índice

Note: En esta presentación vamos a ver, paso a paso, qué es un **servidor de
aplicaciones**, cómo encaja en una arquitectura web, y cómo se **despliegan**
aplicaciones de forma segura. El objetivo es que el alumnado entienda el
enfoque del **RA3**: implantar, configurar con seguridad, probar y documentar.


### Índice I

- 5.1. Servidores de aplicaciones (contexto y objetivo)
- 1. RA3 y criterios de evaluación
- 2. Concepto y papel del servidor de aplicaciones
- 3. Servidor web vs servidor de aplicaciones

Note: En esta primera parte ubicamos el tema: venimos de ver **HTTP** y
**servidores web**, y ahora damos el salto al servidor de aplicaciones. Luego
aterrizamos el **RA3** y pasamos al núcleo: definición, terminología y por qué
se usa. Cerraremos con el flujo de peticiones y la comparación entre capas.


### Índice II

- 4. Despliegue: entornos, proceso y tipos
- 5. Buenas prácticas de despliegue
- 6. Despliegue de aplicaciones Java (WAR, Maven, Gradle)
- 7. Despliegue Node.js con Express (npm)
- 8. CI/CD en el despliegue moderno
- 9. Evidencias típicas para evaluar el RA3

Note: En esta segunda parte conectamos el servidor de aplicaciones con el
trabajo real: **despliegues** por entornos, buenas prácticas y ejemplos en
**Java** y **Node.js**. Terminamos con **CI/CD** para automatizar, y con la
lista de **evidencias** que suelen pedirse para demostrar el RA3.

---

## 5.1. Servidores de aplicaciones

Note: Abrimos la unidad 5.1. Venimos de la unidad 3, donde ya trabajamos la
base de arquitecturas web, **HTTP/HTTPS** y servidores web. Aquí damos un paso
más: el **servidor de aplicaciones** como pieza clave para ejecutar lógica,
aplicar seguridad, gestionar sesiones y desplegar de forma profesional.


### Contexto y objetivo de la unidad

- Partimos de servidores web y HTTP/HTTPS (unidad 3)
- Añadimos el servidor de aplicaciones como capa de negocio
- Enfoque práctico: configuración, seguridad y pruebas
- Meta: servicio estable, seguro y escalable

Note: Esta unidad busca que el alumnado vea el servidor de aplicaciones como
una capa que aporta **servicios comunes**: sesiones, seguridad, recursos,
transacciones o logs. La idea clave es separar responsabilidades: el servidor
web sirve estático y hace de frontal; el servidor de aplicaciones **procesa**
la lógica de negocio y se integra con la base de datos.

---

## 1. Resultado de aprendizaje y criterios de evaluación (RA3)

Note: En esta sección conectamos el temario con la evaluación. El **RA3** pide
que el alumnado sea capaz de **implantar** una aplicación en un servidor de
aplicaciones, **configurar** con seguridad, **probar** y **documentar** el
proceso. Esto guía qué vamos a practicar y qué evidencias se piden.


### RA3: qué se espera del alumnado

- Implantar aplicaciones web en un servidor de aplicaciones
- Configurar el servidor con criterios de **seguridad**
- Ajustar parámetros y verificar el despliegue
- Documentar administración y recomendaciones

Note: Cuando decimos RA3, hablamos de un ciclo completo: no es solo "subir un
archivo". Implica entender componentes del servidor, tocar configuración,
activar medidas de **seguridad**, comprobar que funciona y dejar una
documentación que permita repetir la instalación sin improvisar.


### 1.1. Criterios de evaluación asociados I

- a) Componentes y funcionamiento de servicios
- b) Ficheros de configuración y librerías compartidas
- c) Cooperación con servidor web (proxy / reverse proxy)
- d) Mecanismos de seguridad del servidor de aplicaciones
- e) Componentes web del servidor (contenedor, etc.)

Note: Estos criterios son la "lista de comprobación" del RA3. Primero,
conocemos qué piezas tiene el servidor y cómo funcionan (**a**). Luego, dónde
se configura (**b**), cómo se integra con el servidor web (**c**), y qué
seguridad hay que activar (**d**). También se valora usar correctamente los
componentes web del servidor (**e**).


### 1.1. Criterios de evaluación asociados II

- f) Parámetros necesarios para el despliegue
- g) Pruebas de funcionamiento y rendimiento
- h) Documentación y recomendaciones de administración
- i) Despliegue con virtualización, nube o contenedores

Note: La segunda parte del RA3 mira lo operativo. Ajustar parámetros (**f**)
puede ser puertos, rutas, variables o permisos. Probar (**g**) no es solo
"abre": también rendimiento básico. Documentar (**h**) es clave para
reproducibilidad. Y desplegar en **contenedores** o nube (**i**) acerca el
trabajo a entornos reales.

---

## 2. Concepto y papel del servidor de aplicaciones

Note: Aquí definimos qué es un servidor de aplicaciones y por qué se usa. La
idea principal: es un **middleware** entre el cliente y los datos que aporta
servicios comunes para que la aplicación no los reimplemente una y otra vez.


### 2.1. Definición y ubicación en la arquitectura

- Plataforma software para **ejecutar** aplicaciones web
- Aporta sesiones, seguridad, transacciones, recursos y logs
- Suele ubicarse entre servidor web y base de datos

![Arquitectura](assets/application-server1.webp) <!-- .element height="20%" -->

Note: Un servidor de aplicaciones es un entorno donde corre nuestra app y que
añade servicios de infraestructura. Se coloca entre el servidor web y la base
de datos para procesar peticiones dinámicas y ejecutar la **lógica de negocio**
de forma controlada. Fijaos en la separación de capas: cada una tiene su rol.


### 2.2. Terminología básica

| Término           | Idea clave               |
|-------------------|--------------------------|
| Servidor web      | Estático + HTTP/HTTPS    |
| Cliente web       | Navegador o app          |
| HTTPS             | Canal cifrado            |
| JSON              | Intercambio de datos     |
| Lógica de negocio | Reglas del dominio       |
| Aplicación        | Presenta y consume datos |
<!-- .element.table: style="font-size:70%;" -->

Note: Esta tabla nos da vocabulario común. **Servidor web** suele servir
estático y actuar como frontal. El **cliente** pide recursos. **HTTPS** es
cifrado y autenticidad del canal. **JSON** es el formato típico en APIs. La
**lógica de negocio** son reglas del dominio. Y la **aplicación** orquesta y
presenta datos al usuario.


### 2.3. Por qué necesitamos servidores de aplicaciones

- El servidor web optimiza estático; lo dinámico requiere más servicios
- Ejecuta la **lógica de negocio** de forma centralizada
- Gestiona sesiones, usuarios y recursos compartidos
- Aporta transacciones, mensajería, logs y seguridad avanzada

Note: La clave es distinguir **servir** de **procesar**. El servidor web es
rápido para HTML, CSS, imágenes y proxy. Cuando hay lógica, sesiones o acceso
a datos, el servidor de aplicaciones aporta mecanismos listos: sesiones,
pools de conexiones, transacciones y mejores herramientas de seguridad y logs.


### 2.4. Optimización del tráfico y seguridad

- Separa tráfico estático del dinámico
- Filtra peticiones antes de tocar datos sensibles
- Permite controles más estrictos en la capa de negocio

![Capa de control](assets/serv_apl.png) <!-- .element height="20%" -->

Note: Al separar capas, protegemos mejor la parte sensible. El frontal puede
hacer caché, limitar tasa y terminar TLS, y el servidor de aplicaciones puede
centrarse en validación, autorización y reglas del negocio. Esta separación
mejora rendimiento y reduce superficie de ataque, porque el acceso a datos
queda más controlado.


### 2.5. Componentes y servicios habituales

- Contenedor web: servlets, JSP o frameworks equivalentes
- Conectores: entrada de peticiones desde web o cliente
- Motor: ejecuta la lógica de negocio
- Sesiones: estado del usuario entre peticiones
- Recursos: pools de conexiones, colas, etc.
- Logs y diagnóstico: auditoría, trazas y errores

Note: Aunque cada producto cambia nombres, suelen repetirse estas piezas.
En Tomcat, por ejemplo, aparecen conceptos como **Service**, **Connector**,
**Engine**, **Host** y **Context**. Comprender estas piezas ayuda a describir
componentes y funcionamiento (criterio **a** del RA3).


### 2.6. Tendencias actuales

- Migración a **cloud** y contenedores
- Aplicaciones distribuidas con cambios frecuentes
- Necesidad de despliegues reproducibles y automatizados
- Seguridad como parte del proceso, no como añadido final

Note: Hoy el servidor de aplicaciones se usa mucho en entornos cloud y
contenedores. Además, con equipos que publican a menudo, necesitamos
**automatización** y control: versiones, pipelines, pruebas y configuración.
La seguridad debe estar integrada desde el principio: credenciales, permisos,
auditoría y prácticas de despliegue seguras.

---

## 3. Funcionamiento general en una arquitectura web

Note: En esta sección vemos el flujo de peticiones y qué aporta un servidor de
aplicaciones en la práctica. Compararemos servidor web y servidor de
aplicaciones, definiremos **servlet**, y revisaremos la lista de servicios
comunes que diferencian un servidor "empresarial" de un contenedor mínimo.


### 3.1. Servidor aplicaciones: Flujo 

- Web recibe HTTP: estático responde; dinámico reenvía
- Servidor de aplicaciones crea Request/Response y ejecuta servlet
- El servlet consulta datos o aplica lógica de negocio
- La respuesta vuelve al servidor web y se entrega al cliente

![Capas](assets/capas.webp) <!-- .element height="20%" -->

Note: El flujo típico separa responsabilidades. El servidor web decide si
responde con estático o si envía al backend. El servidor de aplicaciones
transforma la petición y ejecuta el componente que genera la respuesta (por
ejemplo, un **servlet**). La lógica de negocio y el acceso a datos ocurren en
la capa adecuada y la respuesta vuelve al frontal para entregarse al cliente.


### 3.2. Servidor web vs servidor de aplicaciones

| Aspecto  | Web             | Aplicaciones            |
|----------|-----------------|-------------------------|
| Enfoque  | HTTP + estático | Lógica dinámica         |
| Recursos | Bajo            | Alto (runtime)          |
| Soporta  | proxy, balanceo | sesiones, transacciones |
<!-- .element.table: style="font-size:70%;" -->

Note: En escenarios reales se suelen usar **ambos**: el servidor web como
frontal y el servidor de aplicaciones como backend. El web es muy eficiente
en concurrencia y contenido estático, y además actúa de **reverse proxy**.
El de aplicaciones consume más porque incluye runtime y servicios, pero
aporta capacidades avanzadas para aplicaciones dinámicas.


### Definición clave: Servlet

- Programa Java en el contenedor web del servidor de aplicaciones
- Genera contenido dinámico bajo demanda
- Usa hilos ligeros (no un proceso por petición)

Note: Un **servlet** es un componente Java que vive dentro del contenedor web.
Lo importante es el modelo: el servidor no crea un proceso por petición, sino
que atiende múltiples solicitudes con **hilos**. Esto mejora rendimiento y
permite controlar el ciclo de vida del componente de forma gestionada.


### 3.3. Servicios comunes del servidor de aplicaciones

- En entornos simples se usa lo mínimo para "arrancar y responder"
- Si recortamos demasiado, faltan servicios empresariales críticos
- Diferencia: servidor real (WildFly) vs contenedor básico (Tomcat)

Note: Esta lista es muy importante: define qué esperamos de un servidor de
aplicaciones "de verdad". En un proyecto pequeño puede bastar lo mínimo,
pero en producción echas de menos servicios como transacciones, pools,
autenticación integrada o alta disponibilidad. Por eso conviene dominar esta
lista de referencia con enfoque profesional.


### 3.3.1. Contenedor web (Servlets, JSP)

- Gestiona ciclo de vida de componentes web
- Traduce HTTP a objetos Request y Response
- Invoca el servlet o la JSP adecuada

Note: El **contenedor web** es el motor que nos evita "reinventar HTTP".
Recibe la petición, crea **Request/Response** y llama al componente. Esto
da estructura y seguridad: no estamos escuchando puertos a mano ni parseando
cabeceras. Además controla el ciclo de vida y recursos del lado servidor.


### 3.3.2. Gestión de sesiones y autenticación

- Mantiene estado de usuario (sesión) sin gestionar memoria manualmente
- Cookies (p. ej., JSESSIONID) o reescritura de URL
- Realms: validación contra BD, LDAP o ficheros

Note: La **sesión** permite guardar estado (por ejemplo, carrito) entre
peticiones. El servidor gestiona identificadores como **JSESSIONID** y la
expiración. En autenticación, los **realms** permiten validar usuarios contra
distintas fuentes y aplicar seguridad declarativa (por ejemplo, en `web.xml`)
sin copiar lógica de login por toda la aplicación.


### 3.3.3. Conectores y pools de conexiones

- Conectores: puerta de entrada y conexión con el frontal
- Pool: conexiones a BD preparadas para reutilizar
- Mejora rendimiento y evita saturar la base de datos

Note: Abrir conexiones a base de datos es caro. Por eso se usa un **pool**:
el servidor mantiene conexiones listas, la app pide una, la usa y la devuelve.
Esto reduce latencia y evita agotar el servidor de BD. Los conectores, además,
gestionan la entrada de tráfico y la integración con el servidor web.


### 3.3.4. Gestión de transacciones y mensajería

- JTA: unidad atómica con commit o rollback automático
- JMS: colas para tareas asíncronas (ej.: enviar emails)
- Evita bloquear al usuario en trabajos largos

Note: Las **transacciones** aseguran integridad: si algo falla, se hace
**rollback**. En sistemas reales es crucial para datos consistentes. La
mensajería (JMS) separa procesos: en lugar de hacer todo en la petición HTTP,
se manda a una cola y se procesa después, mejorando experiencia y escalado.


### 3.3.5. Logs, diagnóstico y monitorización

- Logs unificados para todas las apps desplegadas
- Auditoría de eventos, errores y accesos
- JMX: métricas, memoria, usuarios, reinicios en caliente

Note: En producción, lo que no se mide, no se controla. Un servidor de
aplicaciones centraliza **logs** y facilita auditoría. Con **JMX** podemos ver
uso de memoria, hilos, sesiones activas y hacer acciones operativas. La idea
es detectar problemas antes de que afecten al usuario y reaccionar rápido.


### 3.3.6. Servicio de nombres y directorio (JNDI)

- Referencia recursos por nombre lógico (ej.: `jdbc/MiBD`)
- Evita credenciales y endpoints en el código
- Cambios de configuración sin recompilar

Note: **JNDI** es como una agenda: en vez de hardcodear IPs y contraseñas en la
aplicación, pedimos un recurso por nombre lógico. Esto mejora seguridad y
mantenibilidad: podemos cambiar la base de datos o credenciales con una
configuración del servidor, sin tocar el código ni recompilar.


### 3.3.7. Alta disponibilidad (clustering)

- Varios nodos trabajan como un único servicio
- Replicación de sesión para tolerar caídas
- Reduce impacto de fallos y facilita escalado

Note: El **clustering** aporta disponibilidad: si un nodo cae, otro sigue.
Con **replicación de sesión**, el usuario no pierde estado al cambiar de nodo.
Esto es clave en servicios con alta demanda o que no pueden caer. También
ayuda a escalar horizontalmente y planificar mantenimiento con menos impacto.


### 3.3.8. Servicios web y remoting (SOAP/REST/RMI)

- Exponer y consumir APIs entre sistemas
- Integración en arquitecturas distribuidas
- Base para comunicación entre aplicaciones y servicios

Note: Un servidor de aplicaciones suele incluir mecanismos para publicar y
consumir servicios remotos. Esto permite integrar sistemas: aplicaciones que
hablan con otras a través de **REST** o **SOAP**, o tecnologías de remoting.
En arquitecturas distribuidas es una capacidad central, no un extra.


### 3.4. Separación de responsabilidades

- Web: estático, caché y frontal de entrada
- Aplicaciones: escalado independiente del backend
- Seguridad específica en la capa de negocio
- Balanceo y redundancia sin tocar el frontal

Note: Separar capas nos da flexibilidad. Podemos escalar el servidor de
aplicaciones sin cambiar el frontal. Podemos aplicar reglas de seguridad y
autorización en la capa de negocio. Y podemos poner balanceadores y
redundancia en el backend manteniendo estable la entrada del sistema.

---

## 4. Despliegue de aplicaciones web

Note: Ahora pasamos del "qué es" al "cómo se opera". Desplegar es mover una
versión de una aplicación desde desarrollo hasta producción, siguiendo un
proceso. Aquí veremos entornos, pasos, tipos de despliegue y por qué la
monitorización y el rollback son parte del despliegue, no algo opcional.


### 4.1. Qué es el despliegue y qué entornos existen

- Local: desarrollo y pruebas individuales
- Desarrollo: integra cambios del equipo
- Preproducción: replica producción para validación
- Producción: sistema real para personas usuarias

![Entornos](assets/deploy.png) <!-- .element height="20%" -->

Note: El despliegue mueve cambios por entornos, normalmente de izquierda a
derecha. La idea clave: validar en entornos cada vez más parecidos al real.
Si algo falla en un entorno intermedio, se corrige antes de impactar a las
personas usuarias. Esto reduce el riesgo y mejora la calidad del servicio.


### 4.2. Pasos del proceso de despliegue

- 5 pasos: planificación, desarrollo, pruebas, despliegue, supervisión
- Es una simplificación didáctica, no la única forma
- Cada paso reduce riesgo antes de llegar a producción

Note: El modelo de 5 pasos es una guía clara. No es la única forma de trabajar
en empresas, pero ayuda a entender el flujo. Lo importante es el principio:
no saltamos directamente a producción. Planificamos, desarrollamos, probamos,
desplegamos y, finalmente, supervisamos para confirmar que todo va bien.


### 4.2.1. Planificación del despliegue

- Definir cuándo se pasa entre entornos
- Marcar ventanas y horarios de despliegue
- Acordar criterios de aceptación y responsables
- Preparar release candidates en proyectos abiertos

Note: Sin un plan, el despliegue se convierte en improvisación. Aquí definimos
reglas: cuándo sube a preproducción, quién despliega y en qué horario. En
proyectos grandes, incluso se preparan **release candidates** para que se
prueben antes. Un cambio pequeño puede tener plan ligero; uno grande necesita
más detalle y coordinación.


### 4.2.2. Desarrollo del cambio

- Trabajar en local o en entornos de desarrollo
- Evitar conflictos y errores en el entorno real
- Preparar el cambio para integrarlo en el flujo

Note: El desarrollo debe ocurrir en entornos controlados. Así evitamos tocar
producción sin querer y reducimos errores. Una vez terminado el cambio, se
prepara para pasar a la siguiente fase, integrándose en el flujo definido por
el equipo. La idea es que el paso a pruebas sea ordenado y trazable.


### 4.2.3. Pruebas progresivas

- No hay pruebas reales sin desplegar en entornos nuevos
- Validar y avanzar hacia preproducción
- Si falla, volver a desarrollo y repetir el ciclo

Note: Las pruebas progresivas son el "filtro" que evita incidentes en
producción. Cuando algo funciona en local, se prueba en el siguiente entorno.
El objetivo es llegar a **preproducción**, muy parecida a producción. Si se
detecta un fallo, se vuelve a desarrollo, se corrige y se repite. Es un ciclo
controlado, no un salto de fe.


### 4.2.4. Despliegue en entorno real

- Tras pruebas, se despliega en producción
- Puede aparecer un problema inesperado
- Imprescindible seguir el plan y tener vuelta atrás

Note: Aunque hayamos probado, producción siempre tiene riesgo: tráfico real,
datos reales y situaciones no previstas. Por eso el despliegue debe seguir el
plan y tener un criterio de **rollback**. La mentalidad es: desplegar es un
proceso repetible, no un acto heroico. Se prioriza seguridad y control.


### 4.2.5. Supervisión y monitorización

- Revisar logs, comportamiento de usuarios y rendimiento
- Desplegar en baja actividad y con personal disponible
- Revertir con calma siguiendo un proceso claro

Note: El despliegue no termina al "publicar". Termina cuando confirmamos que
el servicio responde y los logs están limpios. Se recomienda desplegar en
momentos de baja actividad y con equipo listo para reaccionar. Si hay que
revertir, se hace con calma y siguiendo el procedimiento, igual de riguroso
que el despliegue en sí.


### 4.3. Tipos de despliegue

- Metadatos: código, plantillas, configuración (equipo dev)
- Contenido: textos e imágenes (roles editor / admin)
- Separar ambos minimiza riesgos y acelera cambios de contenido

Note: No todo despliegue es igual. Cambiar **código** o configuración suele
tener más riesgo y requiere perfiles técnicos. Cambiar **contenido** puede
ser más frecuente y lo puede hacer otro rol. Separar estos flujos reduce
incidencias: evitamos tocar software cuando solo queríamos actualizar textos
o recursos, y ganamos agilidad en publicaciones.


### 4.4. Ventajas de trabajar con múltiples entornos

- Errores graves ocurren en entornos seguros, no en producción
- Pruebas paralelas sin bloquearse entre equipos
- Lanzamientos sensibles al tiempo con validación previa

Note: Tener varios entornos mejora control. Los fallos "catastróficos" deberían
ocurrir en desarrollo o pruebas, no frente al usuario. Además, equipos pueden
trabajar en paralelo sin interferirse. Y en casos como comercio electrónico o
noticias, permite preparar contenido y lanzarlo con confianza en la fecha.


### 4.5. Supervisar y reaccionar

- Revisar logs, estado del servicio y respuesta del sistema
- Plan de rollback y protocolo de comunicación
- La monitorización continua forma parte del despliegue

Note: Supervisar es revisar indicadores y logs para detectar problemas que no
aparecieron en pruebas. Si falla algo, necesitamos **rollback** y también
comunicación: quién informa, a quién, y qué mensajes se trasladan. Un buen
despliegue termina cuando confirmamos estabilidad. En entornos profesionales,
la monitorización y alertas son parte del proceso continuo.


### 4.6. Buenas prácticas específicas del proceso

- Control de versiones y ramas
- Probar en local antes de mover cambios
- Revisar diferencias antes de producción
- Definir roles y un plan de rollback
- Elegir la mejor franja de despliegue

Note: Estas prácticas convierten el despliegue en algo **predecible** y
repetible. Las veremos en detalle en el punto 5, pero fijaos en la idea:
todo lo que reduce improvisación reduce incidentes. Versionado, pruebas,
revisiones, roles claros y buena ventana de despliegue son pilares básicos.

---

## 5. Buenas prácticas de despliegue

Note: Ahora bajamos a recomendaciones concretas. Estas prácticas se aplican
principalmente al desarrollo de software y web, pero el enfoque general sirve
para cualquier entorno: trabajar con control, reducir errores, y poder volver
atrás. Vamos punto por punto para que el alumnado pueda aplicarlas.


### 5.1. Usar control de versiones (Git)

- Imprescindible para trabajar en equipo
- Permite volver a versiones anteriores con seguridad
- Aporta consistencia al flujo de despliegue

Note: Git no es un "extra": es la base para desplegar sin caos. En equipo,
evita pisarse y permite revisar cambios. Incluso trabajando en solitario,
sirve para volver atrás cuando algo sale mal o cuando se incorpora alguien al
proyecto. Sin control de versiones, aumentan errores y despliegues de código
inacabado.


### 5.2. Trabajar en ramas

- Varias tareas en paralelo sin interferencias
- Facilita arreglos de bugs sin frenar nuevas features
- Mejora la validación en preproducción (qué se sube y qué se prueba)

Note: Las **ramas** separan trabajos. Si aparece un bug urgente, se crea una
rama para el arreglo sin mezclar con una feature. Además, en preproducción,
tener cambios separados ayuda a validar: se ve claramente qué se ha fusionado
y qué hay que probar. Esto reduce conflictos y hace el flujo más ordenado.


### 5.3. Desarrollar en local antes de desplegar

- Más rápido iterar y verificar cambios
- Evita desplegar continuamente para probar
- Cuando funciona en local, se pasa a pruebas más rigurosas

Note: Trabajar en local ahorra tiempo. Si probamos directamente en desarrollo,
acabamos en un ciclo lento: subir, desplegar, ver que falla, revertir, repetir.
En local podemos ejecutar, depurar y validar rápido. Cuando el cambio funciona,
entonces se empuja al siguiente entorno para una prueba más seria.


### 5.4. Revisar diferencias antes de producir

- Comparar producción vs preproducción antes del paso final
- Reduce correcciones urgentes y despliegues de emergencia
- Último filtro tras QA y pruebas exhaustivas

Note: Antes de desplegar a producción conviene revisar diferencias. Aunque
hayamos probado mucho, el último paso puede fallar por configuración, datos o
detalles del entorno real. Una revisión final reduce la necesidad de hotfixes
urgentes o un rollback completo. Es un hábito de equipos maduros.


### 5.5. Limitar permisos de despliegue

- Restringir quién puede desplegar en producción
- En equipos grandes, despliegue por perfiles senior
- Aumenta control sobre releases (aunque pueda ralentizar)

Note: Limitar permisos no es desconfianza: es control. En producción el coste
de un error es alto, así que suele desplegar personal con experiencia o con
doble revisión. En equipos muy iterativos puede ralentizar, pero compensa al
evitar incidentes. Lo importante es que haya un proceso claro y auditable.


### 5.6. Gestionar errores y rollback

- No entrar en pánico: analizar antes de actuar
- Un rollback no siempre arregla el problema
- Tener plan claro y actuar con criterio

Note: Si falla algo, lo peor es improvisar. Primero se analiza si el fallo se
debe al despliegue o a otra causa. Hay cambios irreversibles, y si lo roto no
estaba en la nueva versión, el rollback no ayudará. Por eso es clave tener un
plan y mantener la calma. **Rollback** es una herramienta, no la única salida.


### 5.7. Escoger la mejor franja de despliegue

- Menos usuarios activos
- Equipo disponible para supervisar y arreglar
- Equilibrio: no sirve "de noche" si nadie puede reaccionar

Note: Elegir la franja es una decisión de impacto. Queremos minimizar usuarios
afectados y, a la vez, asegurar que hay equipo para responder. Muchas empresas
hacen guardias rotativas para cubrir despliegues. La idea clave: desplegar
cuando el riesgo es menor y hay capacidad de reacción, no solo "por costumbre".

---

## 6. Despliegue de aplicaciones Java

Note: En entornos empresariales, JavaEE y servidores de aplicaciones han sido
históricamente muy comunes. Aquí vemos conceptos y pasos: componentes web
(servlets/JSP), estructura, empaquetado **WAR**, despliegue y herramientas de
build como **Maven** y **Gradle** para automatizar y hacer reproducible.


### 6.1. Servlets y JSP

- Servlets: lógica de negocio y control de peticiones
- JSP: capa de presentación (HTML + Java)
- Hoy se usan menos JSP, pero el concepto se mantiene

Note: En JavaEE, el servlet suele encargarse de la lógica y la JSP de la vista.
Aunque hoy se usan frameworks que sustituyen JSP, el patrón sigue siendo el
mismo: **recibir una petición**, procesarla y devolver una respuesta. Es clave
entender la separación de responsabilidades dentro de la aplicación web.


### 6.2. Estructura básica de una aplicación JavaEE

- Raíz: páginas HTML o JSP
- `WEB-INF`: configuración y clases
- Recursos: imágenes, CSS y JavaScript
- Cada app es un **contexto** con una ruta base

Note: La estructura JavaEE tiene convenciones. `WEB-INF` es especial: no se
sirve directamente al cliente y guarda configuración y clases. La aplicación
se despliega como un **contexto**, que define la ruta base (por ejemplo,
`/miapp`). Entender estructura y contexto ayuda a configurar y desplegar sin
errores, y conecta con los criterios de configuración del RA3.


### 6.3. Empaquetamiento en WAR

- WAR: estándar para distribuir aplicaciones web JavaEE
- Se crea empaquetando el directorio con `jar`
- Incluye páginas, clases, librerías y configuración

Note: Un **WAR** es un paquete listo para desplegar. Contiene todo lo
necesario: clases compiladas, librerías, recursos y ficheros de configuración.
La ventaja es la portabilidad: el servidor puede desplegarlo de forma
automática y consistente. Es el formato típico en servidores como Tomcat.


### 6.4. Despliegue de WAR

- Consola de administración o directorio de despliegue
- En entornos reales: automatizar con pipelines
- Objetivo: proceso reproducible y controlado

Note: Desplegar un WAR puede ser tan simple como copiarlo a un directorio
monitorizado o usar una consola web. En la práctica profesional, se integra
en pipelines (por ejemplo, GitHub Actions) o herramientas del servidor, para
evitar pasos manuales y garantizar que el despliegue siempre sigue el mismo
proceso y deja trazabilidad.


### 6.5. Herramientas de build: Maven y Gradle

- Automatizan compilación, pruebas, empaquetado y despliegue
- Resuelven dependencias y estandarizan estructura
- Diferentes enfoques: ciclos (Maven) vs tareas (Gradle)

Note: Maven y Gradle atacan el mismo problema: hacer el build reproducible.
Ambas gestionan dependencias, ejecutan pruebas y generan artefactos. Maven se
organiza por **fases** del ciclo; Gradle por un **grafo de tareas**. Elegir
una u otra depende del proyecto, pero lo importante es entender conceptos.


### 6.5.1. Maven

- Comando típico: `mvn install` o `mvn package`
- Ciclo por fases: validate, compile, test, package, install, deploy
- Configuración en `pom.xml`
- Dependencias desde repos (ej.: Maven Central)

![Maven](assets/maven-logo.png) <!-- .element height="20%" -->

Note: Maven simplifica builds complejas. Con un comando ejecuta fases en orden.
Si hacemos `mvn package`, Maven ejecuta fases previas automáticamente. La
configuración vive en `pom.xml`, donde declaramos módulos y dependencias.
Maven descarga librerías desde repos como **Maven Central**, asegurando
versiones y consistencia. También fija estructura típica de directorios.


### 6.5.2. Gradle

- Configuración con DSL en `build.gradle` (Groovy o Kotlin)
- Wrapper: ejecutar sin instalar Gradle (`./gradlew build`)
- Modelo por tareas: `test`, `assemble`, `check`, etc.
- Compilación incremental para mejorar rendimiento

Note: Gradle es más moderno y flexible. El **Wrapper** es clave: garantiza que
todo el equipo usa la misma versión. Su modelo es un grafo de tareas, lo que
permite builds eficientes. Además, usa compilación **incremental**: si no hay
cambios, evita repetir trabajo. En dependencias también usa repos como Maven
Central y suele respetar la misma estructura de directorios que Maven.

---

## 7. Despliegue de aplicaciones Node.js con Express

Note: No todo servidor de aplicaciones es "Java". En el mundo JavaScript,
Node.js actúa como entorno de ejecución en servidor. Para aplicaciones web,
se suele usar **Express** (u otros frameworks) y se gestiona todo con `npm`.
Esto conecta con despliegue moderno y con proyectos fullstack.


### 7.1. Node.js

- Entorno de ejecución de JavaScript en servidor
- No es un lenguaje ni un framework
- Módulos nativos: `http`, `fs`, etc.
- En profesional: frameworks como Express, Fastify o NestJS

![Node.js](assets/nodejs-new-pantone-black.svg) <!-- .element height="20%" -->

Note: Node.js permite ejecutar JavaScript fuera del navegador. Importante:
no es un framework. Trae módulos para HTTP o ficheros, pero en proyectos
reales se usa un framework para enrutado y middlewares. También existen
alternativas a Express como Fastify o NestJS, según necesidades del equipo.


### 7.2. Express

- Framework ligero para APIs y apps web
- Simplifica rutas y middlewares
- Permite centrarse en la lógica de negocio

![Express](assets/express-logo.png) <!-- .element height="20%" -->

Note: Express reduce "trabajo repetitivo": define rutas, middlewares,
controladores y estructura. Así el equipo se centra en la **lógica de negocio**
y en buenas prácticas de la API. En despliegue, esto ayuda a tener un servidor
consistente, con logging, seguridad y validaciones en puntos centralizados.


### 7.3. npm y gestión de paquetes

- Gestor de paquetes por defecto en Node.js
- Instala dependencias y fija versiones
- Define scripts de build, lint, test y empaquetado
- Alternativas: Yarn, pnpm, y runtime Bun

![npm](assets/npm-logo.png) <!-- .element height="20%" -->

Note: `npm` es clave para despliegues reproducibles: fija dependencias con
lockfiles y permite automatizar tareas con scripts. Un `package.json` suele
tener scripts como **build**, **lint**, **test** y un "all" que encadena todo.
También existen Yarn o pnpm por rendimiento, y Bun como runtime alternativo.

---

## 8. CI/CD en el despliegue moderno

Note: La automatización conecta todo lo anterior. CI/CD reduce errores humanos
y hace que entregar cambios sea frecuente y seguro. Aquí veremos concepto,
diferencias entre CI, CD y despliegue continuo, y qué requisitos hacen falta
para automatizar sin romper producción.


### 8.1. Concepto general

- Automatiza integración, pruebas, distribución y despliegue
- Reduce errores humanos
- Entrega cambios frecuente, segura y medible

![CI/CD](assets/ci-cd-flow-desktop.png) <!-- .element height="20%" -->

Note: CI/CD es un conjunto de prácticas, no una herramienta concreta. La idea
es que cada cambio pase por una cadena automatizada: compilar, probar,
empaquetar y preparar despliegue. Esto reduce errores manuales, mejora
trazabilidad y permite entregar con más frecuencia y con métricas claras.


### 8.2. CI, CD y despliegue continuo

- CI: integración frecuente y pruebas automáticas
- CD: entrega de artefactos listos para producción
- Despliegue continuo: publica en producción automáticamente

Note: Diferenciad conceptos. **CI** asegura que integrar cambios no rompe el
proyecto: pruebas y validación constante. **CD** deja artefactos preparados
para desplegar cuando el equipo decida. El **despliegue continuo** va más allá:
si pasa pruebas, se despliega solo. Muchas empresas empiezan con CI y maduran
hacia CD cuando el proceso es fiable.


### 8.3. Integración continua (CI)

- Integrar cambios a diario o con alta frecuencia
- Ejecutar pruebas automatizadas en cada integración
- Detectar fallos temprano, antes de producción

![CI](assets/ci.png) <!-- .element height="20%" -->

Note: La CI reduce conflictos y sorpresas. Integrar frecuentemente evita que
una rama se quede descolgada semanas. Cada push ejecuta pruebas, linters y
checks. Así detectamos fallos cuando aún son baratos de arreglar. Es una
práctica de calidad y de colaboración en equipo.


### 8.4. Distribución continua (CD)

- Automatiza la entrega de artefactos
- Listos para desplegar cuando operaciones lo decida
- Reduce pasos manuales y errores en releases

![CD](assets/cd.png) <!-- .element height="20%" -->

Note: En CD, el objetivo es tener un artefacto listo: un WAR, una imagen
Docker, un paquete, etc. No siempre se despliega automáticamente, pero el
equipo puede hacerlo con confianza cuando toque. Esto mejora control del
release y reduce dependencia de pasos manuales que suelen introducir errores.


### 8.5. Despliegue continuo (Continuous Deployment)

- Publica en producción tras superar pruebas
- Requiere pruebas completas y confiables
- Aporta velocidad, pero exige mucha madurez

![Deploy](assets/cd2.png) <!-- .element height="20%" -->

Note: El despliegue continuo automatiza hasta producción. Su beneficio es
rapidez, pero el requisito es duro: **pruebas fiables** y cobertura suficiente.
Si las pruebas son flojas, automatizar puede romper producción más rápido.
Por eso muchas organizaciones hacen CI primero, luego CD, y solo algunas
dan el salto a despliegue continuo en todos los sistemas.

---

## 9. Evidencias habituales para evaluar el RA3

Note: Cerramos con lo que normalmente se pide para demostrar el RA3. Son
evidencias prácticas: esquemas, configuración, integración con servidor web,
seguridad, logs, pruebas y documentación. La idea es que el alumnado pueda
probar que sabe implantar y administrar, no solo explicar teoría.


### 9. Evidencias RA3 I

- Esquema del servidor de aplicaciones
- Configuración localizada (server.xml, context.xml, etc.)
- Integración con servidor web (proxy / reverse proxy)
- Usuarios, roles y accesos configurados y probados
- App desplegada con logs correctos

Note: Estas evidencias cubren comprensión y ejecución. Un esquema demuestra
arquitectura. La configuración localizada y explicada (server.xml, context.xml)
demuestra criterio **b**. La integración con servidor web valida criterio **c**.
Usuarios y roles prueban seguridad (**d**). Y logs correctos muestran operación
real y capacidad de diagnóstico en despliegue.


### 9. Evidencias RA3 II

- Ajustes: puertos, rutas, variables, permisos
- Pruebas de funcionamiento y rendimiento básicas
- Documentación reproducible de instalación y uso
- Despliegue en contenedor o nube si aplica

Note: Aquí entran los aspectos operativos. Ajustes concretos prueban criterio
**f**. Las pruebas de funcionamiento y rendimiento conectan con **g**. La
documentación reproducible es clave para **h**: que otra persona pueda repetir
instalación sin depender de memoria o improvisación. Y desplegar en contenedor
o nube demuestra criterio **i** y madurez del proceso.

---

## Recursos de consulta

Note: Para terminar, dejamos recursos para ampliar. Hay una fuente principal
de apoyo, varias referencias para conceptos (servidores de aplicaciones,
despliegue, Maven, Node.js y CI/CD) y recursos adicionales recomendados para
profundizar, como documentación oficial de servidores y guías de producción.


### Fuente

- Material base: "Tema 3 - Servidores de aplicaciones" (R. del Río)

Note: Esta unidad se apoya en un material de referencia sobre servidores de
aplicaciones. Conviene usarlo como lectura complementaria para reforzar
conceptos y ver ejemplos adicionales. Recordad: las referencias ayudan, pero
en clase priorizamos comprender y aplicar en prácticas del RA3.


### Referencias y bibliografía

- Servidores de aplicaciones: ITPro y ServerWatch
- Despliegue: guía de Umbraco (conceptos)
- Maven: guía rápida y docs oficiales
- Node.js: explicación y motivación de uso
- CI/CD: guía de Red Hat (enfoque DevOps)

Note: Estas referencias cubren los pilares del tema. Para servidor de
aplicaciones hay artículos introductorios. Para despliegue hay una guía
conceptual. Para Maven, una lectura rápida y documentación oficial. Para
Node.js, una explicación de qué es y por qué usarlo. Y para CI/CD, un recurso
de DevOps muy completo. Son buenos puntos de partida para ampliar.


### Recursos adicionales

- Documentación oficial de Apache Tomcat y WildFly
- Guías de despliegue de Node.js en producción

Note: Los recursos adicionales son los que usaremos en prácticas reales.
Tomcat y WildFly tienen documentación extensa sobre configuración, seguridad y
despliegue. Para Node.js, las guías de producción enseñan temas como variables
de entorno, logging, procesos y seguridad. La recomendación es usarlos cuando
surjan dudas concretas durante el despliegue y la administración.
