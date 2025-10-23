---
title: "UD 2 - 2.1 Introducción a los contenedores Docker"
description: Introducción a Docker, instalación y primeros pasos con contenedores
summary: Docker, instalación, contenedores, comandos básicos
authors:
    - Eduardo Fdez
date: 2025-01-23
icon: 
permalink: /daw/unidad2/2.1
categories:
    - DAW
tags:
    - Docker
    - Contenedores
    - Instalación
---

## 2.1. Introducción a los contenedores Docker

Docker es una plataforma de código abierto que permite automatizar el despliegue de aplicaciones dentro de contenedores de software. Los contenedores son entornos ligeros y portátiles que incluyen todo lo necesario para ejecutar una aplicación: código, runtime, herramientas del sistema, bibliotecas y configuración.

### 1. ¿Qué es Docker?

Docker proporciona una capa adicional de abstracción y automatización de virtualización a nivel de sistema operativo. A diferencia de las máquinas virtuales tradicionales, los contenedores Docker comparten el kernel del sistema operativo host, lo que los hace mucho más ligeros y eficientes.

**Ventajas de usar Docker:**

- **Portabilidad**: Los contenedores funcionan de la misma manera en cualquier entorno
- **Eficiencia**: Menos sobrecarga que las máquinas virtuales tradicionales
- **Aislamiento**: Cada contenedor se ejecuta de forma aislada
- **Rapidez**: Los contenedores se inician en segundos
- **Consistencia**: Mismo entorno en desarrollo, pruebas y producción

### 2. Instalación de Docker Engine

Docker Engine está disponible en varias distribuciones de Linux, macOS y Windows 10 a través de Docker Desktop. En este apartado realizaremos la instalación en una distribución Linux (Debian/Ubuntu).

Para instalar Docker usando los repositorios oficiales:

#### 2.1. Actualizar repositorios e instalar prerequisitos

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
```

#### 2.2. Añadir la clave GPG oficial de Docker

```bash
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

#### 2.3. Añadir el repositorio oficial de Docker

```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

#### 2.4. Instalar Docker Engine

```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

#### 2.5. Configurar usuario sin privilegios

Para manejar Docker con un usuario sin privilegios, debemos añadir el usuario al grupo `docker`:

```bash
sudo usermod -aG docker $USER
```

Reiniciar la sesión del usuario o ejecutar:

```bash
su - $USER
```

#### 2.6. Verificar la instalación

```bash
docker --version
```

Deberías ver algo similar a:

```
Docker version 24.0.7, build afdd53b
```

### 3. Tu primer contenedor: "Hello World"

Vamos a crear nuestro primer contenedor usando la imagen `hello-world`:

```bash
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
0e03bdcc26d7: Pull complete 
Digest: sha256:31b9c7d48790f0d8c50ab433d9c3b7e17666d6993084c002c2ff1ca09b96391d
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
```

**¿Qué ha sucedido?**

1. El cliente Docker contacta con el demonio Docker
2. El demonio descarga la imagen "hello-world" de Docker Hub
3. El demonio crea un nuevo contenedor a partir de esa imagen
4. El contenedor ejecuta el programa que produce la salida
5. El demonio envía la salida al cliente Docker

### 4. Ejecución simple de contenedores

Vamos a crear un contenedor ejecutando un comando simple:

```bash
$ docker run ubuntu echo 'Hello world'
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
Status: Downloaded newer image for ubuntu:latest
Hello world
```

El contenedor ejecuta el comando y se detiene automáticamente. Para ver los contenedores (incluidos los detenidos):

```bash
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND              CREATED          STATUS                      PORTS     NAMES
3bbf39d0ec26   ubuntu    "echo 'Hello wo…"    31 seconds ago   Exited (0) 29 seconds ago             wizardly_edison
```

Para ver las imágenes descargadas:

```bash
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
ubuntu        latest    f63181f19b2f   7 days ago     72.9MB
hello-world   latest    bf756fb1ae65   13 months ago  13.3kB
```

!!! note "Nota importante"
    Un contenedor ejecuta un proceso y cuando termina la ejecución, el contenedor se para.

### 5. Contenedores interactivos

Podemos crear contenedores con los que interactuar mediante una terminal:

```bash
$ docker run -it --name contenedor1 ubuntu bash
root@2bfa404bace0:/#
```

**Opciones utilizadas:**

- `-i`: Modo interactivo (mantiene STDIN abierto)
- `-t`: Asigna un pseudo-terminal
- `--name`: Asigna un nombre al contenedor
- `bash`: Comando a ejecutar (shell bash)

#### 5.1. Gestionar contenedores interactivos

**Iniciar un contenedor detenido:**

```bash
$ docker start contenedor1
```

**Conectarse a un contenedor en ejecución:**

```bash
$ docker attach contenedor1
root@2bfa404bace0:/#
```

**Ejecutar comandos en un contenedor en ejecución:**

```bash
$ docker exec contenedor1 ls -al
```

**Reiniciar un contenedor:**

```bash
$ docker restart contenedor1
```

### 6. Contenedores en segundo plano (demonio)

Para crear contenedores que se ejecuten en segundo plano, usamos la opción `-d` (detached):

```bash
$ docker run -d --name servidor_web nginx
a9dbf94c1f43...
```

Para ver los logs del contenedor:

```bash
$ docker logs servidor_web
```

Para detener el contenedor:

```bash
$ docker stop servidor_web
```

### 7. Servidor web con contenedor

Podemos ejecutar un servidor web Nginx y mapear sus puertos:

```bash
$ docker run -d --name mi_nginx -p 8080:80 nginx
```

**Opciones:**

- `-p 8080:80`: Mapea el puerto 80 del contenedor al puerto 8080 del host

Ahora puedes acceder al servidor en: `http://localhost:8080`

### 8. Configuración con variables de entorno

Muchos contenedores permiten configuración mediante variables de entorno:

```bash
$ docker run -d --name mi_mysql \
  -e MYSQL_ROOT_PASSWORD=secreto \
  -e MYSQL_DATABASE=midb \
  mysql:5.7
```

**Opción `-e`**: Define variables de entorno en el contenedor

### 9. Comandos básicos de gestión

#### 9.1. Listar contenedores

```bash
# Contenedores en ejecución
$ docker ps

# Todos los contenedores
$ docker ps -a
```

#### 9.2. Eliminar contenedores

```bash
# Por ID
$ docker rm 372ca4634d53

# Por nombre
$ docker rm elastic_johnson

# Forzar eliminación de contenedor en ejecución
$ docker rm -f mi_contenedor
```

#### 9.3. Inspeccionar contenedores

```bash
$ docker inspect contenedor1
```

Muestra información detallada en formato JSON sobre:

- ID del contenedor
- Puertos abiertos y redirecciones
- Volúmenes y bind mounts
- Configuración de red
- Variables de entorno
- Estado del contenedor

#### 9.4. Ver estadísticas de recursos

```bash
$ docker stats contenedor1
```

### 10. Ciclo de vida de un contenedor

1. **Crear** (`docker create`): Crea un contenedor sin iniciarlo
2. **Iniciar** (`docker start`): Inicia un contenedor detenido
3. **Ejecutar** (`docker run`): Crea e inicia en un solo paso
4. **Pausar** (`docker pause`): Pausa la ejecución
5. **Reanudar** (`docker unpause`): Reanuda un contenedor pausado
6. **Detener** (`docker stop`): Detiene un contenedor de forma ordenada
7. **Matar** (`docker kill`): Detiene un contenedor inmediatamente
8. **Eliminar** (`docker rm`): Elimina un contenedor detenido

### Resumen

En esta sección hemos aprendido:

- ✅ Qué es Docker y sus ventajas
- ✅ Cómo instalar Docker Engine en Linux
- ✅ Crear y ejecutar contenedores básicos
- ✅ Trabajar con contenedores interactivos
- ✅ Ejecutar servicios en segundo plano
- ✅ Configurar contenedores con variables de entorno
- ✅ Comandos básicos para gestionar contenedores

### Recursos adicionales

- [Documentación oficial de instalación](https://docs.docker.com/engine/install/)
- [Referencia de comandos Docker](https://docs.docker.com/engine/reference/commandline/cli/)
- [Curso Docker IES - Módulo 1](../u01/teoria/OtrosRecursos/curso_docker_ies/modulo1/)

!!! tip "Consejo"
    Practica ejecutando diferentes contenedores y experimentando con los comandos. La mejor forma de aprender Docker es usándolo.
