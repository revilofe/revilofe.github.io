---
title: "UD 5 - P3: Informe RA3 sobre el despliegue (WildFly contenedor + Gradle)"
summary: Informe de evidencias y preguntas RA3 a partir de la práctica P5.2.
description: Práctica de consolidación. Responde 1 pregunta por criterio (a-i) sobre tu despliegue de P5.2 en WildFly dentro de contenedor, justificando con evidencias.
authors:
    - Eduardo Fdez
date: 2026-01-28
icon: "material/file-document-edit"
permalink: /daw/unidad5/p5.3
categories:
    - DAW
tags:
    - RA3
    - WildFly
    - Gradle
    - Jakarta EE
    - Docker
    - Despliegue
---

## P5.3 - Informe RA3 sobre el despliegue (WildFly contenedor + Gradle)

### 1. Introducción

En la **P5.2** desplegaste una API RESTful de Jakarta EE en **WildFly** dentro de un **contenedor Docker**, generando el artefacto con **Gradle** y verificando el funcionamiento con navegador y `curl`.

En esta práctica, vas a consolidar lo aprendido respondiendo a varias preguntas. La clave no es “contestar por contestar”, sino **justificar** con evidencias del despliegue que ya hiciste
en la P5.2.

https://github.com/revilofe/2526_DAW_u5.3_jakarta-wildfly-gradle-otra

### 2. Objetivos

- Consolidar los conocimientos vistos en la práctica P5.2.
- Explicar configuración, seguridad y pruebas con evidencias verificables.
- Documentar el proceso para que otra persona pueda reproducirlo.

### 3. Entregables

Entrega un documento llamado `P5.3-informe-ra3.md` que incluya:

- Las respuestas a las **9 preguntas** (a-i).
- Evidencias (capturas, logs o salidas de comandos) junto a cada respuesta.

!!! tip "Evidencias mínimas recomendadas"
    - `docker ps` y `docker logs`
    - Copia del comando `docker cp` del WAR (o alternativa usada)
    - URL(s) probadas y salida de `curl`
    - Ejecución de comando de prueba de rendimiento (ab/hey/wrk) y resultado
    - Rutas internas del contenedor cuando apliquen

### 4. Pasos a seguir

#### 4.1. Reúne evidencias de la P5.2

Recupera (o vuelve a generar) evidencias de:

1. Contenedor WildFly levantado (`docker ps`).
2. Puertos publicados (8080 y 9990).
3. Despliegue del WAR (logs de WildFly).
4. Pruebas funcionales con navegador y con `curl`.

#### 4.2. Estructura tu informe

Ordena el informe en 9 apartados, uno por criterio, y en cada punto indica que has hecho para contestar al punto, y que evidencia aportas para justificarlo. Luego, adjunta lo hecho y la evidencia (comandos, logs, capturas, URLs, etc.) que lo respalde.

- **a)** Descripción de componentes y funcionamiento.
- **b)** ...
- **c)** ...
- **d)** ...
- **e)** ...
- **f)** ...
- **g)** ...
- **h)** ...
- **i)** ...

### 5. Ejercicios (1 pregunta por criterio)

Responde a **una** pregunta por criterio. Todas las respuestas deben referirse al [último despliegue planteado en la **P5.2** (WildFly en contenedor + Gradle)](https://github.com/revilofe/2526_DAW_u5.3_jakarta-wildfly-gradle-otra) y aportar evidencias.

#### a) Componentes y funcionamiento de los servicios del servidor

Explica qué componentes/servicios intervienen en tu despliegue de P5.2 y qué papel tiene cada uno (como mínimo: contenedor Docker, WildFly, aplicación WAR,puertos 8080/9990 y endpoint REST). Ten en cuenta el punto c) sobre el servidor web frontal.

Describe el flujo de una petición desde el cliente hasta tu endpoint.

**Evidencias típicas**

- `docker ps` mostrando el contenedor y los puertos publicados.
- `docker logs -f wildfly` mostrando el despliegue y el acceso.
- Respuesta del endpoint (`curl`).

#### b) Archivos principales de configuración y bibliotecas compartidas

Identifica dentro de WildFly (en el contenedor) el/los archivo(s) de configuración principal(es) que gobiernan el servidor y señala:

1. Dónde están (ruta).
2. Qué tipo de ajustes podrías tocar ahí para tu despliegue.

Además, explica qué dependencias de tu proyecto se consideran “provided” porque el servidor ya las incluye, y qué ventaja tiene esto.

**Evidencias típicas**

- Captura/salida de `docker exec -it wildfly ls .../standalone/configuration`.
- Fragmento del `build.gradle.kts` donde se ve `compileOnly`.

#### c) Cooperación con el servidor web (proxy / reverse proxy) y https

En P5.2 accediste directamente a WildFly por `localhost:8080`. Imagina ahora un entorno real donde hay un **servidor web frontal** (por ejemplo, Nginx) delante de WildFly.

Plantea una configuración de reverse proxy para tu despliegue de P5.2 que:

- Publique la API bajo una ruta clara (por ejemplo `/api/`).
- No exponga el puerto 9990 hacia fuera.

Incluye un ejemplo de configuración (fragmento) y explica qué cambia respecto a tu despliegue actual.

Realiza una configuración de TLS (HTTPS) en el servidor web frontal y explica qué ventajas aporta esto. ¿Cambiaría algo en tu aplicación o en la configuración de WildFly?

**Evidencias típicas**

- Fragmento de `nginx.conf` o `sites-enabled`.
- Explicación de qué puertos publicarías en Docker y cuáles no.
- Como has configurado TLS (certificados, etc.) y qué ventajas aporta.


#### d) Mecanismos de seguridad del servidor de aplicaciones

Indica qué medidas de seguridad aplicaste en P5.2 y qué medidas añadirías para producción (mínimo 4), justificando cada una. Debes cubrir al menos:

- Consola de administración (9990) y credenciales.
- Exposición de puertos.
- Gestión de secretos (usuarios/contraseñas).
- Registro y trazabilidad (logs).

**Evidencias típicas**

- Captura de puertos expuestos.
- Captura de que la consola solo es accesible internamente.
- Ejemplo de política de secretos.

#### e) Componentes web del servidor de aplicaciones

Explica cómo se “engancha” tu aplicación REST a WildFly en P5.2:

- Qué es el WAR y qué contiene a alto nivel.
- Qué significa el contexto/ruta base de la app.
- Qué parte del servidor se encarga de servir la API (contenedor web).

Incluye una URL real de tu práctica y desglósala (host, puerto, contexto, ruta del recurso).

**Evidencias típicas**

- URLs probadas en navegador/curl. 
- Log del servidor mostrando el acceso.

#### f) Parámetros necesarios para el despliegue

Enumera y justifica los parámetros que fueron necesarios en tu despliegue de P5.2 (mínimo 5), por ejemplo:

- Parámetros de `docker run` (nombre, puertos, etc.).
- Nombre del WAR y ruta de despliegue.
- Variables o ajustes del build (Gradle).

Explica qué pasaría si uno de esos parámetros estuviera mal.

#### g) Pruebas de funcionamiento y rendimiento

Describe qué pruebas funcionales hiciste en P5.2 y aporta evidencias.

Además, ejecuta una prueba de rendimiento básica (elige una):

- `ab` (ApacheBench)
- `hey`
- `wrk`

Incluye el comando utilizado, el endpoint probado y un breve análisis del resultado (latencia, peticiones/segundo o errores).


**Evidencias típicas**

- Salida completa de `ab`/`hey`/`wrk` y análisis.
- Logs durante la prueba.

#### h) Documentación de administración y recomendaciones

RECOMIENDO, hacer antes el punto i) y luego redactar esta sección con lo aprendido.

Redacta una mini-guía de administración para tu despliegue de P5.2 que incluya:

1. Cómo levantar WildFly.
2. Cómo desplegar una nueva versión del WAR.
3. Cómo comprobar el estado (logs y endpoint de prueba).
4. Recomendaciones para evitar errores comunes.

Debe ser reproducible para otra persona del equipo.

**Evidencias típicas**

Manual con instrucciones claras y paso a paso, acompañado de:
- Ficheros Docker: dockerfile y compose.
- Arquitectura de desplieuge
- Comandos clave (docker, despliegue, pruebas).
- URLs de prueba.
- Acceso a logs y endpoints.
- Pruebas de funcionamiento.
- Pruebas de rendimiento.
- Recomendaciones de seguridad.

#### i) Virtualización, nube o contenedores en el despliegue

Realiza un despliegue haciendo uso de docker compose que auné todo. Servidor web (Nginx) + servidor de aplicaciones (WildFly) + tu aplicación REST.

Ten en cuenta volúmenes para logs, secretos, healthchecks y reinicio automático, limitación de recursos, redes, etc.

Una mejora adicional, sería separar frontend y backend en contenedores distintos, con comunicación entre ellos, y no exponer el backend directamente al host.

