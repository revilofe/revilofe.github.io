---
title: "UD 2 - 2.2 Imágenes Docker"
description: Gestión y trabajo con imágenes Docker
summary: Docker Hub, gestión de imágenes, capas, registros
authors:
    - Eduardo Fdez
date: 2025-01-23
icon: 
permalink: /daw/unidad2/2.2
categories:
    - DAW
tags:
    - Docker
    - Imágenes
    - Docker Hub
---

## 2.2. Imágenes Docker

Las **imágenes de Docker** son plantillas de solo lectura que contienen un sistema de archivos y parámetros de configuración para crear contenedores. Una imagen puede contener un sistema operativo completo con aplicaciones instaladas o simplemente una aplicación específica.

### 1. Concepto de imagen Docker

Una imagen es una plantilla inmutable que sirve de base para crear contenedores. Las características principales son:

- **Solo lectura**: No se pueden modificar directamente
- **Basadas en capas**: Construidas mediante capas superpuestas
- **Reutilizables**: Múltiples contenedores pueden usar la misma imagen
- **Versionables**: Se pueden etiquetar con versiones diferentes

!!! note "Diferencia imagen vs contenedor"
    Una **imagen** es la plantilla estática, mientras que un **contenedor** es una instancia en ejecución de esa imagen.

### 2. Registros de imágenes: Docker Hub

**Docker Hub** es el registro público oficial de Docker donde se almacenan millones de imágenes. Es el componente que nos permite distribuir aplicaciones.

#### 2.1. Nomenclatura de imágenes

El nombre completo de una imagen tiene el formato:

```
usuario/nombre:etiqueta
```

**Componentes:**

- `usuario`: Nombre del usuario/organización que creó la imagen
- `nombre`: Nombre descriptivo de la imagen
- `etiqueta` (tag): Versión o variante de la imagen

**Ejemplos:**

```bash
ubuntu:22.04              # Imagen oficial Ubuntu versión 22.04
mysql:8.0                 # Imagen oficial MySQL versión 8.0
josedom24/app_web:v1      # Imagen de usuario con versión
nginx:latest              # Nginx última versión (por defecto)
```

!!! tip "Imágenes oficiales"
    Las imágenes oficiales mantenidas por Docker no tienen prefijo de usuario (ej: `ubuntu`, `nginx`, `mysql`).

### 3. Gestión de imágenes

#### 3.1. Comandos principales

**Ver imágenes locales:**

```bash
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
ubuntu        latest    f63181f19b2f   7 days ago     72.9MB
nginx         1.21      ad4c705f24d3   2 weeks ago    133MB
mysql         8.0       3218b38490ce   3 weeks ago    516MB
```

**Descargar una imagen:**

```bash
$ docker pull ubuntu:22.04
22.04: Pulling from library/ubuntu
Digest: sha256:...
Status: Downloaded newer image for ubuntu:22.04
```

**Buscar imágenes en Docker Hub:**

```bash
$ docker search nginx
NAME                      DESCRIPTION                     STARS     OFFICIAL
nginx                     Official build of Nginx         15000     [OK]
jwilder/nginx-proxy       Automated Nginx reverse...      2000      
```

**Eliminar una imagen:**

```bash
$ docker rmi ubuntu:22.04
```

!!! warning "Restricción"
    No se puede eliminar una imagen si existen contenedores (aunque estén detenidos) creados a partir de ella.

**Inspeccionar una imagen:**

```bash
$ docker inspect ubuntu:latest
```

Muestra información detallada:
- ID y checksum de la imagen
- Puertos expuestos
- Arquitectura y sistema operativo
- Tamaño de la imagen
- Volúmenes definidos
- Comando ENTRYPOINT
- Capas que componen la imagen

### 4. Organización de imágenes por capas

Las imágenes Docker están compuestas por **capas ordenadas** de solo lectura. Cada capa representa un conjunto de cambios en el sistema de archivos.

<figure markdown>
![Capas de una imagen](assets/DAW-U2.2-capas-imagen.png)
<figcaption>Estructura de capas en imágenes Docker</figcaption>
</figure>

#### 4.1. Ventajas del sistema de capas

**Reutilización:** Si varias imágenes comparten capas comunes (como el SO base), esas capas se almacenan una sola vez.

**Ejemplo:**

```bash
ubuntu:20.04          ├── Capa base Ubuntu
                      └── Total: 72 MB

nginx:latest          ├── Capa base Ubuntu (compartida)
                      ├── Capa instalación Nginx  
                      └── Total único: +60 MB
```

#### 4.2. Capas en contenedores

Cuando se crea un contenedor desde una imagen:

1. Todas las capas de la imagen son **solo lectura**
2. Se añade una **capa superior de escritura**
3. Los cambios del contenedor se almacenan en esta capa superior

<figure markdown>
![Contenedor con capas](assets/DAW-U2.2-contenedor-capas.png)
<figcaption>Capa de escritura en contenedores</figcaption>
</figure>

**Copy-on-Write (CoW):**

- El contenedor no modifica archivos de las capas de imagen
- Crea una copia del archivo en su capa superior
- Los accesos posteriores usan la copia de la capa superior

#### 4.3. Verificar tamaño de contenedores

Ver tamaño de imagen:

```bash
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED      SIZE
ubuntu        latest    f63181f19b2f   7 days ago   72.9MB
```

Ver tamaño de contenedor con la opción `-s`:

```bash
$ docker ps -a -s
CONTAINER ID   IMAGE    COMMAND      CREATED    STATUS    SIZE
a2d1ce6990d8   ubuntu   "/bin/bash"  1 min ago  Exited    0B (virtual 72.9MB)
```

- **SIZE**: Tamaño de la capa de escritura del contenedor (0B inicialmente)
- **VIRTUAL SIZE**: Tamaño total incluyendo capas compartidas con la imagen

Si creamos un archivo en el contenedor:

```bash
$ docker start contenedor1
$ docker attach contenedor1
root@a2d1ce6990d8:/# echo "datos" > archivo.txt
root@a2d1ce6990d8:/# exit

$ docker ps -a -s
CONTAINER ID   IMAGE    SIZE
a2d1ce6990d8   ubuntu   52B (virtual 72.9MB)
```

El tamaño del contenedor aumenta con los cambios realizados.

### 5. Creación de contenedores desde imágenes

#### 5.1. Proceso de creación

Cuando ejecutamos `docker run`:

1. Docker busca la imagen en el registro local
2. Si no existe, la descarga de Docker Hub
3. Crea el contenedor añadiendo la capa de escritura
4. Configura la red y volúmenes
5. Ejecuta el comando especificado

#### 5.2. Ejemplo práctico: MediaWiki

```bash
# Descargar imagen de MediaWiki
$ docker pull mediawiki

# Crear contenedor con MediaWiki
$ docker run -d \
  --name mi_wiki \
  -p 8080:80 \
  mediawiki

# Acceder en navegador
# http://localhost:8080
```

### 6. Etiquetas y versiones

#### 6.1. Trabajar con etiquetas

```bash
# Descargar versión específica
$ docker pull ubuntu:20.04
$ docker pull ubuntu:22.04

# La etiqueta 'latest' es la predeterminada
$ docker pull nginx
$ docker pull nginx:latest  # Equivalente
```

#### 6.2. Etiquetar imágenes locales

```bash
# Crear una nueva etiqueta para una imagen
$ docker tag ubuntu:22.04 mi-ubuntu:dev

# Ver resultado
$ docker images
REPOSITORY    TAG       IMAGE ID
ubuntu        22.04     f63181f19b2f
mi-ubuntu     dev       f63181f19b2f  # Mismo ID
```

### 7. Buenas prácticas con imágenes

1. **Usar etiquetas específicas** en producción (no `latest`)
2. **Mantener imágenes actualizadas** por seguridad
3. **Limpiar imágenes no utilizadas** periódicamente
4. **Preferir imágenes oficiales** cuando sea posible
5. **Revisar el tamaño** de las imágenes antes de usarlas

#### 7.1. Limpieza de imágenes

```bash
# Eliminar imágenes sin usar
$ docker image prune

# Eliminar todas las imágenes no usadas por contenedores
$ docker image prune -a

# Ver espacio usado por Docker
$ docker system df
```

### Resumen

En esta sección hemos aprendido:

- ✅ Qué son las imágenes Docker y sus características
- ✅ Cómo funciona Docker Hub como registro de imágenes
- ✅ Gestionar imágenes: descargar, listar, eliminar
- ✅ La organización por capas de las imágenes
- ✅ Cómo las capas optimizan el almacenamiento
- ✅ Crear contenedores desde imágenes
- ✅ Trabajar con etiquetas y versiones

### Recursos adicionales

- [Docker Hub](https://hub.docker.com/)
- [Documentación sobre imágenes](https://docs.docker.com/engine/reference/commandline/images/)
- [Curso Docker IES - Módulo 2](../u01/teoria/OtrosRecursos/curso_docker_ies/modulo2/)

!!! tip "Siguiente paso"
    En la siguiente sección aprenderemos sobre almacenamiento persistente y redes en Docker.
