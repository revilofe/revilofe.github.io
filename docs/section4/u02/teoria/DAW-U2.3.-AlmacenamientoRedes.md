---
title: "UD 2 - 2.3 Almacenamiento y redes en Docker"
description: Volúmenes, bind mounts y redes en Docker
summary: Persistencia de datos, volúmenes Docker, bind mount, redes
authors:
    - Eduardo Fdez
date: 2025-01-23
icon: 
permalink: /daw/unidad2/2.3
categories:
    - DAW
tags:
    - Docker
    - Volúmenes
    - Redes
    - Almacenamiento
---

## 2.3. Almacenamiento y redes en Docker

Los contenedores Docker son efímeros por naturaleza. Esto significa que cuando un contenedor se elimina, todos los datos almacenados en él se pierden. Para solucionar esto, Docker proporciona mecanismos de almacenamiento persistente. Además, los contenedores necesitan comunicarse entre sí, para lo cual Docker ofrece diferentes tipos de redes.

### 1. Almacenamiento en Docker

#### 1.1. Tipos de almacenamiento

Docker ofrece tres mecanismos principales para persistir datos:

1. **Volúmenes Docker** (recomendado)
2. **Bind mounts**
3. **tmpfs mounts** (datos temporales en memoria)

#### 1.2. Volúmenes Docker

Los volúmenes son el mecanismo preferido para persistir datos. Son gestionados completamente por Docker.

**Características:**

- Gestionados por Docker
- Independientes del sistema de archivos del host
- Pueden ser compartidos entre contenedores
- Fáciles de respaldar y migrar
- Funcionan en Linux y Windows

**Comandos básicos:**

```bash
# Crear un volumen
$ docker volume create mi_volumen

# Listar volúmenes
$ docker volume ls

# Inspeccionar un volumen
$ docker volume inspect mi_volumen

# Eliminar un volumen
$ docker volume rm mi_volumen

# Eliminar volúmenes no utilizados
$ docker volume prune
```

**Usar volúmenes en contenedores:**

```bash
# Montar volumen en /datos del contenedor
$ docker run -d --name app \
  -v mi_volumen:/datos \
  ubuntu

# Verificar montaje
$ docker inspect app
```

#### 1.3. Bind mounts

Los bind mounts vinculan un directorio del host con un directorio del contenedor.

**Ventajas:**
- Acceso directo a archivos del host
- Útil para desarrollo
- Compartir configuraciones

**Desventajas:**
- Dependen de la estructura del host
- Menos portables que volúmenes

**Uso:**

```bash
# Montar directorio del host
$ docker run -d --name web \
  -v /home/usuario/web:/usr/share/nginx/html \
  nginx

# Sintaxis alternativa con --mount
$ docker run -d --name web \
  --mount type=bind,source=/home/usuario/web,target=/usr/share/nginx/html \
  nginx
```

#### 1.4. Ejemplo: Base de datos con volumen

```bash
# Crear volumen para MySQL
$ docker volume create mysql_data

# Ejecutar MySQL con volumen persistente
$ docker run -d \
  --name mysql_db \
  -e MYSQL_ROOT_PASSWORD=secreto \
  -e MYSQL_DATABASE=miapp \
  -v mysql_data:/var/lib/mysql \
  mysql:8.0

# Los datos persisten aunque eliminemos el contenedor
$ docker rm -f mysql_db

# Al crear nuevo contenedor con el mismo volumen, los datos siguen ahí
$ docker run -d \
  --name mysql_db_nuevo \
  -e MYSQL_ROOT_PASSWORD=secreto \
  -v mysql_data:/var/lib/mysql \
  mysql:8.0
```

### 2. Redes en Docker

Docker proporciona diferentes tipos de redes para la comunicación entre contenedores.

#### 2.1. Tipos de redes

1. **bridge** (predeterminada): Red privada interna
2. **host**: Usa la red del host directamente
3. **none**: Sin conectividad de red
4. **overlay**: Para Docker Swarm (múltiples hosts)
5. **macvlan**: Asigna MAC address al contenedor

#### 2.2. Red bridge (predeterminada)

Todos los contenedores se conectan a la red bridge por defecto.

```bash
# Ver redes disponibles
$ docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
a1b2c3d4e5f6   bridge    bridge    local
1234567890ab   host      host      local
fedcba098765   none      null      local

# Inspeccionar la red bridge
$ docker network inspect bridge
```

**Características de la red bridge predeterminada:**

- Aislamiento entre contenedores
- Comunicación por IP
- Puerto mapping necesario para acceso desde host

#### 2.3. Redes definidas por el usuario

Es recomendable crear redes personalizadas para mejor control y seguridad.

**Ventajas:**

- Resolución DNS automática por nombre de contenedor
- Mejor aislamiento
- Conexión/desconexión dinámica de contenedores
- Configuración personalizada

**Comandos:**

```bash
# Crear red personalizada
$ docker network create mi_red

# Crear red con configuración específica
$ docker network create \
  --driver bridge \
  --subnet 172.20.0.0/16 \
  --gateway 172.20.0.1 \
  mi_red_custom

# Conectar contenedor a la red
$ docker run -d --name app --network mi_red nginx

# Conectar contenedor existente a una red
$ docker network connect mi_red contenedor1

# Desconectar de una red
$ docker network disconnect mi_red contenedor1

# Eliminar red
$ docker network rm mi_red
```

#### 2.4. Comunicación entre contenedores

**En red personalizada (recomendado):**

```bash
# Crear red
$ docker network create app_network

# Contenedor 1: Base de datos
$ docker run -d \
  --name db \
  --network app_network \
  -e MYSQL_ROOT_PASSWORD=secreto \
  mysql:8.0

# Contenedor 2: Aplicación
$ docker run -d \
  --name app \
  --network app_network \
  mi_aplicacion

# La aplicación puede conectarse a la BD usando 'db' como hostname
# Ejemplo: mysql://db:3306/midb
```

### 3. Ejemplos prácticos

#### 3.1. WordPress con MySQL

```bash
# Crear red y volúmenes
$ docker network create wordpress_net
$ docker volume create wp_db
$ docker volume create wp_files

# MySQL
$ docker run -d \
  --name wordpress_db \
  --network wordpress_net \
  -v wp_db:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secreto \
  -e MYSQL_DATABASE=wordpress \
  -e MYSQL_USER=wpuser \
  -e MYSQL_PASSWORD=wppass \
  mysql:8.0

# WordPress
$ docker run -d \
  --name wordpress \
  --network wordpress_net \
  -p 8080:80 \
  -v wp_files:/var/www/html \
  -e WORDPRESS_DB_HOST=wordpress_db \
  -e WORDPRESS_DB_NAME=wordpress \
  -e WORDPRESS_DB_USER=wpuser \
  -e WORDPRESS_DB_PASSWORD=wppass \
  wordpress
```

#### 3.2. Aplicación web con Nginx y Tomcat

```bash
# Crear red
$ docker network create web_network

# Tomcat (backend)
$ docker run -d \
  --name tomcat \
  --network web_network \
  tomcat:9.0

# Nginx (proxy inverso)
$ docker run -d \
  --name nginx \
  --network web_network \
  -p 80:80 \
  -v /ruta/nginx.conf:/etc/nginx/nginx.conf:ro \
  nginx
```

### 4. Buenas prácticas

1. **Usar volúmenes** para datos persistentes
2. **Crear redes personalizadas** por aplicación
3. **Nombrar volúmenes y redes** descriptivamente
4. **Aislar aplicaciones** en redes diferentes
5. **Limpiar recursos** no utilizados regularmente

```bash
# Limpieza general
$ docker system prune -a --volumes
```

### Resumen

En esta sección hemos aprendido:

- ✅ Tipos de almacenamiento en Docker
- ✅ Uso de volúmenes y bind mounts
- ✅ Persistencia de datos en contenedores
- ✅ Tipos de redes en Docker
- ✅ Crear y gestionar redes personalizadas
- ✅ Comunicación entre contenedores
- ✅ Despliegue de aplicaciones multi-contenedor

### Recursos adicionales

- [Documentación sobre volúmenes](https://docs.docker.com/storage/volumes/)
- [Documentación sobre redes](https://docs.docker.com/network/)
- [Curso Docker IES - Módulo 3](../u01/teoria/OtrosRecursos/curso_docker_ies/modulo3/)

!!! tip "Siguiente paso"
    En la siguiente sección aprenderemos Docker Compose para gestionar aplicaciones multi-contenedor de forma más sencilla.
