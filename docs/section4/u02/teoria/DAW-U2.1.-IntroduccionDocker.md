---
title: "UD 2 - 2.1 Introducción a los contenedores Docker"
description: Introducción a Docker, instalación y primeros pasos con contenedores
summary: Docker, instalación, contenedores, comandos básicos
authors:
    - Eduardo Fdez
date: 2025-01-23
icon: "material/file-document-outline"
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

**Explicación del comando:**

- `docker run`: Comando para crear y ejecutar un contenedor
- `hello-world`: Nombre de la imagen a utilizar

**¿Qué ha sucedido? Análisis paso a paso:**

1. **Búsqueda local**: Docker busca la imagen `hello-world` en tu ordenador
2. **Descarga**: Al no encontrarla, la descarga automáticamente de Docker Hub (el registro público oficial)
3. **Extracción**: Descomprime las capas de la imagen (`Pull complete`)
4. **Creación**: Crea un nuevo contenedor a partir de esa imagen
5. **Ejecución**: El contenedor ejecuta el programa predefinido que muestra el mensaje
6. **Salida**: El demonio Docker envía la salida al terminal
7. **Finalización**: El contenedor se detiene automáticamente al terminar su tarea

!!! tip "Consejo"
    La primera vez que ejecutas una imagen tarda más porque debe descargarla. Las siguientes ejecuciones serán instantáneas ya que la imagen está en tu ordenador.

### 4. Ejecución simple de contenedores

Vamos a crear un contenedor ejecutando un comando personalizado:

```bash
$ docker run ubuntu echo 'Hello world'
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
Status: Downloaded newer image for ubuntu:latest
Hello world
```

**Análisis del comando:**

- `docker run`: Crea y ejecuta un contenedor
- `ubuntu`: Imagen base del sistema operativo Ubuntu
- `echo 'Hello world'`: Comando que queremos ejecutar dentro del contenedor

**¿Qué hace este comando?**

1. Descarga la imagen de Ubuntu (solo la primera vez)
2. Crea un contenedor basado en Ubuntu
3. Ejecuta el comando `echo 'Hello world'` dentro del contenedor
4. Muestra el resultado en tu terminal
5. El contenedor se detiene automáticamente al finalizar

#### 4.1. Ver contenedores existentes

Para ver los contenedores (incluidos los detenidos):

```bash
$ docker ps -a
CONTAINER ID   IMAGE     COMMAND              CREATED          STATUS                      PORTS     NAMES
3bbf39d0ec26   ubuntu    "echo 'Hello wo…"    31 seconds ago   Exited (0) 29 seconds ago             wizardly_edison
```

**Explicación de las columnas:**

- `CONTAINER ID`: Identificador único del contenedor (primeros caracteres)
- `IMAGE`: Imagen utilizada para crear el contenedor
- `COMMAND`: Comando ejecutado en el contenedor
- `CREATED`: Hace cuánto se creó el contenedor
- `STATUS`: Estado actual (`Exited (0)` significa terminado correctamente)
- `PORTS`: Puertos mapeados (ninguno en este caso)
- `NAMES`: Nombre asignado automáticamente por Docker

!!! note "Opciones de docker ps"
    - `docker ps`: Solo muestra contenedores en ejecución
    - `docker ps -a`: Muestra todos los contenedores (incluidos detenidos)
    - `docker ps -q`: Solo muestra los IDs de los contenedores

#### 4.2. Ver imágenes descargadas

```bash
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
ubuntu        latest    f63181f19b2f   7 days ago     72.9MB
hello-world   latest    bf756fb1ae65   13 months ago  13.3kB
```

**Explicación de las columnas:**

- `REPOSITORY`: Nombre de la imagen
- `TAG`: Etiqueta de versión (`latest` = última versión)
- `IMAGE ID`: Identificador único de la imagen
- `CREATED`: Cuándo se creó la imagen (no cuándo la descargaste)
- `SIZE`: Tamaño en disco de la imagen

!!! tip "Buena práctica"
    Observa la diferencia de tamaño: `hello-world` ocupa solo 13.3kB mientras que `ubuntu` ocupa 72.9MB. Esto demuestra la eficiencia de Docker para crear imágenes ligeras.

!!! note "Nota importante"
    Un contenedor ejecuta un proceso y cuando termina la ejecución, el contenedor se para.

### 5. Contenedores interactivos

Ahora vamos a crear un contenedor con el que podamos interactuar mediante una terminal, como si estuviéramos dentro de un ordenador Ubuntu:

```bash
$ docker run -it --name contenedor1 ubuntu bash
root@2bfa404bace0:/#
```

**Análisis detallado del comando:**

- `docker run`: Crear y ejecutar un contenedor
- `-i`: **Interactive** - Mantiene abierta la entrada estándar (STDIN) para que puedas escribir comandos
- `-t`: **TTY** - Asigna un pseudo-terminal para tener una interfaz de línea de comandos
- `--name contenedor1`: Asigna el nombre "contenedor1" (en lugar de uno aleatorio como "wizardly_edison")
- `ubuntu`: Imagen base a utilizar
- `bash`: Ejecuta el intérprete de comandos bash

**¿Qué significa el prompt `root@2bfa404bace0:/#`?**

- `root`: Eres el usuario root (administrador) dentro del contenedor
- `2bfa404bace0`: ID del contenedor (primeros caracteres)
- `/`: Estás en el directorio raíz del sistema
- `#`: Símbolo que indica que eres root (si fueras usuario normal sería `$`)

**Prueba estos comandos dentro del contenedor:**

```bash
root@2bfa404bace0:/# whoami
root

root@2bfa404bace0:/# pwd
/

root@2bfa404bace0:/# ls
bin  boot  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var

root@2bfa404bace0:/# cat /etc/os-release
NAME="Ubuntu"
VERSION="22.04.3 LTS (Jammy Jellyfish)"
...
```

!!! warning "Importante"
    Estás dentro de un sistema Ubuntu completamente aislado. Los archivos de tu ordenador NO están accesibles aquí. Es como tener un mini-ordenador dentro de tu ordenador.

#### 5.1. Gestionar contenedores interactivos

**Salir del contenedor:**

Para salir del contenedor sin detenerlo:

```bash
root@2bfa404bace0:/# exit
# O presiona Ctrl+D
```

Esto detiene el contenedor. Verás que vuelves a tu terminal normal.

**Iniciar un contenedor detenido:**

```bash
$ docker start contenedor1
contenedor1
```

- `docker start`: Inicia un contenedor que está detenido
- `contenedor1`: Nombre del contenedor a iniciar
- El contenedor ahora está ejecutándose en segundo plano

**Conectarse a un contenedor en ejecución:**

```bash
$ docker attach contenedor1
root@2bfa404bace0:/#
```

- `docker attach`: Te conecta a la terminal de un contenedor que ya está ejecutándose
- Ahora puedes interactuar con el contenedor como antes
- Para salir sin detener el contenedor: presiona `Ctrl+P` seguido de `Ctrl+Q`

**Ejecutar comandos en un contenedor sin conectarte:**

```bash
$ docker exec contenedor1 ls -al
total 56
drwxr-xr-x   1 root root 4096 Oct 23 17:00 .
drwxr-xr-x   1 root root 4096 Oct 23 17:00 ..
drwxr-xr-x   2 root root 4096 Sep 15 00:00 bin
...
```

**Explicación de docker exec:**

- `docker exec`: Ejecuta un comando en un contenedor que YA está ejecutándose
- `contenedor1`: Nombre del contenedor
- `ls -al`: Comando a ejecutar (lista archivos con detalles)
- La salida aparece en tu terminal, pero el comando se ejecuta DENTRO del contenedor

**Ejemplo interactivo con exec:**

```bash
$ docker exec -it contenedor1 bash
root@2bfa404bace0:/#
```

Esto abre una nueva sesión bash en el contenedor. Si sales con `exit`, el contenedor seguirá ejecutándose.

**Reiniciar un contenedor:**

```bash
$ docker restart contenedor1
contenedor1
```

- Equivalente a hacer `docker stop` seguido de `docker start`
- Útil cuando necesitas "reiniciar" el contenedor para aplicar cambios

### 6. Contenedores en segundo plano (demonio)

Los servicios como servidores web o bases de datos deben ejecutarse continuamente en segundo plano. Para esto usamos la opción `-d`:

```bash
$ docker run -d --name servidor_web nginx
a9dbf94c1f43d2e8f1a0b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6
```

**Explicación del comando:**

- `-d`: **Detached mode** - El contenedor se ejecuta en segundo plano
- `--name servidor_web`: Asignamos un nombre descriptivo
- `nginx`: Imagen del servidor web Nginx
- El comando devuelve el ID completo del contenedor y vuelve a tu terminal

**Verificar que está ejecutándose:**

```bash
$ docker ps
CONTAINER ID   IMAGE   COMMAND                  CREATED         STATUS         PORTS     NAMES
a9dbf94c1f43   nginx   "/docker-entrypoint.…"   5 seconds ago   Up 4 seconds   80/tcp    servidor_web
```

Observa que `STATUS` indica `Up 4 seconds` - está activo.

**Ver los logs del contenedor:**

```bash
$ docker logs servidor_web
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty...
...
2024/01/23 17:00:00 [notice] 1#1: nginx/1.25.3
2024/01/23 17:00:00 [notice] 1#1: start worker processes
```

**Opciones útiles de logs:**

```bash
# Ver logs en tiempo real (como tail -f)
$ docker logs -f servidor_web

# Ver solo las últimas 50 líneas
$ docker logs --tail 50 servidor_web

# Ver logs con marcas de tiempo
$ docker logs -t servidor_web
```

**Detener el contenedor:**

```bash
$ docker stop servidor_web
servidor_web
```

- Envía una señal SIGTERM al proceso principal
- Espera 10 segundos a que termine limpiamente
- Si no termina, envía SIGKILL para forzar el cierre

**Detener inmediatamente (no recomendado):**

```bash
$ docker kill servidor_web
```

!!! tip "Buena práctica"
    Usa siempre `docker stop` en lugar de `docker kill` para permitir que el servicio se cierre correctamente (guardar datos, cerrar conexiones, etc.).

### 7. Servidor web con contenedor

Vamos a ejecutar un servidor web Nginx y hacerlo accesible desde nuestro navegador:

```bash
$ docker run -d --name mi_nginx -p 8080:80 nginx
```

**Análisis detallado del comando:**

- `docker run -d`: Ejecutar en segundo plano
- `--name mi_nginx`: Nombre del contenedor
- `-p 8080:80`: **Port mapping** - Mapeo de puertos
  - `8080`: Puerto en TU ordenador (host)
  - `80`: Puerto dentro del contenedor (donde escucha Nginx)
  - Significado: "Las peticiones al puerto 8080 de mi ordenador se redirigen al puerto 80 del contenedor"
- `nginx`: Imagen del servidor web Nginx

**¿Cómo funciona el mapeo de puertos?**

```
Tu navegador → localhost:8080 → Docker → Contenedor:80 → Nginx
```

1. Abres `http://localhost:8080` en tu navegador
2. Tu ordenador envía la petición al puerto 8080
3. Docker intercepta esa petición
4. Docker la redirige al puerto 80 del contenedor
5. Nginx dentro del contenedor responde
6. La respuesta vuelve por el mismo camino

**Probar el servidor:**

Abre tu navegador y ve a: `http://localhost:8080`

Deberías ver la página de bienvenida de Nginx que dice "Welcome to nginx!"

**Ver qué puertos están mapeados:**

```bash
$ docker ps
CONTAINER ID   IMAGE   COMMAND                  PORTS                  NAMES
abc123def456   nginx   "/docker-entrypoint.…"   0.0.0.0:8080->80/tcp   mi_nginx
```

La columna `PORTS` muestra `0.0.0.0:8080->80/tcp`:
- `0.0.0.0`: Escucha en todas las interfaces de red
- `8080->80`: Puerto host → puerto contenedor
- `tcp`: Protocolo TCP

**Mapear múltiples puertos:**

```bash
$ docker run -d --name mi_nginx_ssl -p 8080:80 -p 8443:443 nginx
```

Esto mapea tanto HTTP (puerto 80) como HTTPS (puerto 443).

!!! warning "Conflicto de puertos"
    Si el puerto 8080 ya está en uso en tu ordenador, verás un error. Cambia a otro puerto libre, por ejemplo `-p 9090:80`.

### 8. Configuración con variables de entorno

Las variables de entorno son el método estándar para configurar contenedores. Permiten personalizar el comportamiento sin modificar la imagen.

**Ejemplo: Base de datos MySQL**

```bash
$ docker run -d --name mi_mysql \
  -e MYSQL_ROOT_PASSWORD=secreto \
  -e MYSQL_DATABASE=midb \
  -e MYSQL_USER=usuario \
  -e MYSQL_PASSWORD=pass123 \
  mysql:5.7
```

**Explicación línea por línea:**

1. `docker run -d --name mi_mysql`: Crear contenedor MySQL en segundo plano
2. `-e MYSQL_ROOT_PASSWORD=secreto`: Define la contraseña del usuario root
   - Variable obligatoria para MySQL
   - Sin ella, el contenedor no iniciará
3. `-e MYSQL_DATABASE=midb`: Crea automáticamente una base de datos llamada "midb"
4. `-e MYSQL_USER=usuario`: Crea un usuario llamado "usuario"
5. `-e MYSQL_PASSWORD=pass123`: Contraseña para ese usuario
6. `mysql:5.7`: Imagen de MySQL versión 5.7

**¿Cómo sabe MySQL qué hacer con estas variables?**

Cada imagen Docker define qué variables de entorno acepta. La imagen `mysql` está programada para:
- Leer estas variables al iniciar
- Configurar el servidor MySQL según los valores
- Ejecutar scripts de inicialización automáticos

**Ver variables de entorno de un contenedor:**

```bash
$ docker exec mi_mysql env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=abc123def456
MYSQL_ROOT_PASSWORD=secreto
MYSQL_DATABASE=midb
MYSQL_USER=usuario
MYSQL_PASSWORD=pass123
...
```

**Conectarse a la base de datos:**

```bash
$ docker exec -it mi_mysql mysql -u usuario -ppass123 midb
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| midb              |
+--------------------+
mysql> exit
```

!!! warning "Seguridad"
    NO pongas contraseñas reales en la línea de comandos. Usa archivos de variables de entorno (`.env`) o secrets de Docker. Veremos esto más adelante.

**Ejemplo: Variables de entorno para desarrollo vs producción**

```bash
# Desarrollo
$ docker run -d --name app_dev \
  -e APP_ENV=development \
  -e DEBUG=true \
  -e LOG_LEVEL=debug \
  mi_aplicacion

# Producción
$ docker run -d --name app_prod \
  -e APP_ENV=production \
  -e DEBUG=false \
  -e LOG_LEVEL=warning \
  mi_aplicacion
```

La misma imagen se comporta diferente según las variables de entorno.

### 9. Comandos básicos de gestión

#### 9.1. Listar contenedores

```bash
# Contenedores en ejecución
$ docker ps

# Todos los contenedores
$ docker ps -a
```

#### 9.2. Eliminar contenedores

**Eliminar un contenedor detenido:**

```bash
# Por ID (puedes usar solo los primeros caracteres)
$ docker rm 372ca4634d53
# o simplemente
$ docker rm 372

# Por nombre
$ docker rm elastic_johnson
elastic_johnson
```

**Intentar eliminar un contenedor en ejecución:**

```bash
$ docker rm mi_nginx
Error response from daemon: You cannot remove a running container abc123. 
Stop the container before attempting removal or force remove
```

Docker no te deja eliminar contenedores en ejecución por seguridad.

**Opciones para eliminar un contenedor en ejecución:**

Opción 1: Detenerlo primero (recomendado)
```bash
$ docker stop mi_nginx
$ docker rm mi_nginx
```

Opción 2: Forzar eliminación
```bash
$ docker rm -f mi_nginx
mi_nginx
```

- `-f`: **Force** - Fuerza la eliminación
- Envía SIGKILL al proceso (terminación inmediata)
- Úsalo solo cuando sea necesario

**Eliminar varios contenedores a la vez:**

```bash
$ docker rm contenedor1 contenedor2 contenedor3
```

**Eliminar todos los contenedores detenidos:**

```bash
$ docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
abc123def456...
def456ghi789...
Total reclaimed space: 1.5MB
```

**Eliminar contenedor automáticamente al salir:**

```bash
$ docker run --rm ubuntu echo "Hola"
Hola
```

- `--rm`: Elimina el contenedor automáticamente cuando termina
- Útil para contenedores temporales o de prueba
- No necesitas hacer `docker rm` después

!!! tip "Limpieza recomendada"
    Ejecuta periódicamente `docker container prune` para eliminar contenedores detenidos que ya no necesitas y liberar espacio.

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
