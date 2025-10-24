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

**Comandos básicos explicados:**

**Crear un volumen:**

```bash
$ docker volume create mi_volumen
mi_volumen
```

- Crea un volumen gestionado por Docker
- Se almacena en `/var/lib/docker/volumes/` (Linux)
- Docker gestiona automáticamente permisos y persistencia

**Listar volúmenes:**

```bash
$ docker volume ls
DRIVER    VOLUME NAME
local     mi_volumen
local     mysql_data
local     wp_files
```

- `DRIVER`: Controlador de almacenamiento (normalmente `local`)
- `VOLUME NAME`: Nombre del volumen

**Inspeccionar un volumen:**

```bash
$ docker volume inspect mi_volumen
[
    {
        "CreatedAt": "2024-01-23T17:00:00Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/mi_volumen/_data",
        "Name": "mi_volumen",
        "Options": {},
        "Scope": "local"
    }
]
```

**Información relevante:**

- `Mountpoint`: Ruta física donde Docker almacena los datos
- `Driver`: Tipo de almacenamiento (local, nfs, etc.)
- `Scope`: Alcance (local = solo en este host)

**Eliminar un volumen:**

```bash
$ docker volume rm mi_volumen
mi_volumen
```

!!! warning "No se puede eliminar si está en uso"
    Si un contenedor usa el volumen, debes detenerlo primero.

**Eliminar volúmenes no utilizados:**

```bash
$ docker volume prune
WARNING! This will remove all local volumes not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Volumes:
volumen_antiguo
volumen_temporal
Total reclaimed space: 1.2GB
```

**Usar volúmenes en contenedores:**

```bash
$ docker run -d --name app \
  -v mi_volumen:/datos \
  ubuntu sleep infinity
```

**Explicación del montaje:**

- `-v mi_volumen:/datos`: Sintaxis es `volumen:ruta_en_contenedor`
- `mi_volumen`: Volumen de Docker (si no existe, se crea automáticamente)
- `/datos`: Directorio dentro del contenedor donde se montará
- Cualquier dato guardado en `/datos` persistirá en el volumen

**Verificar el montaje:**

```bash
$ docker inspect app | grep -A 10 "Mounts"
"Mounts": [
    {
        "Type": "volume",
        "Name": "mi_volumen",
        "Source": "/var/lib/docker/volumes/mi_volumen/_data",
        "Destination": "/datos",
        "Driver": "local",
        "Mode": "z",
        "RW": true,
        "Propagation": ""
    }
],
```

**Probar la persistencia:**

```bash
# Escribir datos en el volumen
$ docker exec app sh -c "echo 'datos importantes' > /datos/archivo.txt"

# Eliminar el contenedor
$ docker rm -f app

# Crear nuevo contenedor con el mismo volumen
$ docker run -d --name app2 -v mi_volumen:/datos ubuntu sleep infinity

# Verificar que los datos persisten
$ docker exec app2 cat /datos/archivo.txt
datos importantes
```

!!! tip "Los datos sobreviven"
    Aunque elimines todos los contenedores, los datos en el volumen permanecen hasta que elimines el volumen explícitamente.

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

**Comandos explicados:**

**Crear red personalizada (simple):**

```bash
$ docker network create mi_red
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
```

- Crea una red bridge con configuración automática
- Docker asigna automáticamente una subred (ej: 172.18.0.0/16)
- Los contenedores en esta red pueden comunicarse por nombre

**Crear red con configuración específica:**

```bash
$ docker network create \
  --driver bridge \
  --subnet 172.20.0.0/16 \
  --gateway 172.20.0.1 \
  mi_red_custom
```

**Explicación de cada parámetro:**

- `--driver bridge`: Tipo de red (bridge para un solo host)
- `--subnet 172.20.0.0/16`: Rango de IPs disponibles
  - `/16` = 65,536 direcciones IP (172.20.0.0 a 172.20.255.255)
- `--gateway 172.20.0.1`: Puerta de enlace (IP del host Docker)

**¿Qué significa cada valor?**

```
172.20.0.0/16 → Rango de red
172.20.0.1    → Gateway (conexión a internet/host)
172.20.0.2+   → IPs disponibles para contenedores
```

**Conectar contenedor nuevo a la red:**

```bash
$ docker run -d --name app --network mi_red nginx
```

- El contenedor se conecta a `mi_red` desde el inicio
- Obtiene automáticamente una IP de la red (ej: 172.20.0.2)
- Puede resolver otros contenedores por nombre

**Conectar contenedor existente:**

```bash
$ docker network connect mi_red contenedor1
```

**¿Qué hace esto?**

1. Añade una segunda interfaz de red al contenedor
2. Ahora el contenedor está en DOS redes simultáneamente
3. Puede comunicarse con contenedores de ambas redes

**Ejemplo práctico:**

```bash
# Contenedor en red predeterminada
$ docker run -d --name web nginx

# Conectar a red personalizada
$ docker network connect mi_red web

# Verificar (tiene dos IPs)
$ docker inspect web | grep IPAddress
"IPAddress": "172.17.0.2",  # Red bridge default
"IPAddress": "172.20.0.2",  # mi_red
```

**Desconectar de una red:**

```bash
$ docker network disconnect mi_red contenedor1
```

- Elimina la interfaz de red de esa red específica
- El contenedor sigue funcionando en sus otras redes

**Eliminar red:**

```bash
$ docker network rm mi_red
mi_red
```

!!! warning "Solo redes sin contenedores"
    No puedes eliminar una red si todavía tiene contenedores conectados.

**Limpieza de redes sin uso:**

```bash
$ docker network prune
WARNING! This will remove all custom networks not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Networks:
red_antigua
red_test
```

**Inspeccionar una red:**

```bash
$ docker network inspect mi_red
[
    {
        "Name": "mi_red",
        "Id": "a1b2c3d4e5f6",
        "Driver": "bridge",
        "Scope": "local",
        "IPAM": {
            "Config": [
                {
                    "Subnet": "172.20.0.0/16",
                    "Gateway": "172.20.0.1"
                }
            ]
        },
        "Containers": {
            "abc123": {
                "Name": "app",
                "IPv4Address": "172.20.0.2/16"
            }
        }
    }
]
```

**Información útil:**

- `Containers`: Qué contenedores están conectados
- `IPv4Address`: IP asignada a cada contenedor
- `IPAM`: Configuración de direccionamiento IP

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

#### 3.1. WordPress con MySQL (Paso a paso)

Este ejemplo completo muestra cómo desplegar WordPress conectado a MySQL con datos persistentes.

**Paso 1: Crear la infraestructura**

```bash
# Crear red privada para que WordPress y MySQL se comuniquen
$ docker network create wordpress_net
wordpress_net

# Crear volúmenes para datos persistentes
$ docker volume create wp_db        # Para la base de datos
wp_db
$ docker volume create wp_files     # Para archivos de WordPress
wp_files
```

**Paso 2: Lanzar MySQL**

```bash
$ docker run -d \
  --name wordpress_db \
  --network wordpress_net \
  -v wp_db:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secreto \
  -e MYSQL_DATABASE=wordpress \
  -e MYSQL_USER=wpuser \
  -e MYSQL_PASSWORD=wppass \
  mysql:8.0
```

**Explicación línea por línea:**

- `--name wordpress_db`: Nombre que usará WordPress para conectarse
- `--network wordpress_net`: Conectar a nuestra red privada
- `-v wp_db:/var/lib/mysql`: Persistir base de datos en volumen
- `-e MYSQL_ROOT_PASSWORD`: Contraseña del administrador de MySQL
- `-e MYSQL_DATABASE=wordpress`: Crear BD "wordpress" automáticamente
- `-e MYSQL_USER=wpuser`: Crear usuario "wpuser"
- `-e MYSQL_PASSWORD=wppass`: Contraseña del usuario
- `mysql:8.0`: Usar MySQL versión 8.0

**Verificar que MySQL está funcionando:**

```bash
$ docker logs wordpress_db | grep "ready for connections"
2024-01-23 17:00:00 [Note] mysqld: ready for connections.
```

**Paso 3: Lanzar WordPress**

```bash
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

**Explicación línea por línea:**

- `--name wordpress`: Nombre del contenedor
- `--network wordpress_net`: Misma red que MySQL (pueden comunicarse)
- `-p 8080:80`: Accesible desde navegador en puerto 8080
- `-v wp_files:/var/www/html`: Persistir archivos de WordPress
- `-e WORDPRESS_DB_HOST=wordpress_db`: **Nombre del contenedor MySQL**
  - ¡Docker resuelve este nombre automáticamente a la IP de MySQL!
- `-e WORDPRESS_DB_NAME=wordpress`: Nombre de la base de datos
- `-e WORDPRESS_DB_USER/PASSWORD`: Credenciales de MySQL

**¿Cómo se conectan WordPress y MySQL?**

```
WordPress contenedor (172.20.0.3)
      ↓
Busca: wordpress_db (nombre)
      ↓
DNS de Docker resuelve: wordpress_db = 172.20.0.2
      ↓
WordPress conecta a: 172.20.0.2:3306
      ↓
MySQL contenedor (172.20.0.2)
```

**Paso 4: Acceder a WordPress**

Abre tu navegador: `http://localhost:8080`

Verás el instalador de WordPress. Completa la instalación.

**Paso 5: Verificar persistencia**

```bash
# Detener y eliminar los contenedores
$ docker stop wordpress wordpress_db
$ docker rm wordpress wordpress_db

# Volver a crearlos con los mismos comandos
$ docker run -d ...  # (repite los comandos anteriores)

# ¡Tu WordPress sigue funcionando con todos tus datos!
```

**¿Por qué persiste?**

- Los archivos de WordPress están en el volumen `wp_files`
- La base de datos está en el volumen `wp_db`
- Los volúmenes no se eliminan con los contenedores

!!! tip "Backup fácil"
    Para hacer backup, solo necesitas respaldar los volúmenes `wp_db` y `wp_files`.

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
