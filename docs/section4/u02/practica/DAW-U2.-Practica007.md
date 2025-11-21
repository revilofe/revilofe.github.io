---
title: "UD 2 - P7: Despliegue de WordPress con Docker Compose"
description: "Automatización del despliegue de WordPress y MariaDB con Docker Compose"
summary: "Actividad práctica para desplegar WordPress con MariaDB utilizando Docker Compose con volúmenes y bind mounts."
authors:
    - Eduardo Fdez
date: 2025-01-12
icon: 
permalink: /daw/unidad2/p2.7
categories:
    - DAW
tags:
    - Docker
    - Docker Compose
    - WordPress
    - MariaDB
    - CMS
    - Persistencia
---

## Relación 2.7

### Descripción

**Actividad:** *Despliegue de WordPress con MariaDB usando Docker Compose*

En esta práctica retomarás el despliegue de **WordPress con MariaDB** de la Práctica 2.3, pero utilizando **Docker Compose** para simplificar la gestión de esta aplicación compleja con múltiples contenedores, volúmenes y variables de entorno.

#### Objetivo general

Aprender a:

- Desplegar aplicaciones complejas con base de datos usando Docker Compose.
- Gestionar múltiples volúmenes de forma declarativa.
- Comparar volúmenes Docker vs. bind mounts en Docker Compose.
- Configurar aplicaciones con múltiples variables de entorno.
- Entender la gestión de datos persistentes con Compose.
- Realizar backups y migraciones de datos.

---

### Contexto de trabajo

**Recordatorio de WordPress:**

- **WordPress:** CMS en PHP con Apache (puerto 80/tcp) - imagen `wordpress`
- **MariaDB:** Base de datos relacional (puerto 3306/tcp) - imagen `mariadb`
- **Persistencia:** Dos volúmenes necesarios (WordPress y base de datos)
- **Variables:** Múltiples variables de entorno para la configuración

**Complejidad:**

Esta es la aplicación más compleja que has desplegado hasta ahora, con:

- Doble persistencia de datos
- Múltiples variables de entorno críticas
- Dependencia estricta entre servicios

---

### 🔹 Parte 1: Despliegue con volúmenes Docker

#### Tarea 1.1: Creación del archivo docker-compose.yml

1. Crea un directorio: `~/wordpress_compose`.

2. Investiga en la documentación de Docker Hub las imágenes de WordPress y MariaDB para identificar:
   
    - Variables de entorno necesarias para WordPress
    - Variables de entorno necesarias para MariaDB
    - Puertos que utilizan
    - Directorios para persistencia de datos

3. Crea un archivo `docker-compose.yml` que defina:
   
    **Servicio de WordPress:**
    - Imagen: `wordpress`
    - Puerto 80 del host mapeado al puerto del contenedor
    - Variables de entorno necesarias para conexión a base de datos
    - Volumen Docker para el contenido de WordPress (`/var/www/html/wp-content`)
    - Dependencia del servicio de base de datos
    - Política de reinicio automático
    
    **Servicio de MariaDB:**
    - Imagen: `mariadb`
    - Variables de entorno para configuración inicial (base de datos, usuario, contraseñas)
    - Volumen Docker para los datos de la base de datos (`/var/lib/mysql`)
    - Política de reinicio automático
    
    **Volúmenes:** Define dos volúmenes Docker (uno para WordPress, otro para MariaDB)

4. Analiza y responde:
   
    - ¿Por qué hay dos volúmenes diferentes?
    - ¿Qué datos almacena cada volumen?
    - ¿Por qué WordPress usa el nombre del servicio de base de datos como hostname?

#### Tarea 1.2: Despliegue y configuración

1. Despliega el escenario con Docker Compose.

2. Observa qué recursos se crean automáticamente.

3. Verifica el estado de los servicios.

4. Accede a WordPress (http://localhost) y completa la instalación:
   
    - Título del sitio
    - Usuario administrador
    - Contraseña
    - Email

5. Crea contenido:
   
    - Al menos 3 páginas
    - Al menos 5 posts/entradas
    - Instala y activa un tema
    - Instala al menos 2 plugins

#### Tarea 1.3: Gestión del escenario

1. **Detener servicios:**
   
    - Detén ambos servicios
    - Verifica que están detenidos pero no eliminados

2. **Reiniciar y verificar persistencia:**
   
    - Arranca los servicios nuevamente
    - Accede a WordPress
    - Verifica que todo el contenido persiste

3. **Eliminar contenedores (sin volúmenes):**
   
    - Elimina el escenario manteniendo los volúmenes
    - Verifica que los volúmenes siguen existiendo
    - Recrea el escenario
    - Comprueba que los datos persisten

4. **Eliminar todo (con volúmenes):**
   
    - Elimina el escenario incluyendo volúmenes
    - Verifica que los volúmenes se han eliminado
    - Recrea el escenario
    - Comprueba que WordPress pide instalación inicial

---

### 🔹 Parte 2: Despliegue con bind mounts

#### Tarea 2.1: Archivo docker-compose.yml con bind mount

1. Crea un nuevo directorio: `~/wordpress_bind`.

2. Crea los directorios necesarios para los bind mounts:
   
    - Directorio para datos de WordPress
    - Directorio para datos de MySQL/MariaDB

3. Crea un nuevo archivo `docker-compose.yml` que use **bind mounts** en lugar de volúmenes Docker:
   
    - Investiga la sintaxis para bind mounts en Docker Compose
    - Usa rutas relativas (`./directorio`) para montar desde el host
    - Mantén la misma estructura de servicios que en la Parte 1
    - Cambia solo la definición de volúmenes por bind mounts

4. Despliega la aplicación y configura WordPress nuevamente.

#### Tarea 2.2: Comparación de enfoques

1. Explora los directorios `wordpress` y `mysql` en el host.

2. Identifica qué archivos hay en cada directorio.

3. Compara con los volúmenes Docker:
   
    | Aspecto                | Volúmenes Docker  | Bind Mounts  |
    |------------------------|-------------------|--------------|
    | Ubicación              |                   |              |
    | Visibilidad desde host |                   |              |
    | Portabilidad           |                   |              |
    | Backups                |                   |              |
    | Permisos               |                   |              |

---

### 🔹 Parte 3: Configuración avanzada

#### Tarea 3.1: Variables de entorno desde archivo

1. Investiga cómo usar archivos `.env` con Docker Compose.

2. Crea un archivo `.env` que contenga todas las variables de configuración:
   
    - Contraseña root de MySQL
    - Nombre de la base de datos
    - Usuario de la base de datos
    - Contraseña del usuario
    - Variables correspondientes para WordPress
    - Puerto de WordPress

3. Modifica tu `docker-compose.yml` para usar variables del archivo `.env` con la sintaxis `${VARIABLE}`.

4. Despliega y verifica que funciona correctamente.

5. Reflexiona sobre las ventajas de seguridad de este enfoque.

#### Tarea 3.2: Configuración de red personalizada

1. Investiga en la documentación cómo definir redes personalizadas en Docker Compose.

2. Modifica tu archivo `docker-compose.yml` para incluir:
   
    - Definición de una red personalizada tipo bridge
    - Conecta ambos servicios a esta red
    - Usa un nombre descriptivo para la red

3. Verifica la configuración de red usando comandos de Docker Compose e inspección de red.

#### Tarea 3.3: Healthchecks y límites de recursos

1. Investiga la sintaxis de healthchecks y límites de recursos en Docker Compose.

2. Añade a tu archivo `docker-compose.yml`:
   
    **Para WordPress:**
    - Healthcheck que verifique la disponibilidad del puerto 80
    - Límites: 1 CPU y 512MB de memoria

    - cpus: 1 para WordPress
    - memoria: 512M para ambos
    - test: curl -f http://localhost para WordPress
    - interval: 30s
    - timeout: 10s
    - retries: 3
    
    **Para MariaDB:**
    - Healthcheck que verifique la disponibilidad de MySQL
    - Límites: 0.5 CPU y 512MB de memoria

    - cpus: 0.5 para MariaDB
    - memoria: 512M para ambos
    - test: mysqladmin ping -h localhost para MariaDB
    - interval: 30s
    - timeout: 3s
    - retries: 3


3. Investiga qué comando usar para verificar el estado de salud de los servicios.

4. Verifica que los healthchecks funcionan correctamente.

---

### 🔹 Parte 4: Backup y restauración

#### Tarea 4.1: Backup con volúmenes Docker

1. Investiga estrategias para realizar backups de volúmenes Docker.

2. Crea un directorio para backups.

3. Investiga y ejecuta comandos para:
   
    - Crear un backup del volumen de WordPress usando un contenedor temporal
    - Crear un backup del volumen de MariaDB usando un contenedor temporal
    - Comprimir los datos en archivos tar.gz
    - Almacenar los backups en el directorio del host

4. Verifica que los archivos de backup se han creado correctamente.

**Pista:** Necesitarás usar contenedores temporales que monten el volumen y un directorio de backup.

#### Tarea 4.2: Restauración desde backup

1. Elimina el escenario completo incluyendo los volúmenes.

2. Vuelve a crear el escenario (se crearán volúmenes vacíos).

3. Investiga y ejecuta comandos para restaurar los datos desde los backups:
   
    - Usa contenedores temporales para descomprimir y restaurar datos
    - Restaura el volumen de WordPress
    - Restaura el volumen de MariaDB

4. Arranca el escenario con Docker Compose.

5. Verifica que todos los datos se han restaurado correctamente (contenido, configuración, base de datos).

**Reflexión:** ¿Por qué es importante probar regularmente los procesos de restauración?

#### Tarea 4.3: Backup con bind mounts

1. Para el escenario con bind mounts, el backup es más directo.

2. Investiga qué comandos del sistema operativo puedes usar para:
   
    - Crear copias de seguridad de directorios completos
    - Comprimir los directorios en archivos tar.gz
    - Verificar la integridad de los backups

3. Realiza backups de ambos directorios (wordpress y mysql).

4. Compara las ventajas y desventajas del backup con bind mounts vs. volúmenes Docker:
   
    - Facilidad de ejecución
    - Necesidad de comandos Docker
    - Visibilidad de los datos
    - Portabilidad

---

### 🔹 Parte 5: Análisis y documentación

#### Tarea 5.1: Preguntas de análisis

Responde en tu documentación:

1. **Volúmenes vs. bind mounts:**
   
    - ¿Cuándo preferirías volúmenes Docker?
    - ¿Cuándo preferirías bind mounts?
    - ¿Cuál es más fácil para backups?

2. **Seguridad:**
   
    - ¿Es seguro tener las contraseñas en el archivo Compose?
    - ¿Cómo mejorarías la seguridad usando `.env`?
    - ¿Qué otras medidas de seguridad aplicarías?

3. **Persistencia:**
   
    - ¿Qué pasaría si pierdes el volumen de WordPress?
    - ¿Y si pierdes el volumen de MariaDB?
    - ¿Cuál es más crítico?

4. **Dependencias:**
   
    - ¿Por qué WordPress depende de la base de datos?
    - ¿Qué pasa si intentas iniciar WordPress sin MariaDB?
    - ¿`depends_on` garantiza que MariaDB esté lista?

5. **Comparación con práctica anterior:**
   
    - ¿Cuántos comandos necesitabas en la Práctica 2.3?
    - ¿Cuántos comandos necesitas con Docker Compose?
    - ¿Qué es más fácil de mantener?

#### Tarea 5.2: Escenarios de uso

Describe cómo usarías cada enfoque en estos escenarios:

1. **Desarrollo local:** ¿Volúmenes o bind mounts?
2. **Producción:** ¿Volúmenes o bind mounts?
3. **Testing/CI:** ¿Volúmenes o bind mounts?

---

## Entregables

1. **Documentación en formato Markdown** con:
   
    - Ambos archivos `docker-compose.yml` (volúmenes y bind mounts)
    - Archivo `.env` con variables de entorno
    - Todos los comandos utilizados
    - Capturas de pantalla:
        - WordPress funcionando
        - Contenido creado (páginas, posts, tema, plugins)
        - Servicios en ejecución
        - Estructura de volúmenes/directorios
        - Proceso de backup y restauración
        - Healthchecks
    - Respuestas a todas las preguntas
    - Comparación volúmenes vs. bind mounts
    - Comparación con gestión manual (Práctica 2.3)

2. **Archivos de configuración:**
   
    - `docker-compose.yml` con volúmenes
    - `docker-compose.yml` con bind mounts
    - `docker-compose.yml` completo (con redes, healthchecks, etc.)
    - `.env`

---

### Evaluación

Se evaluará:

- Correcta configuración con volúmenes y bind mounts.
- Comprensión de persistencia de datos.
- Realización exitosa de backups y restauración.
- Análisis crítico de diferentes enfoques.
- Comparación con gestión manual.

---

### Condiciones de entrega

Las publicadas en la plataforma Moodle del curso.

---

### Recursos de apoyo

- Documentación oficial de Docker Compose: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
- Volúmenes en Compose: [https://docs.docker.com/compose/compose-file/07-volumes/](https://docs.docker.com/compose/compose-file/07-volumes/)
- WordPress en Docker: [https://hub.docker.com/_/wordpress](https://hub.docker.com/_/wordpress)
- MariaDB en Docker: [https://hub.docker.com/_/mariadb](https://hub.docker.com/_/mariadb)
- Backups de volúmenes: [https://docs.docker.com/storage/volumes/#back-up-restore-or-migrate-data-volumes](https://docs.docker.com/storage/volumes/#back-up-restore-or-migrate-data-volumes)

