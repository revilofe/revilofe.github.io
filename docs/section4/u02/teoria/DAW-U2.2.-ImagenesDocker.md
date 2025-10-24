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

**Interpretación de cada columna:**

- `REPOSITORY`: Nombre de la imagen (sin el tag)
- `TAG`: Versión o variante (latest, 22.04, 8.0, alpine, etc.)
- `IMAGE ID`: Identificador único (hash). Dos imágenes con mismo ID son idénticas
- `CREATED`: Cuándo se construyó la imagen (NO cuándo la descargaste tú)
- `SIZE`: Espacio que ocupa en disco

**Comandos adicionales útiles:**

```bash
# Ver solo los IDs
$ docker images -q

# Filtrar por nombre
$ docker images ubuntu

# Mostrar imágenes intermedias (normalmente ocultas)
$ docker images -a

# Formato personalizado
$ docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"
```

**Descargar una imagen:**

```bash
$ docker pull ubuntu:22.04
22.04: Pulling from library/ubuntu
Digest: sha256:...
Status: Downloaded newer image for ubuntu:22.04
```

**¿Qué sucede al hacer pull?**

1. Docker contacta con Docker Hub
2. Verifica si tienes la última versión
3. Descarga solo las capas que te faltan (optimización)
4. Verifica la integridad con el Digest (checksum)
5. Almacena la imagen en tu registro local

**Descargar sin especificar tag:**

```bash
$ docker pull nginx
# Equivale a:
$ docker pull nginx:latest
```

!!! warning "latest no significa 'la más reciente'"
    `latest` es solo una etiqueta por defecto. No se actualiza automáticamente. Si quieres la última versión, debes hacer `docker pull` de nuevo.

**Buscar imágenes en Docker Hub:**

```bash
$ docker search nginx
NAME                      DESCRIPTION                     STARS     OFFICIAL
nginx                     Official build of Nginx         15000     [OK]
jwilder/nginx-proxy       Automated Nginx reverse...      2000      
nginx/nginx-ingress       NGINX Ingress Controller        500
```

**Explicación de las columnas:**

- `NAME`: Nombre completo de la imagen (usuario/nombre)
- `DESCRIPTION`: Descripción breve
- `STARS`: Número de estrellas (popularidad)
- `OFFICIAL`: [OK] indica que es una imagen oficial

**Buscar con filtros:**

```bash
# Solo imágenes oficiales
$ docker search --filter is-official=true nginx

# Mínimo de estrellas
$ docker search --filter stars=100 nginx

# Limitar resultados
$ docker search --limit 5 nginx
```

**Eliminar una imagen:**

```bash
$ docker rmi ubuntu:22.04
Untagged: ubuntu:22.04
Untagged: ubuntu@sha256:...
Deleted: sha256:f63181f19b2f...
Deleted: sha256:abc123def456...
```

**¿Por qué dice "Untagged" y "Deleted"?**

- `Untagged`: Elimina la etiqueta (nombre) de la imagen
- `Deleted`: Elimina las capas físicas del disco
- Si otra imagen usa las mismas capas, solo se elimina el tag

**Eliminar por IMAGE ID:**

```bash
$ docker rmi f63181f19b2f
```

**Eliminar varias imágenes:**

```bash
$ docker rmi ubuntu:22.04 nginx:1.21 mysql:8.0
```

**Forzar eliminación:**

```bash
$ docker rmi -f ubuntu:22.04
```

Esto es necesario si hay contenedores (aunque estén parados) creados desde esa imagen.

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

1. Todas las capas de la imagen son **solo lectura** (inmutables)
2. Se añade una **capa superior de escritura** (thin read-write layer)
3. Los cambios del contenedor se almacenan SOLO en esta capa superior

**Ejemplo visual:**

```
┌──────────────────────────┐
│  Capa de escritura       │ ← Aquí van TODOS los cambios del contenedor
│  (Read-Write Layer)      │    (archivos nuevos, modificados, eliminados)
├──────────────────────────┤
│  Capa 3: Aplicación      │ ↑
├──────────────────────────┤ │ 
│  Capa 2: Dependencias    │ │ Solo lectura
├──────────────────────────┤ │ (compartidas entre contenedores)
│  Capa 1: Sistema Base    │ ↓
└──────────────────────────┘
     IMAGEN DOCKER
```

**Copy-on-Write (CoW): ¿Cómo funciona?**

Imagina que quieres editar el archivo `/etc/nginx/nginx.conf` dentro de un contenedor:

1. **Lectura inicial**: El archivo existe en una capa de solo lectura de la imagen
2. **Modificación**: Cuando intentas modificarlo:
   - Docker COPIA el archivo completo a la capa de escritura
   - Editas la copia en la capa de escritura
   - El original en la imagen permanece intacto
3. **Lecturas posteriores**: Docker lee automáticamente la versión de la capa superior

**Ejemplo práctico:**

```bash
# Crear contenedor
$ docker run -it --name test ubuntu bash

# Dentro del contenedor, modificar un archivo del sistema
root@abc123:/# echo "Prueba" >> /etc/hosts
root@abc123:/# exit

# Ver el tamaño
$ docker ps -a -s
CONTAINER ID   IMAGE    SIZE
abc123def456   ubuntu   45B (virtual 72.9MB)
```

Los 45B son el tamaño de los cambios (el texto añadido a /etc/hosts).

**¿Qué pasa al eliminar archivos en un contenedor?**

```bash
root@abc123:/# rm -rf /var/log/*
```

Docker NO elimina los archivos de las capas de imagen. En su lugar:
- Crea un "archivo de eliminación" (whiteout file) en la capa de escritura
- Este archivo oculta los archivos de las capas inferiores
- Los archivos originales siguen en la imagen, ocupando espacio

!!! warning "Importante"
    Por esto es crucial construir imágenes ligeras desde el inicio. Eliminar archivos en un contenedor NO reduce el tamaño de la imagen.

#### 4.3. Verificar tamaño de contenedores

**Ver tamaño de imagen:**

```bash
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED      SIZE
ubuntu        latest    f63181f19b2f   7 days ago   72.9MB
```

Esto muestra el tamaño total de todas las capas de la imagen.

**Ver tamaño de contenedor con la opción `-s`:**

```bash
$ docker ps -a -s
CONTAINER ID   IMAGE    COMMAND      CREATED    STATUS    SIZE
a2d1ce6990d8   ubuntu   "/bin/bash"  1 min ago  Exited    0B (virtual 72.9MB)
```

**Interpretación de SIZE:**

- **0B**: Tamaño de la capa de escritura (cambios únicos del contenedor)
- **virtual 72.9MB**: Tamaño total = capa de escritura + imagen base

**¿Por qué es 0B?**

Porque NO hemos hecho ningún cambio. La capa de escritura está vacía.

**Experimento: Crear un archivo en el contenedor**

```bash
$ docker start contenedor1
$ docker attach contenedor1
root@a2d1ce6990d8:/# echo "datos de prueba" > archivo.txt
root@a2d1ce6990d8:/# exit

$ docker ps -a -s
CONTAINER ID   IMAGE    SIZE
a2d1ce6990d8   ubuntu   52B (virtual 72.9MB)
```

Ahora el tamaño es **52B** porque hemos creado un archivo que ocupa 52 bytes.

**Crear un archivo grande:**

```bash
$ docker attach contenedor1
root@a2d1ce6990d8:/# dd if=/dev/zero of=archivo_grande bs=1M count=100
# Esto crea un archivo de 100MB
root@a2d1ce6990d8:/# exit

$ docker ps -a -s
CONTAINER ID   IMAGE    SIZE
a2d1ce6990d8   ubuntu   100MB (virtual 172.9MB)
```

Observa:
- SIZE: 100MB (nuestra capa de escritura)
- virtual: 172.9MB (100MB + 72.9MB de la imagen)

**Conclusión importante:**

```
Espacio usado por contenedor = Espacio único de capa escritura
Espacio compartido = Capas de la imagen (compartidas con todos los contenedores)
```

Si creas 10 contenedores desde ubuntu:
- Imagen ubuntu: 72.9MB (compartida)
- Cada contenedor: solo ocupa lo que modifique

**Ejemplo real:**

```bash
$ docker run -d --name cont1 ubuntu sleep 1000
$ docker run -d --name cont2 ubuntu sleep 1000
$ docker run -d --name cont3 ubuntu sleep 1000

$ docker ps -s
CONTAINER ID   IMAGE    SIZE
abc123         ubuntu   0B (virtual 72.9MB)
def456         ubuntu   0B (virtual 72.9MB)
ghi789         ubuntu   0B (virtual 72.9MB)
```

3 contenedores, pero solo ocupan 72.9MB en total (no 218.7MB) porque comparten las capas de imagen.

!!! tip "Eficiencia de Docker"
    Esta es una de las grandes ventajas de Docker: puedes tener decenas de contenedores ocupando mucho menos espacio que máquinas virtuales equivalentes.

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
