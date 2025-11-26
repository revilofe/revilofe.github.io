---
title: "UD 2 - P5: Despliegue de Guestbook con Docker Compose"
description: "Automatización del despliegue de Guestbook usando Docker Compose"
summary: "Actividad práctica para desplegar la aplicación Guestbook utilizando Docker Compose y gestionar escenarios multi-contenedor de forma declarativa."
authors:
    - Eduardo Fdez
date: 2025-01-12
icon: "material/file-document-edit"
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

2. Investiga la estructura de un archivo `docker-compose.yml` consultando la documentación oficial.

3. Crea un archivo `docker-compose.yml` que defina:
   
    - **Versión del formato:** Investiga qué versión de Docker Compose usar (mínimo 3.1)
    - **Dos servicios:**
        - Servicio para la aplicación Guestbook (imagen `iesgn/guestbook`)
        - Servicio para la base de datos Redis (imagen `redis`)
    
    - **Para el servicio de Guestbook:**
        - Nombre del contenedor
        - Puerto del host mapeado al puerto 5000 del contenedor
        - Variable de entorno que indica el servidor Redis
        - Política de reinicio automático
    
    - **Para el servicio de Redis:**
        - Nombre del contenedor
        - Comando para ejecutar Redis con persistencia (modo append-only)
        - Volumen Docker para almacenar datos en `/data`
        - Política de reinicio automático
    
    - **Volúmenes:** Define el volumen Docker necesario

4. Consulta la documentación de Docker Compose para entender:
   
    - La sintaxis YAML correcta
    - Cómo definir servicios
    - Cómo configurar volúmenes
    - Cómo establecer variables de entorno
    - Políticas de reinicio disponibles

#### Tarea 1.3: Comprensión de las diferencias

Compara el archivo `docker-compose.yml` con los comandos de la Práctica 2.1:

1. **Red:** ¿Por qué no se define explícitamente la red en el archivo Compose?

2. **Volumen:** ¿Qué diferencia hay entre usar un volumen Docker (`redis:`) y un bind mount (`/opt/redis:/data`)?

3. **Variables de entorno:** Aunque la variable `REDIS_SERVER` es `redis` por defecto, ¿por qué es buena práctica declararla explícitamente?

4. **Nombres de servicios:** ¿Cuál es la diferencia entre el nombre del servicio (`db`) y el nombre del contenedor (`redis`)?

---

### 🔹 Parte 2: Gestión del escenario con Docker Compose

#### Tarea 2.1: Despliegue del escenario

1. Investiga qué comando de Docker Compose sirve para crear y arrancar servicios en segundo plano.

2. Ejecuta el comando desde el directorio donde está el archivo `docker-compose.yml`.

3. Observa la salida del comando. ¿Qué recursos se crean automáticamente?

4. Investiga y ejecuta el comando para listar los contenedores gestionados por Docker Compose.

5. Accede a la aplicación desde tu navegador en el puerto que configuraste.

6. Añade varios mensajes en el libro de visitas.

#### Tarea 2.2: Gestión del ciclo de vida

1. **Ver logs:**
   
    - Investiga el comando para ver logs de todos los servicios
    - Investiga cómo ver logs de un servicio específico
    - Visualiza los logs del servicio de aplicación
    - Visualiza los logs del servicio de base de datos

2. **Detener servicios:**
   
    - Investiga el comando para detener servicios sin eliminarlos
    - Detén todos los servicios
    - Verifica el estado de los contenedores
    - Intenta acceder a la aplicación (debería estar inaccesible)

3. **Reiniciar servicios:**
   
    - Investiga el comando para arrancar servicios detenidos
    - Arranca nuevamente los servicios
    - Verifica que los datos persisten

4. **Escalar servicios (opcional):**
   
    - Investiga el comando para escalar servicios
    - Intenta escalar el servicio de aplicación a 3 instancias
    - Observa qué problemas aparecen y analiza por qué

#### Tarea 2.3: Eliminación del escenario

1. **Eliminar sin volúmenes:**
   
    - Investiga el comando para eliminar el escenario manteniendo los volúmenes
    - Ejecuta el comando y observa qué recursos se eliminan
    - Verifica con comandos Docker que el volumen sigue existiendo

2. **Recrear y verificar persistencia:**
   
    - Vuelve a crear el escenario con Docker Compose
    - Verifica que los datos del libro de visitas persisten

3. **Eliminar con volúmenes:**
   
    - Investiga el comando para eliminar el escenario incluyendo volúmenes
    - Ejecuta el comando y verifica que el volumen también se ha eliminado
    - Recrea el escenario
    - Comprueba que el libro de visitas está vacío (instalación nueva)

---

### 🔹 Parte 3: Modificación y personalización

#### Tarea 3.1: Cambio del puerto de la aplicación

1. Modifica el archivo `docker-compose.yml` para que la aplicación sea accesible en el puerto 9090 del host.

2. Investiga qué comando recrear el escenario aplicando los cambios sin perder datos.

3. Accede a la aplicación en el nuevo puerto y verifica que funciona.

#### Tarea 3.2: Configuración avanzada

1. Investiga en la documentación de Docker Compose cómo añadir:
   
    - Límites de recursos (CPU y memoria)
    - Redes personalizadas explícitas

2. Modifica tu archivo `docker-compose.yml` para incluir:
   
    - **Límites de recursos** para el servicio de aplicación:
        - Límite de memoria: 256MB
        - Límite de CPU: 0.5
    
    - **Red personalizada:**
        - Crea una red tipo bridge con nombre personalizado
        - Conecta ambos servicios a esta red

3. Aplica los cambios y verifica que el escenario funciona correctamente.

#### Tarea 3.3: Variables de entorno desde archivo

1. Investiga cómo Docker Compose utiliza archivos `.env` para variables de entorno.

2. Crea un archivo `.env` que contenga:
   
    - Variable para el puerto de la aplicación Guestbook
    - Variable para el nombre del contenedor/servicio de Redis

3. Modifica tu `docker-compose.yml` para usar estas variables con la sintaxis `${NOMBRE_VARIABLE}`.

4. Despliega y verifica que funciona con las variables del archivo `.env`.

5. Prueba a cambiar los valores en `.env` y verifica que se aplican correctamente.

---

### 🔹 Parte 4: Comandos de Docker Compose

#### Tarea 4.1: Comandos esenciales

Investiga, practica y documenta los comandos de Docker Compose para:

1. **Crear y arrancar:**
   
    - Arrancar en primer plano (ver la salida directamente)
    - Arrancar en segundo plano (modo daemon)
    - Forzar recreación de contenedores aunque no hayan cambiado

2. **Información:**
   
    - Ver estado de servicios
    - Ver procesos en ejecución dentro de los contenedores
    - Ver la configuración final con variables de entorno resueltas

3. **Gestión:**
   
    - Detener servicios sin eliminarlos
    - Arrancar servicios que están detenidos
    - Reiniciar servicios
    - Pausar y despausar servicios

4. **Logs:**
   
    - Ver logs de todos los servicios
    - Ver logs de un servicio específico
    - Seguir logs en tiempo real (modo follow)

5. **Limpieza:**
   
    - Eliminar escenario manteniendo volúmenes
    - Eliminar escenario incluyendo volúmenes
    - Eliminar imágenes que ya no se utilizan

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

| Aspecto              | Gestión Manual  | Docker Compose  |
|----------------------|-----------------|-----------------|
| Creación de red      |                 |                 |
| Despliegue           |                 |                 |
| Variables de entorno |                 |                 |
| Gestión de volúmenes |                 |                 |
| Inicio/detención     |                 |                 |
| Escalabilidad        |                 |                 |
| Reproducibilidad     |                 |                 |
| Documentación        |                 |                 |

---

### 🔹 Parte 6 (opcional): Gestión avanzada

#### Tarea 6.1: Múltiples entornos

1. Investiga cómo Docker Compose permite usar múltiples archivos para diferentes entornos.

2. Crea archivos para diferentes entornos:
   
    - `docker-compose.yml` - Configuración base común
    - `docker-compose.dev.yml` - Configuración específica de desarrollo (ej: puertos diferentes, logging verbose)
    - `docker-compose.prod.yml` - Configuración específica de producción (ej: límites de recursos, restart policies)

3. Investiga la sintaxis del comando para usar múltiples archivos simultáneamente.

4. Prueba a desplegar con diferentes combinaciones de archivos.

#### Tarea 6.2: Healthchecks

1. Investiga qué son los healthchecks en Docker Compose y para qué sirven.

2. Investiga la sintaxis de healthchecks en el archivo `docker-compose.yml`:
   
    - Comando de test
    - Intervalo entre comprobaciones
    - Timeout
    - Número de reintentos

3. Añade un healthcheck al servicio de Redis que verifique su disponibilidad.

4. Investiga el comando para ver el estado de salud de los servicios.

5. Verifica que el healthcheck funciona correctamente.

---

## Entregables

1. **Documentación en formato Markdown** que incluya:
   
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
