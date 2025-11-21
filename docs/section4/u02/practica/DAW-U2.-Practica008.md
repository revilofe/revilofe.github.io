---
title: "UD 2 - P8: Despliegue de Tomcat con Nginx usando Docker Compose"
description: "Automatización del despliegue de Tomcat con proxy inverso Nginx usando Docker Compose"
summary: "Actividad práctica para desplegar aplicación Java con Tomcat y Nginx como proxy inverso utilizando Docker Compose y bind mounts."
authors:
    - Eduardo Fdez
date: 2025-01-12
icon: 
permalink: /daw/unidad2/p2.8
categories:
    - DAW
tags:
    - Docker
    - Docker Compose
    - Tomcat
    - Nginx
    - Proxy inverso
    - Java
---

## Relación 2.8

### Descripción

**Actividad:** *Despliegue de Tomcat con Nginx usando Docker Compose*

En esta práctica retomarás el despliegue de **Tomcat con Nginx como proxy inverso** de la Práctica 2.4, pero utilizando **Docker Compose** para simplificar la gestión de archivos de configuración y aplicaciones mediante bind mounts.

#### Objetivo general

Aprender a:

- Desplegar arquitecturas de proxy inverso con Docker Compose.
- Gestionar archivos de configuración con bind mounts de forma declarativa.
- Automatizar el despliegue de aplicaciones Java.
- Comprender la gestión de archivos estáticos vs. archivos de aplicación.
- Comparar la orquestación manual con Docker Compose en arquitecturas complejas.

---

### Contexto de trabajo

**Recordatorio de la arquitectura:**

- **Tomcat:** Servidor de aplicaciones Java (puerto 8080/tcp) - imagen `tomcat:9.0`
- **Nginx:** Proxy inverso (puerto 80/tcp) - imagen `nginx`
- **Archivos necesarios:**
    - `sample.war` - Aplicación Java
    - `default.conf` - Configuración de Nginx
- **Flujo:** Cliente → Nginx (80) → Tomcat (8080) → App Java

**Particularidad:** Esta práctica requiere archivos externos (bind mounts) para configuración y despliegue.

---

### 🔹 Parte 1: Preparación del entorno

#### Tarea 1.1: Estructura de archivos

1. Crea el directorio del proyecto: `~/tomcat_compose`.

2. Investiga qué archivos necesitas para este despliegue:
   
    - Un archivo WAR de una aplicación Java (puedes descargarlo del repositorio del curso o usar uno propio)
    - Un archivo de configuración de Nginx para el proxy inverso

3. Dentro del directorio, crea la siguiente estructura:

```
tomcat_compose/
├── docker-compose.yml
├── default.conf
└── sample.war
```

3. Descarga o crea los archivos necesarios:
   
    - `sample.war` - Aplicación Java de ejemplo
    - Puedes descargar desde el repositorio del curso o usar cualquier WAR simple

4. Crea el archivo `default.conf` con la configuración de Nginx:

```nginx
server {
    listen       80;
    listen  [::]:80;
    server_name  localhost;
   
    location / {
        root   /usr/share/nginx/html;
        proxy_pass http://aplicacionjava:8080/sample/;
    }
    
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
```

#### Tarea 1.2: Creación del docker-compose.yml

1. Investiga la documentación de Docker Compose sobre bind mounts.

2. Crea un archivo `docker-compose.yml` que defina:
   
    **Servicio de Tomcat:**
    - Imagen: `tomcat:9.0`
    - Bind mount del archivo WAR al directorio de despliegue de Tomcat (`/usr/local/tomcat/webapps/`)
    - Montaje en modo solo lectura (`:ro`)
    - NO mapear puertos al host (acceso solo interno)
    - Política de reinicio
    
    **Servicio de Nginx (proxy):**
    - Imagen: `nginx`
    - Puerto 80 del host mapeado al puerto 80 del contenedor
    - Bind mount del archivo de configuración a la ubicación correcta en Nginx
    - Montaje en modo solo lectura (`:ro`)
    - Dependencia del servicio de Tomcat
    - Política de reinicio

3. Analiza y responde:
   
    - ¿Por qué se usan bind mounts en lugar de volúmenes Docker?
    - ¿Qué significa `:ro` y por qué es importante?
    - ¿Por qué Nginx depende de Tomcat?
    - ¿Por qué Tomcat no expone puertos al host?

---

### 🔹 Parte 2: Despliegue y verificación

#### Tarea 2.1: Despliegue del escenario

1. Desde el directorio del proyecto, despliega con Docker Compose.

2. Observa la salida y verifica qué recursos se crean.

3. Comprueba que ambos servicios están en ejecución.

4. Accede a la aplicación (http://localhost).

5. Verifica que estás accediendo a través del proxy (puerto 80, no 8080).

#### Tarea 2.2: Verificación de bind mounts

1. Verifica que los archivos se han montado correctamente:
   
    - Accede al contenedor de Tomcat y verifica `sample.war`
    - Accede al contenedor de Nginx y verifica `default.conf`

2. Modifica el archivo `default.conf` en el host (cambia algo en un comentario).

3. Recarga la configuración de Nginx sin reiniciar el contenedor.

4. Verifica que el cambio se ha aplicado.

#### Tarea 2.3: Análisis de logs

1. Visualiza los logs de ambos servicios.

2. Identifica en los logs de Nginx las peticiones que redirige a Tomcat.

3. Identifica en los logs de Tomcat el despliegue de la aplicación WAR.

4. Realiza varias peticiones y observa cómo se registran en ambos servicios.

---

### 🔹 Parte 3: Configuración avanzada

#### Tarea 3.1: Mejora de la configuración de Nginx

1. Modifica `default.conf` para añadir cabeceras de proxy:

```nginx
server {
    listen       80;
    listen  [::]:80;
    server_name  localhost;

    location / {
        proxy_pass http://aplicacionjava:8080/sample/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
    
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
```

2. Recarga Nginx sin detener el contenedor.

3. Verifica que las cabeceras se están enviando correctamente.

#### Tarea 3.2: Múltiples aplicaciones WAR

1. Si tienes acceso a múltiples archivos WAR, modifica tu `docker-compose.yml`:
   
    - Añade bind mounts adicionales para cada archivo WAR
    - Investiga cómo montar múltiples archivos en el mismo servicio

2. Modifica el archivo `default.conf` de Nginx para configurar diferentes rutas:
   
    - Cada aplicación debe ser accesible en una ruta diferente
    - Por ejemplo: `/app1/` → aplicacion1.war, `/app2/` → aplicacion2.war
    - Investiga la directiva `location` de Nginx

3. Verifica el acceso a todas las aplicaciones desde diferentes URLs.

#### Tarea 3.3: Variables de entorno y customización

1. Crea un archivo `.env` con variables para:
   
    - Puerto de Nginx
    - Versión de Tomcat a usar
    - Nombre del archivo WAR

2. Modifica tu `docker-compose.yml` para usar estas variables con la sintaxis `${VARIABLE}`.

3. Prueba cambiando valores en `.env` (por ejemplo, cambiar la versión de Tomcat) y verifica que los cambios se aplican correctamente.

---

### 🔹 Parte 4: Gestión avanzada

#### Tarea 4.1: Healthchecks

1. Investiga cómo configurar healthchecks en Docker Compose.

2. Añade healthchecks a ambos servicios:
   
    **Para Tomcat:**
    - Verifica la disponibilidad de la aplicación en el puerto 8080
    - Intervalo de 30 segundos
    - Timeout de 10 segundos
    - 3 reintentos
    - Periodo de inicio de 60 segundos (Tomcat puede tardar en iniciar)
    
    **Para Nginx:**
    - Verifica la disponibilidad del puerto 80
    - Intervalo de 30 segundos
    - Timeout de 3 segundos
    - 3 reintentos

3. Investiga el comando para ver el estado de salud de los servicios.

4. Detén Tomcat y observa cómo afecta al healthcheck de Nginx.

#### Tarea 4.2: Límites de recursos

1. Investiga cómo establecer límites de recursos en Docker Compose.

2. Añade a tu archivo `docker-compose.yml`:
   
    **Para Tomcat:**
    - Límite de CPU: 1
    - Límite de memoria: 512M
    - Reserva de CPU: 0.5
    - Reserva de memoria: 256M
    
    **Para Nginx:**
    - Límite de CPU: 0.5
    - Límite de memoria: 128M

3. Investiga comandos Docker para verificar el consumo de recursos de los contenedores.

4. Verifica que los límites se están aplicando correctamente.

#### Tarea 4.3: Red personalizada

1. Investiga cómo definir redes personalizadas con configuración IPAM en Docker Compose.

2. Añade una red personalizada a tu archivo `docker-compose.yml`:
   
    - Tipo: bridge
    - Nombre descriptivo (ej: tomcat_net)
    - Configuración IPAM con subred personalizada (ej: 172.28.0.0/16)
    - Conecta ambos servicios a esta red

3. Investiga comandos Docker para inspeccionar la configuración de red.

4. Verifica que la red está correctamente configurada y que los servicios están conectados.

---

### 🔹 Parte 5: Despliegue de nueva aplicación

#### Tarea 5.1: Actualización de aplicación

1. Prepara una nueva versión de `sample.war` (o usa otro WAR).

2. Sustituye el archivo WAR en el host.

3. Reinicia solo el servicio de Tomcat.

4. Verifica que la nueva versión se ha desplegado.

5. Observa que Nginx no necesitó reiniciarse.

#### Tarea 5.2: Configuración sin downtime

1. Realiza una modificación en el archivo `default.conf` (puede ser un cambio en un comentario o en alguna configuración).

2. Investiga qué comando de Docker Compose permite ejecutar comandos dentro de un contenedor en ejecución.

3. Investiga qué señal debe enviarse a Nginx para recargar su configuración sin detener el servicio.

4. Ejecuta el comando para recargar Nginx sin downtime.

5. Verifica que el cambio se ha aplicado y que no hubo interrupción del servicio.

**Reflexión:** ¿Por qué es importante poder actualizar configuraciones sin downtime en producción?

---

### 🔹 Parte 6: Análisis y documentación

#### Tarea 6.1: Preguntas de análisis

Responde en tu documentación:

1. **Comparación con práctica anterior:**
    
    - ¿Cuántos comandos necesitabas en la Práctica 2.4?
    - ¿Qué ventajas ofrece Docker Compose?
    - ¿Es más fácil versionar la configuración?

2. **Montajes de solo lectura (`:ro`):**
   
    - ¿Por qué es buena práctica montar archivos como solo lectura?
    - ¿Qué riesgos evitas?
    - ¿En qué casos no usarías `:ro`?

3. **Proxy inverso:**
   
    - ¿Qué ventajas aporta Docker Compose a esta arquitectura?
    - ¿Es más fácil modificar la configuración del proxy?
    - ¿Cómo facilita el despliegue de nuevas aplicaciones?

4. **Dependencias:**
   
    - ¿Por qué Nginx depende de Tomcat?
    - ¿Qué pasa si Tomcat no está listo cuando Nginx arranca?
    - ¿Cómo mejorarías esto con healthchecks?


#### Tarea 6.2: Tabla comparativa

| Aspecto                | Gestión manual  | Docker Compose  |
|------------------------|-----------------|-----------------|
| Creación de red        |                 |                 |
| Montaje de archivos    |                 |                 |
| Despliegue de app WAR  |                 |                 |
| Configuración de Nginx |                 |                 |
| Actualización de app   |                 |                 |
| Modificación de config |                 |                 |
| Reproducibilidad       |                 |                 |

---

## Entregables

1. **Documentación en formato Markdown o PDF** con:
   
    - Archivo `docker-compose.yml` completo y comentado
    - Archivo `default.conf` completo y explicado
    - Archivo `.env` (si lo utilizas)
    - Todos los comandos Docker Compose utilizados
    - Capturas de pantalla:
        - Aplicación funcionando a través del proxy
        - Estructura de archivos del proyecto
        - Servicios en ejecución
        - Logs de ambos servicios
        - Healthchecks
        - Actualización de aplicación sin downtime
    - Respuestas a todas las preguntas
    - Tabla comparativa
    - Comparación con la Práctica 2.4

2. **Archivos del proyecto:**
   
    - `docker-compose.yml` básico
    - `docker-compose.yml` avanzado (con healthchecks, redes, límites)
    - `default.conf` básico
    - `default.conf` avanzado
    - `.env`

---

### Evaluación

Se evaluará:

- Correcta configuración del proxy inverso con Compose.
- Uso apropiado de bind mounts.
- Comprensión de arquitecturas de múltiples capas.
- Gestión de actualizaciones sin downtime.
- Comparación crítica con gestión manual.

---

### Condiciones de entrega

Las publicadas en la plataforma Moodle del curso.

---

### Recursos de apoyo

- Documentación oficial de Docker Compose: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
- Bind mounts en Compose: [https://docs.docker.com/compose/compose-file/07-volumes/](https://docs.docker.com/compose/compose-file/07-volumes/)
- Tomcat en Docker: [https://hub.docker.com/_/tomcat](https://hub.docker.com/_/tomcat)
- Nginx en Docker: [https://hub.docker.com/_/nginx](https://hub.docker.com/_/nginx)
- Configuración de Nginx: [https://nginx.org/en/docs/](https://nginx.org/en/docs/)
- Repositorio con ejemplos: [https://github.com/josedom24/curso_docker_ies](https://github.com/josedom24/curso_docker_ies)
