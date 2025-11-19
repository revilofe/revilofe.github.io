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

2. Crea el archivo `docker-compose.yml` para usar **volúmenes Docker**:

3. Analiza la configuración:
   
    - ¿Por qué hay dos volúmenes diferentes?
    - ¿Qué datos almacena cada volumen?
    - ¿Por qué WordPress usa `db` como hostname de la base de datos?

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

1. Crea un nuevo directorio: `~/wordpress_bind` y accede.

2. Crea los directorios para los datos:

```bash
mkdir -p wordpress mysql
```

3. Crea un `docker-compose.yml` usando **bind mounts**:

4. Despliega y configura WordPress de nuevo.

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

1. Crea un archivo `.env` con las siguientes variables:

    - MYSQL_ROOT_PASSWORD
    - MYSQL_DATABASE
    - MYSQL_USER
    - MYSQL_PASSWORD
    - WP_DB_HOST
    - WP_DB_USER
    - WP_DB_PASSWORD
    - WP_DB_NAME
    - WP_PORT

2. Modifica el `docker-compose.yml` para usar las variables del archivo `.env`:

3. Despliega y verifica que funciona.

#### Tarea 3.2: Configuración de red personalizada

1. Añade una red personalizada llamada `wordpress_net`, y modifica el archivo `docker-compose.yml` para conectar ambos servicios a esta red:

2. Verifica la configuración de red con Docker Compose.

#### Tarea 3.3: Healthchecks y límites de recursos

1. Añade healthchecks y límites:

    - cpus: 1 para WordPress
    - cpus: 0.5 para MariaDB
    - memoria: 512M para ambos
    - test: curl -f http://localhost para WordPress
    - interval: 30s
    - timeout: 10s
    - retries: 3
    - test: mysqladmin ping -h localhost para MariaDB
    - interval: 30s
    - timeout: 3s
    - retries: 3


2. Verifica el estado de salud de los servicios.

---

### 🔹 Parte 4: Backup y restauración

#### Tarea 4.1: Backup con volúmenes Docker

1. Realiza un backup de los volúmenes:

```bash
# Crear directorio de backups
mkdir -p backups

# Backup de WordPress
docker run --rm \
  -v wordpress_compose_wordpress_data:/data \
  -v $(pwd)/backups:/backup \
  alpine tar czf /backup/wordpress_backup.tar.gz -C /data .

# Backup de MariaDB
docker run --rm \
  -v wordpress_compose_mariadb_data:/data \
  -v $(pwd)/backups:/backup \
  alpine tar czf /backup/mysql_backup.tar.gz -C /data .
```

2. Verifica que los archivos de backup existen.

#### Tarea 4.2: Restauración desde backup

1. Elimina el escenario incluyendo volúmenes.

2. Recrea los volúmenes vacíos.

3. Restaura los datos:

```bash
# Restaurar WordPress
docker run --rm \
  -v wordpress_compose_wordpress_data:/data \
  -v $(pwd)/backups:/backup \
  alpine sh -c "cd /data && tar xzf /backup/wordpress_backup.tar.gz"

# Restaurar MariaDB
docker run --rm \
  -v wordpress_compose_mariadb_data:/data \
  -v $(pwd)/backups:/backup \
  alpine sh -c "cd /data && tar xzf /backup/mysql_backup.tar.gz"
```

4. Arranca el escenario y verifica que los datos se han restaurado.

#### Tarea 4.3: Backup con bind mounts

1. Para bind mounts, el backup es más simple:

```bash
tar czf wordpress_backup.tar.gz wordpress/
tar czf mysql_backup.tar.gz mysql/
```

2. Compara la facilidad de backup entre ambos enfoques.

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

