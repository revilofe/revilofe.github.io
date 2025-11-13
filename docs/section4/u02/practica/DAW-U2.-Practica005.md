---
title: "UD 2 - P5: Despliegue de Guestbook con Docker Compose"
description: "Automatización del despliegue de Guestbook usando Docker Compose"
summary: "Actividad práctica para desplegar la aplicación Guestbook utilizando Docker Compose y gestionar escenarios multi-contenedor de forma declarativa."
authors:
    - Eduardo Fdez
date: 2025-01-12
icon: 
permalink: /daw/unidad2/p2.5
categories:
    - DAW
tags:
    - Docker
    - Docker Compose
    - Guestbook
    - Orquestación
    - YAML
---

## Relación 2.5

### Descripción

**Actividad:** *Despliegue de Guestbook con Docker Compose*

En esta práctica retomarás la aplicación **Guestbook** de la Práctica 2.1, pero esta vez utilizarás **Docker Compose** para automatizar y simplificar su despliegue. Docker Compose permite definir y gestionar aplicaciones multi-contenedor mediante un archivo de configuración declarativo en formato YAML.

#### Objetivo general

Aprender a:

- Utilizar Docker Compose para orquestar aplicaciones multi-contenedor.
- Escribir y comprender archivos `docker-compose.yml`.
- Gestionar el ciclo de vida completo de aplicaciones con Docker Compose.
- Comparar la gestión manual de contenedores vs. Docker Compose.
- Trabajar con volúmenes Docker en lugar de bind mounts.
- Entender la configuración declarativa de infraestructura.

---

### Contexto de trabajo

**Recordatorio de la aplicación Guestbook:**

- **Servicio web:** Aplicación Python que escucha en el puerto 5000/tcp (imagen `iesgn/guestbook`)
- **Base de datos:** Redis que escucha en el puerto 6379/tcp (imagen `redis`)
- **Persistencia:** Datos de Redis almacenados en `/data` del contenedor
- **Comunicación:** Red Docker para resolución DNS

**¿Qué es Docker Compose?**

Docker Compose es una herramienta que permite definir y ejecutar aplicaciones Docker multi-contenedor mediante un archivo YAML. En lugar de ejecutar múltiples comandos `docker run`, defines toda la infraestructura en un archivo y la gestionas con comandos simples.

**Ventajas de Docker Compose:**

- Configuración declarativa (Infrastructure as Code)
- Gestión simplificada del ciclo de vida
- Reproducibilidad del entorno
- Documentación implícita de la arquitectura
- Facilita el trabajo en equipo

---

### 🔹 Parte 1: De comandos Docker a Docker Compose

#### Tarea 1.1: Revisión de la práctica anterior

Antes de comenzar, revisa los comandos que utilizaste en la Práctica 2.1 para:

1. Crear la red `red_guestbook`
2. Crear el contenedor de Redis con volumen
3. Crear el contenedor de Guestbook con variables de entorno

Identifica:

- Parámetros de red
- Variables de entorno
- Volúmenes
- Mapeo de puertos
- Comandos de ejecución

#### Tarea 1.2: Creación del archivo docker-compose.yml

1. Crea un directorio para esta práctica, por ejemplo `~/guestbook_compose`.

2. Crea un archivo llamado `docker-compose.yml` con la siguiente estructura base:

```yaml
version: '3.1'

services:
  app:
    container_name: guestbook
    image: iesgn/guestbook
    restart: always
    environment:
      REDIS_SERVER: redis
    ports:
      - 8080:5000
      
  db:
    container_name: redis
    image: redis
    restart: always
    command: redis-server --appendonly yes
    volumes:
      - redis:/data

volumes:
  redis:
```

3. Analiza cada sección del archivo:
   
    - `version`: Versión del formato de Docker Compose
    - `services`: Define los contenedores de la aplicación
    - `volumes`: Define los volúmenes Docker
    - `restart`: Política de reinicio automático
    - `command`: Comando a ejecutar en el contenedor

#### Tarea 1.3: Comprensión de las diferencias

Compara el archivo `docker-compose.yml` con los comandos de la Práctica 2.1:

1. **Red:** ¿Por qué no se define explícitamente la red en el archivo Compose?

2. **Volumen:** ¿Qué diferencia hay entre usar un volumen Docker (`redis:`) y un bind mount (`/opt/redis:/data`)?

3. **Variables de entorno:** Aunque la variable `REDIS_SERVER` es `redis` por defecto, ¿por qué es buena práctica declararla explícitamente?

4. **Nombres de servicios:** ¿Cuál es la diferencia entre el nombre del servicio (`db`) y el nombre del contenedor (`redis`)?

---

### 🔹 Parte 2: Gestión del escenario con Docker Compose

#### Tarea 2.1: Despliegue del escenario

1. Desde el directorio donde está el archivo `docker-compose.yml`, ejecuta el comando para crear y arrancar el escenario en segundo plano.

2. Observa la salida del comando. ¿Qué recursos se crean automáticamente?

3. Verifica los contenedores en ejecución usando el comando específico de Docker Compose.

4. Accede a la aplicación desde tu navegador (http://localhost:8080).

5. Añade varios mensajes en el libro de visitas.

#### Tarea 2.2: Gestión del ciclo de vida

1. **Ver logs:**
   
    - Visualiza los logs de todos los servicios
    - Visualiza solo los logs del servicio `app`
    - Visualiza solo los logs del servicio `db`

2. **Detener servicios:**
   
    - Detén todos los servicios sin eliminarlos
    - Verifica el estado de los contenedores
    - Accede a la aplicación (debería estar inaccesible)

3. **Reiniciar servicios:**
   
    - Arranca nuevamente los servicios
    - Verifica que los datos persisten

4. **Escalar servicios (opcional):**
   
    - Intenta escalar el servicio `app` a 3 instancias
    - Observa qué problemas aparecen (conflicto de puertos)

#### Tarea 2.3: Eliminación del escenario

1. **Eliminar sin volúmenes:**
   
    - Elimina el escenario pero mantén los volúmenes
    - Verifica qué recursos se eliminan
    - Comprueba que el volumen sigue existiendo

2. **Recrear y verificar persistencia:**
   
    - Vuelve a crear el escenario con Docker Compose
    - Verifica que los datos del libro de visitas persisten

3. **Eliminar con volúmenes:**
   
    - Elimina el escenario incluyendo los volúmenes
    - Verifica que el volumen también se ha eliminado
    - Recrea el escenario
    - Comprueba que el libro de visitas está vacío

---

### 🔹 Parte 3: Modificación y personalización

#### Tarea 3.1: Cambio del puerto de la aplicación

1. Modifica el archivo `docker-compose.yml` para que la aplicación sea accesible en el puerto 9090 del host.

2. Recrea el escenario aplicando los cambios.

3. Accede a la aplicación en el nuevo puerto.

#### Tarea 3.2: Configuración avanzada

1. Añade las siguientes configuraciones al servicio `app`:
   
    - Límites de recursos (memoria: 256MB, CPU: 0.5)
    - Red personalizada explícita

2. Ejemplo de configuración avanzada:

```yaml
services:
  app:
    container_name: guestbook
    image: iesgn/guestbook
    restart: always
    environment:
      REDIS_SERVER: redis
    ports:
      - 8080:5000
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 256M
    networks:
      - guestbook_net
      
  db:
    container_name: redis
    image: redis
    restart: always
    command: redis-server --appendonly yes
    volumes:
      - redis:/data
    networks:
      - guestbook_net

volumes:
  redis:

networks:
  guestbook_net:
    driver: bridge
```

3. Aplica los cambios y verifica que el escenario funciona correctamente.

#### Tarea 3.3: Variables de entorno desde archivo

1. Crea un archivo `.env` con variables de entorno:

```env
GUESTBOOK_PORT=8080
REDIS_CONTAINER=redis
```

2. Modifica el `docker-compose.yml` para usar estas variables:

```yaml
services:
  app:
    environment:
      REDIS_SERVER: ${REDIS_CONTAINER}
    ports:
      - ${GUESTBOOK_PORT}:5000
```

3. Despliega y verifica que funciona con las variables del archivo `.env`.

---

### 🔹 Parte 4: Comandos de Docker Compose

#### Tarea 4.1: Comandos esenciales

Practica y documenta los siguientes comandos de Docker Compose:

1. **Crear y arrancar:**
   
    - Arrancar en primer plano
    - Arrancar en segundo plano
    - Forzar recreación de contenedores

2. **Información:**
   
    - Ver estado de servicios
    - Ver procesos en ejecución
    - Ver configuración final (con variables resueltas)

3. **Gestión:**
   
    - Detener servicios
    - Arrancar servicios detenidos
    - Reiniciar servicios
    - Pausar y despausar servicios

4. **Logs:**
   
    - Ver logs de todos los servicios
    - Ver logs de un servicio específico
    - Seguir logs en tiempo real

5. **Limpieza:**
   
    - Eliminar escenario sin volúmenes
    - Eliminar escenario con volúmenes
    - Eliminar imágenes no utilizadas

---

### 🔹 Parte 5: Análisis y documentación

#### Tarea 5.1: Preguntas de análisis

Responde a las siguientes preguntas en tu documentación:

1. **Docker Compose vs. comandos manuales:**
   
    - ¿Qué ventajas ofrece Docker Compose frente a ejecutar comandos `docker run` manualmente?
    - ¿En qué escenarios sería preferible usar comandos manuales?
    - ¿Cómo facilita Docker Compose el trabajo en equipo?

2. **Archivo docker-compose.yml:**
   
    - ¿Por qué se considera "Infrastructure as Code"?
    - ¿Qué ventajas tiene definir la infraestructura de forma declarativa?
    - ¿Cómo se versionaría este archivo en un proyecto real?

3. **Redes en Docker Compose:**
   
    - ¿Qué red se crea automáticamente si no se define una explícitamente?
    - ¿Cómo funcionan los nombres de servicio para la resolución DNS?
    - ¿Cuándo es necesario definir redes personalizadas?

4. **Volúmenes Docker vs. bind mount:**
   
    - ¿Qué ventajas tienen los volúmenes Docker sobre bind mounts?
    - ¿Cuándo usarías bind mount en Docker Compose?
    - ¿Cómo se gestionan los volúmenes con Docker Compose?

5. **Escalabilidad:**
   
    - ¿Por qué no se puede escalar el servicio `app` fácilmente?
    - ¿Cómo se podría modificar el archivo para permitir escalado?
    - ¿Se puede escalar el servicio de base de datos `db`?

6. **Políticas de reinicio:**
   
    - ¿Qué significa `restart: always`?
    - ¿Qué otras políticas de reinicio existen?
    - ¿En qué casos utilizarías cada una?

#### Tarea 5.2: Comparación con la Práctica 2.1

Crea una tabla comparativa entre la gestión manual (Práctica 2.1) y Docker Compose:

| Aspecto | Gestión Manual | Docker Compose |
|---------|----------------|----------------|
| Creación de red | | |
| Despliegue | | |
| Variables de entorno | | |
| Gestión de volúmenes | | |
| Inicio/detención | | |
| Escalabilidad | | |
| Reproducibilidad | | |
| Documentación | | |

---

### 🔹 Parte 6 (opcional): Gestión avanzada

#### Tarea 6.1: Múltiples entornos

1. Crea archivos `docker-compose.yml` para diferentes entornos:
   
    - `docker-compose.yml` - Configuración base
    - `docker-compose.dev.yml` - Override para desarrollo
    - `docker-compose.prod.yml` - Override para producción

2. Practica el uso de múltiples archivos:

```bash
docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d
```

#### Tarea 6.2: Healthchecks

1. Añade healthchecks a los servicios:

```yaml
services:
  db:
    image: redis
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 30s
      timeout: 3s
      retries: 3
```

2. Verifica el estado de salud de los servicios.

---

## Entregables

1. **Documentación en formato Markdown o PDF** que incluya:
   
    - Archivo `docker-compose.yml` final completo y comentado
    - Todos los comandos de Docker Compose utilizados
    - Capturas de pantalla que demuestren:
        - Creación del escenario con Docker Compose
        - Lista de servicios en ejecución
        - Logs de los servicios
        - Aplicación funcionando
        - Persistencia de datos tras recrear el escenario
        - Recursos creados automáticamente (red, volúmenes)
    - Tabla comparativa entre gestión manual y Docker Compose
    - Respuestas detalladas a todas las preguntas de análisis

2. **Archivos de configuración:**
   
    - `docker-compose.yml` - Versión básica
    - `docker-compose.yml` - Versión avanzada (con redes, límites, etc.)
    - `.env` - Archivo de variables de entorno (si lo usas)

---

### Evaluación

Se evaluará:

- La correcta escritura del archivo `docker-compose.yml`.
- El dominio de los comandos de Docker Compose.
- La comprensión de las ventajas de Docker Compose.
- La comparación crítica con la gestión manual.
- La profundidad del análisis técnico.
- La claridad y completitud de la documentación.

---

### Condiciones de entrega

Las publicadas en la plataforma Moodle del curso.

---

### Recursos de apoyo

- Documentación oficial de Docker Compose: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
- Referencia del archivo Compose: [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)
- CLI de Docker Compose: [https://docs.docker.com/compose/reference/](https://docs.docker.com/compose/reference/)
- Volúmenes en Docker: [https://docs.docker.com/storage/volumes/](https://docs.docker.com/storage/volumes/)
- Redes en Docker Compose: [https://docs.docker.com/compose/networking/](https://docs.docker.com/compose/networking/)
- Repositorio con ejemplos: [https://github.com/josedom24/curso_docker_ies](https://github.com/josedom24/curso_docker_ies)

---

### Presentación de la práctica

[:fontawesome-solid-file-pdf: Descargar presentación](https://revilofe.github.io/slides/section4-daw/DAW-U2.5.-DockerCompose.html){ .md-button }
