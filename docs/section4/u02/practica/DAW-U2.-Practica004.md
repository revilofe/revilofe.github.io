---
title: "UD 2 - P4: Despliegue de Tomcat con Nginx como proxy inverso"
description: "Despliegue de aplicación Java con servidor de aplicaciones y proxy inverso"
summary: "Actividad práctica para desplegar una aplicación Java en Tomcat utilizando Nginx como proxy inverso con Docker."
authors:
    - Eduardo Fdez
date: 2025-01-12
icon: 
permalink: /daw/unidad2/p2.4
categories:
    - DAW
tags:
    - Docker
    - Tomcat
    - Nginx
    - Proxy inverso
    - Java
    - Bind mount
---

## Relación 2.4

### Descripción

**Actividad:** *Despliegue de Tomcat con Nginx como proxy inverso*

En esta práctica desplegarás una aplicación Java en un **servidor de aplicaciones Tomcat** y configurarás **Nginx como proxy inverso** para acceder a ella. Esta arquitectura es muy común en entornos de producción, ya que permite separar las responsabilidades: Nginx maneja las peticiones HTTP y las redirige al servidor de aplicaciones.

#### Objetivo general

Aprender a:

- Desplegar aplicaciones Java en servidores de aplicaciones (Tomcat).
- Configurar Nginx como proxy inverso.
- Utilizar bind mount para montar archivos de configuración y aplicaciones.
- Comprender la arquitectura de múltiples capas en aplicaciones web.
- Trabajar con archivos WAR (Web Application Archive).
- Entender el flujo de peticiones en una arquitectura con proxy inverso.

---

### Contexto de trabajo

En esta arquitectura utilizaremos dos componentes principales:

**1. Servidor de aplicaciones Tomcat:**

- Servidor de aplicaciones Java que ejecuta aplicaciones web empaquetadas en formato WAR.
- Escucha en el puerto 8080/tcp por defecto.
- Directorio de despliegue: `/usr/local/tomcat/webapps/`
- Imagen Docker: `tomcat:9.0`

**2. Servidor web Nginx (Proxy inverso):**

- Actúa como punto de entrada para las peticiones HTTP.
- Recibe peticiones en el puerto 80 y las redirige a Tomcat.
- Se configura mediante archivos de configuración en `/etc/nginx/conf.d/`
- Imagen Docker: `nginx`

**Flujo de peticiones:**

```
Cliente → Nginx (puerto 80) → Tomcat (puerto 8080) → Aplicación Java
```

---

### 🔹 Parte 1: Preparación del entorno

#### Tarea 1.1: Obtención de recursos

1. Crea un directorio de trabajo para esta práctica, por ejemplo `~/tomcat_practica`.

2. Descarga o crea un archivo WAR de ejemplo. Puedes:
   
    - Descargar `sample.war` desde el repositorio del curso
    - Utilizar cualquier aplicación WAR simple que tengas disponible
    - Crear una aplicación Java básica y empaquetarla como WAR

3. Investiga la estructura básica de un archivo de configuración de Nginx para proxy inverso.

4. Crea un archivo de configuración de Nginx llamado `default.conf` que debe incluir:
   
    - Servidor que escucha en el puerto 80
    - Configuración de `location /` con proxy_pass
    - El proxy_pass debe apuntar al contenedor de Tomcat (puerto 8080)
    - Debe incluir el nombre de la aplicación en la ruta
    - Gestión de páginas de error (500, 502, 503, 504)
    
    **Nota:** Usa placeholders (como NOMBRE_CONTENEDOR_TOMCAT y NOMBRE_APLICACION) que luego sustituirás por los valores reales.

5. Verifica que tienes ambos archivos:
   
    - `sample.war` (o el nombre de tu aplicación WAR)
    - `default.conf`

#### Tarea 1.2: Creación de la red

1. Crea una red Docker personalizada llamada `red_tomcat` para la comunicación entre los contenedores.

2. Verifica que la red se ha creado correctamente.

---

### 🔹 Parte 2: Despliegue del servidor Tomcat

#### Tarea 2.1: Despliegue básico de Tomcat

1. Despliega un contenedor de Tomcat con las siguientes características:
   
    - Nombre del contenedor: `aplicacionjava`
    - Conectado a la red `red_tomcat`
    - Bind mount del archivo WAR desde el host al directorio de despliegue de Tomcat
    - Montaje en modo solo lectura (`:ro`)
    - **NO mapees puertos** (el acceso será solo interno a través de Nginx)
    - Ejecutando en modo daemon

2. Verifica que el contenedor está en ejecución.

3. Inspecciona los logs del contenedor para verificar que la aplicación se ha desplegado correctamente.

4. Accede al contenedor y verifica que el archivo WAR está en el directorio de despliegue.

5. Comprueba que la aplicación se ha desplegado automáticamente (Tomcat descomprime el WAR).

---

### 🔹 Parte 3: Configuración y despliegue de Nginx

#### Tarea 3.1: Configuración del proxy inverso

1. Revisa y completa el archivo `default.conf` con la configuración correcta:
   
    - Sustituye `NOMBRE_CONTENEDOR_TOMCAT` por el nombre real de tu contenedor de Tomcat
    - Sustituye `NOMBRE_APLICACION` por el nombre de tu aplicación (sin la extensión .war)
    - Asegúrate de que la directiva `proxy_pass` apunta correctamente

2. Comprende qué hace cada directiva de la configuración:
   
    - `listen`: Puerto en el que escucha Nginx
    - `server_name`: Nombre del servidor
    - `location /`: Configuración del proxy inverso
    - `proxy_pass`: Dirección a la que se redirigen las peticiones

#### Tarea 3.2: Despliegue de Nginx

1. Despliega un contenedor de Nginx con las siguientes características:
   
    - Nombre del contenedor: `proxy`
    - Puerto 80 del host mapeado al puerto 80 del contenedor
    - Conectado a la red `red_tomcat`
    - Bind mount del archivo `default.conf` al directorio de configuración de Nginx
    - Montaje en modo solo lectura (`:ro`)
    - Ejecutando en modo daemon

2. Verifica que el contenedor está en ejecución.

3. Inspecciona los logs de Nginx para verificar que no hay errores de configuración.

#### Tarea 3.3: Verificación del despliegue

1. Accede a la aplicación desde tu navegador web (http://localhost).

2. Verifica que la aplicación Java se muestra correctamente.

3. Comprueba que estás accediendo a través de Nginx (puerto 80) y no directamente a Tomcat.

---

### 🔹 Parte 4: Análisis de la arquitectura

#### Tarea 4.1: Flujo de peticiones

1. Analiza el flujo completo de una petición HTTP:
   
    - ¿Qué componente recibe primero la petición del navegador?
    - ¿Cómo sabe Nginx dónde redirigir la petición?
    - ¿Por qué funciona la resolución del nombre del contenedor de Tomcat?
    - ¿Qué respuesta envía Tomcat de vuelta?

2. Realiza pruebas de conectividad:
   
    - Desde el contenedor Nginx, intenta hacer ping al contenedor de Tomcat
    - Desde el contenedor Nginx, verifica que puedes acceder al puerto 8080 de Tomcat

#### Tarea 4.2: Bind mount vs volúmenes

1. Compara el uso de bind mount en esta práctica con los volúmenes usados en prácticas anteriores:
   
    - ¿Cuándo es más apropiado usar bind mount?
    - ¿Cuándo es mejor usar volúmenes nombrados?
    - ¿Qué ventajas y desventajas tiene cada enfoque?

2. Verifica en el host la ubicación de los archivos montados con bind mount.

---

### 🔹 Parte 5: Configuración avanzada

#### Tarea 5.1: Modificación de la configuración de Nginx

1. Investiga qué cabeceras HTTP adicionales puede configurar un proxy inverso para mejorar la funcionalidad.

2. Modifica el archivo `default.conf` para añadir dentro de `location /`:
   
    - Cabecera `Host` con el valor del host original
    - Cabecera `X-Real-IP` con la IP real del cliente
    - Cabecera `X-Forwarded-For` con las IPs de proxies intermedios
    - Cabecera `X-Forwarded-Proto` con el protocolo usado
    
    **Pista:** Investiga las directivas `proxy_set_header` de Nginx y las variables disponibles.

3. Investiga qué comando permite recargar la configuración de Nginx sin detener el contenedor.

4. Aplica los cambios y verifica que funcionan correctamente.

#### Tarea 5.2: Acceso directo a Tomcat

1. Recrea el contenedor de Tomcat exponiendo el puerto 8080 al host.

2. Accede directamente a Tomcat desde tu navegador (http://localhost:8080/sample).

3. Compara el acceso directo con el acceso a través del proxy:
   
    - ¿Qué diferencias observas en las URLs?
    - ¿Qué cabeceras HTTP son diferentes?

4. Reflexiona sobre por qué en producción no se suele exponer directamente Tomcat.

#### Tarea 5.3: Múltiples aplicaciones

1. Si tienes múltiples archivos WAR, despliega más de una aplicación en Tomcat.

2. Configura Nginx para que cada aplicación sea accesible en rutas diferentes:
   
    - `/app1/` → aplicacion1.war
    - `/app2/` → aplicacion2.war

---

### 🔹 Parte 6: Análisis y documentación

#### Tarea 6.1: Preguntas de análisis

Responde a las siguientes preguntas en tu documentación:

1. **Proxy inverso:**
   
    - ¿Qué es un proxy inverso y para qué sirve?
    - ¿Qué ventajas aporta Nginx como proxy inverso frente al acceso directo a Tomcat?
    - ¿Qué otros usos tiene Nginx además de proxy inverso?

2. **Arquitectura de capas:**
   
    - ¿Por qué separar el servidor web del servidor de aplicaciones?
    - ¿Qué componente debería manejar contenido estático (imágenes, CSS, JS)?
    - ¿Cómo se podría añadir balanceo de carga en esta arquitectura?

3. **Tomcat y aplicaciones Java:**
   
    - ¿Qué es un archivo WAR?
    - ¿Cómo despliega Tomcat las aplicaciones WAR?
    - ¿Por qué el nombre del directorio desplegado coincide con el nombre del archivo WAR?

4. **Bind mount:**
   
    - ¿Por qué en esta práctica usamos bind mount en lugar de volúmenes?
    - ¿Qué ventajas tiene montar archivos en modo solo lectura (`:ro`)?
    - ¿Qué pasa si modificas el archivo de configuración en el host?

5. **Seguridad:**
   
    - ¿Por qué no exponemos directamente el puerto de Tomcat al exterior?
    - ¿Qué medidas de seguridad adicionales implementarías?
    - ¿Cómo configurarías HTTPS en esta arquitectura?

6. **Comparación con prácticas anteriores:**
   
    - ¿En qué se diferencia esta arquitectura de las anteriores?
    - ¿Qué tienen en común con la aplicación Temperaturas (microservicios)?
    - ¿Cuál de todas las prácticas representa mejor un entorno de producción real?

#### Tarea 6.2: Comandos utilizados

Documenta todos los comandos Docker utilizados para:

- Crear la red
- Desplegar y gestionar el contenedor de Tomcat
- Desplegar y gestionar el contenedor de Nginx
- Verificar logs y estado de los contenedores
- Inspeccionar la configuración de red
- Recargar la configuración de Nginx

---

## Entregables

1. **Documentación en formato Markdown o PDF** que incluya:
   
    - Todos los comandos utilizados en cada tarea
    - Archivo de configuración `default.conf` completo y explicado
    - Capturas de pantalla que demuestren:
        - La aplicación funcionando a través del proxy
        - Lista de contenedores en ejecución
        - Inspección de la red Docker
        - Logs de Tomcat mostrando el despliegue de la aplicación
        - Logs de Nginx
        - Acceso directo a Tomcat (si realizas la tarea 5.2)
        - Estructura de directorios con bind mounts
    - Diagrama del flujo de peticiones (cliente → Nginx → Tomcat)
    - Respuestas detalladas a todas las preguntas de análisis
    - Comparación con las prácticas anteriores

2. **Archivos de configuración:**
   
    - `default.conf` - Configuración de Nginx


---

### Evaluación

Se evaluará:

- La correcta configuración del proxy inverso.
- El funcionamiento completo de la aplicación a través de Nginx.
- La comprensión del flujo de peticiones.
- El uso apropiado de bind mount.
- La profundidad del análisis de la arquitectura.
- La claridad y completitud de la documentación.
- La comparación crítica entre diferentes arquitecturas.

---

### Condiciones de entrega

Las publicadas en la plataforma Moodle del curso.

---

### Recursos de apoyo

- Documentación oficial de Docker: [https://docs.docker.com](https://docs.docker.com)
- Imagen Tomcat en Docker Hub: [https://hub.docker.com/_/tomcat](https://hub.docker.com/_/tomcat)
- Imagen Nginx en Docker Hub: [https://hub.docker.com/_/nginx](https://hub.docker.com/_/nginx)
- Documentación de Tomcat: [https://tomcat.apache.org/tomcat-9.0-doc/](https://tomcat.apache.org/tomcat-9.0-doc/)
- Documentación de Nginx: [https://nginx.org/en/docs/](https://nginx.org/en/docs/)
- Nginx como proxy inverso: [https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)
- Bind mounts en Docker: [https://docs.docker.com/storage/bind-mounts/](https://docs.docker.com/storage/bind-mounts/)
- Repositorio con ejemplos: [https://github.com/josedom24/curso_docker_ies](https://github.com/josedom24/curso_docker_ies)

---

### Presentación de la práctica

[:fontawesome-solid-file-pdf: Descargar presentación](https://revilofe.github.io/slides/section4-daw/DAW-U2.4.-Tomcat.html){ .md-button }
