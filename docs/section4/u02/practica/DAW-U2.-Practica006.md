---
title: "UD 2 - P6: Despliegue de Temperaturas con Docker Compose"
description: "Automatización del despliegue de la aplicación Temperaturas con Docker Compose"
summary: "Actividad práctica para desplegar la aplicación de microservicios Temperaturas utilizando Docker Compose."
authors:
    - Eduardo Fdez
date: 2025-01-12
icon: 
permalink: /daw/unidad2/p2.6
categories:
    - DAW
tags:
    - Docker
    - Docker Compose
    - Microservicios
    - Temperaturas
    - API REST
---

## Relación 2.6

### Descripción

**Actividad:** *Despliegue de Temperaturas con Docker Compose*

En esta práctica retomarás la aplicación de microservicios **Temperaturas** de la Práctica 2.2, pero esta vez la desplegarás utilizando **Docker Compose**. Verás cómo la gestión de aplicaciones sin estado y microservicios se simplifica enormemente con una configuración declarativa.

#### Objetivo general

Aprender a:

- Desplegar arquitecturas de microservicios con Docker Compose.
- Gestionar dependencias entre servicios.
- Configurar comunicación entre microservicios de forma declarativa.
- Comparar la orquestación de aplicaciones con y sin estado.
- Entender las ventajas de Docker Compose en arquitecturas de microservicios.

---

### Contexto de trabajo

**Recordatorio de la aplicación Temperaturas:**

- **Frontend:** Interfaz web en Python (puerto 3000/tcp) - imagen `iesgn/temperaturas_frontend`
- **Backend:** API REST en Python (puerto 5000/tcp) - imagen `iesgn/temperaturas_backend`
- **Tipo:** Aplicación sin estado (stateless)
- **Comunicación:** El frontend consulta el backend vía HTTP

**Diferencias con Guestbook:**

- No requiere persistencia de datos
- Arquitectura de microservicios más clara
- Uso de dependencias explícitas entre servicios

---

### 🔹 Parte 1: Creación del archivo docker-compose.yml

#### Tarea 1.1: Estructura básica

1. Crea un directorio para esta práctica: `~/temperaturas_compose`.

2. Crea el archivo `docker-compose.yml` con la siguiente estructura:

```yaml
version: '3.1'

services:
  frontend:
    container_name: temperaturas-frontend
    image: iesgn/temperaturas_frontend
    restart: always
    ports:
      - 8081:3000
    environment:
      TEMP_SERVER: temperaturas-backend:5000
    depends_on:
      - backend
      
  backend:
    container_name: temperaturas-backend
    image: iesgn/temperaturas_backend
    restart: always
```

3. Analiza la estructura del archivo:
   
    - ¿Por qué el frontend tiene `depends_on: - backend`?
    - ¿Qué indica la variable `TEMP_SERVER`?
    - ¿Por qué el backend no expone puertos al host?

#### Tarea 1.2: Comprensión de dependencias

1. Investiga qué hace la directiva `depends_on`:
   
    - ¿Garantiza que el backend esté completamente iniciado antes que el frontend?
    - ¿Solo controla el orden de inicio?
    - ¿Qué limitaciones tiene?

2. Modifica el archivo para usar el nombre del servicio en lugar del contenedor:
   
    ```yaml
    environment:
      TEMP_SERVER: backend:5000
    ```

3. Verifica que ambas configuraciones funcionan correctamente.

---

### 🔹 Parte 2: Despliegue y gestión

#### Tarea 2.1: Despliegue del escenario

1. Despliega la aplicación con Docker Compose.

2. Observa el orden en que se crean los servicios. ¿Se crea primero el backend?

3. Verifica los contenedores en ejecución.

4. Accede a la aplicación (http://localhost:8081).

5. Realiza búsquedas de varios municipios.

#### Tarea 2.2: Análisis de logs

1. Visualiza los logs de ambos servicios simultáneamente.

2. Visualiza solo los logs del frontend.

3. Visualiza solo los logs del backend.

4. En los logs del frontend, busca las peticiones HTTP que realiza al backend.

5. En los logs del backend, identifica las respuestas que envía.

#### Tarea 2.3: Pruebas de resiliencia

1. Detén solo el servicio backend.

2. Intenta acceder a la aplicación. ¿Qué sucede?

3. Observa los logs del frontend. ¿Qué errores aparecen?

4. Arranca nuevamente el backend.

5. Verifica que la aplicación vuelve a funcionar sin necesidad de reiniciar el frontend.

---

### 🔹 Parte 3: Escalado de microservicios

#### Tarea 3.1: Escalado del backend

1. Escala el servicio backend a 3 instancias.

2. Verifica que las tres instancias están en ejecución.

3. Realiza varias búsquedas en la aplicación.

4. ¿Las peticiones se distribuyen entre las instancias? ¿Por qué?

#### Tarea 3.2: Escalado del frontend

1. Intenta escalar el frontend a 2 instancias.

2. ¿Qué problema aparece? (conflicto de puertos)

3. Modifica el `docker-compose.yml` para permitir el escalado del frontend:

```yaml
frontend:
  image: iesgn/temperaturas_frontend
  restart: always
  ports:
    - "8081-8083:3000"
  environment:
    TEMP_SERVER: backend:5000
  depends_on:
    - backend
```

4. Escala el frontend y verifica que funciona.

---

### 🔹 Parte 4: Configuración avanzada

#### Tarea 4.1: Límites de recursos

1. Añade límites de recursos a los servicios:

```yaml
services:
  frontend:
    # ... resto de configuración
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 128M
        reservations:
          cpus: '0.25'
          memory: 64M
          
  backend:
    # ... resto de configuración
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 128M
      replicas: 2
```

2. Despliega y verifica el consumo de recursos.

#### Tarea 4.2: Healthchecks

1. Añade healthchecks a los servicios:

```yaml
backend:
  image: iesgn/temperaturas_backend
  healthcheck:
    test: ["CMD", "curl", "-f", "http://localhost:5000"]
    interval: 30s
    timeout: 3s
    retries: 3
    start_period: 40s
```

2. Verifica el estado de salud de los servicios.

#### Tarea 4.3: Variables de entorno desde archivo

1. Crea un archivo `.env`:

```env
FRONTEND_PORT=8081
BACKEND_HOST=backend
BACKEND_PORT=5000
```

2. Modifica el `docker-compose.yml`:

```yaml
services:
  frontend:
    ports:
      - "${FRONTEND_PORT}:3000"
    environment:
      TEMP_SERVER: ${BACKEND_HOST}:${BACKEND_PORT}
```

3. Verifica que funciona con las variables del archivo `.env`.

---

### 🔹 Parte 5: Análisis y documentación

#### Tarea 5.1: Preguntas de análisis

Responde en tu documentación:

1. **Aplicaciones sin estado:**
   
    - ¿Por qué es más fácil escalar aplicaciones sin estado?
    - ¿Qué ventajas tiene no necesitar volúmenes?
    - Compara con Guestbook (que sí tiene estado).

2. **Dependencias entre servicios:**
   
    - ¿Qué diferencia hay entre `depends_on` y `links`?
    - ¿`depends_on` garantiza que el servicio esté listo para recibir peticiones?
    - ¿Cómo se podría mejorar esto con healthchecks?

3. **Arquitectura de microservicios:**
   
    - ¿Qué ventajas tiene separar frontend y backend?
    - ¿Cómo facilita Docker Compose el desarrollo de microservicios?
    - ¿Qué pasa si el backend falla? ¿Y si el frontend falla?

4. **Escalado:**
   
    - ¿Por qué es más fácil escalar el backend que el frontend?
    - ¿Cómo se distribuirían las peticiones con múltiples backends?
    - ¿Necesitarías un balanceador de carga?

5. **Comparación con práctica anterior:**
   
    - ¿Qué comandos de la Práctica 2.2 sustituye Docker Compose?
    - ¿Es más fácil gestionar esta aplicación con Compose?
    - ¿Qué ventajas adicionales obtienes?

#### Tarea 5.2: Tabla comparativa

Crea una tabla comparando:

| Aspecto | Temperaturas manual | Temperaturas Compose |
|---------|---------------------|----------------------|
| Comandos para desplegar | | |
| Gestión de red | | |
| Variables de entorno | | |
| Escalado | | |
| Orden de inicio | | |
| Logs | | |

---

## Entregables

1. **Documentación en formato Markdown o PDF** con:
   
    - Archivo `docker-compose.yml` completo y comentado
    - Todos los comandos Docker Compose utilizados
    - Capturas de pantalla:
        - Aplicación funcionando
        - Búsquedas de municipios
        - Servicios en ejecución
        - Logs de ambos microservicios
        - Escalado de servicios
        - Healthchecks
    - Respuestas a las preguntas de análisis
    - Tabla comparativa

2. **Archivos de configuración:**
   
    - `docker-compose.yml` básico
    - `docker-compose.yml` avanzado (con healthchecks, límites, etc.)
    - `.env` (si lo utilizas)

---

### Evaluación

Se evaluará:

- Correcta configuración del archivo Compose.
- Comprensión de dependencias entre servicios.
- Análisis de aplicaciones sin estado.
- Práctica con escalado de microservicios.
- Comparación crítica con gestión manual.

---

### Condiciones de entrega

Las publicadas en la plataforma Moodle del curso.

---

### Recursos de apoyo

- Documentación oficial de Docker Compose: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
- Depends_on: [https://docs.docker.com/compose/compose-file/05-services/#depends_on](https://docs.docker.com/compose/compose-file/05-services/#depends_on)
- Healthchecks: [https://docs.docker.com/compose/compose-file/05-services/#healthcheck](https://docs.docker.com/compose/compose-file/05-services/#healthcheck)
- Escalado: [https://docs.docker.com/compose/reference/scale/](https://docs.docker.com/compose/reference/scale/)
- Repositorio con ejemplos: [https://github.com/josedom24/curso_docker_ies](https://github.com/josedom24/curso_docker_ies)

---

### Presentación de la práctica

[:fontawesome-solid-file-pdf: Descargar presentación](https://revilofe.github.io/slides/section4-daw/DAW-U2.6.-TemperaturasCompose.html){ .md-button }
