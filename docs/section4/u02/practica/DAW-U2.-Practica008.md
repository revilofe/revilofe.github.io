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

2. Dentro del directorio, crea la siguiente estructura:

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

1. Crea el archivo `docker-compose.yml`:

2. Analiza la configuración:
   
    - ¿Por qué se usan bind mounts en lugar de volúmenes?
    - ¿Qué significa `:ro` al final de los volúmenes?
    - ¿Por qué Nginx depende de Tomcat?
    - ¿Por qué Tomcat no expone puertos?

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

1. Si tienes múltiples archivos WAR, modifica el `docker-compose.yml`:

```yaml
services:
  aplicacionjava:
    volumes:
      - ./sample.war:/usr/local/tomcat/webapps/sample.war:ro
      - ./otra-app.war:/usr/local/tomcat/webapps/otra.war:ro
```

2. Configura Nginx para acceder a ambas aplicaciones en diferentes rutas:

```nginx
location /sample/ {
    proxy_pass http://aplicacionjava:8080/sample/;
}

location /otra/ {
    proxy_pass http://aplicacionjava:8080/otra/;
}
```

3. Verifica el acceso a ambas aplicaciones.

#### Tarea 3.3: Variables de entorno y customización

1. Crea un archivo `.env`:

```env
NGINX_PORT=80
TOMCAT_VERSION=9.0
APP_WAR=sample.war
```

2. Modifica el `docker-compose.yml`:

```yaml
services:
  aplicacionjava:
    image: tomcat:${TOMCAT_VERSION}
    volumes:
      - ./${APP_WAR}:/usr/local/tomcat/webapps/sample.war:ro
      
  proxy:
    ports:
      - "${NGINX_PORT}:80"
```

3. Prueba cambiando valores en `.env` y verificando que funcionan.

---

### 🔹 Parte 4: Gestión avanzada

#### Tarea 4.1: Healthchecks

1. Añade healthchecks a los servicios:

```yaml
services:
  aplicacionjava:
    # ... configuración anterior
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/sample/"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s
      
  proxy:
    # ... configuración anterior
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/"]
      interval: 30s
      timeout: 3s
      retries: 3
```

2. Verifica el estado de salud de los servicios.

3. Detén Tomcat y observa cómo afecta al healthcheck de Nginx.

#### Tarea 4.2: Límites de recursos

1. Añade límites de recursos:

```yaml
services:
  aplicacionjava:
    # ... configuración anterior
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M
          
  proxy:
    # ... configuración anterior
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 128M
```

2. Verifica el consumo de recursos.

#### Tarea 4.3: Red personalizada

1. Añade una red explícita `tomcat_net`, `subnet: 172.28.0.0/16` y conecta ambos servicios:

2. Verifica la configuración de red.

---

### 🔹 Parte 5: Despliegue de nueva aplicación

#### Tarea 5.1: Actualización de aplicación

1. Prepara una nueva versión de `sample.war` (o usa otro WAR).

2. Sustituye el archivo WAR en el host.

3. Reinicia solo el servicio de Tomcat.

4. Verifica que la nueva versión se ha desplegado.

5. Observa que Nginx no necesitó reiniciarse.

#### Tarea 5.2: Configuración sin downtime

1. Modifica la configuración de Nginx.

2. Recarga Nginx sin detener el servicio:

```bash
docker compose exec proxy nginx -s reload
```

3. Verifica que no hubo downtime.

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
