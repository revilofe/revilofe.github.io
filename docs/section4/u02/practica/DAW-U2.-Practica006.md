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

2. Investiga la documentación de Docker Compose para crear un archivo `docker-compose.yml` que incluya:
   
    **Servicio Frontend:**
    - Imagen: `iesgn/temperaturas_frontend`
    - Puerto del host mapeado al puerto 3000 del contenedor
    - Variable de entorno que indica dónde se encuentra el backend (nombre:puerto)
    - Dependencia explícita del servicio backend
    - Política de reinicio
    
    **Servicio Backend:**
    - Imagen: `iesgn/temperaturas_backend`
    - Política de reinicio
    - NO exponer puertos al host (comunicación interna)


```yaml
version: '3.1'

services:
  ???????????:
    ....
    ....
    restart: always
    ports:
      - 8081:?????
    environment:
      TEMP_SERVER: temperaturas-backend:5000
    depends_on:
      - backend
      
  ???????????:
    ....
    ....
    restart: always
```


3. Analiza y responde:
   
    - ¿Por qué el frontend tiene una dependencia del backend?
    - ¿Qué indica la variable de entorno del servidor backend?
    - ¿Por qué el backend no expone puertos al host?

#### Tarea 1.2: Comprensión de dependencias

1. Investiga en la documentación oficial qué hace la directiva `depends_on`:
   
    - ¿Garantiza que el backend esté completamente iniciado antes que el frontend?
    - ¿Solo controla el orden de inicio de contenedores?
    - ¿Qué limitaciones tiene esta directiva?

2. Experimenta con diferentes configuraciones:
   
    - Prueba usando el nombre del contenedor en la variable de entorno
    - Prueba usando el nombre del servicio en la variable de entorno
    - Verifica que ambas configuraciones funcionan correctamente

3. Reflexiona sobre cuál es mejor práctica y por qué.

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

1. Investiga el comando de Docker Compose para escalar servicios.

2. Escala el servicio backend a 3 instancias.

3. Verifica que las tres instancias están en ejecución.

4. Realiza varias búsquedas en la aplicación.

5. Investiga y responde:
   
    - ¿Las peticiones se distribuyen entre las instancias?
    - ¿Por qué sí o por qué no?
    - ¿Qué mecanismo de Docker gestiona esto?

#### Tarea 3.2: Escalado del frontend

1. Intenta escalar el frontend a 2 instancias usando el comando de escalado.

2. Observa y documenta qué problema aparece.

3. Investiga cómo permitir el escalado del frontend modificando el mapeo de puertos en el archivo `docker-compose.yml`:
   
    - Investiga cómo especificar un rango de puertos
    - Modifica la configuración del servicio frontend
    - Asegúrate de no especificar nombres de contenedor fijos

4. Escala el frontend a múltiples instancias y verifica que funciona.

5. Identifica en qué puertos del host quedó cada instancia.

---

### 🔹 Parte 4: Configuración avanzada

#### Tarea 4.1: Límites de recursos

1. Investiga en la documentación de Docker Compose cómo establecer límites de recursos.

2. Añade a tu archivo `docker-compose.yml`:
   
    **Para el servicio frontend:**
    - Límite de CPU: 0.5
    - Límite de memoria: 128M
    - Reserva de CPU: 0.25
    - Reserva de memoria: 64M
    
    **Para el servicio backend:**
    - Límite de CPU: 0.5
    - Límite de memoria: 128M
    - Configuración para 2 réplicas

3. Despliega con los cambios y verifica el consumo de recursos usando comandos Docker.

#### Tarea 4.2: Healthchecks

1. Investiga la sintaxis de healthchecks en Docker Compose.

2. Añade un healthcheck al servicio backend que:
   
    - Verifique la disponibilidad del puerto 5000
    - Se ejecute cada 30 segundos
    - Tenga un timeout de 3 segundos
    - Permita 3 reintentos
    - Espere 40 segundos antes del primer check (start_period)

3. Verifica el estado de salud con comandos de Docker Compose.

4. Detén el backend y observa cómo cambia el estado de salud.

#### Tarea 4.3: Variables de entorno desde archivo

1. Crea un archivo `.env` con las siguientes variables:
   
    - Puerto para el frontend
    - Hostname del backend
    - Puerto del backend

2. Modifica tu `docker-compose.yml` para utilizar estas variables con la sintaxis `${VARIABLE}`.

```yaml
services:
  ???????????:
    ports:
      - "${FRONTEND_PORT}:3000"
    ???????????:
      TEMP_SERVER: ${BACKEND_HOST}:${BACKEND_PORT}
```

3. Despliega y verifica que funciona correctamente con las variables del archivo `.env`.

4. Experimenta cambiando valores en `.env` sin modificar el `docker-compose.yml`.

---

### 🔹 Parte 5: Análisis y documentación

#### Tarea 5.1: Preguntas de análisis

Responde en tu documentación:

1. **Comparación con práctica anterior:**
    
    - ¿Qué comandos de la Práctica 2.2 sustituye Docker Compose?
    - ¿Es más fácil gestionar esta aplicación con Compose?
    - ¿Qué ventajas adicionales obtienes?
   
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



#### Tarea 5.2: Tabla comparativa

Crea una tabla comparando:

| Aspecto                 | Temperaturas manual  | Temperaturas Compose  |
|-------------------------|----------------------|-----------------------|
| Comandos para desplegar |                      |                       |
| Gestión de red          |                      |                       |
| Variables de entorno    |                      |                       |
| Escalado                |                      |                       |
| Orden de inicio         |                      |                       |
| Logs                    |                      |                       |

---

## Entregables

1. **Documentación en formato Markdown** con:
   
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

