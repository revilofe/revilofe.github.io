---
title: "UD 5 - P2: Despliegue de una API RESTful con Jakarta (Java) usando Gradle en WildFly (contenedor)"
summary: Despliegue de una API RESTful con Jakarta EE en WildFly dentro de contenedor usando Gradle.
description: Práctica guiada con WildFly en Docker, build con Gradle y despliegue del WAR.
authors:
    - Eduardo Fdez
date: 2026-01-26
icon: "material/file-document-edit"
permalink: /daw/unidad5/p5.2
categories:
    - DAW
tags:
    - WildFly
    - Gradle
    - Jakarta EE
    - REST
    - Docker
---

## P5.2 - Despliegue de una API RESTful con Jakarta (Java) usando Gradle en WildFly (contenedor)

### 1. Introducción y contexto

En esta práctica vas a desplegar una API REST con **Jakarta EE** sobre **WildFly** usando **Gradle con Kotlin DSL**, pero ejecutando el servidor en un contenedor Docker. Esto permite un entorno reproducible, limpio y rápido de levantar.

#### 1.1. REST en pocas líneas

REST (Representational State Transfer) es un estilo arquitectónico para diseñar servicios web. Usa métodos HTTP (GET, POST, PUT, DELETE) para interactuar con recursos identificados por URLs. Es simple, ligero y muy común en APIs modernas.

#### 1.2. Jakarta REST en Java

En el ecosistema Java, REST se implementa con **JAX-RS** (ahora **Jakarta RESTful Web Services**). Se trabaja con anotaciones como `@GET`, `@POST` o `@Path` para exponer endpoints que devuelven JSON.

#### 1.3. WildFly

WildFly es un servidor de aplicaciones Jakarta EE (antes JBoss AS). Es ligero, modular y muy usado en entornos empresariales. En esta práctica lo ejecutaremos dentro de un contenedor Docker.

### 2. Objetivos

- Levantar WildFly en un contenedor Docker.
- Configurar un proyecto Jakarta RESTful con Gradle.
- Generar un WAR y desplegarlo en WildFly dentro del contenedor.
- Probar la API con navegador y con `curl`.
- Revisar logs del servidor y evidenciar el despliegue.

### 3. Pasos a seguir

#### 3.1. Preparar el entorno Docker

Asegúrate de tener Docker instalado y funcionando. Comprueba la versión:

```sh
docker --version
```

Descarga la imagen oficial de WildFly:

```sh
docker pull quay.io/wildfly/wildfly:latest
```

Levanta el contenedor exponiendo los puertos 8080 (aplicaciones) y 9990 (consola):

```sh
docker run -d --name wildfly -p 8080:8080 -p 9990:9990 quay.io/wildfly/wildfly:latest
```

Comprueba que el contenedor está activo:

```sh
docker ps
```

#### 3.2. Crear usuario de administración en el contenedor

Necesitas un usuario de gestión para acceder a la consola:

```sh
docker exec -it wildfly /opt/jboss/wildfly/bin/add-user.sh
```

Selecciona usuario de gestión (Management User) y crea tu usuario y contraseña.

```
What type of user do you wish to add?
a) Management User (mgmt-users.properties)
b) Application User (application-users.properties)
(a):

Enter the details of the new user to add.
Using realm 'ManagementRealm' as discovered from the existing property files.
Username : wildfly

Password recommendations are listed below. To modify these restrictions edit the add-user.properties configuration file.
 - The password should be different from the username
 - The password should not be one of the following restricted values {root, admin, administrator}
 - The password should contain at least 8 characters, 1 alphabetic character(s), 1 digit(s), 1 non-alphanumeric symbol(s)
Password : 
Re-enter Password : 
What groups do you want this user to belong to? (Please enter a comma separated list, or leave blank for none)[  ]: 
About to add user 'wildfly' for realm 'ManagementRealm'
Is this correct yes/no? yes

About to add user 'wildfly' for realm 'ManagementRealm'
Is this correct yes/no? yes
Added user 'wildfly' to file '/opt/jboss/wildfly/standalone/configuration/mgmt-users.properties'
Added user 'wildfly' to file '/opt/jboss/wildfly/domain/configuration/mgmt-users.properties'
Added user 'wildfly' with groups  to file '/opt/jboss/wildfly/standalone/configuration/mgmt-groups.properties'
Added user 'wildfly' with groups  to file '/opt/jboss/wildfly/domain/configuration/mgmt-groups.properties'
```

Para reiniciar el contenedor si es necesario:

```sh
docker restart wildfly
```

#### 3.3. Acceder a la consola de administración del contenedor


Accede a la consola web:

`http://localhost:8080/console` o `http://localhost:9990`

pisiblemente, hayas obtenido el siguiente mensaje de error al intentar acceder a la consola de administración:

!!! warning "Error de redirección en la consola de administración de WildFly"
    Welcome to WildFly
    Unable to redirect.
    An automatic redirect to the Administration Console is not currently available. This is most likely due to the administration console being exposed over a network interface different from the one to which you are connected to.
    
    To access the Administration console you should contact the administrator responsible for this WildFly installation and ask them to provide you with the correct address.


Es necesario añadir un parámetro extra al comando `docker run` para "abrir" la consola de administración a conexiones externas (fuera del contenedor).

Por defecto, la consola de administración de WildFly solo escucha en `127.0.0.1` (localhost **dentro** del contenedor). Al intentar entrar desde tu navegador (que está fuera), WildFly rechaza la conexión o no sabe cómo redirigirte porque detecta que vienes de una IP externa.

##### 3.3.1. Solución: Exponer la interfaz de administración

Debes modificar el comando de arranque para incluir `-bmanagement 0.0.0.0`. Esto le dice a WildFly que acepte conexiones a la consola de gestión desde cualquier dirección IP.

**Pasos para corregirlo ahora mismo:**

1.  Borra el contenedor actual (si no lo has hecho ya):
    ```bash
    docker rm -f wildfly
    ```

2.  Lanza el contenedor con el comando corregido:
    ```bash
    docker run -d --name wildfly -p 8080:8080 -p 9990:9990 quay.io/wildfly/wildfly:latest /opt/jboss/wildfly/bin/standalone.sh -b 0.0.0.0 -bmanagement 0.0.0.0
    ```

!!! Note "levantar el contenedor WildFly con acceso externo a la consola"
    Los parámetros `-b 0.0.0.0` y `-bmanagement 0.0.0.0` son necesarios para poder acceder a la aplicación y a la consola desde fuera del contenedor Docker.

Ahora deberás ejecutar el punto 3.2 para crear el usuario de administración, y después podrás acceder a la consola sin problemas.

Entendido. Vamos a reforzar ese punto recuperando el nivel de detalle "práctico" de la versión anterior y combinándolo con la nueva estructura. Aquí tienes la versión definitiva, más robusta en el "Cuándo" y manteniendo la explicación del "Cómo".

***

##### 3.3.2. El corazón de WildFly: `standalone.xml`

Es fundamental entender dónde se guarda la configuración del servidor. En WildFly, el archivo maestro es **`standalone.xml`**.

Ruta dentro del contenedor:
`/opt/jboss/wildfly/standalone/configuration/standalone.xml`

**¿Qué es?**

Es el archivo XML que gobierna el comportamiento de tu servidor WildFly en modo "standalone" (una única instancia). Define todos los servicios disponibles: base de datos, seguridad, logs, servidor web, etc.

**¿Cuándo hay que modificarlo?**

Normalmente no lo tocas para despliegues básicos "Hello World", pero es **obligatorio** editarlo cuando necesitas integraciones reales. Aquí tienes los casos del día a día:

1. **Conectar una Base de Datos (Datasources):**

    Si tu aplicación necesita guardar datos en MySQL, PostgreSQL u Oracle, debes configurar aquí el **Datasource** (la URL, usuario y contraseña de la BD) y registrar el **Driver** JDBC correspondiente.

    *¿Por qué?* Para que el servidor gestione el pool de conexiones de forma eficiente y tu código solo pida "dame una conexión".

2. **Seguridad y Usuarios (Security Domains):**

    Cuando quieres que tu API solo sea accesible para ciertos usuarios o roles, o quieres conectarte a un LDAP/Active Directory corporativo para validar contraseñas.

3. **Colas de Mensajería (JMS/ActiveMQ):**

    Si tu aplicación necesita enviar o recibir mensajes asíncronos entre sistemas, aquí defines las *Queues* y *Topics* donde se guardarán esos mensajes.

4. **Ajustar Puertos e Interfaces:**

    Si necesitas cambiar el puerto por defecto (8080) porque choca con otro servicio, o quieres que el servidor escuche en una IP específica de una red interna.

5. **Logs y Depuración (Logging):**

    Para cambiar el nivel de detalle de los logs (ej. activar `DEBUG` para ver trazas SQL o errores ocultos) o decidir en qué archivo se guardan.

6. **Configuración Web (Undertow):**
    Para ajustes del servidor web interno, como aumentar el tamaño máximo de subida de archivos (imprescindible si tu app permite subir PDFs o imágenes grandes).

**¿Cómo se modifica? ¿A mano o por consola?**

Tienes tres formas de modificar esta configuración, de menos a más recomendada:

* **A mano (Edición del XML):** Paras el servidor, editas el fichero de texto y vuelves a arrancar.

    * *Riesgo:* Es fácil cometer errores de sintaxis XML que impidan que el servidor arranque. **No recomendado** para principiantes.

* **Consola de Administración Web (`/9990`):** Entras en la web de gestión.

    * *Ventaja:* Es visual, validas los datos y **no necesitas reiniciar** el servidor para la mayoría de cambios. El servidor escribe los cambios en el XML por ti automáticamente.

* **CLI (Command Line Interface):** Usando scripts de comandos (`jboss-cli`).

    * *Ventaja:* Es la forma profesional y automatizable (DevOps). Permite crear un script que configure todo automáticamente al crear el contenedor.

!!! tip "Recomendación"
    Para aprender, usa la **Consola Web**. Si te equivocas, WildFly te avisará antes de guardar. Recuerda que al estar en Docker, si eliminas el contenedor (`docker rm`), el `standalone.xml` volverá a su estado original (se pierden los cambios).

**Comando útil:**
Puedes extraer este archivo para estudiarlo en tu editor de código favorito con:
```bash
docker cp wildfly:/opt/jboss/wildfly/standalone/configuration/standalone.xml ./mi-configuracion.xml
```


#### 3.4. Preparar el proyecto con Gradle

Usaremos un proyecto base con una API REST sencilla:

https://github.com/revilofe/2526_DAW_u5.2_jakarta-wildfly-gradle

Clona el repositorio. En este caso trabajaremos con Gradle y usaremos **Kotlin DSL**, por lo que debes tener un archivo `build.gradle.kts`.

Ejemplo de configuración mínima para generar un WAR con Jakarta EE:

```kotlin
plugins {
    java
    war
}

group = "com.mycompany.myproject"
version = "0.0.1-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    // Jakarta EE 10 API (Provided porque WildFly ya lo incluye)
    compileOnly("jakarta.platform:jakarta.jakartaee-api:10.0.0")

    // JUnit 5 para tests
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.2")
}

tasks.test {
    useJUnitPlatform()
}


tasks.withType<War> {
    archiveBaseName.set("modulename.backend")
}


```

##### 3.4.1. Generar el wrapper de Gradle

Si el proyecto no incluye `gradlew`, necesitas crear el **Gradle Wrapper**. Para ello debes tener Gradle instalado en tu sistema.

Comprueba si tienes Gradle:

```sh
gradle --version
```

Si no lo tienes, en Debian puedes instalarlo con:

```sh
sudo apt update
sudo apt install gradle
```

Tanto si ya tenías instalado `gradle`, como si lo has instalado, genera el wrapper desde la raíz del proyecto ejecutando:

```sh
gradle wrapper
```

Esto crea los archivos `gradlew`, `gradlew.bat` y la carpeta `gradle/wrapper/`.

Después ya puedes usar el wrapper para evitar problemas de versión:

```sh
./gradlew --version
```

#### 3.5. Build del WAR con Gradle

Genera el WAR:

```sh
./gradlew clean build
```

El archivo se genera en:

`build/libs/modulename.backend-0.0.1-SNAPSHOT.war`

##### 3.5.1. Componentes web: artefacto web (WAR), contenedor y contexto

Acabas de generar un archivo `.war`. Este fichero es el **Componente Web** principal en Jakarta EE. Es crucial entender tres conceptos que definen cómo tu aplicación será accesible:

**1. El Contenedor Web (Undertow)**

WildFly tiene un motor interno (llamado Undertow) encargado de recibir las peticiones HTTP (puerto 8080). Su trabajo es mirar la URL que escribe el usuario y decidir a qué aplicación entregársela.

**2. El Contexto de Despliegue (Context Path)**

Es la parte de la URL que identifica a tu aplicación. Por defecto, WildFly usa el **nombre del archivo WAR** como contexto.

   * En nuestro caso, Gradle ha generado: `modulename.backend-0.0.1-SNAPSHOT.war`
   * Por tanto, la URL base será: `http://localhost:8080/modulename.backend-0.0.1-SNAPSHOT/`

Esta URL es larga y difícil de recordar. En un entorno real, querrás cambiarla.

**¿Cómo personalizamos el contexto?**

Tienes dos formas de decirle al servidor "quiero que mi app responda en `/api`":

* **Opción A (Renombrado - La rápida):** Simplemente renombra el archivo WAR antes de copiarlo. Si despliegas `api.war`, el contexto será `/api`.

* **Opción B (Configuración - La profesional):** Crear un archivo descriptor específico para WildFly en tu código fuente: `src/main/webapp/WEB-INF/jboss-web.xml`.
    
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <jboss-web>
        <context-root>/api</context-root>
    </jboss-web>
    ```
    
    Con esto, aunque tu archivo se llame `proyecto-final-v3.war`, la URL seguirá siendo limpia: `/api`.

En esta práctica, usaremos el contexto raiz definido en jboss-web.xml`.

#### 3.6. Despliegue en WildFly (contenedor)

Hay dos formas sencillas de desplegar el WAR en el contenedor. Usaremos la más directa: copiar al directorio `deployments`.

```sh
docker cp build/libs/modulename.backend-0.0.1-SNAPSHOT.war wildfly:/opt/jboss/wildfly/standalone/deployments/
```

Comprueba logs del contenedor:

```sh
docker logs -f wildfly
```

Si todo va bien, verás que el WAR se despliega automáticamente.

#### 3.7. Pruebas de la API

Siendo la siguiente URL base para la API desplegada:

`http://localhost:8080/myproject/module/backend/api/myservice`

Prueba el endpoint `hello` en el navegador:

`http://localhost:8080/myproject/module/backend/api/myservice/hello`

<figure markdown>
  ![](assets/api1.png)
  <figcaption>Respuesta del endpoint hello.</figcaption>
</figure>

Comprueba `/pojo/list`:

`http://localhost:8080/myproject/module/backend/api/myservice/pojo/list`

<figure markdown>
  ![](assets/api2.png)
  <figcaption>Respuesta JSON del endpoint /pojo/list.</figcaption>
</figure>

#### 3.8. Pruebas con curl

- Crear nueva entrada `/pojo/new`:

```sh
curl -d '{"id":"2023", "name":"Despliegue"}' -H "Content-Type: application/json" -X POST http://localhost:8080/myproject/module/backend/api/myservice/pojo/new
```

- Actualizar una entrada `/pojo/update`:

```sh
curl -d '{"id":"55", "name":"Raul"}' -H "Content-Type: application/json" -X PUT http://localhost:8080/myproject/module/backend/api/myservice/pojo/update
```

- Eliminar una entrada `/pojo/remove`:

```sh
curl -X DELETE http://localhost:8080/myproject/module/backend/api/myservice/pojo/remove?id=3
```


#### 3.9. Pruebas de Carga y Rendimiento 

Para validar que nuestro despliegue no solo "funciona", sino que es capaz de soportar tráfico real, debemos realizar una prueba de carga (*Load Testing*). Esto responde directamente al criterio de evaluación **g)** del RA3.

**¿Qué es el Load Testing?**

Su objetivo es "bombardear" tu API con peticiones simultáneas para ver cómo aguanta el servidor:
1. **Rendimiento:** Cuántas peticiones por segundo es capaz de servir.
2. **Latencia:** Cuánto tarda en responder cada una.
3. **Estabilidad:** Si el servidor explota (errores 500) bajo presión.

Existen tres herramientas estándar para esto. **Solo necesitas usar UNA de ellas** para la práctica. Elige la que más te guste:

##### 3.9.1. Opción 1: `ab` (ApacheBench) - El clásico
Viene instalado en casi todos los Linux/Mac y es muy estándar. Es antiguo, pero perfecto para pruebas rápidas y sencillas.

* **Instalación:**

    ```bash
    sudo apt install apache2-utils
    ```

* **Comando típico:**

    ```bash
    ab -n 1000 -c 10 http://localhost:8080/modulename.backend-0.0.1-SNAPSHOT/api/myservice/hello
    ```
  
    * `-n 1000`: Lanza **1000 peticiones** en total.
    * `-c 10`: Mantiene **10 usuarios simultáneos** (concurrencia).
  
* **Qué mirar en el resultado:**

    * `Requests per second`: Cuanto más alto, mejor (ej: 2500 [#/sec]).
    * `Failed requests`: Debería ser 0.

##### 3.9.2. Opción 2: `hey` - La moderna

Es la versión moderna de `ab`. Escrita en Go, soporta HTTP/2 y tiene una salida visual mucho más bonita y fácil de leer. **Recomendada si quieres algo visual.**

* **Instalación:**

    * Opción rápida (si tienes snap): `sudo snap install hey`
    * Opción manual: Descargar el binario desde su [GitHub](https://github.com/rakyll/hey).

* **Comando típico:**
 
    ```bash
    hey -n 1000 -c 10 http://localhost:8080/modulename.backend-0.0.1-SNAPSHOT/api/myservice/hello
    ```

* **Qué mirar:**

    * Te muestra un histograma de barras con los tiempos de respuesta.
    * Busca `Status code distribution`: `[200] 1000 responses` (Todo OK).

##### 3.9.3. Opción 3: `wrk` - La bestia

Usa scripts en Lua y multihilo real. Es capaz de generar cargas brutales que tumbarían a las otras herramientas antes que al servidor. Se usa para benchmarks profesionales de alto rendimiento.

* **Instalación:**

    ```bash
    sudo apt install wrk
    ```

* **Comando típico:**

    ```bash
    wrk -t4 -c100 -d10s http://localhost:8080/modulename.backend-0.0.1-SNAPSHOT/api/myservice/hello
    ```

    * `-t4`: Usa 4 hilos de tu CPU.
    * `-d10s`: Machaca el servidor durante **10 segundos** sin parar (sin límite de peticiones totales).
  
* **Qué mirar:**

    * `Latency`: Tiempo medio de respuesta.
    * `Req/Sec`: Peticiones por segundo.

##### 3.9.4. Ejemplo de análisis real (Caso con `ab`)

A continuación, mostramos una salida real de ejecución correcta y cómo debes interpretarla en tu informe.

**Comando ejecutado:**
```bash
ab -n 1000 -c 10 http://localhost:8080/myproject/module/backend/api/myservice/pojo/list
```

**Salida obtenida:**
```text
Server Software:        
Server Hostname:        localhost
Server Port:            8080

Document Path:          /myproject/module/backend/api/myservice/pojo/list
Document Length:        51 bytes

Concurrency Level:      10
Time taken for tests:   1.219 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      178000 bytes
HTML transferred:       51000 bytes
Requests per second:    820.47 [#/sec] (mean)
Time per request:       12.188 [ms] (mean)
Time per request:       1.219 [ms] (mean, across all concurrent requests)
Transfer rate:          142.62 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:     2   12  10.6      9      94
Waiting:        2   11  10.2      8      94
Total:          2   12  10.6      9      94
```

!!! tip "Cómo interpretar los resultados de la prueba de carga"
    En esta prueba se lanzaron 1000 peticiones al endpoint `/pojo/list` con una concurrencia de 10 usuarios simultáneos.
    1. **Estado de la respuesta:**
        `Failed requests: 0` y ausencia de `Non-2xx responses`. Esto confirma que el servidor respondió correctamente (HTTP 200) a las 1000 peticiones. Además, el `Document Length` es 51 bytes, lo que indica que estamos recibiendo datos (el JSON).
    2. **Rendimiento (Throughput):**
        `Requests per second: 820.47`. El contenedor Docker es capaz de servir unas **820 peticiones por segundo**. Es un buen rendimiento para un entorno de desarrollo en local.
    3. **Latencia:**
        `Time per request: 12.188 ms`. En promedio, cada usuario espera unos **12 ms** por respuesta.
         Mirando los percentiles (`99% 66 ms`), vemos que incluso en los peores casos la respuesta es rápida (menos de 0.1 segundos).
    *Conclusión:* El despliegue es estable y rápido, procesando correctamente la carga sin errores ni cuellos de botella evidentes."

#### 3.10. Consideraciones de Seguridad para Producción

En esta práctica hemos configurado un entorno de **desarrollo**, priorizando la rapidez. Sin embargo, este despliegue **no es seguro para un entorno de producción**.

Si fueras a desplegar este servidor en Internet, tendrías que aplicar medidas que te garanticen la seguridad de la aplicación y del servidor. Aquí tienes algunas recomendaciones clave:

1. **Protección de la Gestión (Puerto 9990):**
    
    * **Nunca expongas la consola de administración a Internet.** En la práctica la hemos abierto (`-bmanagement 0.0.0.0`) por comodidad, pero en producción solo debería ser accesible desde una red privada (VPN) o tunel seguro.

2. **Cifrado de Comunicaciones (HTTPS):**
    
    * El tráfico HTTP plano es visible para cualquiera en la red. En producción es obligatorio usar **HTTPS** para cifrar los datos. Lo ideal es colocar un servidor web frontal (como Nginx) que gestione los certificados SSL y redirija todo el tráfico HTTP a HTTPS.

3. **Gestión de Secretos (Secrets):**
    
    * **Las contraseñas no van en el código.** Nunca escribas credenciales en archivos `README`, `Dockerfile` o scripts. Deben inyectarse al arrancar el contenedor usando mecanismos seguros (como Docker Secrets o variables de entorno ocultas), para que no queden huellas en el repositorio Git.

4. **Auditoría y Logs Centralizados:**
    
    * Si un contenedor se borra, sus logs desaparecen. Para investigar incidentes de seguridad, debes configurar el servidor para enviar los logs en tiempo real a un sistema externo y persistente. Si te atacan, los logs son tu única "caja negra".

5. **Hardening (Endurecimiento) del Contenedor:**
    
    * **Mínimos privilegios:** Evita que el contenedor corra como usuario `root`.
    * **Solo lectura:** Configura el sistema de archivos del contenedor como "read-only" siempre que sea posible. Esto impide que un atacante que logre entrar pueda descargar herramientas de hacking, modificar la configuración del servidor o instalar puertas traseras (*backdoors*).

!!! security "Seguridad en Docker"
    Recuerda: Un contenedor seguro es aquel que tiene lo mínimo necesario para funcionar y nada más. Cuantos menos permisos, puertos y archivos modificables tenga, menor será el daño en caso de ataque.


### 4. Ejercicios

1. Despliega la aplicación, siguiendo esta guía, desde el repositorio:

    https://github.com/revilofe/2526_DAW_u5.3_jakarta-wildfly-gradle-otra
    
    Estúdiala en profundidad y realiza los pasos necesarios para levantarla en tu entorno local (Docker + Gradle).

    Ten en cuenta que puedes tener las dos aplicaciones en el mismo contenedor (cambiando el nombre del WAR y el contexto) o en contenedores separados.

2. Adjunta una captura de `docker ps` mostrando el contenedor `wildfly` activo.
3. Adjunta evidencia de despliegue en logs (`docker logs -f wildfly`).
4. Realiza llamadas a la app y adjunta evidencias y sus respuestas (navegador y `curl`).

## Referencias

- [Primer despliegue](https://github.com/revilofe/2526_DAW_u5.2_jakarta-wildfly-gradle)
- [Segundo despliegue](https://github.com/revilofe/2526_DAW_u5.3_jakarta-wildfly-gradle-otra)
- https://www.wildfly.org/
- https://quay.io/repository/wildfly/wildfly
- https://docs.gradle.org/current/userguide/war_plugin.html
